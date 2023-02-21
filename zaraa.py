import pyttsx3    # ye install kiya
import speech_recognition as sr
import datetime
import pyaudio
import emoji
import wikipedia  
import webbrowser 
import os
import random

engine = pyttsx3.init('sapi5')                     #sapi5 use hota h voice ko lene k liye
voices = engine.getProperty('voices')
print(voices[0].id)                                 # 0-1 se voice different hogi
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("hello i am zara, please tell me how may i help you")

def takeCommand():
    #it take microphones i/p from the users and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.8
        audio = r.listen(source)
    

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        #print(e)

        print("please said that again....")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    if 1:
        query= takeCommand().lower()
    #speak("akash is a good boy")
    ### logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query)
            speak("According to wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        
        elif 'play english music' in query:
            music_dir= 'F:\\New folder\\eng sound'
            songs= os.listdir(music_dir)
            print(songs)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))

        elif 'show me emoji' in query:
            speak("okay why not")
            print(emoji.emojize(":grinning_face_with_big_eyes:")) 
            print("\U0001F606") 
            print("U+1F618")
  
        
        elif 'play punjabi music' in query:
            music_dir= 'F:\\New folder\\music'
            songs= os.listdir(music_dir)
            songs.append
            print(songs)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))

        elif 'play movie' in query:
            movie_dir = 'F:\\New folder\\movie'
            movies = os.listdir(movie_dir)
            movies.append
            for number,movie in enumerate(movies):
                print(number,movie)
            speak("sir,which movie would you like to play ")
            movie_no = int(input("enter the movie number you want to play "))
            #random_movies = random.choice(movies)
            os.startfile(os.path.join(movie_dir,movies[movie_no]))


        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime} ")

        elif 'open vs code' in query:
            codepath= 'C:\\Program Files\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)

        elif 'open pycharm' in query:
            codepath1= 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains'
            os.startfile(codepath1)
