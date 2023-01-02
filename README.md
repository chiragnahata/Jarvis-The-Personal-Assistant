# J.A.R.V.I.S - Personal Assistant

![image](https://user-images.githubusercontent.com/63905783/167343172-23256b14-ad83-40c6-a114-2fe78f1fe86f.png)

## Project Setup

While you're coding this project, you'll come across various modules and external libraries. Let's learn about them and install them. But before we install them, let's create a virtual environment and activate it.

We are going to create a virtual environment using `virtualenv`. Python now ships with a pre-installed `virtualenv` library. So, to create a virtual environment, you can use the below command:
```
$ python -m venv env
```
The above command will create a virtual environment named `env`. Now, we need to activate the environment using the command:
```
$ . env/Scripts/activate
```
To verify if the environment has been activated or not, you can see `(env)` in your terminal. Now, we can install the libraries.

1. pyttsx3: pyttsx is a cross-platform text to speech library which is platform-independent. The major advantage of using this library for text-to-speech conversion is that it works offline. To install this module, type the below command in the terminal:
```
$ pip install pyttsx3
```
2. SpeechRecognition: This allows us to convert audio into text for further processing. To install this module, type the below command in the terminal:
```
$ pip install SpeechRecognition
```
3. pywhatkit: This is an easy-to-use library that will help us interact with the browser very easily. To install the module, run the following command in the terminal:
```
$ pip install pywhatkit
```
4. wikipedia: We'll use this to fetch a variety of information from the Wikipedia website. To install this module, type the below command in the terminal:
```
$ pip install wikipedia
```
5. requests: This is an elegant and simple HTTP library for Python that allows you to send HTTP/1.1 requests extremely easily. To install the module, run the following command in the terminal:
```
$ pip install requests
```
## .env File

We need this file to store some private data such as API Keys, Passwords, and so on that are related to the project. For now, let's store the name of the user and the bot.

Create a file named `.env` and add the following content there:

```
USER=None
BOTNAME=JARVIS
EMAIL=None
PASSWORD=None
NEWS_API_KEY=None
OPENWEATHER_APP_ID=None
TMDB_API_KEY=None
```

Replace `None` with your values

To use the contents from the `.env` file, we'll install another module called python-decouple as:
```
$ pip install python-decouple
```
## How to Set Up JARVIS with Python

Before we start defining a few important functions, let's create a speech engine first.
```
import pyttsx3
from decouple import config
USERNAME = config('USER')
BOTNAME = config('BOTNAME')
engine = pyttsx3.init('sapi5')
# Set Rate
engine.setProperty('rate', 190)
# Set Volume
engine.setProperty('volume', 1.0)
# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
```
Let's analyze the above script. First of all, we have initialized an `engine` using the `pyttsx3` module. `sapi5` is a Microsoft Speech API that helps us use the voices.

Next, we are setting the `rate` and `volume` properties of the speech engine using `setProperty` method.

Now, we can get the voices from the engine using the `getProperty` method. `voices` will be a list of voices available in our system. If we print it, we can see as below:
```
[<pyttsx3.voice.Voice object at 0x000001AB9FB834F0>, <pyttsx3.voice.Voice object at 0x000001AB9FB83490>]
```
The first one is a male voice and the other one is a female voice. JARVIS was a male assistant in the movies, but I've chosen to set the `voice` property to the female for this tutorial using the `setProperty` method.

#### Note: If you get an error related to PyAudio, download PyAudio wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it within the virtual environment.

Also, using the `config` method from decouple, we are getting the value of `USER` and `BOTNAME` from the environment variables.

## Enable the Speak Function

The speak function will be responsible for speaking whatever text is passed to it. Let's see the code:
```
# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""
    
    engine.say(text)
    engine.runAndWait()
 ```
 In the `speak()` method, the engine speaks whatever text is passed to it using the `say()` method. Using the `runAndWait()` method, it blocks during the event loop and returns when the commands queue is cleared.

## Enable the Greet Function

This function will be used to greet the user whenever the program is run. According to the current time, it greets *Good Morning*, *Good Afternoon*, or *Good Evening* to the user.
```
from datetime import datetime
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
 ```
First, we get the current hour, that is if the current time is 11:15 AM, the hour will be 11. If the value of hour is between 6 and 12, wish Good Morning to the user. If the value is between 12 and 16, wish Good Afternoon and similarly, if the value is between 16 and 19, wish Good Evening. We are using the speak method to speak to the user.

## How to Take User Input

We use this function to take the commands from the user and recognize the command using the `speech_recognition` module.
```
import speech_recognition as sr
from random import choice
from utils import opening_text
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
        query = 'None'
    return query
  ```
We have imported `speech_recognition` module as `sr`. The Recognizer class within the `speech_recognition` module helps us recognize the audio. The same module has a Microphone class that gives us access to the microphone of the device. So with the microphone as the `source`, we try to listen to the audio using the `listen()` method in the Recognizer class.

We have also set the `pause_threshold` to 1, that is it will not complain even if we pause for one second during we speak.

Next, using the `recognize_google()` method from the Recognizer class, we try to recognize the audio. The `recognize_google()` method performs speech recognition on the audio passed to it, using the **Google Speech Recognition API**.

We have set the language to `en-in`, which is English India. It returns the transcript of the audio which is nothing but a string. We've stored it in a variable called `query`.

If the query has exit or stop words in it, it means we're asking the assistant to stop immediately. So, before stopping, we greet the user again as per the current hour. If the hour is between 21 and 6, wish Good Night to the user, else, some other message.

We create a `utils.py` file which has just one list containing a few statements like this:
```
opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]
```
If the query doesn't have those two words (exit or stop), we speak something to tell the user that we have heard them. For that, we will use the choice method from the random module to randomly select any statement from the `opening_text` list. After speaking, we exit from the program.

During this entire process, if we encounter an exception, we apologize to the user and set the `query` to None. In the end, we return the `query`.

## How to Set Up Offline Functions

Inside the `functions` folder, create a Python file called `os_ops.py`. In this file, we'll create various functions to interact with the OS.
```
import os
import subprocess as sp
paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}
```
In the above script, we have created a dictionary called `paths` which has a software name as the key and its path as the value. You can change the paths according to your system and add more software paths if you need to do so.

### How to Open the Camera

We'll use this function to open the camera in our system. We'll be using the `subprocess` module to run the command.
```
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
```
### How to Open Notepad and Discord

We'll use these functions to open Notepad++ and Discord in the system.
```
def open_notepad():
    os.startfile(paths['notepad'])
def open_discord():
    os.startfile(paths['discord'])
```
### How to Open the Command Prompt

We'll use this function to open the command prompt in our system.
```
def open_cmd():
    os.system('start cmd')
```
### How to Open the Calculator

We'll use this function to open the calculator on our system.
```
def open_calculator():
    sp.Popen(paths['calculator'])
```
## How to Set Up Online Functions

We'll be adding several online functions. They are:

1. Find my IP address
2. Search on Wikipedia
3. Play videos on YouTube
4. Search on Google
5. Send WhatsApp message
6. Send Email
7. Get Latest News Headlines
8. Get Weather Report
9. Get Trending Movies
10. Get Random Jokes
11. Get Random Advice
 
Let's create a file called `online_ops.py` within the `functions` directory, and start creating these functions one after another. For now, add the following code in the file:
```
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
```
### How to Add the Find my IP Address Function
[ipify](https://www.ipify.org/) provides a simple public IP address API. We just need to make a GET request on this URL: https://api64.ipify.org/?format=json. It returns JSON data as:
```
{
  "ip": "117.214.111.199"
}
```
We can then simply return the `ip` from the JSON data. So, let's create this method:
```
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
```
### How to Add the Search on Wikipedia Function

For searching on Wikipedia, we'll be using the `wikipedia` module that we had installed earlier in this tutorial.
```
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results
```
Inside the `wikipedia` module, we have a `summary()` method that accepts a query as an argument. Additionally, we can also pass the number of sentences required. Then we simply return the result.

### How to Add the Play Videos on YouTube Function

For playing videos on YouTube, we are using PyWhatKit. We have already imported it as `kit`.
```
def play_on_youtube(video):
    kit.playonyt(video)
```
PyWhatKit has a `playonyt()` method that accepts a topic as an argument. It then searches the topic on YouTube and plays the most appropriate video. It uses [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) under the hood.

### How to Add the Search on Google Function

Again we'll be using PyWhatKit for searching on Google.
```
def search_on_google(query):
    kit.search(query)
```
It has a method `search()` that helps us search on Google instantly.

### How to Add the Send WhatsApp Message Function

We'll be using *PyWhatKit* once again for sending WhatsApp messages.
```
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
```
Our method accepts two arguments – the phone number `number` and the `message`. It then calls the `sendwhatmsg_instantly()` method to send a WhatsApp message. Make sure you've already logged in into your WhatsApp account on WhatsApp for Web.

### How to Add the Send Email Function

For sending emails, we will be using the built-in `smtplib` module from Python.
```
EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
```
The method accepts `receiver_address`, `subject`, and `message` as arguments. We create an object of the SMTP class from the `smtplib` module. It takes host and port number as the parameters.

We then start a session and login with the email address and password and send the email. Make sure you add **EMAIL** and **PASSWORD** in the `.env` file.

### How to Add the Get Latest News Headlines Function

To fetch the latest news headlines, we'll be using [NewsAPI](https://newsapi.org/). Signup for a free account on NewsAPI and get the API Key. Add the **NEWS_API_KEY** in the `.env` file.
```
NEWS_API_KEY = config("NEWS_API_KEY")
def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]
```
In the above method, we're first creating an empty list called `news_headlines`. We are then making a GET request on the API URL specified in the [NewsAPI Documentation](https://newsapi.org/docs). A sample JSON response from the request looks like this:
```
{
  "status": "ok",
  "totalResults": 38,
  "articles": [
    {
      "source": {
        "id": null,
        "name": "Sportskeeda"
      },
      "author": "Aniket Thakkar",
      "title": "Latest Free Fire redeem code to get Weapon loot crate today (14 October 2021) - Sportskeeda",
      "description": "Gun crates are one of the ways that players in Free Fire can obtain impressive and appealing gun skins.",
      "url": "https://www.sportskeeda.com/free-fire/latest-free-fire-redeem-code-get-weapon-loot-crate-today-14-october-2021",
      "urlToImage": "https://staticg.sportskeeda.com/editor/2021/10/d0b83-16341799119781-1920.jpg",
      "publishedAt": "2021-10-14T03:51:50Z",
      "content": null
    },
    {
      "source": {
        "id": null,
        "name": "NDTV News"
      },
      "author": null,
      "title": "BSF Gets Increased Powers In 3 Border States: What It Means - NDTV",
      "description": "Border Security Force (BSF) officers will now have the power toarrest, search, and of seizure to the extent of 50 km inside three newstates sharing international boundaries with Pakistan and Bangladesh.",
      "url": "https://www.ndtv.com/india-news/bsf-gets-increased-powers-in-3-border-states-what-it-means-2574644",
      "urlToImage": "https://c.ndtvimg.com/2021-08/eglno7qk_-bsf-recruitment-2021_625x300_10_August_21.jpg",
      "publishedAt": "2021-10-14T03:44:00Z",
      "content": "This move is quickly snowballing into a debate on state autonomy. New Delhi: Border Security Force (BSF) officers will now have the power to arrest, search, and of seizure to the extent of 50 km ins… [+4143 chars]"
    },
    {
      "source": {
        "id": "the-times-of-india",
        "name": "The Times of India"
      },
      "author": "TIMESOFINDIA.COM",
      "title": "5 health conditions that can make your joints hurt - Times of India",
      "description": "Joint pain caused by these everyday issues generally goes away on its own when you stretch yourself a little and flex your muscles.",
      "url": "https://timesofindia.indiatimes.com/life-style/health-fitness/health-news/5-health-conditions-that-can-make-your-joints-hurt/photostory/86994969.cms",
      "urlToImage": "https://static.toiimg.com/photo/86995017.cms",
      "publishedAt": "2021-10-14T03:30:00Z",
      "content": "Depression is a mental health condition, but the symptoms may manifest even on your physical health. Unexpected aches and pain in the joints that you may experience when suffering from chronic depres… [+373 chars]"
    },
    {
      "source": {
        "id": null,
        "name": "The Indian Express"
      },
      "author": "Devendra Pandey",
      "title": "Rahul Dravid likely to be interim coach for New Zealand series - The Indian Express",
      "description": "It’s learnt that a few Australian coaches expressed interest in the job, but the BCCI isn’t keen as they are focussing on an Indian for the role, before they look elsewhere.",
      "url": "https://indianexpress.com/article/sports/cricket/rahul-dravid-likely-to-be-interim-coach-for-new-zealand-series-7570990/",
      "urlToImage": "https://images.indianexpress.com/2021/05/rahul-dravid.jpg",
      "publishedAt": "2021-10-14T03:26:09Z",
      "content": "Rahul Dravid is likely to be approached by the Indian cricket board to be the interim coach for Indias home series against New Zealand. Head coach Ravi Shastri and the core of the support staff will … [+1972 chars]"
    },
    {
      "source": {
        "id": null,
        "name": "CNBCTV18"
      },
      "author": null,
      "title": "Thursday's top brokerage calls: Infosys, Wipro and more - CNBCTV18",
      "description": "Goldman Sachs has maintained its 'sell' rating on Mindtree largely due to expensive valuations, while UBS expects a muted reaction from Wipro's stock. Here are the top brokerage calls for the day:",
      "url": "https://www.cnbctv18.com/market/stocks/thursdays-top-brokerage-calls-infosys-wipro-and-more-11101072.htm",
      "urlToImage": "https://images.cnbctv18.com/wp-content/uploads/2019/03/buy-sell.jpg",
      "publishedAt": "2021-10-14T03:26:03Z",
      "content": "MiniGoldman Sachs has maintained its 'sell' rating on Mindtree largely due to expensive valuations, while UBS expects a muted reaction from Wipro's stock. Here are the top brokerage calls for the day:"
    }
  ]
}
```
Since the news is contained in a list called `articles`, we are creating a variable `articles` with the value `res['articles']`. Now we are iterating over this `articles` list and appending the `article["title"]` to the `news_headlines` list. We are then returning the first five news headlines from this list.

### How to Add the Get Weather Report Function

To get the weather report, we're using the [OpenWeatherMap API](https://openweathermap.org/). Signup for a free account and get the APP ID. Make sure you add the **OPENWEATHER_APP_ID** in the `.env` file.
```
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"
```
As per the [OpenWeatherMap API](https://openweathermap.org/current), we need to make a GET request on the above-mentioned URL with the city name. We'll get a JSON response as:
```
{
    "coord": {
        "lon": 85,
        "lat": 24.7833
    },
    "weather": [
        {
            "id": 721,
            "main": "Haze",
            "description": "haze",
            "icon": "50d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 26.95,
        "feels_like": 26.64,
        "temp_min": 26.95,
        "temp_max": 26.95,
        "pressure": 1011,
        "humidity": 36
    },
    "visibility": 3000,
    "wind": {
        "speed": 2.57,
        "deg": 310
    },
    "clouds": {
        "all": 57
    },
    "dt": 1637227634,
    "sys": {
        "type": 1,
        "id": 9115,
        "country": "IN",
        "sunrise": 1637195904,
        "sunset": 1637235130
    },
    "timezone": 19800,
    "id": 1271439,
    "name": "Gaya",
    "cod": 200
}
```
We'll just need the `weather`, `temperature`, and `feels_like` from the above response.

### How to Add the Get Trending Movies Function

To get the trending movies, we'll be using [The Movie Database (TMDB)](https://www.themoviedb.org/) API. Signup for a free account and get the API Key. Add the **TMDB_API_KEY** in the `.env` file.
```
TMDB_API_KEY = config("TMDB_API_KEY")
def get_trending_movies():
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]
```
Just as we did for the latest news headlines, we are creating `trending_movies` list. Then, as per the TMDB API, we're making a GET request. A sample JSON response looks like this:
```
{
  "page": 1,
  "results": [
    {
      "video": false,
      "vote_average": 7.9,
      "overview": "Shang-Chi must confront the past he thought he left behind when he is drawn into the web of the mysterious Ten Rings organization.",
      "release_date": "2021-09-01",
      "title": "Shang-Chi and the Legend of the Ten Rings",
      "adult": false,
      "backdrop_path": "/cinER0ESG0eJ49kXlExM0MEWGxW.jpg",
      "vote_count": 2917,
      "genre_ids": [28, 12, 14],
      "id": 566525,
      "original_language": "en",
      "original_title": "Shang-Chi and the Legend of the Ten Rings",
      "poster_path": "/1BIoJGKbXjdFDAqUEiA2VHqkK1Z.jpg",
      "popularity": 9559.446,
      "media_type": "movie"
    },
    {
      "adult": false,
      "backdrop_path": "/dK12GIdhGP6NPGFssK2Fh265jyr.jpg",
      "genre_ids": [28, 35, 80, 53],
      "id": 512195,
      "original_language": "en",
      "original_title": "Red Notice",
      "overview": "An Interpol-issued Red Notice is a global alert to hunt and capture the world's most wanted. But when a daring heist brings together the FBI's top profiler and two rival criminals, there's no telling what will happen.",
      "poster_path": "/wdE6ewaKZHr62bLqCn7A2DiGShm.jpg",
      "release_date": "2021-11-04",
      "title": "Red Notice",
      "video": false,
      "vote_average": 6.9,
      "vote_count": 832,
      "popularity": 1990.503,
      "media_type": "movie"
    },
    {
      "genre_ids": [12, 28, 53],
      "original_language": "en",
      "original_title": "No Time to Die",
      "poster_path": "/iUgygt3fscRoKWCV1d0C7FbM9TP.jpg",
      "video": false,
      "vote_average": 7.6,
      "overview": "Bond has left active service and is enjoying a tranquil life in Jamaica. His peace is short-lived when his old friend Felix Leiter from the CIA turns up asking for help. The mission to rescue a kidnapped scientist turns out to be far more treacherous than expected, leading Bond onto the trail of a mysterious villain armed with dangerous new technology.",
      "id": 370172,
      "vote_count": 1804,
      "title": "No Time to Die",
      "adult": false,
      "backdrop_path": "/1953j0QEbtN17WFFTnJHIm6bn6I.jpg",
      "release_date": "2021-09-29",
      "popularity": 4639.439,
      "media_type": "movie"
    },
    {
      "poster_path": "/5pVJ9SuuO72IgN6i9kMwQwnhGHG.jpg",
      "video": false,
      "vote_average": 0,
      "overview": "Peter Parker is unmasked and no longer able to separate his normal life from the high-stakes of being a Super Hero. When he asks for help from Doctor Strange the stakes become even more dangerous, forcing him to discover what it truly means to be Spider-Man.",
      "release_date": "2021-12-15",
      "id": 634649,
      "adult": false,
      "backdrop_path": "/vK18znei8Uha2z7ZhZtBa40HIrm.jpg",
      "vote_count": 0,
      "genre_ids": [28, 12, 878],
      "title": "Spider-Man: No Way Home",
      "original_language": "en",
      "original_title": "Spider-Man: No Way Home",
      "popularity": 1084.815,
      "media_type": "movie"
    },
    {
      "video": false,
      "vote_average": 6.8,
      "overview": "After finding a host body in investigative reporter Eddie Brock, the alien symbiote must face a new enemy, Carnage, the alter ego of serial killer Cletus Kasady.",
      "release_date": "2021-09-30",
      "adult": false,
      "backdrop_path": "/70nxSw3mFBsGmtkvcs91PbjerwD.jpg",
      "vote_count": 1950,
      "genre_ids": [878, 28, 12],
      "id": 580489,
      "original_language": "en",
      "original_title": "Venom: Let There Be Carnage",
      "poster_path": "/rjkmN1dniUHVYAtwuV3Tji7FsDO.jpg",
      "title": "Venom: Let There Be Carnage",
      "popularity": 4527.568,
      "media_type": "movie"
    }
  ],
  "total_pages": 1000,
  "total_results": 20000
}
```
From the above response, we just need the title of the movie. We get the `results` which is a list and then iterate over it to get the movie title and append it to the `trending_movies` list. In the end, we return the first five elements of the list.

### How to Add the Get Random Jokes Function

To get a random joke, we just need to make a GET request on this URL: https://icanhazdadjoke.com/.
```
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]
```

### How to Add the Get Random Advice Function

To get a piece of random advice, we're using the [Advice Slip API](https://api.adviceslip.com/).
```
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
```

## How to Create the Main Method

To run the project, we'll need to create a main method. Create a `main.py` file and add the following code:
```
import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from pprint import pprint
if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()
        if 'open notepad' in query:
            open_notepad()
        elif 'open discord' in query:
            open_discord()
        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()
        elif 'open camera' in query:
            open_camera()
        elif 'open calculator' in query:
            open_calculator()
        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')
        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)
        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)
        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)
        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")
        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")
        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)
        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)
        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')
        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')
        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
```
While the above script looks quite lengthy, it is very simple and easy to understand.

If you look closely, all we have done is imported the required modules and the online and offline functions. Then within the main method, the first thing we do is greet the user using the `greet_user()` function.

Next, we run a while loop to continuously take input from the user using the `take_user_input()` function. Since we have our query string here, we can add if-else ladder to check for the different conditions on the `query` string.

#### Note: For Python 3.10, you can use [Python Match Case](https://peps.python.org/pep-0636/) instead of if-else ladder.

To run the program, you can use the following command:
```
$ python main.py
```
## Conclusion

We just created our very own virtual personal assistant with the help of Python. You can add more features to the application if you like.
