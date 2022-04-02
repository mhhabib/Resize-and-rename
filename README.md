## :rocket: Mutiple image resize and rename with Python Pillow

**What's the looks?**
![web](https://user-images.githubusercontent.com/17263976/64958697-8b562380-d8b1-11e9-8bcf-981bb6a07790.jpg)

**Why this app you need to use?**

- [x] This app can resize a multiple file such as jpg and png images within a second.
- [x] This app can edit your all file name such as images, videos within a second
- [x] In the time of resizing your images, this app maintain aspect ratio
- [x] Option also available to force resize  
- [x] After rename your file, it's easy to sort

**How the code works?**

> To make this, first you need to [download](https://pillow.readthedocs.io/en/stable/installation.html#windows-installation) pillow & them import to your code 
```sh
from PIL import Image
import os
```
> to maintain aspect ratio, following line will work better
```sh
i.thumbnail((200,200)) # (width,height) in pixel
```
> to mforce the size, following line will work better
```sh
i=i.resize((200,200),Image.ANTIALIAS) # Image.ANTIALIAS forces here to make the image into 200px X 200px
```
> In the following [rename](https://github.com/mhhabib/Image-Manipulation-with-Python-Pillow/blob/master/rename.py) code, we have to be said the current image folder and target folder
```sh
img_source='C:\\Users\\MH HABIB\\Desktop\\python\\projet\\images\\'
img_destination='C:\\Users\\MH HABIB\\Desktop\\python\\projet\\images\\200'
```
