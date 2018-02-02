from PIL import Image

#获取图片尺寸
im = Image.open('my_girl.jpg')
w,h = im.size
print('Original image size: %sx%s' % (w, h))


#缩放
im.thumbnail((w//4, h//4))
print('Resize image to: %sx%s' % (w//2, h//2))
im.save('thumbnail.jpg', 'jpeg')
