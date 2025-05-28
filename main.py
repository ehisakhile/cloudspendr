from fastapi import FastAPI
from routes.users import router as users_router


app = FastAPI()

@app.get("/")
def homepage():
    return {"status": "CloudSpendr Home"}

@app.get("/health")
def health_check():
    return {"status": "API is running"}

app.include_router(users_router)