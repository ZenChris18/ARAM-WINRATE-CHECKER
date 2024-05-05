 # ARAM WINRATE CHECKER
#### Video Demo:  <URL https://youtu.be/o5H828ZTb5c>
#### Description:
#### This is my final project to conclude the CS50 Introduction to programming with python course.

# Libraries Used
1. dotenv - Used this library for security purposes. Need to hide Keys that i don't want to share to the public
2. OS - in order to access the .env file and get the data.
3. requests - to extract the dict in a json file. 

## Description

This project is a simple command-line tool that allows users to calculate their win rate in the gamemode ARAM(all random all mid) in League of Legends. It uses the Riot Games API to get user match data and analyze win/loss stats. (it only calculates the past 50 games because it takes too long to process when more than 50)

## Installation
To use this tool, you need to have Python installed on your system. Additionally, you need to install the required libraries. You can install them by using pip install on the command line interface:

```bash
pip install requests
pip install python-dotenv
```

i also used OS and requests library but that is already built in so no need to install it by yourself.

You also need to set up a Riot Games API key on your own. Follow these steps to obtain your own private API key:

1. Go to the Riot Games Developer and make your own account: [Riot Developer Portal](https://developer.riotgames.com/).
2. After signing up, create a new application and get your API key. 
note: keep your API keys private.

Once you have your API key, create a file named `.env` in the project directory and add the following line:

```
riot_api_key=YOUR_API_KEY_HERE
```

Replace `YOUR_API_KEY_HERE` with your very own private Riot Games API key.

## Usage

To use this tool yourself, simply run the `project.py` file:

```bash
python project.py
```

Follow the instructions on the screen to enter your League of Legends username, tagline, and server. The program will then get your match data and calculate your win rate. And do not worry if you enter a wrong letter or wrong server the program will tell you if you made a mistake.

## Credits

This project was created by Yujison Lagamayo. Special thanks to Riot Games for providing the API, and CS50p for teaching the course.

## Contact

If you have any questions, suggestions, or feedback, feel free to email me at: yujisons@gmail.com 

## Additional Information

For more information on how to use the Riot Games API and League of Legends, refer to the [Riot Developer Portal](https://developer.riotgames.com/) and the [League of Legends website](https://www.leagueoflegends.com/en-ph/). 

# About CS50p 

An introduction to programming using a language called Python. Learn how to read and write code as well as how to test and “debug” it. Designed for students with or without prior programming experience who’d like to learn Python specifically. Learn about functions, arguments, and return values (oh my!); variables and types; conditionals and Boolean expressions; and loops. Learn how to handle exceptions, find and fix bugs, and write unit tests; use third-party libraries; validate and extract data with regular expressions; model real-world entities with classes, objects, methods, and properties; and read and write files. Hands-on opportunities for lots of practice. Exercises inspired by real-world programming problems. No software required except for a web browser, or you can write code on your own PC or Mac.

link to CS50p: https://cs50.harvard.edu/python/2022/ 






