import numpy as np

import json
import pickle
import nltk

from tensorflow.keras.models import load_model
from profitability import get_profitability
from weather import get_weather
from selenium.webdriver.common.keys import Keys

model = load_model("chatbot_model.h5")
biblioteca = json.loads(open("intents.json").read())


bolsadepalabras = []
clases = []
documents = []
for intent in biblioteca['intents']:

    clases.append(intent['tag'])

    for pattern in intent['patterns']:
        result = nltk.word_tokenize(pattern)
        bolsadepalabras.extend(result)

        documents.append((result, intent['tag']))

pickle.dump(bolsadepalabras, open("bolsadepalabras.pkl", "wb"))
pickle.dump(clases, open("classes.pkl", "wb"))


from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer('spanish')

ignore_words = ["?", "¿", "!", "¡", "."]

bolsadepalabras2 = []

for w in bolsadepalabras:
    if w not in ignore_words:
        wprocesada = w.lower()
        wprocesada = stemmer.stem(wprocesada)
        bolsadepalabras2.append(wprocesada)

print("bolsadepalabras2:", bolsadepalabras2)


bolsadepalabras = [stemmer.stem(w.lower()) for w in bolsadepalabras if w not in ignore_words]

def cleanEntrada(entradaUsuario):
    entradaUsuario = nltk.word_tokenize(entradaUsuario)
    entradaUsuario = [stemmer.stem(w.lower()) for w in entradaUsuario if w not in ignore_words]
    return entradaUsuario


def convVector(entradaUsuario, bolsadepalabras):
    entradaUsuario = cleanEntrada(entradaUsuario)

    vectorentrada = [0] * len(bolsadepalabras)
    for palabra in entradaUsuario:

        if palabra in bolsadepalabras:

            indice = bolsadepalabras.index(
                palabra)
            vectorentrada[indice] = 1

    vectorentrada = np.array(vectorentrada)
    return vectorentrada


entradausuario = "buenos dias gracias hasta luego"
vectorentrada = convVector(entradausuario, bolsadepalabras)
vectorentrada


def gettag(vectorentrada, LIMITE=0):
    vectorsalida = model.predict(np.array([vectorentrada]))[0]

    vectorsalida = [[i, r] for i, r in enumerate(vectorsalida) if r > LIMITE]

    vectorsalida.sort(key=lambda x: x[1], reverse=True)
    print(vectorsalida)

    listEtiquetas = []
    for r in vectorsalida:
        listEtiquetas.append({"intent": clases[r[0]], "probability": str(r[1])})
    return listEtiquetas


listEtiquetas = gettag(vectorentrada, LIMITE=0.1)


import random

crops = ['maiz', 'banano', 'arroz']



def getResponse(listEtiquetas, biblioteca):
    response = ''
    etiqueta = listEtiquetas[0]['intent']
    if etiqueta in crops:
        temperature, weatherValue = get_weather()
        profitabilityValue, bestValue = get_profitability(temperature, etiqueta)
        response = "\nLa temperatura actual es " + "{:.2f}".format(temperature) + "°C \u2602 y el clima es " +\
                   weatherValue + (Keys.SHIFT)+(Keys.ENTER)+(Keys.SHIFT) + "La estimacion de produccion del cultivo " + etiqueta +\
                   " es de " + str(profitabilityValue) + " ton/ha \u2692 \n" + "Si el clima se mantiene se producirá el " + "{:.1f}".format(profitabilityValue*100/bestValue) + \
                   "% del producto como resultado del cambio climático \u2757 recuerda contribuir con pequeñas obras para mejorar el planeta \u267B"
    else:
        response = ''

    listadediccionarios = biblioteca['intents']

    for dicionario in listadediccionarios:

        if etiqueta == dicionario['tag']:
            listaDeRespuestas = dicionario['responses']
            respuesta = random.choice(listaDeRespuestas)
            break
    return respuesta + response


respuesta = getResponse(listEtiquetas, biblioteca)


def chatbotRespuesta(entradaUsuario):
    vectorentrada = convVector(entradaUsuario, bolsadepalabras)
    listEtiquetas = gettag(vectorentrada, LIMITE=0)
    respuesta = getResponse(listEtiquetas, biblioteca)
    return respuesta