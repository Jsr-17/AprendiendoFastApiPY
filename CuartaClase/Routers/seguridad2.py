from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime,timedelta

Algoritmo="HS256"
ACCESS_TOKEN_DURATION= 1
SECRET="lkasd3221343jk345l2;q3kkj223"

crypt = CryptContext(schemes=["bcrypt"])

router=APIRouter()

oauth2=OAuth2PasswordBearer(tokenUrl="login2")

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
        "contrasena":"$2a$12$6ueMSV6iwNeAzB4mABxX/.2caNRq37tbk2/mR4GyG/g01E2rdJcZa"
    },
    "jose_2":{
        "nombre":"Jose ",
        "nombreCompleto":"Marp Pierre",
        "email":"Letsgo@gmail.com",
        "habilitado":False,
        "contrasena":"$2a$12$6ueMSV6iwNeAzB4mABxX/.2caNRq37tbk2/mR4GyG/g01E2rdJcZa"
    },
}

def buscarUsuarioBaseDatos(nombre:str):
    if nombre in usuarios_DB:
        return UserDB(**usuarios_DB[nombre])

def buscarUsuario(nombre:str):
    if nombre in usuarios_DB:

        return Usuario(**usuarios_DB[nombre])

@router.post("/login2")
async def login(form:OAuth2PasswordRequestForm= Depends()):

    usuario_DB=usuarios_DB.get(form.nombre)

    if not usuario_DB:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail="El usuario no es correcto"
        )
    
    usuario=buscarUsuarioBaseDatos(form.nombre)

    if not crypt.verify(form.contrasena,usuario.contrasena):

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail="La contrasena no es correcta "
        )
    
    access_token={
        "sub":usuario.nombre,
        "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }
    return {"access_token":jwt.encode(access_token,algorithm=Algoritmo),"token_type":"bearer"}