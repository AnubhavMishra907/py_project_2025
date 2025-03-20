import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(f"You said: {data}")
            return data.lower()
        except sr.UnknownValueError:
            print("Not Understanding")
            return ""
        except sr.RequestError:
            print("Request failed")
            return ""

def speechtx(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

def close_apps():
    os.system("taskkill /IM chrome.exe /F")  # Google Chrome बंद करने के लिए
    os.system("taskkill /IM firefox.exe /F")  # Firefox बंद करने के लिए

if __name__ == '__main__':
    speechtx("I am listening. Say stop to exit.")

    while True:
        command = sptext()

        if command in ["stop", "exit", "bye", "see you soon"]:
            speechtx("Okay, shutting down.")
            break

        elif "shut down all applications" in command:
            speechtx("Closing all applications.")
            close_apps()

        elif "your name" in command:
            speechtx("My name is Alisa Funandas")

        elif "how old are you" in command:
            speechtx("I'm 22 years old")

        elif "what's your number" in command:
            speechtx("I'm an AI assistant, I don't provide personal details.")

        elif "now what is the time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speechtx(f"The time is {time}")

        elif "where are you from" in command:
            speechtx("I'm from the United States of America, suna to hoga hi name...")

        elif "wikipedia" in command or "who is" in command or "what is" in command:
            query = command.replace("wikipedia", "").replace("who is", "").replace("what is", "").strip()
            speechtx("Searching on Wikipedia...")
            try:
                result = wikipedia.summary(query, sentences=2)
                speechtx(result)
            except wikipedia.exceptions.PageError:
                speechtx("Sorry, I couldn't find information on that.")
            except wikipedia.exceptions.DisambiguationError:
                speechtx("There are multiple results, please be more specific.")
            except Exception as e:
                speechtx("An error occurred while searching on Wikipedia.")
                print(e)

        elif "youtube" in command:
            speechtx("Opening YouTube")
            webbrowser.open("https://www.youtube.com/")
        
        elif "latest spacex video" in command:
            speechtx("Opening the latest SpaceX video")
            webbrowser.open("https://www.youtube.com/watch?v=hI9HQfCAw64&pp=ygUSc3BhY2V4IGxhdGVzdCB2aWRl")

        elif "google" in command:
            speechtx("Opening Google")
            webbrowser.open("https://www.google.com/")

        elif "facebook" in command:
            speechtx("Opening Facebook")
            webbrowser.open("https://www.facebook.com/")

        elif "amazon" in command:
            speechtx("Opening Amazon")
            webbrowser.open("https://www.amazon.com/")

        elif "chatgpt" in command:
            speechtx("Opening ChatGPT")
            webbrowser.open("https://chat.openai.com/")

        elif "openai" in command:
            speechtx("Opening OpenAI")
            webbrowser.open("https://www.openai.com/")

        else:
            speechtx("I didn't understand. Searching on Wikipedia...")
            try:
                result = wikipedia.summary(command, sentences=2)
                speechtx(result)
            except wikipedia.exceptions.PageError:
                speechtx("Sorry, no page found on Wikipedia.")
            except wikipedia.exceptions.DisambiguationError:
                speechtx("There are multiple results. Please be more specific.")
            except Exception as e:
                speechtx("An error occurred while searching on Wikipedia.")
                print(e)  # Debugging purpose
