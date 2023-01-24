import cv2
from get_url_image import uploadToBlobStorage
def format_image():
    img = cv2.imread('C:\screenshot\photo.png')
    croppep_image = img[320:730, 573: 880]
    print(img.shape)
    cv2.imwrite("Cropped_Image.jpg", croppep_image)
    uploadToBlobStorage('C:\\Users\\gerar\\OneDrive\\Documents\\GitHub\\AgroBot\Cropped_Image.jpg', 'Cropped_Image.jpg')