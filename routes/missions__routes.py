from logs.logs_file import logger
from fastapi import APIRouter
from utils.utils_file import *
from database.mission_db import MissionDB
from database.agent_db import AgentDB

class_agent = AgentDB()
class_missions = MissionDB()

route = APIRouter(prefix="/missions", tags=["missions"])

@route.post("")
def create_mission_r(mission : mission):
    new_mission = mission.model_dump()
    result_creation = class_missions.create_missions(new_mission)
    return {"status" :200 , "result": result_creation}
    

@route.get("")
def get_all_missions_r():
    all_missions = class_missions.get_all_missions()
    return {"status" :200 , "result": all_missions}

@route.get("/{id}")
def get_mission_by_agent_id_r(id):
    my_mission = class_missions.get_mission_by_id(id)
    return {"status" :200 , "result": my_mission}

@route.put("/{mission_id}/assign/{agent_id}")
def assign_mission_to_agent(mission_id, agent_id):
    assignment_result = class_missions.assign_mission(mission_id, agent_id)
    return {"status" :200 , "result": assignment_result}

@route.put("/{id}/start")
def start_mission(id):
    logger.info("start func route")
    result_start = class_missions.update_mission_status(id, "in_progress")
    return {"status" :200 , "result": result_start}

@route.put("/{id}/complete")
def mission_complete(id):
    mission_complete = class_missions.update_mission_status(id, "completed")
    return {"status" :200 , "result": mission_complete}

@route.put("/{id}/fail")
def mission_fail(id):
    fail = class_missions.update_mission_status(id, "failed")
    return {"status" :200 , "result": fail}

@route.put("/{id}/cancel")
def mission_cancel(id):
    canceled = class_missions.update_mission_status(id, "canceled")
    return {"status" :200 , "result": canceled}



