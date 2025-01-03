import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
from openai import OpenAI
recognizer = sr.Recognizer()
engine=pyttsx3.init()
news_api="NEWS API KEY"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiprogress(command):
    client = OpenAI(
    api_key= "OPEN AI API KEY",
)
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a Virtual assitant known as Jarvis skilled in general tasks like alexa and google cloud."},
        {
            "role": "user",
            "content": command
        }
    ]
)
    return completion.choices[0].message.content
    
def processcommand(command):
    command = command.lower()
    if "open google" in command:
        speak("opening google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in command:
        speak("opening facebook")
        webbrowser.open("https://www.facebook.com")
    elif command.lower().startswith("play"):
        song=command.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in command.lower():
        
        r=requests.get( "https://newsapi.org/v2/top-headlines?country=us&apiKey=365860ea196541d284a5d76653dd91a9")
        
        if r.status_code==200:
        #successful parse the Json Response
            speak("Here are some top news")
            data=r.json()
            articles=data.get('articles',[])
            for article in articles:
                speak(article.get('title'))
            
    else:
        
        speak(aiprogress(command))
        print(command)
    pass
if __name__=="__main__":
    speak("Hello, I am your virtual assistant. How can I help you?")
    #Recognizing the voice jarvis
    while True:
        r = sr.Recognizer()
        
        print('Recoginizing...')
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                    print("Listening...")
                    recognizer.adjust_for_ambient_noise(source,duration=1)
                    audio = recognizer.listen(source, timeout=5)
            word = recognizer.recognize_google(audio).lower()
            print(f"Detected word: {word}")   
            
            if(word=='jarvis'):
                speak("hii, how can i help you")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                command = recognizer.recognize_google(audio)
                processcommand(command)
                
            
        
        except Exception as e:
            print("error; {0}".format(e))

            pass