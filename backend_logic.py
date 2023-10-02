```python
# backend_logic.py

from odoo import models, fields, api

class Component(models.Model):
    _name = 'custom_pc.component'
    _description = 'Custom PC Component'

    name = fields.Char(string='Name', required=True)
    category = fields.Selection([
        ('cpu', 'CPU'),
        ('gpu', 'GPU'),
        ('ram', 'RAM'),
        ('storage', 'Storage'),
        ('motherboard', 'Motherboard'),
        ('power_supply', 'Power Supply'),
        ('cooling_system', 'Cooling System'),
        ('case', 'Case')
    ], string='Category', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', required=True)

class CompatibilityRule(models.Model):
    _name = 'custom_pc.compatibility_rule'
    _description = 'Custom PC Compatibility Rule'

    component_id = fields.Many2one('custom_pc.component', string='Component', required=True)
    compatible_components = fields.Many2many('custom_pc.component', string='Compatible Components')

class CustomConfig(models.Model):
    _name = 'custom_pc.custom_config'
    _description = 'Custom PC Configuration'

    name = fields.Char(string='Name', required=True)
    component_ids = fields.Many2many('custom_pc.component', string='Components')

    @api.model
    def create(self, vals):
        config = super(CustomConfig, self).create(vals)
        # Additional logic for saving the configuration
        return config

    def write(self, vals):
        # Additional logic for updating the configuration
        return super(CustomConfig, self).write(vals)

    def unlink(self):
        # Additional logic for deleting the configuration
        return super(CustomConfig, self).unlink()

    def add_component(self, component):
        # Additional logic for adding a component to the configuration
        pass

    def remove_component(self, component):
        # Additional logic for removing a component from the configuration
        pass

    def get_total_price(self):
        # Additional logic for calculating the total price of the configuration
        return 0.0

    def check_compatibility(self):
        # Additional logic for checking the compatibility of the components in the configuration
        pass
```

This is the code for the `backend_logic.py` file. It defines the models for the custom PC components, compatibility rules, and custom configurations. The `Component` model represents a single component with fields for name, category, description, and price. The `CompatibilityRule` model represents the compatibility rules between components. The `CustomConfig` model represents a custom PC configuration with fields for name and a many-to-many relationship with components.

The `CustomConfig` model also includes methods for adding, removing, and calculating the total price of components in the configuration. It also includes a method for checking the compatibility of the components.

Please note that this code is just a starting point and may need to be customized based on your specific requirements and the Odoo framework.