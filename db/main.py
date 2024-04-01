from fastapi import FastAPI
import usuarios

app=FastAPI()

app.include_router(usuarios.route) 


@app.get("/")
async def inicio():
        return "Has iniciado correctamente el servidor"