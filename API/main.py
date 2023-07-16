from fastapi import FastAPI

from Ui import routes

app = FastAPI()
app.include_router(routes.routers)
