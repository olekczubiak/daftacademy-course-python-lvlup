from typing import Dict, List
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel


app = FastAPI()
app.counter = -1
app.patients = {}

# Zadanie 1
@app.get('/')
def hello_world():
    return {"message": "Hello World during the coronavirus pandemic!"}

# Zadanie 2
@app.get("/method")
def method_get():
    return {"method": "GET"}

@app.post("/method")
def method_post():
    return {"method": "POST"}

@app.delete("/method")
def method_delete():
    return {"method": "DELETE"}

@app.put("/method")
def method_put():
    return {"method": "PUT"}

class PatientRq(BaseModel):
    name: str
    surename: str

# Zadanie 3-4
class PatientResp(BaseModel): 
    id: int
    patient: Dict

@app.post("/patient", response_model=PatientResp)
async def receive_something(*,rq: PatientRq):
    app.counter += 1
    rq_dict = rq.dict()
    app.patients[app.counter] = rq_dict
    return PatientResp(id=app.counter,patient=rq.dict())

@app.get("/patient/{id}")
def hello_name(id: int):
    try:
        return app.patients[id]
    except  Exception:
        raise HTTPException(status_code=204, detail="No Content")

@app.get("/test")
def patients_list():
    return app.patients
