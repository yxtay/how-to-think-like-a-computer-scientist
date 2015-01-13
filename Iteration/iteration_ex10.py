import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        oldred = p.getRed()
        oldgreen = p.getGreen()
        oldblue = p.getBlue()
        
        newred = int(oldred * 0.393 + oldgreen * 0.769 + oldblue * 0.189)
        newgreen = int(oldred * 0.349 + oldgreen * 0.686 + oldblue * 0.168)
        newblue = int(oldred * 0.272 + oldgreen * 0.534 + oldblue * 0.131)

        newpixel = image.Pixel(newred, newgreen, newblue)

        newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()