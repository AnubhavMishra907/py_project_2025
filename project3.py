import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknowValueError:
            print("Not Understand")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    
    if sptext().lower == "hay peter":
        data1=sptext().lower()

        if "your name" in data1:
            name="my name is peter"
            speechtx(name)
        elif "how old are you " in data1:
            age="I'm 22 yrs old"
            speechtx(age)