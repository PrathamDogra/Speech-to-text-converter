import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Now:")
    audio = r.listen(source)
    
    
    
    try:
        
        text = r.recognize_google(audio)
        print("You Said :{}".format(text))
    
    except:
        print("Sorry couldn't hear your voice")