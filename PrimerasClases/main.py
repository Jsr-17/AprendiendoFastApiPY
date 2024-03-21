from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def primer():
    return "Hola mundo"

@app.get("/saludar")
async def saludo():
    return "Saludo compa"

@app.get("/json")
async def pruebaJson():
    return {"Hola mundo":"http://127.0.0.1:8000/saludar"}

@app.get("/prueba")
async def prueba():
        return "Funciona sin recargar"

