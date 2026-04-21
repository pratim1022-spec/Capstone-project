from fastapi import FastAPI, HTTPException
from agent.assistant import get_all_steps, get_step_details, simulate_order_flow

app = FastAPI(
    title="SAP O2C API",
    description="Simulates SAP Order-to-Cash Process",
    version="1.0"
)


@app.get("/")
def home():
    return {"message": "SAP O2C API is running"}


@app.get("/steps")
def steps():
    return {"steps": get_all_steps()}


@app.get("/steps/{code}")
def step_info(code: str):
    data = get_step_details(code)
    if data["description"] == "Not found":
        raise HTTPException(status_code=404, detail="Invalid SAP Code")
    return data


@app.post("/simulate")
def simulate(customer: str, material: str, qty: int):
    if qty <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be > 0")

    result = simulate_order_flow(customer, material, qty)
    return result
