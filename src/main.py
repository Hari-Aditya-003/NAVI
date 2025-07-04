from fastapi import FastAPI
from core.routes import router
from db import Base, SQL_ENGINE

app = FastAPI()

# Include your API router
app.include_router(router)

# If you need to create tables on startup
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=SQL_ENGINE)