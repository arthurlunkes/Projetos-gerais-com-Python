import speech_recognition as sr
import pyaudio

rec = sr.Recognizer()

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar agora")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print("O que você falou: " + texto)