from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "ini default"}

@app.get("/login")
def root():
    return {"message": "ini login"}

@app.get("/home")
def root():
    return {"message": "ini home"}
