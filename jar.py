import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

p = 'C:\\Program Files (x86)\\ArcSoft\\WebCam Companion 3\\uWebCam.exe'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hello Boss")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<15:
        speak("Good Afternoon!")

    elif hour>=16 and hour<19:
        speak("Good Evening!")
    
    else:
        speak("Good Night!")

    speak("I am Chitti ,How May I Help You ?")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print("You said : "+ query)

    except Exception as e:
        #print(e)
        print("Say that again Please!!")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email','password')
    server.sendmail('email', to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("opening google ")
            webbrowser.open("google.com")

        elif 'play music' in query:
            speak("playing music")
            music_dir = 'F:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, The time is"+ strTime)

        elif 'good job' in query:
            speak("Thank you ,Boss ,What else can i do for you?")

        elif 'how are you' in query:
            speak("Great Boss, What about you?")

        elif "about yourself" in query:
            speak("I am chitti! RAM 4 Gigabyte, memory 1 terabyte")

        elif 'vs code' in query:
            speak("opening vs code")
            path = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'sublime text' in query:
            speak("opening sublime text!")
            path = "C:\\Program Files\\Sublime Text 3\\subl.exe"
            os.startfile(path)

        elif 'email to x' in query:
            try:
                speak("Ok! Boss")
                speak("what should i say?")
                content = takeCommand()
                to = "x's email"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("email not sent!")

        elif 'teamviewer' in query:
            speak("opening team viewer")
            path = 'C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe'
            os.startfile(path)

        elif 'firefox' in query:
            speak("opening Mozilla Firefox")
            path = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
            os.startfile(path)

        elif 'dev c plus plus' in query:
            speak("opening dev c plus plus")
            path = 'C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe'
            os.startfile(path)
        
        elif 'camera' in query:
            speak("opening camera!")
            path = p
            os.startfile(path)
        
        elif 'chitti go on sleep mode' in query:
            speak("Ok! Boss,Going to sleep mode")
            break
        