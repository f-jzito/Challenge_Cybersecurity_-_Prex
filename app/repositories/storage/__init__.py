import psycopg2

from app.helpers.logger import log
import json
from config import Config

def dbinit():
    # Database connection details (replace with your actual credentials)
    conn = psycopg2.connect(
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        host=Config.DB_HOST,
        port=Config.DB_PORT
    )

    cursor = conn.cursor()
    #ONLY FOR MIGRATIONS
    db_create(cursor, conn)
    return conn, cursor

def db_create(cursor, conn):
    try:
        cursor.execute("BEGIN;")

        cursor.execute("""CREATE TABLE IF NOT EXISTS server_info (
                server_ip VARCHAR(255) NOT NULL,
                timestamp VARCHAR(255) NOT NULL,
                system_os_name VARCHAR(255),
                system_os_version VARCHAR(255),
                system_processes JSONB,
                system_users JSONB,
                processor_name VARCHAR(255),
                processor_cpu_cores_per_package INT,
                processor_cpu_core_count INT,
                processor_cpu_logical_per_package INT,
                processor_cpu_thread_count INT,
                processor_cpu_brand_string VARCHAR(255),
                PRIMARY KEY (server_ip, timestamp)
        );""")

        conn.commit()  # Commit the changes to the database
    except psycopg2.errors.UniqueViolation as e:  # Catch duplicate key errors
        conn.rollback()  # Rollback the transaction in case of error
        log.error(f"Error inserting data: {e}")

    except psycopg2.Error as e:
        # Catch other PostgreSQL errors
        conn.rollback()  # Rollback the transaction
        log.error(f"Error inserting data: {e}")
        return {'error': 'An error occurred while inserting data', 'status_code': 500}

    log.info(f"Table created successfully.")
    return {'message': 'Data inserted successfully', 'status_code': 200}