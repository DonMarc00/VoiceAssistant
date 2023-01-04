import warnings
import pyttsx3
import speech_recognition as sr

from gtts import gTTS
import playsound
import os
import datetime
import calendar

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 130)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def rec_audio():
    recog = sr.Recognizer()


    with sr.Microphone() as source:
        # For Noise: Microphone can't differentiate between noise and speech well
        recog.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("Du sagtest: " + data)

    except sr.UnknownValueError:
        print("Ich habe nicht verstanden, was du gesagt hast")

    except sr.RequestError as ex:
        print("Request error from Google Speech Recognition " + ex)

    return data


def response(text):
    print(text)

    tts= gTTS(text=text, lang="en")

    audio = "Audio.mp3"
    # Creates a file named audio.mp3
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)


def call(text):
    action_call = "boss"

    text = text.lower()

    if action_call in text:
        return True

    return False


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months=[
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st"
    ]

