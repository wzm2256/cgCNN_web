import os
import PIL.Image as Image

All = os.listdir('TextureNet')
for i in All:
    image = Image.open('TextureNet/' + i)
    new_image = image.crop((0,0,896,896))
    new_image.save('TextureNet_Crop/'+i)