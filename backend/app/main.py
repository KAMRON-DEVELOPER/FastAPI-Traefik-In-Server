from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get(path="/", tags=["root"])
async def root():
    return {"status": "🚀"}


@app.get(path="/health", tags=["check health"])
async def health_check():
    return {"status": "healthy"}
