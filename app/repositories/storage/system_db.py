from app.helpers.logger import log
import psycopg2
import json
from config import Config


class AgentModel:
    def __init__(self, connection, cursor):
        self.conn = connection
        self.cursor = cursor

    def db_insert_data(self,data):
        try:
            self.cursor.execute("""
                INSERT INTO server_info (
                    server_ip, timestamp, system_os_name, system_os_version, 
                    system_processes, system_users, processor_name,all_processor
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                data["server_ip"],
                data["timestamp"],
                data["system"]["os_name"],
                data["system"]["os_version"],
                json.dumps(data["system"]["processes"]),
                json.dumps(data["system"]["users"]),
                data["processor"]["name"],
                json.dumps(data["processor"])
            ))
            self.conn.commit()
            log.info(f"Data inserted successfully")

        except Exception as e:
            self.conn.rollback()  # Rollback the transaction in case of any error
            log.error(f"Error inserting data: {e}")

    def db_get_server_by_ip(self, ip_address):
        try:
            self.cursor.execute("SELECT * FROM server_info WHERE server_ip = %s;", (ip_address,))
            data = self.cursor.fetchall()
            if not data:
                return json.dumps({"message": "No data found for this IP.", "status_code": 404})
            # Convert data to a list of dictionaries
            columns = [desc[0] for desc in self.cursor.description]
            result = []
            for row in data:
                row_dict = {}
                for i, col in enumerate(columns):
                    row_dict[col] = row[i]
                result.append(row_dict)
            return result
        except Exception as e:
            log.error(f"Error retrieving server IPs: {e}")
            return None