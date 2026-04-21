from fastapi import FastAPI
from agent.assistant import get_o2c_steps, explain_step

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SAP O2C Assistant Running"}

@app.get("/steps")
def steps():
    return {"o2c_steps": get_o2c_steps()}

@app.get("/explain/{code}")
def explain(code: str):
    return {"description": explain_step(code)}
