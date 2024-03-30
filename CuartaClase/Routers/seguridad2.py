from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt

router=APIRouter()

oauth2=OAuth2PasswordBearer(tokenUrl="login")

class Usuario(BaseModel):
    nombre:str
    nombreCompleto:str
    email:str
    habilitado:str

class UserDB(Usuario):
    contrasena:str


usuarios_DB={
    "jose":{
        "nombre":"Jose ",
        "nombreCompleto":"boloneo Ramirez",
        "email":"Jarmoreno5",
        "habilitado":False,
        "contrasena":"12345678"
    },
    "jose_2":{
        "nombre":"Jose ",
        "nombreCompleto":"Marp Pierre",
        "email":"Letsgo@gmail.com",
        "habilitado":False,
        "contrasena":"12345678"
    },
}