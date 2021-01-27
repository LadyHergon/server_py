from PIL import Image
import colorsys
image = Image.open('Companylogo.png')
image_data = image.load()
height,width = image.size
print(height)
print(width)

for loop1 in range(height):
    for loop2 in range(width):
        r,g,b,a = image_data[loop1,loop2]
        if (r+g+b) ==0 and a !=0:
            image_data[loop1,loop2] =255,255,255,255
        # h,l,s = colorsys.rgb_to_hls(r, g, b)
        # if (h < 150/255 and  l != 255.0 and l > 130 and s>-1) or (30<r+g+b<600 and (r>210 or (g>120 and b<200))):
            # image_data[loop1,loop2] =255,255,255,255
            # if (g - 128) < 10:
            #     print(r,g,b)

image.save('changed.png')