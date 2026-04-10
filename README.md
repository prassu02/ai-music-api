# AI Music Generator API

This project generates simple music from text prompts using FastAPI.

## Run
pip install fastapi uvicorn numpy scipy
python -m uvicorn app:app --reload
pip install -r requirements.txt

## API
POST /generate-music

Input:
{
  "prompt": "happy birthday tune"
}
