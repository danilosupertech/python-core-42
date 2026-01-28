"""
ft_circular_curse.py
Demonstrating how to break circular import dependency patterns using late imports.

The Circular Curse: When module A needs function from module B, and module B needs
something from module A, a circular dependency forms. Python refuses to execute this pattern.

The Solution: Import inside the function (late import) - defers the import until the
function is called, by which time both modules are fully loaded.
"""

print("═" * 60)
print("PART IV: CIRCULAR CURSE - BREAKING CIRCULAR DEPENDENCIES")
print("═" * 60)

# Direct absolute import path
from alchemy.grimoire import record_spell, validate_ingredients

print("\n📖 The Curse Scenario:")
print("   - spellbook.py needs validate_ingredients")
print("   - validator.py might eventually need spellbook.py")
print("   - This creates a CIRCULAR DEPENDENCY")

print("\n⚔️ The Solution: LATE IMPORT")
print("   - record_spell() imports validator INSIDE the function")
print("   - Import happens when function is called, not at module load")
print("   - Both modules are fully loaded by then ✓")

print("\n" + "─" * 60)
print("Testing Spell Recording with Validation:")
print("─" * 60)

# Test valid spell
spell_result = record_spell("Fireball", "fire earth")
print(f"\n✓ {spell_result}")

# Test invalid spell  
spell_result = record_spell("Shadowburst", "shadow void")
print(f"✗ {spell_result}")

# Test another valid spell
spell_result = record_spell("Healing Light", "water air")
print(f"✓ {spell_result}")

# Direct validation
validation = validate_ingredients("fire water earth air")
print(f"\n✓ Direct validation: {validation}")

print("\n" + "─" * 60)
print("Why This Works:")
print("─" * 60)
print("""
1. grimoire/__init__.py imports from spellbook and validator
2. spellbook.py imports validator INSIDE record_spell()
3. When record_spell() is first called, both modules are already loaded
4. No circular import error occurs!

This is the KEY technique for breaking circular dependencies in Python.
""")

print("═" * 60)
print("Circular Curse Successfully Broken! 🎉")
print("═" * 60)
