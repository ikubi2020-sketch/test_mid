from logs.logs_file import logger
from fastapi import APIRouter
from utils.utils_file import *
from database.agent_db import AgentDB
from database.mission_db import MissionDB

class_agents = AgentDB()

route = APIRouter(prefix="/agents", tags="agents")


@route.post("")
def create_agent_r(body : agent):
    new_body = body.model_dump()
    result_creation = class_agents.create_agent(new_body)
    return {"status" :200 , "result": "agent created"}

@route.get("")
def get_all_agents_r():
    pass

@route.get("/{id}")
def get_agent_by_id_r(id):
    pass


@route.get("/{id}/performance")
def get_performance(id):
    pass


@route.put("/{id}")
def update_agent(body : agent):
    pass

@route.put("/{id}/deactivate")
def deactivate(id):
    pass
