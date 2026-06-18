from fastapi import FastAPI
from routes.agents_routes import route as agents_routes
from routes.missions__routes import route as missions__routes
from routes.reports_routes import route as reports_routes



app = FastAPI()

app.include_router(agents_routes)
app.include_router(missions__routes)
app.include_router(reports_routes)