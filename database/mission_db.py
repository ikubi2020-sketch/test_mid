from logs.logs_file import logger
from utils.utils_file import *



class MissionDB:
    def create_missions(self,data):
        logger.info("active func | create_missions |")
        risk_level = risk_cumulation(data)
        logger.info("point")
        param = (data["title"], data["description"], data["location"], data["difficulty"], data["importance"], data["status"], risk_level)
        query = "insert into missions (title, description, location, difficulty, importance, status, risk_level) values(%s, %s, %s, %s, %s, %s, %s);"
        run_query_dml(query, param)
        logger.info("sucssefuly added mission")
        return ("sucssefuly added mission")
    
    def get_all_missions(self):
        logger.info("active func | get_all_missions |")
        query = "select * from missions;"
        all_agent = run_query_fetchall(query)
        logger.info("return all agents")
        return all_agent
    
    def get_mission_by_id(self, id):
        logger.info("active func | get_mission_by_id |")
        param = tuple(id)
        query = "select * from missions where id = %s;"
        mission = run_query_fetchone(query, param)
        logger.info(f"return mission id {id}")
        return mission

    def assign_mission(self, m_id, a_id):
        logger.info("active func | assign_mission |")
        valid_assignment(m_id, a_id)
        param = a_id, m_id
        query = "update missions set assigned_agent_id = %s where id = %s;"
        run_query_dml(query, param)
        logger.info("mission was assign to agent")
        return "mission was assign well"
    
    def update_mission_status(self, id, status):
        logger.info("active func | update_mission_status |")
        param = status, id
        query = "update missions set status = %s where id = %s;"
        run_query_dml(query, param)
        logger.info(f"mission {id} updated status to {status}")
        return "status update well"
    
    def get_open_missions_by_agent(self, id):
        logger.info("active func | get_open_missions_by_agent |")
        param = tuple(id)
        query = "select * from missions where id = %s and status = in_progress or assigned"
        all_agent_missions = run_query_fetchall(query, param)
        logger.info(f"return agent {id} open missions")
        return all_agent_missions
    
    def count_all_missions(self):
        logger.info("active func | count_all_missions |")
        query = "select count(*) from missions"
        all_missions_num  = run_query_fetchone(query)
        logger.info(f"return count of open missions {all_missions_num}")
        return all_missions_num
    
    def count_by_status(self, status):
        logger.info("active func | count_by_status |")
        param = tuple(status)
        query = "select count(*) as count_status from  missions where status = %s;"
        num_of_missions = run_query_fetchone(query, param)
        logger.info(f"return count mission by status {status}")
        count_final = num_of_missions["count_status"]
        return count_final

    def count_open_missions(self):
        logger.info("active func | count_open_missions |")
        query = "select count(*) from  missions where status = in_progress or assigned;"
        open_missions = run_query_fetchone(query)
        logger.info("return count of open missions")
        return open_missions
    
    def count_critical_missions(self):
        logger.info("active func | count_critical_missions |")
        query = "select count(*) from  missions where status = critical;"
        critical_missions_count = run_query_fetchone(query)
        logger.info("return count of critical missions")
        return critical_missions_count
    
    def get_top_agent(self):
        logger.info("active func | get_top_agent |")
        query_1 = "select max(completed_missions) as top from agents"
        max_completed = run_query_fetchone(query_1["top"])
        max_completed_t = tuple(max_completed)
        query_2 = "select agent from agents where completed_missions = %s;"
        top_agent = run_query_fetchone(query_2, max_completed_t)
        logger.info("return top agent")
        return top_agent
    
    def all_by_status(self):
        all_missions_by_status = {}
        a=MissionDB()
        new =a.count_by_status("new")
        assign =a.count_by_status("assign")
        in_progress = a.count_by_status("in_progress")
        completed =a.count_by_status("completed")
        failed = a.count_by_status("failed")
        canceled = a.count_by_status("canceled")
        all_missions_by_status["new"] = new
        all_missions_by_status["assign"] = assign
        all_missions_by_status["in_progress"] = in_progress
        all_missions_by_status["completed"] = completed
        all_missions_by_status["failed"] = failed
        all_missions_by_status["canceled"] = canceled
        return all_missions_by_status