from fastapi import FastAPI
from pydantic import BaseModel
from generator import generate_music
from fastapi.responses import FileResponse

app = FastAPI()

class MusicRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/generate-music")
def generate(req: MusicRequest):
    file_path = generate_music(req.prompt)

    return {
        "result": file_path
    }

@app.get("/download")
def download(file: str):
    return FileResponse(file, media_type="audio/wav")