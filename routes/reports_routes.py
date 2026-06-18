from logs.logs_file import logger
from fastapi import APIRouter
from utils.utils_file import *
from database.agent_db import AgentDB
from database.mission_db import MissionDB

class_missions = MissionDB()

route = APIRouter(prefix="/reports", tags=["reports"])

@route.get("/summery")
def get_summery():
    pass

@route.get("/missions-by-status")
def get_missions_by_status_r():
    all_by_status = class_missions.all_by_status()
    return {"status" :200 , "result": all_by_status}

@route.get("/top-agent")
def get_top_agent():
    top_agent = class_missions.get_top_agent()
    return {"status" :200 , "result": top_agent}