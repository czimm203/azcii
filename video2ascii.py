import cv2
import numpy as np
from os import system

ASCII_CHARS = "B#&@$%KL*)l1+>c;:,. "
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

def parse_image_cv(img):
    nums = np.vectorize(ASCII_DICT.get)(img)
    chars = [''.join(item) for item in nums.astype(str)]

    return chars

def ascii_cam():
    name = 'HI, MY NAME IS: ...'
    cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
    cv2.namedWindow(name, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    while(1):

        # Take each frame
        _, frame = cap.read()
        width,height,_ = frame.shape
        scaler = 1
        bg = np.zeros((int(width/scaler),int(height/scaler))).astype('uint8')

        #convert to grayscale
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #resize image to a width of 200 or user input. Reduce height to correct for character aspect ratio
        squish = (resize_image(grayscale,new_width=100)/REDUCER).astype('uint8')

        #parse array into characters
        ch = parse_image_cv(squish)

        for line in range(len(ch)):
            i = 0
            for char in ch[line]:
                cv2.putText(bg, char, (int(width/100*i)+5,line*10), 3,.25, (255, 255, 255), 1, cv2.LINE_AA)
                i += 1
        #Real feed and exit stuff
        cv2.imshow('frame',grayscale)
        cv2.imshow(name,bg)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

def ascii_terminal_player(show_cam=False):
    cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
    while(1):

        # Take each frame
        _, frame = cap.read()
        width,height,_ = frame.shape
        scaler = 1

        #convert to grayscale
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #resize image to a width of 200 or user input. Reduce height to correct for character aspect ratio
        squish = (resize_image(grayscale,new_width=200)/REDUCER).astype('uint8')

        #parse array into characters
        ch = parse_image_cv(squish)
        print(ch)
        
        #Real feed and exit stuff
        if show_cam:
            cv2.imshow('frame',grayscale)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()





if __name__ == '__main__':
    ascii_cam()

