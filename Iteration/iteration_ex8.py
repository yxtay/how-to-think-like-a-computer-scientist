import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        average = (p.getRed() + p.getGreen() + p.getBlue()) / 3
        newred = average
        newgreen = average
        newblue = average

        newpixel = image.Pixel(newred, newgreen, newblue)

        newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()