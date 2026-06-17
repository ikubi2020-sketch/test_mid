from fastapi import FastAPI, HTTPException
import _mysql_connector
from utils.logs import logger
from database.db_connection import DB_connection

class_connection = DB_connection()

def run_query_dml(query, params = None):
    logger.info("active func | run_query_dml |")
    connection = class_connection.create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, params)
    cursor.close()
    connection.commit()
    return None

def run_query_fetchall(query, params = None):
    logger.info("active func | run_query_fetchall |")
    connection = class_connection.create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result


def run_query_fetchone(query, params = None):
    logger.info("active func | run_query_fetchone |")
    connection = class_connection.create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchone()
    cursor.close()
    return result

def ____():
    logger.info("active func |  |")
    query = "" 
    try:
            logger.info("")
    except Exception as e:
        raise HTTPException (status_code = 400, detail={"message" : f"reach error {e}" })
