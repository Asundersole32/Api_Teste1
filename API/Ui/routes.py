from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from Models import token_model, actors, users
from Application import route_functions
from Persistence import data_manipulation

from Application import security
from datetime import timedelta

from typing import Annotated

routers = APIRouter()


@routers.get("/")
async def presentation():
    return route_functions.presentation_function()


@routers.post("/token", response_model=token_model.Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = security.authenticate_user(data_manipulation.user_manipulation_r(), form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=security.accessTokenExpireMinutes)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@routers.get("/users/me/", response_model=users.User)
async def read_users_me(
    current_user: Annotated[users.User, Depends(security.get_current_active_user)]
):
    return current_user


@routers.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[users.User, Depends(security.get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]

@routers.post("/worker")
async def worker_cad(worker: actors.Worker):
    return "Em construção"

@routers.post("/Administrators")
async def adm_cad(adm: actors.Administrator, worker_id):
    return "Em construção"

@routers.post("/Engeneers")
async def eng_cad(eng: actors.Engineers, worker_id):
    return "Em construção"

@routers.post("/Commons")
async def commons_cad(com: actors.Common, worker_id):
    return "Em construção"