from fastapi import FastAPI
from routes.users import router as users_router
from config.database import Base, engine                ##SOPIA,MAGGIE&EKON
from models import users                                ##SOPIA,MAGGIE&EKON

app = FastAPI()

@app.get("/")
def homepage():
    return {"status": "CloudSpendr Home"}

@app.get("/health")
def health_check():
    return {"status": "API is running"}

app.include_router(users_router)



##===================================================================================================
#to Auto create tables cos i ran my code and no user tables was found in te db ##SOPIA,MAGGIE&EKON
##=================================================================================================
Base.metadata.create_all(bind=engine)
