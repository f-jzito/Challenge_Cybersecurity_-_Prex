from app.helpers import system
from flask import request
from app.helpers.logger import log
import requests
from datetime import datetime
from config import Config
import json
import socket

class Agent:
    def __init__(self):
        self.api_endpoint = "http://127.0.0.1:8080/information_system"
        self.headers = {
                'Authorization': f'Bearer {Config.USER_TOKEN}'
            }
        pass

    def get_all_information_system(self):
        context_message = "[Agent] get_all_information_system "
        try:
            system_info = system.get_system_information()
            processor_info = system.get_processor_information()
            client_ip = system.get_ip_address()
            timestamp = datetime.now().strftime("%Y-%m-%d")
            centralized_information_system_data = {'centralized_information_system_data':{
                'server_ip': client_ip,
                'system': system_info,
                'processor': processor_info,
                'timestamp':timestamp
            }}
            log.info(f"{context_message} all_information_system: {centralized_information_system_data}")
            return centralized_information_system_data
        except Exception as e:
            log.error(f"{context_message} An unexpected error occurred: {e}")

    def send_data_to_api(self, centralized_information_system_data):
        """
        Sends the collected data to the API endpoint.

        Args:
            self.api_endpoint (str): The URL of the API endpoint.
            data (dict): The data to be sent.
        """
        context_message = "[Agent] send_data_to_api "
        try:
            response = requests.post(self.api_endpoint, json=centralized_information_system_data,headers=self.headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            log.info(context_message + "Data sent to API successfully.")
        except requests.exceptions.RequestException as e:
            log.error(f"{context_message} Error sending data to API: {e}")

    def collect_and_send_system_info(self):
        context_message = "[Agent] collect_and_send_system_info "
        try:
            centralized_information_system_data = self.get_all_information_system()
            self.send_data_to_api(centralized_information_system_data)
        except Exception as e:
            log.error(f"{context_message} An unexpected error occurred: {e}")

