import speech_recognition as sr
import pyttsx3


#engine2.say('How can i help you...?')



def talk(text):
    engine.say(text)
    engine.runAndWait()



listener = sr.Recognizer()
engine = pyttsx3.init()
engine2 = pyttsx3.init()
#engine2.say('Hello, what is your name ?')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

try:
    with sr.Microphone() as source:
        talk ("Hello, what is your name ?")
        print('Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        # compand2 = listener.record(voice)
        # print(compand2)
        print (command)

        #if 'sumon' in  command:
        talk("let's talk "+command)
        talk ("what do you want me to do?")
        print('Listening...')
        voice = listener.listen(source)
        command1 = listener.recognize_google(voice)
        if 'do you know my name' in command1:
            talk("yes its "+command)
        elif 'play' in command1:
            talk("what song?")
        else:
            talk("thank you!")
        print (command1)




except:
    pass