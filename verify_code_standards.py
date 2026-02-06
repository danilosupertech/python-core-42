"""
Script to verify whether Python files follow style rules.

Rules checked:
1. Classes in PascalCase
2. Functions and variables in snake_case
3. Docstrings for functions, classes, and methods
4. Type hints on all functions and methods
"""

import ast
import sys
from pathlib import Path
from typing import List, Dict, Any, Tuple


class CodeStandardsChecker:
    """Python code standards checker."""

    def __init__(self) -> None:
        """Initialize the checker."""
        self.issues: List[Dict[str, Any]] = []

    def is_snake_case(self, name: str) -> bool:
        """Check if a name is in snake_case."""
        if name.startswith('_'):
            name = name.lstrip('_')
        return name.islower() and (name == name.replace(' ', '_'))

    def is_pascal_case(self, name: str) -> bool:
        """Check if a name is in PascalCase."""
        if not name:
            return False
        return name[0].isupper() and '_' not in name and ' ' not in name

    def check_class_name(self, node: ast.ClassDef, filepath: str) -> None:
        """Check if the class name is in PascalCase."""
        if not self.is_pascal_case(node.name):
            self.issues.append({
                'file': filepath,
                'line': node.lineno,
                'type': 'naming',
                'message': f'Class "{node.name}" must be in PascalCase'
            })

    def check_function_name(self, node: ast.FunctionDef, filepath: str) -> None:
        """Check if the function name is in snake_case."""
        # Ignore special methods like __init__, __str__, etc.
        if node.name.startswith('__') and node.name.endswith('__'):
            return
        
        if not self.is_snake_case(node.name):
            self.issues.append({
                'file': filepath,
                'line': node.lineno,
                'type': 'naming',
                'message': f'Function/method "{node.name}" must be in snake_case'
            })

    def check_docstring(self, node: Any, filepath: str, node_type: str, name: str) -> None:
        """Check whether a docstring exists."""
        docstring = ast.get_docstring(node)
        if not docstring:
            self.issues.append({
                'file': filepath,
                'line': node.lineno,
                'type': 'docstring',
                'message': f'{node_type} "{name}" is missing a docstring'
            })

    def check_type_hints(self, node: ast.FunctionDef, filepath: str) -> None:
        """Check whether a function has type hints."""
        # Ignore __init__ return annotation
        if node.name == '__init__':
            has_param_hints = all(
                arg.annotation is not None 
                for arg in node.args.args 
                if arg.arg != 'self'
            )
            if not has_param_hints:
                self.issues.append({
                    'file': filepath,
                    'line': node.lineno,
                    'type': 'type_hints',
                    'message': f'Method "{node.name}" is missing parameter type hints'
                })
            return

        # For other functions, check parameters and return type.
        has_return_hint = node.returns is not None
        has_param_hints = all(
            arg.annotation is not None 
            for arg in node.args.args 
            if arg.arg != 'self' and arg.arg != 'cls'
        )

        if not has_param_hints or not has_return_hint:
            self.issues.append({
                'file': filepath,
                'line': node.lineno,
                'type': 'type_hints',
                'message': f'Function/method "{node.name}" is missing full type hints'
            })

    def visit_node(self, node: ast.AST, filepath: str) -> None:
        """Recursively visit AST nodes."""
        if isinstance(node, ast.ClassDef):
            self.check_class_name(node, filepath)
            self.check_docstring(node, filepath, 'Class', node.name)
            
            # Check class methods.
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    self.check_function_name(item, filepath)
                    self.check_docstring(item, filepath, 'Method', item.name)
                    self.check_type_hints(item, filepath)

        elif isinstance(node, ast.FunctionDef):
            # Only module-level functions.
            self.check_function_name(node, filepath)
            self.check_docstring(node, filepath, 'Function', node.name)
            self.check_type_hints(node, filepath)

        for child in ast.iter_child_nodes(node):
            self.visit_node(child, filepath)

    def check_file(self, filepath: str) -> None:
        """Check a Python file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content, filepath)
            self.visit_node(tree, filepath)
            
        except SyntaxError as e:
            self.issues.append({
                'file': filepath,
                'line': e.lineno if e.lineno else 0,
                'type': 'syntax',
                'message': f'Syntax error: {e.msg}'
            })
        except Exception as e:
            self.issues.append({
                'file': filepath,
                'line': 0,
                'type': 'error',
                'message': f'Error processing file: {str(e)}'
            })

    def check_directory(self, directory: str) -> None:
        """Check all Python files in a directory."""
        path = Path(directory)
        
        for py_file in path.rglob('*.py'):
            # Ignore files in __pycache__ and .venv.
            if '__pycache__' in str(py_file) or '.venv' in str(py_file):
                continue
            
            self.check_file(str(py_file))

    def print_report(self) -> None:
        """Print the report of found issues."""
        if not self.issues:
            print("All files follow the style rules.")
            return

        print(f"\nFound {len(self.issues)} issue(s):\n")
        
        # Group by file.
        issues_by_file: Dict[str, List[Dict[str, Any]]] = {}
        for issue in self.issues:
            file = issue['file']
            if file not in issues_by_file:
                issues_by_file[file] = []
            issues_by_file[file].append(issue)

        # Print issues per file.
        for filepath, file_issues in sorted(issues_by_file.items()):
            try:
                relative_path = Path(filepath).relative_to(Path.cwd())
            except ValueError:
                relative_path = filepath
            print(f"\n{relative_path}")
            print("=" * 80)
            
            for issue in sorted(file_issues, key=lambda x: x['line']):
                line = issue['line']
                issue_type = issue['type']
                message = issue['message']
                print(f"  Line {line:4d} | {issue_type:12s} | {message}")

        # Summary by type.
        print("\n" + "=" * 80)
        print("\nSummary by type:")
        type_counts: Dict[str, int] = {}
        for issue in self.issues:
            issue_type = issue['type']
            type_counts[issue_type] = type_counts.get(issue_type, 0) + 1
        
        for issue_type, count in sorted(type_counts.items()):
            print(f"  {issue_type:12s}: {count:3d} issue(s)")


def main() -> None:
    """Main entry point."""
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = '.'

    print(f"Checking code standards in: {directory}")
    print("=" * 80)

    checker = CodeStandardsChecker()
    checker.check_directory(directory)
    checker.print_report()

    # Return the appropriate exit code.
    sys.exit(0 if not checker.issues else 1)


if __name__ == '__main__':
    main()
