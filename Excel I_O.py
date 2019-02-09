import xlwt
from tempfile import TemporaryFile
from PIL import Image
import time

book = xlwt.Workbook()
Sheet1 = book.add_sheet('Sheet1')

#Image analysis
now = time.time()

img = Image.open('NOIR800ISO.png').convert('L') #converts image to 8-bit grayscale
WIDTH, HEIGHT = img.size

data = list(img.getdata()) #converts image data to a list of integers

data1 = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]
#converts the data into a 2D representation (list) of the data

#for row in data1:
#    print(' '.join('{:3}'.format(value) for value in row))
#reads out the data


#Output to Excel file
#list1= [1,2,3,4,5,6,7,8,9,10]
#for j in range(0,2):
#    for i in range(0,5):
#        Sheet1.write(j,i,list1[5*j+i])

for j in range(0,HEIGHT):
    for i in range(0,WIDTH):
        Sheet1.write(j,i,data[(WIDTH*j)+i]) #maximum of 256 columns/rows only!

name = "Test.xls"
book.save(name)
book.save(TemporaryFile())

future = time.time()
print("Time taken: "+ str(future-now) + "s")
