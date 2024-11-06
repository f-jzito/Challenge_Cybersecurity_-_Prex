import platform
import subprocess
import socket
from app.helpers.logger import log
from flask import request

SYSTEM = platform.system()

def get_processor_information():
    """
    Gets information about the processor.

    Returns:
        dict: A dictionary with processor information.
              Keys may vary depending on the operating system
              and the availability of information.
    """
    processor_info = {}
    try:
        # Get basic processor information
        processor_info['name'] = platform.processor()

        # Get additional information (may vary by system)
        if SYSTEM == "Linux":
            with open('/proc/cpuinfo') as f:
                for line in f:
                    if ':' in line:
                        key, value = line.split(':', 1)
                        key = key.strip().replace(' ', '_').lower()
                        value = value.strip()
                        processor_info[key] = value
        elif SYSTEM == "Windows":
            import winreg
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                r"HARDWARE\DESCRIPTION\System\CentralProcessor\0") as key:
                for i in range(1024):  # Iterate over the key values
                    try:
                        name, value, _ = winreg.EnumValue(key, i)
                        processor_info[name] = value
                    except OSError:
                        break
        elif SYSTEM == "Darwin":  # macOS
            command = "sysctl -a machdep.cpu"
            output = subprocess.check_output(command, shell=True).decode()
            for line in output.splitlines():
                if ":" in line:
                    key, value = line.strip().split(":", 1)
                    key = key.strip().replace(" ", "_").lower()
                    value = value.strip()
                    processor_info[key] = value
        return processor_info
    except Exception as e:
        log.error(f"Error getting processor information: {e}")
        return {}

def get_system_information():
    """
    Gets general system information, including:
    - Operating system name
    - Operating system version
    - List of running processes
    - Users with an active session

    Returns:
        dict: A dictionary with system information.
    """
    system_info = {}
    try:
        system_info['os_name'] = SYSTEM
        system_info['os_version'] = platform.release()
        system_info['processes'] = get_active_processes()
        system_info['users'] = get_active_users()
        return system_info
    except Exception as e:
        log.error(f"Error getting system information: {e}")
        return {}

def get_active_processes():
    """
    Gets a list of active processes.

    Returns:
        list: A list of dictionaries, where each dictionary
              represents a process with information such as PID and name.
    """
    try:
        if SYSTEM == "Linux" or SYSTEM == "Darwin":
            command = "ps -eo pid,comm"
            output = subprocess.check_output(command, shell=True).decode()
            return [{'pid': int(parts[0]), 'name': parts[1]}
                    for line in output.splitlines()[1:]
                    for parts in [line.split()]]
        elif SYSTEM == "Windows":
            import psutil
            return [{'pid': proc.info['pid'], 'name': proc.info['name']}
                    for proc in psutil.process_iter(['pid', 'name'])]
    except Exception as e:
        log.error(f"Error getting active processes: {e}")
        return []

def get_active_users():
    """
    Gets a list of users with an active session on the system.

    Returns:
        list: A list of dictionaries, where each dictionary
              represents a user with information such as name,
              terminal, and login time.
    """
    try:
        if SYSTEM == "Linux" or SYSTEM == "Darwin":
            command = "who"
            output = subprocess.check_output(command, shell=True).decode()
            return [{'name': parts[0], 'terminal': parts[1],
                     'login_time': ' '.join(parts[2:])}
                    for line in output.splitlines()
                    for parts in [line.split()]]
        elif SYSTEM == "Windows":
            import psutil
            return [{'name': user.name, 'terminal': user.terminal,
                     'host': user.host, 'login_time': user.started}
                    for user in psutil.users()]
    except Exception as e:
        log.error(f"Error getting active users: {e}")
        return []

def get_ip_address():
      """
      Gets the IP address of the machine.

      Returns:
          str: The IP address of the machine.
      """
      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address

      except Exception as e:
        print(f"Error getting IP address:{e}")
        return None

def get_client_ip():
    """
    Gets the client IP address. If called within a Flask request context,
    it will use request.remote_addr. Otherwise, it will use get_ip_address().

    Returns:
        str: The client IP address.
    """
    if hasattr(request, 'remote_addr'):
        # Within a Flask request context
        client_ip = request.remote_addr
    else:
        # Outside a Flask request context
        client_ip = get_ip_address()
    return client_ip