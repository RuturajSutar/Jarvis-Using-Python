import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss")

    else:
        speak("Good Evening Boss")

    speak("How may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")

    except Exception as e:
        speak("Boss Please Say that again Please")
        print("Boss Please Say that again Please")
        return "None"

    return query



if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open("google.com")

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open('stackoverflow.com')


        elif 'play music' in query:
            music_dir = 'C:\\Users\\Ruturaj\\Desktop\\Jarvis\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            speak("playing song")
            os.startfile(os.path.join(music_dir, songs[0]))
            # C:\\Users\\Ruturaj\\Desktop\\Jarvis

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss the time is {strTime}")

        elif 'open android studio' in query:
            speak("opening android studio")
            code_path = 'C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe'
            os.startfile(code_path)

        elif 'stop' in query:
            break








