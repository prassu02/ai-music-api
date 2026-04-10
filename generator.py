import numpy as np
from scipy.io.wavfile import write
import os
import uuid

NOTES = {
    "C": 261,
    "D": 294,
    "E": 329,
    "F": 349,
    "G": 392,
    "A": 440,
    "B": 493
}

def get_notes(prompt):
    prompt = prompt.lower()

    if "happy" in prompt:
        return ["C", "E", "G", "C"]
    elif "sad" in prompt:
        return ["A", "F", "D"]
    elif "birthday" in prompt:
        return ["C", "C", "D", "C", "F", "E"]
    else:
        return ["C", "D", "E", "F"]

def generate_music(prompt):
    notes = get_notes(prompt)

    sample_rate = 44100
    duration = 0.4
    audio = np.array([])

    for note in notes:
        freq = NOTES[note]
        t = np.linspace(0, duration, int(sample_rate * duration), False)

        tone = np.sin(2 * np.pi * freq * t)

        audio = np.concatenate((audio, tone))

    audio = audio / np.max(np.abs(audio))
    audio = (audio * 32767).astype(np.int16)

    os.makedirs("outputs", exist_ok=True)

    filename = f"outputs/music_{uuid.uuid4().hex[:6]}.wav"
    write(filename, sample_rate, audio)

    return filename