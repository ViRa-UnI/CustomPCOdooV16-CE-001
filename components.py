# components.py

"""
This file contains the implementation of the component-related functionality for the Custom PC Building Module.
"""

import sqlalchemy as db

# Define the components table
components_table = db.Table(
    'components',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('name', db.String(100), nullable=False),
    db.Column('category', db.String(100), nullable=False),
    db.Column('description', db.Text, nullable=False),
    db.Column('price', db.Float, nullable=False),
    db.Column('compatibility', db.Text, nullable=False)
)

def add_component(name, category, description, price, compatibility):
    """
    Add a new component to the components table.

    Args:
        name (str): The name of the component.
        category (str): The category of the component.
        description (str): The description of the component.
        price (float): The price of the component.
        compatibility (str): The compatibility information of the component.

    Returns:
        int: The ID of the newly added component.
    """
    # Create a new component record
    component = {
        'name': name,
        'category': category,
        'description': description,
        'price': price,
        'compatibility': compatibility
    }

    # Insert the component record into the components table
    query = db.insert(components_table).values(**component)
    connection = engine.connect()
    result = connection.execute(query)
    connection.close()

    # Return the ID of the newly added component
    return result.inserted_primary_key[0]

def update_component(component_id, name=None, category=None, description=None, price=None, compatibility=None):
    """
    Update an existing component in the components table.

    Args:
        component_id (int): The ID of the component to be updated.
        name (str, optional): The new name of the component.
        category (str, optional): The new category of the component.
        description (str, optional): The new description of the component.
        price (float, optional): The new price of the component.
        compatibility (str, optional): The new compatibility information of the component.
    """
    # Create a dictionary of the updated component attributes
    updated_component = {}
    if name is not None:
        updated_component['name'] = name
    if category is not None:
        updated_component['category'] = category
    if description is not None:
        updated_component['description'] = description
    if price is not None:
        updated_component['price'] = price
    if compatibility is not None:
        updated_component['compatibility'] = compatibility

    # Update the component record in the components table
    query = db.update(components_table).where(components_table.c.id == component_id).values(**updated_component)
    connection = engine.connect()
    connection.execute(query)
    connection.close()

def delete_component(component_id):
    """
    Delete a component from the components table.

    Args:
        component_id (int): The ID of the component to be deleted.
    """
    # Delete the component record from the components table
    query = db.delete(components_table).where(components_table.c.id == component_id)
    connection = engine.connect()
    connection.execute(query)
    connection.close()

def get_components():
    """
    Retrieve all components from the components table.

    Returns:
        list: A list of dictionaries representing the components.
    """
    # Select all records from the components table
    query = db.select([components_table])
    connection = engine.connect()
    result = connection.execute(query)
    components = result.fetchall()
    connection.close()

    # Convert the components to a list of dictionaries
    components_list = []
    for component in components:
        component_dict = {
            'id': component.id,
            'name': component.name,
            'category': component.category,
            'description': component.description,
            'price': component.price,
            'compatibility': component.compatibility
        }
        components_list.append(component_dict)

    return components_list