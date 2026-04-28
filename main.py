from fastapi import FastAPI

app = FastAPI()

#uv run fastapi dev

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/name/{name}")
def get_name(name: str):
    return {"message": f"Hello, {name}!"}

#Zweiter Endpunkt, bei dem Eine Zahl verdoppelt zurückgegeben wird

@app.get("/calc/{zahl}")
def get_zahl(zahl: int):
    return {"message": f"Doppelte zahl: {zahl*2}"}