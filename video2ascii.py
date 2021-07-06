import cv2
import numpy as np
from os import system

ASCII_CHARS = ['@','#','S','%','?','*','+',';',':',',','.',' ']
INDEX = range(len(ASCII_CHARS))
ASCII_DICT = {i:a for i,a in zip(INDEX,ASCII_CHARS)}
REDUCER = 256/len(ASCII_CHARS)
def load_as_grayscale(img_path):
    return cv2.imread(img_path,0)

def resize_image(image,new_width=200,corrected=True):
    height , width = image.shape
    squash = 1
    if corrected:
        squash = 8/18
    ratio = width/height
    new_img = cv2.resize(image,(int(new_width),(int(new_width*ratio*squash))),interpolation=cv2.INTER_NEAREST)
    return new_img

def parse_image(img):
    nums = np.vectorize(ASCII_DICT.get)(img)
    chars = [''.join(item) for item in nums.astype(str)]
    ascii = '\n'.join(chars)

    return ascii



def capture():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FPS,1) 

    while(1):

        # Take each frame
        _, frame = cap.read()

        #convert to grayscale
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #resize image to a width of 200 or user input. Reduce height to correct for character aspect ratio
        squish = (resize_image(grayscale)/REDUCER).astype('uint8')

        #parse array into characters
        ch = parse_image(squish)

        #"Animate"
        system('cls')
        print(ch)

        #Real feed and exit stuff
        cv2.imshow('frame',grayscale)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    capture()

