from PIL import Image, ImageFilter

im = Image.open('my_girl.jpg')
im2 = im.filter(ImageFilter.BLUR)

im2.save('blur.jpg', 'jpeg')