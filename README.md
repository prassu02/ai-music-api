# AI Music Generator API

This project generates simple music from text prompts using FastAPI.
## Run
pip install -r requirements.txt
uvicorn app:app --reload
## API
POST /generate-music
Input:
{
  "prompt": "happy birthday tune"
}
