# AgroBot
Integrantes del equipo
1. Jennifer Gonzalez
2. Gerardo Moreno
3. Ángeles Pitano
4. Natalia Bustamante
5. Felix Aldeano

# Chatbot inteligente
GreenBot un chatbot interactivo basado en reconocimiento de lenguaje natural para mejorar los servicios principales de MELO. El ambiente de desarrollo del chatbot es la vía de conexión entre los clientes y productores que busquen algún tipo de servicio en la empresa MELO, ya sea a nivle empresarial, agrónomo o para las comodidades de su casa junto a su mascota. La herramienta proveerá una conexión directa con los usuarios para indicar el posible servicio que requieran, permitiendo mandar imágenes para que registre data que pueda serle útil al usuario y devolver un mensaje con el contexto de la imágen gracias a APIs de Azure Cognitive Services. Por otra parte se intengra una conexión a los servidores de OpenWeatherMap para obtener el clima en tiempo real, lo que permite generar una estimación de posibles producción de un cultivo dependiendo de la temperatura del país e indicándole al productor la cantidad de productos que podría obtener en condiciones óptimas.

# Función Script
1.	Train_chatbot: Script de entrenamiento del modelo a utilizar para recrear las conversaciones con el chatbot. Este posee la biblioteca de datos o palabras que dan como resultado el reconocimiento de patrones o contextos en la conversación.
2.	Chatbot: Script con funciones principales para la ejecución del chatbot. Las funciones utilizadas generan los procesamientos de respuestas comunes, donde se toma el contexto de los mensajes del usuario para ser analizados en el modelo del chatbot entrenado, de esta manera, produciendo una respuesta acertada.
3.	Weather: Script de redireccionamiento para el servidor de OpenWeatherMap. El script entrega la dirección url junto a las llaves de verificación que permiten dar el acceso al programa a toda la información o data del servidor, en este caso, verificando el clima de Panamá.
4.	Profiability: Script de data con una lista de los rangos de producción registrados con respecto a temperaturas captadas en territorio nacional. Este script es el encargado de dar las estimaciones de producción de un cultivo utilizando la data de un estudio realizado desde el año 2005 en Panamá con la producción en toneladas por hectárea de los cultivos del maíz, banano y arroz.
5.	Whatsapp: Script que genera el buscador para enlazar un número privado al sistema de respuestas del chatbot.
6.	Screenshot: Script encargado de capturar y editar la imagen del buscador cuando un usuario envia un mensaje o una foto. Esta imagen será almacenada en el disco local para luego ser guardada en un servidor de Azure Storage.
7.	Get_URL: Script con los servicios de Azure Storage para almacenar la imagen capturada por el buscador en un servidor, de manera que se genere un URL que redirige a la imagen guardada.
8.	Computer_vision: Script basado en las tecnologías de Azure Cognitive Service para integrar un módelo de visión artificial en tiempo real. Este recibe el url generado para procesar la data de la imagen y devolver un conjunto de etiquetas que describen la imagen enviada.

# Inicio del sistema
Para ejecutar el codigo, se debe configurar los puertos de enlace a los servicios de Azure Cognitive Service y Azure Storage. Luego solo se deberá ejecutar el archivo whatsaap.py el cual expondrá un buscador para enlazar un numero de telefono al servidor de whatsapp el cual estara conectado a python. A partir de este punto, el chatbot estara totalmente funcional.

# Vistas del funcionamiento
Saludo del chatbot

![image](https://user-images.githubusercontent.com/120022842/214455978-65b641b6-aece-4a99-867e-87d1b3c1a404.png)

Servicios entregados por el chatbot

![image](https://user-images.githubusercontent.com/120022842/214435343-f0a33f3f-f263-4afe-b02a-7aa9d6ef1957.png)

Chatbot empleado los servicios de OpenWeatherMap

![image](https://user-images.githubusercontent.com/120022842/213750975-9b9d3804-3d13-4072-ba39-bf6472ca4bc1.png)
![image](https://user-images.githubusercontent.com/120022842/213750985-cff96566-0fdd-4937-bc81-a449d5ce2515.png)

Vision artificial - reconocimiento de imágenes

![image](https://user-images.githubusercontent.com/120022842/214435880-ad07346e-bf59-4793-b52d-48409f2cfa81.png)
![image](https://user-images.githubusercontent.com/120022842/214435831-feed338d-3bf3-49b1-9196-8fc0cd612dbe.png)
