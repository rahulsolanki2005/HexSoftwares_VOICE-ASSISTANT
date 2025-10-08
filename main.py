import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import time

myName = 'Tom'

engine = pyttsx3.init('espeak')  # For Windows use 'sapi5'
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)
engine.setProperty('rate', 170)   # Make the speaking speed natural

def speak(audio):
    print(f"{myName}: {audio}")
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(f"I am {myName}, your personal AI assistant. How can I help you today?")

def hearMe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
    except Exception:
        speak("Sorry, I didn’t catch that. Can you please repeat?")
        return None
    return query.lower()

def process_command(query):
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace('wikipedia', '')
        try:
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia,")
            print(result)
            speak(result)
        except:
            speak("Sorry, I couldn't find any results on Wikipedia.")
            
    elif 'open google' in query:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
        
    elif 'open youtube' in query:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
        
    elif 'open instagram' in query:
        speak("Opening Instagram.")
        webbrowser.open("https://www.instagram.com")
        
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {strTime}")
        
    else:
        speak("Here’s what I found on the internet.")
        webbrowser.open(f"https://www.google.com/search?q={query}")

if __name__ == "__main__":
    wishme()
    while True:
        query = hearMe()
        if query is None:
            continue
        
        process_command(query)

        # After executing a command, ask user if they want more help
        speak("Do you want me to do something else?")
        ans = hearMe()
        if ans is None:
            speak("I didn’t hear that properly. I’ll take it as a no.")
            break
        elif 'no' in ans or 'stop' in ans or 'exit' in ans or 'quit' in ans:
            speak("Okay, have a great day! Goodbye.")
            break
        elif 'yes' in ans or 'yeah' in ans or 'sure' in ans:
            speak("Alright! What would you like me to do?")
            continue
        else:
            speak("I’ll take that as a no. See you soon!")
            break
