
f1 = open('image1.jpg','rb')

data = f1.read()
f = open('myimage.jpg', 'wb')
f.write(data)


f.close()
f1.close()
