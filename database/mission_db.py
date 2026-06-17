from utils.logs import logger
from utils.utils_file import *

class MissionDB:
    def create_missions(data):
        logger.info("active func | create_missions |")
        param = (data["title"], data["description"], data["location"], data["difficulty"], data["importance"], data["status"], data["risk_level"], data["assigned_agent_id"])
        query = "insert into missions (title, description, location, difficulty, importance, status, risk_level, assigned_agent_id);"
        run_query_dml(query, param)
        logger.info("sucssefuly added mission")
        return ("sucssefuly added mission")
    
    def get_all_missions():
        logger.info("active func | get_all_missions |")
        query = "select * from missions;"
        all_agent = run_query_fetchall(query)
        logger.info("return all agents")
        return all_agent
    
    def get_mission_by_id(id):
        logger.info("active func | get_mission_by_id |")
        logger.info("active func | get_mission_by_id |")
        param = tuple(id)
        query = "select * from missions where id = %s;"
        mission = run_query_fetchone(query, param)
        logger.info(f"return mission id {id}")
        return mission

    def assign_mission(m_id, a_id):
        logger.info("active func | assign_mission |")
        param = a_id, m_id
        query = "updated missions set assigned_agent_id = %s where id = %s;"
        run_query_dml(query, param)
        logger.info("mission was assign to agent")
        return "mission was assign well"
    
    def update_mission_status(id, status):
        logger.info("active func | update_mission_status |")
        param =  status, id
        query = "updated missions set status = %s where id = %s;"
        run_query_dml(query, param)
        logger.info(f"mission {id} updated status to {status}")
        return "status update well"
    
    def get_open_missions_by_agent(id):
        logger.info("active func | get_open_missions_by_agent |")
        param = tuple(id)
        query = "select * from missions where id = %s and status = in_progress or assigned"
        all_agent_missions = run_query_fetchall(query, param)
        logger.info(f"return agent {id} open missions")
        return all_agent_missions
    
    def count_all_missions():
        logger.info("active func | count_all_missions |")
        query = "select count(*) from missions"
        all_missions_num  = run_query_fetchone(query)
        logger.info(f"return count of open missions {all_missions_num}")
        return all_missions_num
    
    def count_by_status(status):
        logger.info("active func | count_by_status |")
        param = tuple(status)
        query = "select count(*) from  missions where status = %s;"
        num_of_missions = run_query_fetchone(query, param)
        logger.info(f"return count mission by status {status}")
        return num_of_missions

    def count_open_missions():
        logger.info("active func | count_open_missions |")
        query = "select count(*) from  missions where status = in_progress or assigned;"
        open_missions = run_query_fetchone(query)
        logger.info("return count of open missions")
        return open_missions
    
    def count_critical_missions():
        logger.info("active func | count_critical_missions |")
        query = "select count(*) from  missions where status = critical;"
        critical_missions_count = run_query_fetchone(query)
        logger.info("return count of critical missions")
        return critical_missions_count
    
    def get_top_agent():
        logger.info("active func | get_top_agent |")
        query_1 = "select max(completed_missions) from agents"
        max_completed = run_query_fetchone(query_1)
        max_completed_t = tuple(max_completed)
        query_2 = "select agent from agents where completed_missions = %s;"
        top_agent = run_query_fetchone(query_2, max_completed_t)
        logger.info("return top agent")
        return top_agent
