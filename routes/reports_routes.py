from logs.logs_file import logger
from fastapi import APIRouter
from utils.utils_file import *

route = APIRouter(prefix="/reports", tags=["reports"])

@route.get("/summery")
def get_summery():
    pass

@route.get("/missions-by-status")
def get_missions_by_status_r():
    pass

@route.get("/top-agent")
def get_top_agent():
    pass