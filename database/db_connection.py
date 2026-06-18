import mysql.connector
from logs.logs_file import logger
from utils.utils_file import *

class DB_connection:
    def __init__(self):
        self.config = {
            "host" : "localhost",
            "port" : 3306,
            "password" : 1234,
            "database" : "Intelligence_db"
            }
        self.connection = None
    def create_connection(self):
        if self.connection is None or  not self.connection.is_connected():
            self.connection =mysql.connector.connect(**self.config)
            return self.connection
        else:
            return self.connection
    
    def create_database():
        query = "create database  if not exists intelligence_db"
        run_query_dml(query)
        return "database created sucssefuly"

    def create_table_agents(self):
        query = "create table if not exists agents( id int primary key auto_increment, name varchar(70), specialty varchar(255), is_active boolean default True, completed_missions int default 0, failed_missions int default 0, agent_rank varchar(20));"
        run_query_dml(query)
        return "table agents created sucssefuly"
    
    def create_table_missions(self):
        query = "create table if not exists missions( id int primary key auto_increment, title varchar(100), description text, location varchar(255), difficulty int, importance int, status varchar(30) default 'new', risk_level varchar(50), assigned_agent_id int default null);"
        run_query_dml(query)
        return "table missions created sucssefuly"

