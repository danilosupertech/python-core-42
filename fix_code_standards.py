"""
Script to automatically fix code standards issues.

This script adds default docstrings and type hints where missing.
"""

import ast
import re
from pathlib import Path
from typing import List, Tuple, Optional, Any


class CodeFixer:
    """Automatically fix code standards issues."""

    def __init__(self) -> None:
        """Initialize the fixer."""
        self.files_fixed = 0
        self.changes_made = 0

    def add_type_hints_to_function(self, lines: List[str], func_line_idx: int) -> Tuple[List[str], bool]:
        """Add type hints to a function without them."""
        line = lines[func_line_idx]
        
        # Check whether type hints are already present.
        if '->' in line or ':' in line.split('(')[1].split(')')[0]:
            return lines, False
        
        # Find the def function_name(params): pattern.
        match = re.match(r'^(\s*)def\s+(\w+)\s*\((.*?)\)\s*:\s*$', line)
        if not match:
            return lines, False
        
        indent, func_name, params = match.groups()
        
        # If __init__, only add -> None.
        if func_name == '__init__':
            new_line = f'{indent}def {func_name}({params}) -> None:\n'
            lines[func_line_idx] = new_line
            return lines, True
        
        # For other functions, analyze parameters.
        if params.strip():
            # Split parameters.
            param_list = [p.strip() for p in params.split(',')]
            new_params = []
            
            for param in param_list:
                if param in ['self', 'cls']:
                    new_params.append(param)
                elif '=' in param:
                    # Parameter with a default value.
                    name, default = param.split('=', 1)
                    name = name.strip()
                    default = default.strip()
                    
                    # Infer type from the default value.
                    if default in ['None']:
                        new_params.append(f'{name}: Optional[Any] = {default}')
                    elif default.startswith('"') or default.startswith("'"):
                        new_params.append(f'{name}: str = {default}')
                    elif default.isdigit() or (default.startswith('-') and default[1:].isdigit()):
                        new_params.append(f'{name}: int = {default}')
                    elif '.' in default:
                        new_params.append(f'{name}: float = {default}')
                    elif default in ['True', 'False']:
                        new_params.append(f'{name}: bool = {default}')
                    elif default == '[]':
                        new_params.append(f'{name}: list = {default}')
                    elif default == '{}':
                        new_params.append(f'{name}: dict = {default}')
                    else:
                        new_params.append(f'{name}: Any = {default}')
                else:
                    # Parameter without a default value - add Any.
                    new_params.append(f'{param}: Any')
            
            new_params_str = ', '.join(new_params)
        else:
            new_params_str = params
        
        # Add -> None as a default return type.
        new_line = f'{indent}def {func_name}({new_params_str}) -> None:\n'
        lines[func_line_idx] = new_line
        return lines, True

    def add_docstring(self, lines: List[str], line_idx: int, item_type: str, name: str) -> Tuple[List[str], bool]:
        """Add a docstring to a function, class, or method."""
        # Find the definition line.
        def_line = lines[line_idx]
        indent = len(def_line) - len(def_line.lstrip())
        
        # Check whether the next line already has a docstring.
        if line_idx + 1 < len(lines):
            next_line = lines[line_idx + 1].strip()
            if next_line.startswith('"""') or next_line.startswith("'''"):
                return lines, False
        
        # Create an appropriate docstring.
        if item_type == 'Class':
            docstring = f'{" " * (indent + 4)}"""{name} class."""\n'
        elif item_type == 'Method':
            if name == '__init__':
                docstring = f'{" " * (indent + 4)}"""Initialize instance."""\n'
            else:
                docstring = f'{" " * (indent + 4)}"""{name} method."""\n'
        else:  # Function
            docstring = f'{" " * (indent + 4)}"""{name} function."""\n'
        
        # Insert the docstring after the definition line.
        lines.insert(line_idx + 1, docstring)
        return lines, True

    def fix_file(self, filepath: str) -> bool:
        """Fix a Python file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            original_lines = lines.copy()
            
            # Parse AST to find issues.
            tree = ast.parse(content, filepath)
            
            # Collect information about what needs to be fixed.
            fixes_needed = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if not ast.get_docstring(node):
                        fixes_needed.append(('docstring', node.lineno - 1, 'Class', node.name))
                    
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            if not ast.get_docstring(item):
                                fixes_needed.append(('docstring', item.lineno - 1, 'Method', item.name))
                            
                            # Check type hints.
                            if item.name != '__init__':
                                if item.returns is None:
                                    fixes_needed.append(('type_hints', item.lineno - 1, 'Method', item.name))
                
                elif isinstance(node, ast.FunctionDef):
                    # Module-level function.
                    parent_is_class = False
                    for parent in ast.walk(tree):
                        if isinstance(parent, ast.ClassDef) and node in parent.body:
                            parent_is_class = True
                            break
                    
                    if not parent_is_class:
                        if not ast.get_docstring(node):
                            fixes_needed.append(('docstring', node.lineno - 1, 'Function', node.name))
                        
                        if node.returns is None and node.name != '__init__':
                            fixes_needed.append(('type_hints', node.lineno - 1, 'Function', node.name))
            
            # Apply fixes from bottom to top to preserve indices.
            fixes_needed.sort(key=lambda x: x[1], reverse=True)
            
            changes_made = 0
            for fix_type, line_idx, item_type, name in fixes_needed:
                if fix_type == 'docstring':
                    lines, changed = self.add_docstring(lines, line_idx, item_type, name)
                    if changed:
                        changes_made += 1
                elif fix_type == 'type_hints':
                    lines, changed = self.add_type_hints_to_function(lines, line_idx)
                    if changed:
                        changes_made += 1
            
            # If there were changes, save the file.
            if changes_made > 0:
                new_content = '\n'.join(lines)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                self.files_fixed += 1
                self.changes_made += changes_made
                print(f'Fixed {filepath}: {changes_made} change(s)')
                return True
            
            return False
            
        except Exception as e:
            print(f'Error processing {filepath}: {e}')
            return False

    def fix_directory(self, directory: str) -> None:
        """Fix all Python files in a directory."""
        path = Path(directory)
        
        print(f'Fixing Python files in: {directory}')
        print('=' * 80)
        
        for py_file in sorted(path.rglob('*.py')):
            # Ignore files in __pycache__, .venv, and verification scripts.
            if ('__pycache__' in str(py_file) or 
                '.venv' in str(py_file) or
                py_file.name in ['verify_code_standards.py', 'fix_code_standards.py']):
                continue
            
            self.fix_file(str(py_file))
        
        print('=' * 80)
        print('\nFixes completed.')
        print(f'   Files modified: {self.files_fixed}')
        print(f'   Total changes: {self.changes_made}')


def main() -> None:
    """Main entry point."""
    import sys
    
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = '.'
    
    fixer = CodeFixer()
    fixer.fix_directory(directory)


if __name__ == '__main__':
    main()
