from PIL import Image
img = Image.open('C:\Program Files\image.png', 'r')
#Using a loop, we run through each pixel and read it:
for i in range(70):
    for j in range(450):
        r,g,b = img.getpixel((j,i))
        #Delete all white pixels:
        if not (r == g == b == 255) :
            print(r,g,b)


