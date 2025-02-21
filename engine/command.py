import pyttsx3
import speech_recognition as sr
import pyaudio
import eel
import time
import os

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',130)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()
   

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("listening.....")
        eel.DisplayMessage("listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)
        
    try:
        print('recognizing....')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio,language='en-in')
        print(f"user-said : {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        
    except Exception as e:
        return ""
    
    return query.lower()
  
@eel.expose   
def allCommands(message = 1):
    
    if message ==1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    
    try:
        
    
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
    
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
            
        elif "send message" in query or "phone call" in query or "video call" in query or "message" in query or "call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query or "message" in query:
                    flag = 'message'
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query, flag, name)
        
        #elif "calculator" in query:
         #   speak("opening calculator")
          #  os.startfile("calc")
            
        elif "how are you" in query:
            speak("I am good,I hope you are also having a good day.")
            
        elif "who are you" in query:
            speak("I am jarvis, an artificial intelligence.")
            
        elif "hello" in query or "hi" in query or "hey" in query:
            speak("Hi, how can i help you")
    
        else:
            print("not running")
    
    except:
        print("error")    
        
    eel.ShowHood()