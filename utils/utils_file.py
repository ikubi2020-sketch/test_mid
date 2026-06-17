from fastapi import FastAPI, HTTPException
import mysql.connector
from utils.logs import logger
from database.db_connection import DB_connection
from typing import Literal
from pydantic import BaseModel,  Field



class_connection = DB_connection()

def run_query_dml(query, params = None):
    try:
        logger.info("active func | run_query_dml |")
        connection = class_connection.create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        connection.commit()
        cursor.close()
        return None
    except Exception as e:
        logger.error(f"reach error {e}")
        raise HTTPException (status_code = 400, detail={"message" : f"reach error {e}" })
    finally:
         cursor.close


def run_query_fetchall(query, params = None):
    try:
        logger.info("active func | run_query_fetchall |")
        connection = class_connection.create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Exception as e:
        logger.error(f"reach error {e}")
        raise HTTPException (status_code = 400, detail={"message" : f"reach error {e}" })
    finally:
         cursor.close

def run_query_fetchone(query, params = None):
    try:
        logger.info("active func | run_query_fetchone |")
        connection = class_connection.create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchone()
        return result
    except Exception as e:
        logger.error(f"reach error {e}")
        raise HTTPException (status_code = 400, detail={"message" : f"reach error {e}" })
    finally:
         cursor.close


class agent(BaseModel):
    name : str = Field(min_length=2, max_length=50)
    specialty : str = Field(min_length=2, max_length=255)
    is_active : bool = Field(default=True)
    completed_missions : int = Field(default=0)
    failed_missions : int = Field(default=0)
    agent_rank : str = Field(Literal["Junior", "Senior", "Commander"])

class mission(BaseModel):
    title : str = Field(min_length=2, max_length=50)
    description : str
    location : str = Field(min_length=2, max_length=255)
    difficulty : int = Field(ge=1, le=10)
    importance : int = Field(ge=1, le=10)
    status : str = Field(default="new")
    risk_level : str = Field(max_length=30)
    assigned_agent_id : str =Field(default=None)


