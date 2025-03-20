import pyttsx3 
import speech_recognition as sr
import datetime
import webbrowser  
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            print(f"You said: {data}")
            return data.lower()
        except sr.UnknownValueError:
            print("Not Understanding")
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    speechtx("I am listening. Say stop to exit.")

    while True:
        command = sptext()

        # **EXIT COMMANDS**
        if any(word in command for word in ["stop", "exit", "bye", "see you soon"]):
            speechtx("Okay, shutting down.")
            break  

        # **SHUT DOWN ALL APPLICATIONS**
        elif "shut down all applications" in command:
            speechtx("Closing all applications.")
            os.system("taskkill /F /IM chrome.exe")  
            os.system("taskkill /F /IM msedge.exe")  
            os.system("taskkill /F /IM firefox.exe")  

        # **GENERAL COMMANDS**
        elif "your name" in command:
            speechtx("My name is Alisa Funandas.")

        elif "how old are you" in command:
            speechtx("I'm 22 years old.")

        elif "what's your number" in command or "your number" in command:
            speechtx("I'm an AI assistant, I don't provide personal details.")

        elif "now what is the time" in command or "current time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speechtx(f"The time is {time}.")

        elif "where are you from" in command:
            speechtx("I'm from the United States of America, suna to hoga hi name.")

        # **OPEN WEBSITES**
        elif "youtube" in command:
            speechtx("Opening YouTube.")
            webbrowser.open("https://www.youtube.com/")

        elif "google" in command:
            speechtx("Opening Google.")
            webbrowser.open("https://www.google.com/")

        elif "facebook" in command:
            speechtx("Opening Facebook.")
            webbrowser.open("https://www.facebook.com/")

        elif "amazon" in command:
            speechtx("Opening Amazon.")
            webbrowser.open("https://www.amazon.com/")

        elif "chatgpt" in command:
            speechtx("Opening ChatGPT.")
            webbrowser.open("https://openai.com//")  

        elif "openai" in command:
            speechtx("Opening OpenAI.")
            webbrowser.open("https://www.openai.com/")

        else:
            speechtx("hello hardik what can i help you.")
