from typing import Dict, List
from fastapi import FastAPI , HTTPException, Response, status, Cookie, Depends, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from hashlib import sha256
import secrets

templates = Jinja2Templates(directory='templates')

class Patient(BaseModel):
    name: str
    surname: str


app = FastAPI()
app.counter: int = 0
app.token_counter: int = 0
app.storage: Dict[int, Patient] = {}
app.secret_key = 'ocbGtx7NnakRyGRKpjnakydXSdNIhlX7p71VUFuQ0ohuShkiAvSEOBFhz0gJxJki'
app.tokens_db = []
app.user = {'trudnY': 'PaC13Nt'}
security = HTTPBasic()


@app.get('/')
def hello():
    return{'message': 'Hello on / page'}



@app.get('/welcome')
async def welcome(request: Request, response: Response, session_token: str = Cookie(None)):
    if session_token not in app.tokens_db:
        raise HTTPException(status_code=401, detail="Unathorised")
    
    return templates.TemplateResponse("welcome.html", {"request": request, "user": "trudnY"})



# @app.get("/login")
@app.post("/login")
def read_current_user(response: Response,credentials: HTTPBasicCredentials = Depends(security)):
    for username, password in app.user.items():
        correct_username = secrets.compare_digest(credentials.username, username)
        correct_password = secrets.compare_digest(credentials.password, password)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    session_token = sha256(bytes(f"{credentials.username}{credentials.password}{app.secret_key}", encoding='utf8')).hexdigest()
    # if session_token in app.tokens_db:
    #     raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    app.tokens_db.append(session_token)
    response.set_cookie(key="session_token", value=session_token)
    response.status_code = status.HTTP_302_FOUND
    response.headers["Location"] = "/welcome"
    return response



# @app.get('/logout')
@app.post('/logout')
def logout(*, response: Response, session_token: str = Cookie(None)):
    print(session_token)
    if session_token not in app.tokens_db:
        raise HTTPException(status_code=401, detail="Unathorised")
    app.tokens_db.remove(session_token)
    response.status_code = status.HTTP_302_FOUND
    response.headers["Location"] = "/"






@app.post("/patient")
async def add_patient(patient: Patient,response: Response, session_token: str = Cookie(None)):
    if session_token not in app.tokens_db:
        raise HTTPException(status_code=401, detail="Unathorised")
    app.storage[app.counter] = patient
    response.headers["Location"] = f"/patient/{app.counter}"
    response.status_code = 302
    app.counter += 1
    return response

@app.get("/patient") 
def show_patient(response:Response, session_token: str = Cookie(None)):
    if session_token not in app.tokens_db:
        raise HTTPException(status_code=401, detail="Unathorised")
    if len(app.storage) == 0:
        raise HTTPException(status_code=204)
    return app.storage


@app.get("/patient/{pk}")
def show_patient(pk: int, response:Response, session_token: str = Cookie(None)):
    if session_token not in app.tokens_db:
        raise HTTPException(status_code=401, detail="Unathorised")
    if pk in app.storage:
        return app.storage.get(pk)
    else:
        raise HTTPException(status_code=204)


@app.delete("/patient/{pk}")
async def delete_patient(pk: int, response: Response, session_token: str = Cookie(None)):
    if session_token not in app.tokens_db:
        raise HTTPException(status_code=401, detail="Unathorised")
    if pk in app.storage:
        del app.storage[pk]
        response.headers["Location"] = "/patient"
        response.status_code = 204
        return response
    else:
        raise HTTPException(status_code=204)

