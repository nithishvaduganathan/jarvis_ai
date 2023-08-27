
import pyttsx3
import warnings
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound  # Fixed import
import os
import datetime
import calendar
import random
import wikipedia
import pygame
import tempfile
import webbrowser
import ctypes
import winshell
import subprocess
import pyjokes
import smtplib
import requests
import json
from twilio.rest import Client






warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Assistant could not understand the audio.")
    except sr.RequestError as ex:
        print("Request Error with Google Speech Recognition: " + str(ex))

    return data


def response(text):
    print(text)
    talk(text)
    tts = gTTS(text=text, lang="en")

    # Use a temporary file to store the audio
    _, temp_audio_path = tempfile.mkstemp(suffix=".mp3")
    tts.save(temp_audio_path)

    pygame.mixer.init()
    pygame.mixer.music.load(temp_audio_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()

    os.remove(temp_audio_path)

def call(text):
    action_call = "jarvis"
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

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    ordinals = [
        '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th',
        '9th', '10th', '11th', '12th', '13th', '14th', '15th',
        '16th', '17th', '18th', '19th', '20th', '21st', '22nd',
        '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st'
    ]
    return f"Today is {week_now}, {months[month_now - 1]} the {ordinals[day_now - 1]}."

def say_hello(text):
    greet = [
        "hello", "hi", "hay", "hey there", "jarvis", ""
    ]
    response_list = [
        "Hello", "Hi", "yes Boss", "Hey there", "good to see you boss " , "how can help you"
    ]
    for word in text.split():
        if word.lower() in greet:
            return random.choice(response_list) + "."
    return ""

# ... (your existing imports and code)

def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 2 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] +" "+ list_wiki[i + 3]

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    mail1 = str(input("enter your mail:"))
    password = str(input("enter your mail password :"))
    mail2 = str(input("enter TO mail:"))
    server.login(mail1, password )
    server.mail( mail2 , to, content)
    server.close()


while True:
    try:
        text = rec_audio()
        speak = ""

        if call(text):
            speak += say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                 get_today = today_date()
                 speak += " " + get_today

            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = "p.m" if now.hour >= 12 else "a.m"
                hour = now.hour - 12 if now.hour >= 12 else now.hour
                minute = "0" + str(now.minute) if now.minute < 10 else str(now.minute)
                speak += f" It is {hour}:{minute} {meridiem}."

            elif "wikipedia" in text.lower():
                if "who is" in text.lower():
                    person = wiki_person(text)
                    if person:
                        try:
                            wiki_summary = wikipedia.summary(person, sentences=2)
                            speak += " " + wiki_summary
                        except wikipedia.exceptions.DisambiguationError as disambiguation_err:
                            speak += " " + "Could not determine the specific person. Please provide more context."
                        except wikipedia.exceptions.PageError as page_err:

                            speak += " " + "Could not find information about that person."


            elif "who are you" in text.lower() or "define yourself" in text.lower():
                speak = speak + """I am jarvis , an AI language model developed by tony stark.
                 I'm here to assist you by providing information, answering questions,
                  generating text,
                 and engaging in conversations on a wide range of topics.
                  Is there something specific you would like to know or discuss?"""


            elif "your name" in text:
                speak = speak + "my name jarvis"

            elif "who am i" in text:
                speak = speak + "you must probably be a humen "

            elif "how are you " in text:
                speak = speak + "i am fine, thank you"
                speak= speak + "\nhow are you"

            elif "fine" in text or "good" in text:
                speak = speak + "it's good to know that you are fine"


            elif "open" in text.lower():
                if "edge" in text.lower():
                    speak = speak + "opening edge browser"
                    os.startfile(
                        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                    )

                elif "word" in text.lower() or "microsoft word" in text.lower():
                     speak = speak + " opening microsoft word "
                     os.startfile(
                        r"C:\Program Files\Microsoft Office\Office16\WINWORD.exe"
                    )

                elif "camera" in text.lower() or "cam" in text.lower():
                     speak = speak + " opening microsoft word "
                     os.startfile(
                        r"C:\Program Files\WindowsApps\Microsoft.WindowsCamera_5.38.3003.0_x64__8wekyb3d8bbwe\WindowsCamera.exe"
                    )


                elif "youtube" in text.lower():
                    speak = speak + "opening youtube"
                    webbrowser.open('https://www.youtube.com/')

                elif "google" in text.lower():
                    speak = speak + "opening google"
                    webbrowser.open('https://www.google.co.in/')

                elif "google" in text.lower():
                    speak = speak + "opening google"
                    webbrowser.open('https://www.google.co.in/')

                elif "whatsapp" in text.lower():
                    speak = speak + "opening whatsapp"
                    webbrowser.open('https://web.whatsapp.com/')

                elif "chatgpt" in text.lower():
                    speak = speak + "opening chatgpt"
                    webbrowser.open('https://chat.openai.com/?model=text-davinci-002-render-sha')

                else:
                    speak = speak + "application not found"

            elif "youtube" in text.lower():
                st = text.lower().split().index("youtube")
                search = text.split()[st + 1:]
                webbrowser.open(
                    "https://www.youtube.com/results?search_query="+
                    "+".join(search)
                )
                speak = speak + "opening" + str(search) + "on youtube"

            elif "search" in text.lower():
                st = text.lower().split().index("search")
                search = text.split()[st + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q="+
                    "+".join(search)
                )

                speak = speak + "searching" + str(search) + "on google"



            elif "change wallpaper" in text.lower() or "change background" in text.lower():
                img = r'E:\images\New folder'
                list_img = os.listdir(img)
                imgchoice = random.choice(list_img)
                randomimg = os.path.join(img, imgchoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomimg, 0)
                speak = speak + "background image changed succesfully"


            elif "play music" in text.lower() or "play song" in text.lower():
                talk("here you go with music")
                st = text.lower().split().index("music" or "song")
                search = text.split()[st + 1:]
                webbrowser.open(
                    'https://open.spotify.com/search/'+ '/'.join(search)
                )
                speak = speak + "searching" + str(search) + "on music"


            elif "empty recycle bin" in text.lower() or "mt recycle bin"in text.lower() or "mt recycle pin" in text.lower():
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak = speak + "recycle bin emptied"



            elif "note" in text.lower() or "remember" in text.lower():
                talk("what would you like me to write down?")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "i have made a note of that"


            elif "joke" in text.lower() or "jokes" in text.lower():
                speak = speak + pyjokes.get_joke()


            elif "mail" in text.lower() or "send email " in text.lower() or "email to computer" in text.lower() or "gmail to computer" in text.lower() or "send gmail " in text.lower():
                try:
                    talk("what should i say?")
                    content = rec_audio()
                    to =(input('TO:'))
                    send_email(to, content)
                    speak = speak + "email has been sent!"

                except Exception as e:
                    print(e)
                    talk("i am not able to send this email")


            elif "news" in text.lower():
                url = ('https://newsapi.org/v2/top-headlines?'
                       'country=in&'
                       'apiKey=d941a5826f6249a7ace479b44e7831a4')

                try:
                    response = requests.get(url)

                except:
                    talk("please check your connection ")

                news = json.loads(response.text)

                for new in news["articles"]:
                    print(str(new["title"]), "\n")
                    talk(str(new["title"]))
                    engine.runAndWait()
                    print(str(new["description"]), "\n")
                    talk(str(new["description"]))
                    engine.runAndWait()




                speak = speak + "send successfully"
                print(message.sid)

            response(speak)

    except Exception as e:
        talk("I don't know that.")


