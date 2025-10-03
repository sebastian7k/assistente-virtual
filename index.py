import os 
os.system("cls")

import speech_recognition as sr

mic = sr.Recognizer()
with sr.Microphone() as source:
    mic.adjust_for_ambient_noise(source)
    print("Fale alguma coisa: ")
    try: 
        audio = mic.listen(source, timeout=5, phrase_time_limit=5)
        frase = mic.recognize_google(audio, language="pt-BR")
        print("Você disse: " + frase)
    except sr.WaitTimeoutError:
        print("Tempo esgotado, tente novamente")
    except sr.UnknownValueError:
        print("Não entendi o que você disse")