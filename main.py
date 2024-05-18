import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Taking voice from system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')       #getting details of current voice

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


#speak function

def speak(text):
    """This function takes and returns voice
    Args: text (_type_): String
    """
    engine.say(text)
    engine.runAndWait()

#Speech recognization function
def takeCommand():
    """this function will recognize voice & return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    
if  __name__ == '__main__':
    print("Welcome to code")