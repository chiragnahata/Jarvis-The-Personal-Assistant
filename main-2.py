import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from random import choice
from utils import opening_text
from pprint import pprint
import mysql.connector
from tabulate import tabulate
import numpy as np
import cv2
import pyautogui
import os
from AppOpener import open

sqltor = mysql.connector.connect(
    host="localhost", user="root", password="Mysql@chiragnahata2005", database="jarvis")
cursor = sqltor.cursor()
if sqltor.is_connected():
    db_Info = sqltor.get_server_info()
    print("Successfully connected to MySQL database... MySQL Server version on ", db_Info)

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Male)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()   

# Greet the user
def greet_user():
    """Greets the user according to the time"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        return 'None'
    return query


def init():
    # Initialize the database table.
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS all_searches (search_type varchar(255), search_query varchar(255), result longtext );")


if __name__ == '__main__':
    init()
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            try:
                open_notepad()
            except Exception as e:
                print("NOTEPAD FAILED>>>>>", e)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'notepad', '{query}', 'opened notepad')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)
            
        elif 'open discord' in query:
            try:
                open_discord()
            except Exception as e:
                print("DISCORD FAILED>>>>>", e)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'discord', '{query}', 'opened discord')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif 'open command prompt' in query or 'open cmd' in query:
            try:
                open_cmd()
            except Exception as e:              
                print("CMD FAILED>>>>>", e)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'cmd', '{query}', 'opened cmd')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif 'open camera' in query:
            try:
                open_camera()
            except Exception as e:
                print("CAMERA FAILED>>>>>", e)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'camera', '{query}', 'opened camera')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif 'open calculator' in query:
            try:
                open_calculator()
            except Exception as e:
                print("CALCULATOR FAILED>>>>>", e)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'calculator', '{query}', 'opened calculator')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif 'ip address' in query:
            ip_address = find_my_ip()
            try:
                speak(
                f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')
            except Exception as ipEx:
                print("IP FAILED>>>>>", ipEx)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'ipaddress', '{query}', '{ip_address}')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif 'wikipedia' in query:
            result = ""
            search_query = ""
            try:
                speak('What do you want to search on Wikipedia, sir?')
                search_query = take_user_input().lower()
                result = search_on_wikipedia(search_query)

                speak(f"According to Wikipedia, {result}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(result)
            except Exception as wikipediaEx:
                print("WIKIPEDIA FAILED>>>>>", wikipediaEx)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'wikipedia', '{search_query}', '{result}')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif 'youtube' in query:
            try:
                speak('What do you want to play on Youtube, sir?')
                video = take_user_input().lower()
                play_on_youtube(video)
                speak("I've played the video sir.")
            except Exception as youtubeEx:
                print("YOUTUBE FAILED>>>>>", youtubeEx)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'youtube', '{query}', '{video}')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif 'search on google' in query:
            try:
                speak('What do you want to search on Google, sir?')
                result = take_user_input().lower()
                search_on_google(result)
                speak("I've searched the query sir.")
            except Exception as googleEx:
                print("GOOGLE FAILED>>>>>", googleEx)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'google', '{query}','{result}')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif "send a whatsapp message" in query:
            try:
                speak(
                'On what number should I send the message sir? Please enter in the console: ')
                number = input("Enter the number: ")
                speak("What is the message sir?")
                message = take_user_input().lower()
                send_whatsapp_message(number, message)
                speak("I've sent the message sir.")
            except Exception as whatsappEx:
                print("WHATSAPP FAILED>>>>>", whatsappEx)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'whatsapp', '{query}', '{number},{message}')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)         

        elif "send an email" in query:
            try:
                speak("On what email address do I send sir? Please enter in the console: ")
                receiver_address = input("Enter email address: ")
                speak("What should be the subject sir?")
                subject = take_user_input().capitalize()
                speak("What is the message sir?")
                message = take_user_input().capitalize()
                if send_email(receiver_address, subject, message):
                    speak("I've sent the email sir.")
                else:
                    speak(
                        "Something went wrong while I was sending the mail. Please check the error logs sir.")
            except Exception as emailEx:
                print("EMAIL FAILED>>>>>", emailEx)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'email', '{query}', '{receiver_address},{subject},{message}')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif 'joke' in query:
            try:
                speak(f"Hope you like this one sir")
                joke = get_random_joke()
                speak(joke)
                speak("For your convenience, I am printing it on the screen sir.")
                pprint(joke)
            except Exception as jokeEx:
                print("JOKE FAILED>>>>>", jokeEx)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'joke', '{query}', '{joke}')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif "advice" in query:
            try:
                speak(f"Here's an advice for you, sir")
                advice = get_random_advice()
                speak(advice)
                speak("For your convenience, I am printing it on the screen sir.")
                pprint(advice)
            except Exception as adviceEx:
                print("ADVICE FAILED>>>>>", adviceEx)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'advice', '{query}', '{advice}')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif "trending movies" in query:
            try:
                speak(f"Some of the trending movies are: {get_trending_movies()}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(get_trending_movies(), sep='\n')
            except Exception as movieEx:
                print("MOVIE FAILED>>>>>", movieEx)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'movie', '{query}', '{get_trending_movies()}')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif 'news' in query:
            latest_news = "";
            try:
                speak(f"I'm reading out the latest news headlines, sir")
                latest_news = get_latest_news()
                speak("For your convenience, I am printing it on the screen sir.")
            except Exception as newsEx:
                print("NEWS FAILED>>>>>", newsEx)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches (search_type, search_query, result) values ( 'news', '{query}', '{latest_news}')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)

        elif 'weather' in query:
            try:
                ip_address = find_my_ip()
                city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
                speak(f"Getting weather report for your city {city}")
                weather, temperature, feels_like = get_weather_report(city)
                speak(
                    f"The current temperature is {temperature}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(
                    f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
            except Exception as weatherEx:
                print("WEATHER FAILED>>>>>", weatherEx)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'weather', '{query}', '{weather},{temperature},{feels_like}')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)
        
        elif "take screenshot" in query or "take a screenshot" in query or "capture the screen" in query:
                speak("Sir, please tell me the name of the screenshot")
                name = take_user_input().capitalize()
                image = pyautogui.screenshot()
                image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
                cv2.imwrite(f"C:\\Users\\Chirag Nahata\\OneDrive\\Pictures\\Screenshots\\{name}.png", image)
                speak("Sir, I have taken the screenshot and saved it in the screenshots folder")

        elif "show me the screenshot" in query:
                try:
                    speak("Sir, please tell me the name of the screenshot")
                    name = take_user_input().capitalize()
                    img = cv2.imread(f"C:\\Users\\Chirag Nahata\\OneDrive\\Pictures\\Screenshots\\{name}.png")
                    cv2.imshow(f"{name}", img)
                    speak("Here it is sir")
                    cv2.waitKey(0)

                except Exception as e:
                    speak("Sorry sir, I couldn't find the screenshot you requested")

        elif "open" in query:
            try:
                app = query.replace("open", "")
                open(app)
                speak("Opened ", app , "successfully")
            except Exception as e:
                print("Sorry sir, I couldn't open ",app)
            try:
                insertQuery = f"INSERT INTO jarvis.all_searches ( search_type, search_query, result) values ( 'open', '{query}', '{app}')"
                cursor.execute(insertQuery)
                sqltor.commit()
            except Exception as sqlExcept:
                print("SQL FAILED>>>>>", sqlExcept)
                
        elif 'history' in query:
            speak("Here's your history sir")
            cursor.execute("SELECT * FROM all_searches")
            results = cursor.fetchall() or [];
            print(tabulate(results, headers=["Search Type", "Query", "Results"]))
