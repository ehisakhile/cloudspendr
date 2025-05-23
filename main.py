from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def homepage():
    return {"status": "CloudSpendr Home"}

@app.get("/health")
def health_check():
    return {"status": "API is running"}