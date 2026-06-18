
from logs.logs_file import logger
from utils.utils_file import *

class AgentDB:
    def create_agent(self, data):
        logger.info("active func | create_agent |")
        param = (data["name"], data["specialty"], data["is_active"], data["completed_missions"], data["failed_missions"], data["agent_rank"])
        query = "insert into agents (name, specialty, is_active, completed_missions, failed_missions, agent_rank) values(%s, %s, %s, %s, %s, %s);"
        run_query_dml(query, param)
        return "agent was added"
    
    def get_all_agent(self):
        logger.info("active func | get_all_agent |")
        query = "select * from agents;"
        all_agent = run_query_fetchall(query)
        return all_agent
    
    def get_agent_by_id(self, id):
        logger.info("active func | get_agent_by_id |")
        param = tuple(id)
        query = "select * from agents where id = %s;"
        agent = run_query_fetchone(query, param)
        return agent
    
    def update_agent(self, id, data):
        logger.info("active func | update_agent |")
        param = (data["name"], data["specialty"], data["is_active"], data["completed_missions"], data["failed_missions"], data["agent_rank"], id)
        query = "update agents set name = %s, specialty = %s, is_active = %s, completed_missions= %s, failed_missions = %s, agent_rank = %s where id = %s;"
        run_query_dml(query, param)
        return "agent was updated"
    
    def agent_deactivate(self, id):
        logger.info("active func | agent_deactivate |")
        param = tuple(id)
        query = "update agents set is_active = False where id = %s;"
        run_query_dml(query, param)
        return "agent was deactivated"
    
    def completed_increment(self, id):
        logger.info("active func | completed_increment |")
        param = tuple(id)
        query = "update agents set completed_missions = completed_missions + 1 where id = %s;"
        run_query_dml(query, param)
        return  "agent missions completed count were updated"
    
    def failed_increment(self, id):
        logger.info("active func | failed_increment |")
        param = tuple(id)
        query = "update agents set failed_missions = failed_missions + 1 where id = %s;"
        run_query_dml(query, param)
        return  "agent missions failed count were updated"
    
    def get_agent_performance(self, id):
        logger.info("active func | get_agent_performance |")
        agent_performance = {}
        param = tuple(id)
        query_1 = "select count(assigned_agent_id) as total from missions where assigned_agent_id = %s;"
        query_2 = "select completed_missions as complete  from agents where id = %s;"
        query_3 = "select failed_missions as failed from agents where id = %s;"
        total = run_query_fetchone(query_1, param)
        completed_missions = run_query_fetchone(query_2, param)
        failed_missions = run_query_fetchone(query_3, param)
        try :
            agent_performance["total"] = total["total"]
            agent_performance["completed_missions"] = completed_missions["complete"]
            agent_performance["failed_missions"] = failed_missions["failed"]
            if  agent_performance["total"]== 0:
                agent_performance["success_rate"] = 0
            else:
                agent_performance["success_rate"] = (agent_performance["completed_missions"] /agent_performance["total"]) * 100 
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException (status_code = 400, detail={"message" : f"reach error {e}" })
        return agent_performance
    
    def agents_active_count(self):
        logger.info("active func | agents_active_count |")
        query = "select count(is_active) from agent where is_active = true"
        active_agent = run_query_fetchone(query)
        return active_agent
