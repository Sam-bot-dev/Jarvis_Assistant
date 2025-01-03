from plyer import notification
import pyttsx3 
import speech_recognition as sr
import pyjokes
import datetime
import webbrowser
import random
import datetime
import pyautogui
#lib
engine= pyttsx3.init()# to initiate the engine.
def speak(audio):
  engine.say(audio)
  engine.runAndWait()
def greet():
  hour=int(datetime.datetime.now().hour)
  if hour<12:
    speak("Good Morning")
    print("Good Morning")
  elif hour<18:
    speak("Good Afternoon")
    print("Good Afternoon")
  else:
    speak("Good Evening")
    print("Good Evening")
    speak("I am Jarvis, your personal assistant. How can I help you today?")
    print("I am Jarvis, your personal assistant. How can I help you today?")

def command():
  content=" "
  while content ==" ":
    r=sr.recognizer()
    with sr.microphone() as source:
      r.pause_threshold=1
      r.energy_threshold=4000
      r.dynamic_enegy_threshold=True
      print("say somthing")
      audio=r.listen(source)
    try:
      content=r.recognize_google(audio,language="en-IN")
      print("you said....  " + content )
      return content
    except sr.RequestError as e:
      print("please try again")

def main_process():
  greet()
  url_yt="https://www.youtube.com/"
  url_g="https://www.google.co.in/"
  url_github="https://github.com/"
  while True:
    pass
    