from app.helpers.logger import log
from app.repositories.storage.system_db import AgentModel
from app.repositories.storage import dbinit
import json


class AgentService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            conn, cursor = dbinit()
            cls.db = AgentModel(conn, cursor)
            cls._instance = super(AgentService, cls).__new__(cls)
        return cls._instance

    def save_data_system(self, centralized_information_system_data):
        """
        Saves the centralized system data using the AgentRepository.

        Args:
            centralized_information_system_data (dict): The centralized system data to be saved.
        """
        try:
            exist = self.db.db_insert_data(centralized_information_system_data)
            if exist == 'File already exists.':
                return 'File already exists.'
        except Exception as e:
            log.error(f"Error saving system data: {e}")

    def get_data_system_by_ip(self, server_ip):
        """
        Gets the centralized system data by server IP.

        Args:
            server_ip (str): The server IP to search for data.

        Returns:
            json: A JSON with the system data if found, or an error message.
        """
        try:
            result = self.db.db_get_server_by_ip(server_ip)
            return result
        except Exception as e:
            log.error(f"Error saving system data: {e}")