from chatbot import chatbotRespuesta
from screenshot import format_image
from computer_vision import tag_name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
import time

animals = {
    'gato',
    'perro',
    'ave'
    }


def checkMensajes(usuario):
    try:
        numMens = usuario.find_element(By.CLASS_NAME,"_1pJ9J").text
        msleer = re.findall('\d+' ,numMens)
        if len(msleer) != 0:
            pending = True
        else:
            pending = False
    except:
        pending = False
    return pending

def getMsgPart(solicitud):
    mensaje = solicitud
    html = solicitud.get_attribute('outerHTML')#page_source
    participante = re.findall(r'data-pre-plain-text=.{1}\[.+](.+?):', html)
    return participante, mensaje

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

driver.get("https://web.whatsapp.com/")

usuariomsg =''

while usuariomsg !='exit':
    print("#", end=" ")
    time.sleep(2)

    conversaciones = driver.find_elements(By.CLASS_NAME, "_1Oe6M")
    for usuario in conversaciones:
        nombres = usuario.find_element(By.CLASS_NAME,"_21S-L")

        porresponder = checkMensajes(usuario)

        if porresponder:
            conversacion = usuario.find_element(By.CLASS_NAME,"_1pJ9J")
            conversacion.click()
            time.sleep(3)
            solicitudes = driver.find_elements(By.CLASS_NAME,"_27K43")
            driver.save_screenshot("C:\screenshot\photo.png")
            format_image()
            tagValues = tag_name()
            state = False
            if "texto" in tagValues:
                print(tagValues)
                for solicitud in solicitudes[-4:]:
                    participante, mensaje = getMsgPart(solicitud)
                    usuariomsg = mensaje.text.lower()

                print("Cliente:", participante, "Mensaje:", usuariomsg, end=" ")

                result = chatbotRespuesta(usuariomsg)
                textRespuesta = driver.find_element(By.CLASS_NAME, "_3Uu1_")
                textRespuesta.send_keys(result)
                textRespuesta.send_keys(Keys.ENTER)
                time.sleep(3)
                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            else:
                for v in animals:
                    if v in tagValues:
                        state = True
                        result = chatbotRespuesta(v)

                if state == True:
                    print(tagValues)
                    textRespuesta = driver.find_element(By.CLASS_NAME, "_3Uu1_")
                    textRespuesta.send_keys(result)
                    textRespuesta.send_keys(Keys.ENTER)
                    time.sleep(3)
                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                elif state == False:
                    print(tagValues)
                    textRespuesta = driver.find_element(By.CLASS_NAME, "_3Uu1_")
                    textRespuesta.send_keys(tagValues)
                    textRespuesta.send_keys(Keys.ENTER)
                    time.sleep(3)
                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()