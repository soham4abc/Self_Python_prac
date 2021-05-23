# import speech_recognition as sr
# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[1].id)

# def talk(text):
#     # engine.say('I am your teacher.')
#     # engine.say('How can i help you...?')
#     engine.say(text)
#     engine.runAndWait()

# listener = sr.Recognizer()

# try:
#     with sr.Microphone() as source:
#         print('Listening...')
#         voice = listener.listen(source)
#         command = listener.recognize_google(voice)
#         # compand2 = listener.record(voice)
#         # print(compand2)
#         print (command)

#         if 'sumon' in  command:
#             talk(command)
# except:
#     pass

import os
from os.path import join, dirname
from pprint import pprint
import vonage

client = vonage.Client(
    application_id="86272994-f37d-4ec0-8945-b2cd5182a20e",
    private_key=os.environ.get("./private_key.key"),
)
voice = vonage.Voice(client)

response = voice.create_call({
    'to': [{'type': 'phone', 'number': "918420850382"}],
    'from': {'type': 'phone', 'number': "918420850382"},
    'ncco': [{'action': 'talk', 'text': 'This is a text to speech call from Nexmo'}]
})


pprint(response)