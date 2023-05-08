import datetime
from datetime import time
import os
import speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 170)
engine.setProperty('volume', 0.5)
engine.setProperty('voice', 'english+f5')
# listener.stop()

def username():
    speak("What should i call you")
    uname = take_command()
    speak("Welcome")
    speak(uname)
    speak("How can i Help you")

def speak(text):
    engine.say(text)
    engine.runAndWait()
#
def take_command():
    global count
    try:
        with sr.Microphone() as source:
            listener.pause_threshold = 1
            print("listening...")
            voice = listener.listen(source, timeout=3, phrase_time_limit=5)
            r = sr.Recognizer()
            r.energy_threshold = 300
            r.adjust_for_ambient_noise(source, 1.0)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'snjbya' in command:
                command = command.replace('snjbya', '')

    except:
        speak("Say Again")
        return "None"

    return command


































# from flask import Flask, request, jsonify
# import speech_recognition as sr
#
# app = Flask(__name__)
#
# @app.route('/assistant', methods=['POST'])
# def assistant():
#     # Get audio data from the request
#     audio_data = request.files['audio'].read()
#
#     # Recognize speech using Google Speech Recognition
#     recognizer = sr.Recognizer()
#     try:
#         text = recognizer.recognize_google(audio_data)
#     except sr.UnknownValueError:
#         text = "Sorry, I didn't catch that."
#     except sr.RequestError:
#         text = "Sorry, there was an error processing your request."
#
#     # Return the recognized text as a JSON response
#     response = {'text': text}
#     return jsonify(response)
#
# if __name__ == '__main__':
#     app.run(debug=True)
