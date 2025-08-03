from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    load_dotenv(dotenv_path="config/.env")
    host = os.environ["HOST"]
    port = int(os.environ["PORT"])
    uvicorn.run(app, host=host, port=port)