from PIL import Image
import os

size_200=(200,200) # Image size
img_source='C:\\Users\\MH HABIB\\Desktop\\python\\projet\\images\\'
img_destination='C:\\Users\\MH HABIB\\Desktop\\python\\projet\\images\\200'
serial=1
for f in os.listdir(img_source):
    s=str(serial)
    if f.endswith('.jpg'):
        new_name='Image_'+s
        i=Image.open(img_source + f)
        f_name,f_ext=os.path.splitext(f)
        i.thumbnail(size_200) # to keep perfect resolution, thumbnail best
        # i=i.resize(size_200,Image.ANTIALIAS) # if you need size ratio 100% perfect, then the line would be better
        print('200/{}{}'.format(new_name,f_ext)) # see what happened
        i.save(img_destination+'/{}{}'.format(new_name,f_ext))
        serial=serial+1
