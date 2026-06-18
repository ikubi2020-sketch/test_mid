from logs.logs_file import logger
from fastapi import APIRouter
from utils.utils_file import *

route = APIRouter(prefix="/missions", tags=["missions"])

@route.post("")
def create_mission_r(mission : mission):
    pass

@route.get("")
def get_all_missions_r():
    

@route.get("/{id}")
def get_mission_by_agent_id_r(id):
    pass

@route.put("/{id}/assign/{agent_id}")
def  assign_mission_to_agent(id, agent_id):
    pass

@route.put("/{id}/start")
def start_mission(id):
    pass

@route.put("/{id}/complete")
def mission_complete(id):
    pass

@route.put("/{id}/fail")
def mission_fail(id):
    pass

@route.put("/{id}/cancel")
def mission_cancel(id):
    pass

