import pandas as pd 
from pathlib import Path
import os
import whisper

file_list = [file for file in os.listdir(AUDIO_DIR) if file.endswith('.mp3')]
file_list

model = whisper.load_model("base")

corpus = [] 
for file_name in file_list :
    result = model.transcribe(f"{AUDIO_DIR}{file_name}")
    corpus.append(result["text"])
