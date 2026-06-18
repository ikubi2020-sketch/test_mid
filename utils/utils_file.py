from fastapi import FastAPI, HTTPException
import mysql.connector
from logs.logs_file import logger
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
    assigned_agent_id : str =Field(default=None)



def risk_cumulation(data):
    risk = data["difficulty"] * 2 = data["importance"]
    if risk < 10:
        risk = "low"
    elif risk < 17:
        risk = "medium"
    elif risk < 24:
        risk = "high"
    else:
        risk = "critical"
    return risk


def valid_assignment(m_id, a_id):
    param_1 = tuple(a_id)
    query_1 = "select * from agents where id = %s"
    the_agent = run_query_fetchone(query_1, param_1)
    param_2 = tuple(m_id)
    query_2 = "select * from missions where id = %s"
    the_mission = run_query_fetchone(query_2, param_2)
    query_3 ="select count(*) from missions where assigned_agent_id = %s"
    missions_count = run_query_fetchone(query_3, param_1)
    if the_agent == None:
         raise HTTPException(status_code=404 , detail={"error": "agent not found"})
    if the_mission == None:
        raise HTTPException(status_code=404 , detail={"error": "mission not found"})
    if the_mission["risk_level"] == "critical" and the_agent["agent_rank"] != "commander":
        raise HTTPException(status_code=400 , detail={"error": "Only Commander can handle critical missions"})
    if the_mission["status"] != "new":
        raise HTTPException(status_code=400 , detail={"error":"Mission not available"})
    if the_agent["is_active"] != True:
        raise HTTPException(status_code=400 , detail={"error":"Agent is not active"})
    if missions_count >= 3:
        raise HTTPException(status_code=400 , detail={"error":"Agent has too many missions"})
    








