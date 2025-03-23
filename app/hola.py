from fastapi import FastAPI

app =FastAPI()

@app.get("/")
def read_root():
    return{"message":"Hola"}

@app.get("/hola_mama")
def read_hello():
    return{"message":"Hi there"}