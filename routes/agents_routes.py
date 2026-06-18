from logs.logs_file import logger
from fastapi import APIRouter
from utils.utils_file import *
from database.agent_db import AgentDB
from database.mission_db import MissionDB

class_agents = AgentDB()

route = APIRouter(prefix="/agents", tags=["agents"])


@route.post("")
def create_agent_r(body : agent):
    new_body = body.model_dump()
    result_creation = class_agents.create_agent(new_body)
    return {"status" :200 , "result": result_creation}

@route.get("")
def get_all_agents_r():
    all_agent= class_agents.get_all_agent()
    return {"status" :200 , "result": all_agent}


@route.get("/{id}")
def get_agent_by_id_r(id):
    my_agent = class_agents.get_agent_by_id(id)
    return {"status" :200 , "result": my_agent}


@route.get("/{id}/performance")
def get_performance(id):
    agent_performance = class_agents.get_agent_performance(id)
    return {"status" :200 , "result": agent_performance}

@route.put("/{id}")
def update_agent(id : int, body : agent):
    data = body.model_dump()
    result_update = class_agents.update_agent(id, data)
    return {"status" :200 , "result": result_update}
    

@route.put("/{id}/deactivate")
def deactivate(id):
    deactivate_result = class_agents.agent_deactivate(id)
    return {"status" :200 , "result": deactivate_result}

