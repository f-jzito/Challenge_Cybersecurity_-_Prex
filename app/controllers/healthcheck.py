from flask import Blueprint, jsonify
from app.helpers.logger import log


bp = Blueprint('healthcheck', __name__)


@bp.route('/ping', methods=['GET'])
def ping():
    """
    Health check endpoint.

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    try:
        log.info('Ping request received')
        return jsonify("pong"), 200
    except Exception as e:
        log.error(f"Error in ping endpoint: {e}")
        return jsonify({'error': 'Failed to process ping request'}), 500