import datetime
import random
import json
import pickle
import nltk
import pymongo
import spacy
import dns
from nltk.stem import WordNetLemmatizer
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import numpy as np
from train import model, lemmatizer, words, classes, intents

import speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 170)
engine.setProperty('volume', 0.5)
engine.setProperty('voice', 'english+f5')
# listener.stop()
import re
import webbrowser
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s" # replace this with the path to your Chrome executable
from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from matplotlib import image
from tabulate import tabulate

# client = pymongo.MongoClient("mongodb+srv://govinda45:govinda45@cluster0.0uyhagm.mongodb.net/?retryWrites=true&w=majority")

# db = client['feedback']
# collection =db['questions']
# que=""

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning!")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")

    assname = ("SNJBEEA")
    talk("I am your Voice Assistant SNJBIA")


def talk(text):
    engine.say(text)
    engine.runAndWait()

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word)
                      for word in sentence_words]

    return sentence_words


c_fail = 0


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)

    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    ans = ""
    global c_fail
    fail = [""]
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    for i, r in enumerate(res):
        print(i, r)

    ERROR_THRESHOLD = 0.50

    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    recommend = [[i, r] for i, r in enumerate(res) if r < ERROR_THRESHOLD and r >= 0.01]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    recommend_list = []

    for r in results:
        return_list.append({'intent': classes[r[0]],
                            'probability': str(r[1])})
    for r in recommend:
        recommend_list.append({'intent': classes[r[0]]})
    #     print(recommend_list)
    if len(return_list) == 0:
        #         talk("Sorry, i can not able to find, you can ask related to")
        for i in recommend_list:
            ans = ans + i['intent'] + ", "
        # print(ans)
        #         talk(ans)
        return [{'intent': "None"}]
    else:
        return return_list

    # r=predict_class("pagal")


# print(r)
# talk(get_response(r, intents))

def get_response(intents_list, intents_json):
#     print(intents_list[0]['intent'])
    if intents_list[0]['intent']=="None":

        # dic = {"question": que}
        #
        # collection.insert_one(dic)

        return "Sorry currently your required answer is not in our database but don't worry we have added this question in our feedback system."
    else:
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        # print(tag)

        result = ''

        for i in list_of_intents:
            if i['tag'] == tag:
                if len(i['responses']) == 0 and i['tag'] == "college achievements":
                    return awards_achievements()

                elif len(i['responses']) == 0 and i['tag'] == "student achievements":
                    return student_placement()

                elif len(i['responses']) == 0 and i['tag'] == "notice board":
                    return notice_board()

                elif len(i['responses']) == 0 and i['tag'] == "past events of college":
                    return past_events()

                elif len(i['responses']) == 0 and i['tag'] == "placement coordinators":
                    placement_cordinators()

                elif len(i['responses']) == 0 and i['tag'] == "placements statistics":
                    return placement_statistics()

                elif len(i['responses']) == 0 and i['tag'] == "computer department faculty list":
                    return faculty_list()

                elif len(i['responses']) == 0 and i['tag'] == "computer event list":
                    return comp_event_list()

                else:
                    result = random.choice(i['responses'])

                    break
        return result

def student_placement():
    url = 'https://www.snjb.org/engineering/'

    # Send an HTTP request to the website and get the HTML content
    response = requests.get(url)
    html_doc = response.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    content_div = soup.find('div', {'id': 'myCarousel1'})
    # print(content_div)
    images = content_div.find_all('img')
    image_urls = [img['src'] for img in images]


    for i in range(1,10):
        webbrowser.get(chrome_path).open(image_urls[i])
    return set(image_urls)

def notice_board():
    url = 'https://www.snjb.org/engineering/'
    response = requests.get(url)
    html_doc = response.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    content_div = soup.find('div', {'class': 'home-div-31'})
    content_div=content_div.text
    content_div = content_div.replace('\n', '<br>')
    content_div = re.sub(r'<br\s*/?>\s*(<br\s*/?>\s*)+', '<br>', content_div)


#     content_div = content_div.replace('\n', '<br>')
#     content_div = re.sub(r'<br\s*/?>\s*(<br\s*/?>\s*)+', '<br>', content_div)
#     # Load the spaCy English model
#     nlp = spacy.load('en_core_web_sm')
#     # Tokenize the text into sentences using spaCy
#     doc = nlp(content_div)
#     sentences = [sent.text.strip() for sent in doc.sents]
#
#     # Remove duplicate sentences
#     unique_sentences = list(set(sentences))
#
# # Print the unique sentences
#     for sentence in unique_sentences:
#         print(sentence)
    return content_div

def past_events():
    url = 'https://www.snjb.org/engineering/'
    # Send an HTTP request to the website and get the HTML content
    response = requests.get(url)
    html_doc = response.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    content_div1= soup.find('div', {'id': 'myCarousel2'})
    content_div1=content_div1.text
    content_div1= content_div1.replace('\n', '<br>')
    content_div1 = re.sub(r'<br\s*/?>\s*(<br\s*/?>\s*)+', '<br>', content_div1)
    return content_div1

def placement_cordinators():
    # Make a request to the website
    response = requests.get('https://www.snjb.org/engineering/Placement/engineering_mba_placement_profile')

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    placement_cordinator = soup.find('section', {'id': 'section61'})
    # print(placement_cordinator)
    # Find the table on the page
    table = placement_cordinator.find('table')
    dir(table)
    # Extract the table headers
    headers = []
    for th in table.findAll('th'):
        headers.append(th.text.strip())

    # Extract the table rows
    rows = []
    for tr in table.findAll('tr')[1:]:
        row = []
        for td in tr.findAll('td'):
            row.append(td.text.strip())
        rows.append(row)

    return tabulate(rows, headers=headers)

def placement_statistics():
# Make a request to the website
    response = requests.get('https://www.snjb.org/engineering/Placement/engineering_mba_placement_profile')

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    placement_statisctics = soup.find('section', {'id': 'section71'})
    placement_statisctics_image=placement_statisctics.find('img')
    placement_statisctics_image_urls= [img['src'] for img in placement_statisctics_image]
    print(placement_statisctics_image_urls)
    for i in range(len(placement_statisctics_image_urls)):
        webbrowser.get(chrome_path).open(placement_statisctics_image_urls[i])
    return "Statistics"

def faculty_list():
    # Make a request to the website
    response = requests.get('https://www.snjb.org/engineering/Computer_engineering/computer_engineering_people')

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    faculty_list = soup.find('table')
    headers = []
    for th in faculty_list.findAll('th'):
        headers.append(th.text.strip())
    # Extract the table rows
    rows = []
    for tr in faculty_list.find_all('tr')[1:]:
        row = []
        for td in tr.find_all('td'):
            if td.find('a'):
                link = td.find('a').get('href')
                row.append(link)
            else:
                row.append(td.text.strip())
        rows.append(row)
    return tabulate(rows, headers=headers)

def comp_event_list():
    response = requests.get('https://www.snjb.org/engineering/Computer_engineering/computer_engineering_events')

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    placement_cordinator = soup.find('div', {'id': 'tab_event'})
    # print(placement_cordinator)
    # Find the table on the page
    table = placement_cordinator.find('table')
    # print(table)
    # Extract the table headers
    headers = []
    for th in table.findAll('th'):
        headers.append(th.text.strip())

    # Extract the table rows
    rows = []
    for tr in table.findAll('tr')[1:]:
        row = []
        for td in tr.findAll('td'):
            row.append(td.text.strip())
        rows.append(row)

    return tabulate(rows, headers=headers)

def awards_achievements():
    url = 'https://www.snjb.org/engineering/About/engineering_mba_awards_acievements'

    # Send an HTTP request to the website and get the HTML content
    response = requests.get(url)
    html_doc = response.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    content_div1= soup.find('div', {'class': 'vm-div-31'})
    awards_achievements=content_div1.find_all('img')
    awards_achievements = [img['src'] for img in awards_achievements]

    for i in range(len(awards_achievements)):
        webbrowser.get(chrome_path).open(awards_achievements[i])
    return content_div1.text



def calling_bot(txt):
    global res
    global que
    que=txt

    predict = predict_class(txt)
    res= get_response(predict, intents)

    # engine.say(res)
    # engine.runAndWait()
    return res
    # engine.say(res)
    # engine.runAndWait()







if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")

    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)
        talk(resp)


