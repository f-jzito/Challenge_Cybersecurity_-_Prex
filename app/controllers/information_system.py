from flask import Blueprint, jsonify, request
from flask_httpauth import HTTPTokenAuth
from app.helpers.logger import log
from app.services.information_system import AgentService
from config import Config

bp = Blueprint('information_system', __name__)


auth = HTTPTokenAuth(scheme='Bearer')

tokens = [Config.USER_TOKEN]

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return token

@bp.route('/information_system', methods=['POST'])
@auth.login_required
def register_system_data():
    """
    Endpoint to register system data.

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    context_message = "[Controllers] register_system_data "
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data received'}), 400

        centralized_information_system_data = data.get('centralized_information_system_data')
        if not centralized_information_system_data:
            return jsonify({'error': 'No system data found in request'}), 400

        log.info(f"{context_message} Received system data: {centralized_information_system_data}")

        # Assuming Agent.collect_and_send_system_info handles saving the data
        agent_service = AgentService()
        if agent_service.save_data_system(centralized_information_system_data)  == 'File already exists.':# Pass the data to the agent
            return jsonify({'message': 'File already exists.'}), 200
        return jsonify({'message': 'System data registered successfully'}), 200

    except Exception as e:
        log.error(f"{context_message} Error registering system data: {e}")
        return jsonify({'error': 'Failed to register system data'}), 500

@bp.route('/information_system/<ip>', methods=['GET'])
def get_system_data_by_ip(ip):
    """
    Endpoint to get system data by IP.

    Args:
        ip (str): The IP address to search for.

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    context_message = "[Controllers] get_system_data_by_ip "
    try:
        log.info(f"{context_message} Retrieving system data for IP: {ip}")

        # Use the AgentRepository to get the data
        agent_service = AgentService()
        system_data = agent_service.get_data_system_by_ip(ip)

        if system_data:
            return jsonify(system_data), 200
        else:
            return jsonify({'error': 'No system data found for this IP'}), 404

    except Exception as e:
        log.error(f"{context_message} Error retrieving system data: {e}")
        return jsonify({'error': 'Failed to retrieve system data'}), 500