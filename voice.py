import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am siri Mam,Please tell me how can I help you")

def takecommand():
    #it takes microphone as input from the user and returns string as output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..............")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that once again please....")
        return "None"
    
    return query.lower()

def main():
    wishMe()
    while True:
        query=takecommand()
        if query=="None":
            continue

        #logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak('searching Wikipedia....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("Acording to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir="C:/Users/dell/Desktop/music/song1"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam,the time is {strTime}")

        elif 'open code' in query:
            codepath="C:/Users/dell/Desktop/python programming/voice.py"
            os.startfile(codepath) 
        
        elif 'exit' in query:
            speak("GoodBye,Mam!")
            break

if __name__=="__main__":
    main()