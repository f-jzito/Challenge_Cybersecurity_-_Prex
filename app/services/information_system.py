from app.repositories.storage.information_system import AgentRepository
from app.helpers.logger import log

class AgentService:
    def save_data_system(self, centralized_information_system_data):
        """
        Saves the centralized system data using the AgentRepository.

        Args:
            centralized_information_system_data (dict): The centralized system data to be saved.
        """
        try:
            exist = AgentRepository().save_system_info_to_json(centralized_information_system_data)
            if exist == 'File already exists.':
                return 'File already exists.'
        except Exception as e:
            log.error(f"Error saving system data: {e}")

    def get_data_system_by_ip(self,ip):
        """
        Saves the centralized system data using the AgentRepository.

        Args:
            centralized_information_system_data (dict): The centralized system data to be saved.
        """
        try:
            data_ips = AgentRepository().get_system_info_by_ip(ip)
            if data_ips is not None:
                return data_ips
        except Exception as e:
            log.error(f"Error saving system data: {e}")