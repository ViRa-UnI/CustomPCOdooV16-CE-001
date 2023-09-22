# custom_configs.py

"""
This file contains the implementation of the custom_configs module for the Custom PC Building Module.
"""

import psycopg2

class CustomConfigs:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def save_config(self, user_id, config):
        """
        Saves the custom PC configuration for the given user.
        """
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO custom_configs (user_id, config) VALUES (%s, %s)", (user_id, config))
            self.db_connection.commit()
            cursor.close()
        except (Exception, psycopg2.Error) as error:
            print("Error saving custom configuration:", error)

    def get_config(self, user_id):
        """
        Retrieves the custom PC configuration for the given user.
        """
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT config FROM custom_configs WHERE user_id = %s", (user_id,))
            config = cursor.fetchone()
            cursor.close()
            return config[0] if config else None
        except (Exception, psycopg2.Error) as error:
            print("Error retrieving custom configuration:", error)

    def delete_config(self, user_id):
        """
        Deletes the custom PC configuration for the given user.
        """
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("DELETE FROM custom_configs WHERE user_id = %s", (user_id,))
            self.db_connection.commit()
            cursor.close()
        except (Exception, psycopg2.Error) as error:
            print("Error deleting custom configuration:", error)