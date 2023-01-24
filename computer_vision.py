from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
from googletrans import Translator, constants


'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = "1d87019fe7a341fa89db36bf3f14b056"
endpoint = "https://hacksic.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

'''
Quickstart variables
These variables are shared by several examples
'''
# Images used for the examples: Describe an image, Categorize an image, Tag an image,
# Detect faces, Detect adult or racy content, Detect the color scheme,
# Detect domain-specific content, Detect image types, Detect objects
images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")

remote_image_url = "https://storagesic.blob.core.windows.net/file-holder/Cropped_Image.jpg"
from selenium.webdriver.common.keys import Keys


def tag_name():
    tags = []
    tags.append('Se ha identificado en la foto:')
    tags.append((Keys.SHIFT) + (Keys.ENTER) + (Keys.SHIFT))
    translator = Translator()

    print("===== Tag an image - remote =====")
    # Call API with remote image
    tags_result_remote = computervision_client.tag_image(remote_image_url )

    # Print results with confidence score
    print("Tags in the remote image: ")
    if (len(tags_result_remote.tags) == 0):
        print("No tags detected.")
    else:
        for tag in tags_result_remote.tags:
            print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
            name = translator.translate(tag.name, dest="es")
            tags.append(name.text)
            tags.append((Keys.SHIFT) + (Keys.ENTER) + (Keys.SHIFT))
        return tags
    print()
    print("End of Computer Vision quickstart.")