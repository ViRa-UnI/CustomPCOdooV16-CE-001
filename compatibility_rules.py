# compatibility_rules.py

```python
class CompatibilityRules:
    def __init__(self):
        self.rules = {}

    def add_rule(self, component1, component2):
        if component1 not in self.rules:
            self.rules[component1] = []
        self.rules[component1].append(component2)

    def check_compatibility(self, component1, component2):
        if component1 in self.rules and component2 in self.rules[component1]:
            return True
        return False
```

This code defines a `CompatibilityRules` class that stores compatibility rules between components. It has methods to add compatibility rules and check if two components are compatible. The compatibility rules are stored in a dictionary where the keys are components and the values are lists of compatible components.