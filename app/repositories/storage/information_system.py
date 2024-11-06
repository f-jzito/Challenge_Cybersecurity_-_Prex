import json
from datetime import datetime
from app.helpers.logger import log
import os

class AgentRepository:
    def save_system_info_to_json(self, data):
        """
        Saves the provided system information to a JSON file.

        Args:
            data (dict): A dictionary containing the system information to be saved.
                         The dictionary should have the following structure:
                         {
                             "processor": { ... },
                             "server_ip": "...",
                             "system": {
                                 "os_name": "...",
                                 "os_version": "...",
                                 "processes": [ ... ],
                                 "users": [ ... ]
                             }
                         }

        Returns:
            bool: True if the data was saved successfully, False otherwise.
        """
        try:
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d")
            filename = f"{data['server_ip']}_{timestamp}.json"
            # Create the 'data' directory if it doesn't exist
            os.makedirs('data', exist_ok=True)
            # Define the filepath including the 'data' folder
            filepath = os.path.join('data', filename)

            # Check if the file already exists
            if os.path.exists(filepath):
                log.info(f"File {filename} already exists.")
                return "File already exists."

            # Save the data to a JSON file
            with open(filepath, 'w') as jsonfile:
                json.dump(data, jsonfile, indent=4)

            log.info(f"Data saved to {filepath}")
            return True

        except Exception as e:
            log.error(f"Error saving system information to JSON: {e}")
            return False

    def get_system_info_by_ip(self,ip):
        """
        Queries all JSON files containing the given IP in their name within the 'data' directory and returns the data.

        Args:
            ip (str): The IP address to search for.

        Returns:
            list: A list of dictionaries, where each dictionary contains the data from one JSON file.
                  Returns an empty list if no files are found.
        """

        try:
            data_dir = 'data'
            all_data = []

            # Iterate over all files in the 'data' directory
            for filename in os.listdir(data_dir):
                # Check if the filename starts with the IP followed by an underscore
                if filename.startswith(ip + "_") and filename.endswith('.json'):
                    filepath = os.path.join(data_dir, filename)

                    # Read the JSON file and append the data to the list
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                        all_data.append(data)
            return all_data

        except Exception as e:
            print(f"Error querying JSON files: {e}")
            return []