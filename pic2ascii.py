#Heavily inspired by https://www.youtube.com/watch?v=v_raWlX7tZY, https://www.youtube.com/watch?v=2fZBLPk-T2Y

import PIL.Image

ASCII_CHARS = ['@','#','S','%','?','*','+',';',':',',','.']

def resize_img(img,new_width=200):
    width,height = img.size
    ratio = height/width
    squash = 8/18    #squash is meant to correct the difference in aspect ratio between a pixel(square) and ascii char(rectangle)

    new_height = int(new_width*ratio)
    resized_image = img.resize((new_width,int(new_height*squash)))
    return resized_image

def grayify(img):
    return img.convert('L')

def pixels_to_ascii(img):
    pixels = img.getdata()
    index_scaler = len(ASCII_CHARS)/256
    chars = ''.join([ASCII_CHARS[int(pixel*index_scaler)] for pixel in pixels])
    return chars

def create_ascii_image(image_path:str,html=False,new_width=200):
    image = PIL.Image.open(image_path)
    new_image_data = pixels_to_ascii(grayify(resize_img(image,new_width=new_width)))
    pixel_count = len(new_image_data)
    if html:
        delimeter='<br>'
    else:
        delimeter='\n'
    ascii_img = '<br>'.join([new_image_data[i:(i + new_width)] for i in range(0,pixel_count,new_width)])
    return ascii_img
    



def cli(prnt=False,new_width=200):
    try:
        path = input('Enter image path:\n')
        image = PIL.Image.open(path)

    except:
        print('No image at the given location')

    new_image_data = pixels_to_ascii(grayify(resize_img(image)))
    pixel_count = len(new_image_data)
    ascii_img = '\n'.join([new_image_data[i:(i + new_width)] for i in range(0,pixel_count,new_width)])
    
    if prnt:
        print(ascii_img)


    with open('ascii_img.txt','w') as f:
        f.write(ascii_img)
        
        
        

if __name__ == '__main__':
    cli()