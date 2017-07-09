
from PIL import Image, ImageDraw
import numpy as np

# size of image
canvas = (64, 64)

# scale ration
scale = 1
thumb = canvas[0]/scale, canvas[1]/scale

# rectangles (width, height, left position, top position)
frames = [(50, 50, 5, 5), (60, 60, 100, 50), (100, 100, 205, 120)]

# init canvas
im = Image.new('RGB', canvas, (255, 255, 255, 255))
draw = ImageDraw.Draw(im)

# draw rectangles
#for frame in frames:
#    x1, y1 = frame[2], frame[3]
#    x2, y2 = frame[2] + frame[0], frame[3] + frame[1]
#    draw.rectangle([x1, y1, x2, y2], outline=(0, 0, 0, 255))

yp = np.random.uniform(10,50)

draw.rectangle([10,yp,30,yp+10], fill = 'grey', outline = (0,0,0,255))

def draw_images(actions):
    #assert actions.shape == (64,4)

    image_batch = np.zeros(shape=(64,3,64,64)).astype('float32')

    for ind in range(0,64):
        im = Image.new('RGB', canvas, (255, 255, 255, 255))
        draw = ImageDraw.Draw(im)

        yp = np.random.uniform(10,50)

        draw.rectangle([10,yp,30,yp+10], fill = 'grey', outline = (0,0,0,255))

        image_batch[ind] = np.array(im).transpose(2,0,1)

    return image_batch

# make thumbnail
#im.thumbnail(thumb)

# save image
#im.save('im.png')

#print np.array(im).shape

print draw_images(None).shape



