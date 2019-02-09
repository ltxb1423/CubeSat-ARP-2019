from PIL import Image
import time


now = time.time()

img = Image.open('Hi.png').convert('L') #converts image to 8-bit grayscale
WIDTH, HEIGHT = img.size

data = list(img.getdata()) #converts image data to a list of integers

data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]
#converts the data into a 2D representation (list) of the data

for row in data:
    print(' '.join('{:3}'.format(value) for value in row))
#reads out the data

future = time.time()
print("Time taken: "+ str(future-now) + "s")
