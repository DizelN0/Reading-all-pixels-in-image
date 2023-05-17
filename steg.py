from PIL import Image

img = Image.open('C:\Program Files\image.png', 'r')
# Using a loop, we run through each pixel and read it:
Weight = int(input('input a weight'))
High = int(input('input a high'))
for i in range(High):
    for j in range(Weight):
        r, g, b = img.getpixel((j, i))
        # Delete all white pixels:
        if not (r == g == b == 255):
            print(r, g, b)
