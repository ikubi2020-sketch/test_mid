system ruining commends :

run the following  commends to run the program

docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234  -e MYSQL_DATABASE=Intelligence_db -p 3306:3306 mysql:8.0

git clone
https://github.com/ikubi2020-sketch/test_mid.git

pip install -r requirements.txt


program purpose :

the program is managing a unit name ShadowNet . 
the unit has agent un a different levels and missions in different levels .
our goal is to have a system that hold in a database all agents and  all mission.
the program can change details in the database using a remote commends 
using the system we can manege all details of all agents and missions , assign missions to agents, and maintain track of record of all of them.
using the system we can get all details on any  mission or agent , and make sure assignment is being done in a controlled way .



stractur of files :
(basic)

intelligence-task-manager  
├── database/
│ ├── db_connection.py
│ ├── agent_db.py
│ └── mission_db.py
├── README.md
├── requirements.txt
└── .gitignore
utils
    logs
    utils_file


intelligence-task-manager  = directory ::: the directory that hold all the project   

database = directory ::: hold all interaction with the database (including making new one and tables)
db_connection = file ::: hold the connection to the database and creation of tablas and database
agent_db = file ::: hold interaction with the database when it comes to the running details of agents 
mission_db = file ::: hold interaction with the database when it comes to the running details of missions

utils = directory  ::: hold serves function and logger
logs = file ::: hold connection to the logger  
utils_file = file ::: holds all validation and run_query functions and more helping  function

README = file ::: this file . hold explanations on the program

requirements = file ::: hold all library and the specific version of this program 

gitignore = file ::: save space in git 

tables :

table 1 . agents :

field = id INT, AUTO_INCREMENT, primary key  ::: hold agent uniq id across all table 
field = name VARCHAR(50)    :::       hold agent name
field  = specialty VARCHAR(255)  ::: hold agent specialty , (the things he focus on)
field =  is_active boolean default True ::: hold if the agent is cogently active and can be assign with missions
field = completed_missions int default 0 ::: hold how many missions whore successfully  done by this agent 
field =  failed_missions int default 0 ::: hold how many missions whore unsuccessfully  done by this agent 
field = agent_rank varchar(10) ::: hold how agent rank only Junior / Senior / Commander

table 2 missions :

field = id INT, AUTO_INCREMENT primary key :::hold mission uniq id
field = title varchar(100) ::: hold mission's name
field =  description text ::: hold the description of the mission
field = location varchar(100) :::  hold mission's location 
field = difficulty int 10-1 ::: hold how difficult is the mission
field = importance  int 10-1 ::: hold how important is the mission 
field = status varchar(20) default new ::: hold information of the mission status 
field = risk_level varchar(20) ::: hold how risky is the mission , automatic being fil , the formula is difficulty * 2 + importance = risk_level
field = assigned_agent_id int default null ::: hold how is doing the mission

classes and methods and what they do 

class connection_db

connection_get() = create and return the connection with database
database_create() = create DB if not exists
tables_create() = create table if not exists

class AgentDB

create_agent(data) =  add  a new agent to the system
get_all_gents() = return all agents in DB
get_agent_by_id(id) = return one agent by id
update_agent(id, data) = update existing agent's details (across all field)
agent_deactivate() = change agent to not active
completed_increment() = update number of missions completed successfully by increment of one
failed_increment(id) = update number of missions completed unsuccessfully by increment of one
get_agent_performance(id) = return a dict holding total mission done by an agent and failed  and completed and success rate 
agents_active_count() = return sum of  active agents

class MissionDB 

mission_create(data) = add a new mission to DB
all_get_missions() = return all missions in database
get_mission_by_id(id) = return one mission by id or None 
assign_mission(m_id, a_id) = assign a mission to agent
update_mission_status(id, status) = change a mission's  status 
get_open_missions_by_agent(id) = return agents missions 
count_all_missions() = return number of all missions
count_by_status(status) = return how many missions in specific status
count_open_missions() = return all  open missions
count_critical_missions =  return all  critical missions
get_top_agent = return agent with the highest completed_missions



system laws :
1: rank must be  Junior  Senior or Commander
2: Commander / importance . ust be between 1  to 10
3: level_risk is automatically being done and does not comes from the user 
4: if is_active is False , agent can not be assign  with missions
5: an agent can not have more then 3 missions at the same time
6: if risk_level is critical only an agent in level commender can be assign to it
7: a mission can be assign if status is new 
8: a mission must be assigned before being in progress 
9:  a mission must be in_progress in order to be canceled 
10: mission can be canceled only if status is assigned or new 
i






