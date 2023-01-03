Read the tutorial series - https://iread.ga/series/10/virtual-personal-assistant-using-python
# Jarvis - Personal Assistant Python and MySQL Computer Project for Class 12 Annual Exam
# J.A.R.V.I.S - Personal Assistant

freeCodeCamp article: https://www.freecodecamp.org/news/python-project-how-to-build-your-own-jarvis-using-python/
![image](https://user-images.githubusercontent.com/63905783/167343172-23256b14-ad83-40c6-a114-2fe78f1fe86f.png)

Demo Video: https://vimeo.com/650156113
## Project Setup

Contents of .env file:
@@ -231,73 +233,85 @@ We'll use this function to open the calculator on our system.
def open_calculator():
    sp.Popen(paths['calculator'])
```
How to Set Up Online Functions
We'll be adding several online functions. They are:
## How to Set Up Online Functions
Find my IP address
Search on Wikipedia
Play videos on YouTube
Search on Google
Send WhatsApp message
Send Email
Get Latest News Headlines
Get Weather Report
Get Trending Movies
Get Random Jokes
Get Random Advice
Let's create a file called online_ops.py within the functions directory, and start creating these functions one after another. For now, add the following code in the file:
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
Before we start working with APIs, if you're not familiar with APIs and how to interact with them using Python, check out this tutorial.

How to Add the Find my IP Address Function
ipify provides a simple public IP address API. We just need to make a GET request on this URL: https://api64.ipify.org/?format=json. It returns JSON data as:

```
### How to Add the Find my IP Address Function
[ipify](https://www.ipify.org/) provides a simple public IP address API. We just need to make a GET request on this URL: https://api64.ipify.org/?format=json. It returns JSON data as:
```
{
  "ip": "117.214.111.199"
}
We can then simply return the ip from the JSON data. So, let's create this method:

```
We can then simply return the `ip` from the JSON data. So, let's create this method:
```
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
How to Add the Search on Wikipedia Function
For searching on Wikipedia, we'll be using the wikipedia module that we had installed earlier in this tutorial.
```
### How to Add the Search on Wikipedia Function
For searching on Wikipedia, we'll be using the `wikipedia` module that we had installed earlier in this tutorial.
```
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results
Inside the wikipedia module, we have a summary() method that accepts a query as an argument. Additionally, we can also pass the number of sentences required. Then we simply return the result.
```
Inside the `wikipedia` module, we have a `summary()` method that accepts a query as an argument. Additionally, we can also pass the number of sentences required. Then we simply return the result.
How to Add the Play Videos on YouTube Function
For playing videos on YouTube, we are using PyWhatKit. We have already imported it as kit.
### How to Add the Play Videos on YouTube Function
For playing videos on YouTube, we are using PyWhatKit. We have already imported it as `kit`.
```
def play_on_youtube(video):
    kit.playonyt(video)
PyWhatKit has a playonyt() method that accepts a topic as an argument. It then searches the topic on YouTube and plays the most appropriate video. It uses PyAutoGUI under the hood.
```
PyWhatKit has a `playonyt()` method that accepts a topic as an argument. It then searches the topic on YouTube and plays the most appropriate video. It uses [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) under the hood.
How to Add the Search on Google Function
Again we'll be using PyWhatKit for searching on Google.
### How to Add the Search on Google Function
Again we'll be using PyWhatKit for searching on Google.
```
def search_on_google(query):
    kit.search(query)
It has a method search() that helps us search on Google instantly.
```
It has a method `search()` that helps us search on Google instantly.
How to Add the Send WhatsApp Message Function
We'll be using PyWhatKit once again for sending WhatsApp messages.
### How to Add the Send WhatsApp Message Function
We'll be using *PyWhatKit* once again for sending WhatsApp messages.
```
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
Our method accepts two arguments – the phone number number and the message. It then calls the sendwhatmsg_instantly() method to send a WhatsApp message. Make sure you've already logged in into your WhatsApp account on WhatsApp for Web.
```
Our method accepts two arguments – the phone number `number` and the `message`. It then calls the `sendwhatmsg_instantly()` method to send a WhatsApp message. Make sure you've already logged in into your WhatsApp account on WhatsApp for Web.
How to Add the Send Email Function
For sending emails, we will be using the built-in smtplib module from Python.
### How to Add the Send Email Function
For sending emails, we will be using the built-in `smtplib` module from Python.
```
EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
@@ -318,13 +332,15 @@ def send_email(receiver_address, subject, message):
    except Exception as e:
        print(e)
        return False
The method accepts receiver_address, subject, and message as arguments. We create an object of the SMTP class from the smtplib module. It takes host and port number as the parameters.
```
The method accepts `receiver_address`, `subject`, and `message` as arguments. We create an object of the SMTP class from the `smtplib` module. It takes host and port number as the parameters.
We then start a session and login with the email address and password and send the email. Make sure you add EMAIL and PASSWORD in the .env file.
We then start a session and login with the email address and password and send the email. Make sure you add **EMAIL** and **PASSWORD** in the `.env` file.
How to Add the Get Latest News Headlines Function
To fetch the latest news headlines, we'll be using NewsAPI. Signup for a free account on NewsAPI and get the API Key. Add the NEWS_API_KEY in the .env file.
### How to Add the Get Latest News Headlines Function
To fetch the latest news headlines, we'll be using [NewsAPI](https://newsapi.org/). Signup for a free account on NewsAPI and get the API Key. Add the **NEWS_API_KEY** in the `.env` file.
```
NEWS_API_KEY = config("NEWS_API_KEY")
@@ -336,8 +352,9 @@ def get_latest_news():
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]
In the above method, we're first creating an empty list called news_headlines. We are then making a GET request on the API URL specified in the NewsAPI Documentation. A sample JSON response from the request looks like this:

```
In the above method, we're first creating an empty list called `news_headlines`. We are then making a GET request on the API URL specified in the [NewsAPI Documentation](https://newsapi.org/docs). A sample JSON response from the request looks like this:
```
{
  "status": "ok",
  "totalResults": 38,
@@ -409,11 +426,13 @@ In the above method, we're first creating an empty list called news_headlines. W
    }
  ]
}
Since the news is contained in a list called articles, we are creating a variable articles with the value res['articles']. Now we are iterating over this articles list and appending the article["title"] to the news_headlines list. We are then returning the first five news headlines from this list.
```
Since the news is contained in a list called `articles`, we are creating a variable `articles` with the value `res['articles']`. Now we are iterating over this `articles` list and appending the `article["title"]` to the `news_headlines` list. We are then returning the first five news headlines from this list.
How to Add the Get Weather Report Function
To get the weather report, we're using the OpenWeatherMap API. Signup for a free account and get the APP ID. Make sure you add the OPENWEATHER_APP_ID in the .env file.
### How to Add the Get Weather Report Function
To get the weather report, we're using the [OpenWeatherMap API](https://openweathermap.org/). Signup for a free account and get the APP ID. Make sure you add the **OPENWEATHER_APP_ID** in the `.env` file.
```
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
@@ -424,8 +443,9 @@ def get_weather_report(city):
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"
As per the OpenWeatherMap API, we need to make a GET request on the above-mentioned URL with the city name. We'll get a JSON response as:

```
As per the [OpenWeatherMap API](https://openweathermap.org/current), we need to make a GET request on the above-mentioned URL with the city name. We'll get a JSON response as:
```
{
    "coord": {
        "lon": 85,
@@ -469,11 +489,13 @@ As per the OpenWeatherMap API, we need to make a GET request on the above-mentio
    "name": "Gaya",
    "cod": 200
}
We'll just need the weather, temperature, and feels_like from the above response.
```
We'll just need the `weather`, `temperature`, and `feels_like` from the above response.
How to Add the Get Trending Movies Function
To get the trending movies, we'll be using The Movie Database (TMDB) API. Signup for a free account and get the API Key. Add the TMDB_API_KEY in the .env file.
### How to Add the Get Trending Movies Function
To get the trending movies, we'll be using [The Movie Database (TMDB)](https://www.themoviedb.org/) API. Signup for a free account and get the API Key. Add the **TMDB_API_KEY** in the `.env` file.
```
TMDB_API_KEY = config("TMDB_API_KEY")
@@ -485,8 +507,9 @@ def get_trending_movies():
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]
Just as we did for the latest news headlines, we are creating trending_movies list. Then, as per the TMDB API, we're making a GET request. A sample JSON response looks like this:

```
Just as we did for the latest news headlines, we are creating `trending_movies` list. Then, as per the TMDB API, we're making a GET request. A sample JSON response looks like this:
```
{
  "page": 1,
  "results": [
@@ -579,26 +602,34 @@ Just as we did for the latest news headlines, we are creating trending_movies li
  "total_pages": 1000,
  "total_results": 20000
}
From the above response, we just need the title of the movie. We get the results which is a list and then iterate over it to get the movie title and append it to the trending_movies list. In the end, we return the first five elements of the list.
```
From the above response, we just need the title of the movie. We get the `results` which is a list and then iterate over it to get the movie title and append it to the `trending_movies` list. In the end, we return the first five elements of the list.
How to Add the Get Random Jokes Function
To get a random joke, we just need to make a GET request on this URL: https://icanhazdadjoke.com/.
### How to Add the Get Random Jokes Function
To get a random joke, we just need to make a GET request on this URL: https://icanhazdadjoke.com/.
```
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]
How to Add the Get Random Advice Function
To get a piece of random advice, we're using the Advice Slip API.
```
### How to Add the Get Random Advice Function
To get a piece of random advice, we're using the [Advice Slip API](https://api.adviceslip.com/).
```
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
How to Create the Main Method
To run the project, we'll need to create a main method. Create a main.py file and add the following code:
```
## How to Create the Main Method
To run the project, we'll need to create a main method. Create a `main.py` file and add the following code:
```
import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
@@ -702,16 +733,19 @@ if __name__ == '__main__':
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
```
While the above script looks quite lengthy, it is very simple and easy to understand.
If you look closely, all we have done is imported the required modules and the online and offline functions. Then within the main method, the first thing we do is greet the user using the greet_user() function.
If you look closely, all we have done is imported the required modules and the online and offline functions. Then within the main method, the first thing we do is greet the user using the `greet_user()` function.
Next, we run a while loop to continuously take input from the user using the take_user_input() function. Since we have our query string here, we can add if-else ladder to check for the different conditions on the query string.
Next, we run a while loop to continuously take input from the user using the `take_user_input()` function. Since we have our query string here, we can add if-else ladder to check for the different conditions on the `query` string.
Note: For Python 3.10, you can use Python Match Case instead of if-else ladder.
To run the program, you can use the following command:
#### Note: For Python 3.10, you can use [Python Match Case](https://peps.python.org/pep-0636/) instead of if-else ladder.
To run the program, you can use the following command:
```
USER=None
BOTNAME=JARVIS
EMAIL=None
PASSWORD=None
NEWS_API_KEY=None
OPENWEATHER_APP_ID=None
TMDB_API_KEY=None
$ python main.py
Conclusion
We just created our very own virtual personal assistant with the help of Python. You can add more features to the application if you like. You can add this project to your résumé or just do it for fun!
```
## Conclusion
Replace `None` with your values
We just created our very own virtual personal assistant with the help of Python. You can add more features to the application if you like.
