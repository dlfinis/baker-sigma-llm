from langchain_community.llms import Ollama
import gradio as gr
import json
import whisper
import torch

def get_language(country, file):
    with open(file, 'r') as f:
        data = f.read()
    return data
    
def get_examples(file):
    with open(file, 'r') as f:
        data = f.read()
    return data

def llm(task, country, number):
    llm = Ollama(model="deepseek-r1")
    lang = get_language(country, file="utils/country_languages.json")
    few_shot = get_examples(file="utils/few_shot_examples.json")
    context = f"You are a helpful assistant. You give an enumerated list of phrases. You answer concisely and only in {lang}"
    icl = f"For example, {few_shot}"
    query = f"I'm traveling to {country}. Which {number} most popular phrases should I learn to {task}?"
    phrases = llm.invoke(context+icl+query)
    return phrases

def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    audio = whisper.load_audio(audio_file, sr=16000)
    audio_tensor = torch.from_numpy(audio).to(torch.float32)
    result = model.transcribe(audio_tensor, fp16=False)['text']
    return result

def match_task(text, audio):
    if text and audio:
        return text
    elif text:
        return text
    elif audio:
        return transcribe_audio(audio)
    else:
        return ReferenceError("Please provide either text or audio input")


if __name__ == "__main__":
