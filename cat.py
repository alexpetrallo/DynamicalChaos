#Arnold's cat map image breakup 
from PIL import Image
# import cv2
import numpy as np

img = np.array((Image.open("andrej.png")))
N = img.shape[0]
x, y = np.meshgrid(range(N), range(N))


print("x:", str(x))
print("y:", str(y))
print("N:", str(N))

xmap = (2*x + y) % N
ymap = (x + y) % N


images = []
for i in range(3*N+1):
    re = Image.fromarray(img)
    # re.save("jack_" + str(i) + ".png")
    img = img[xmap, ymap]
    re.save('andrej' + str(i) + '.png')
    images.append(re)

images[0].save('jack.gif', save_all=True, append_images=images[1:], optimize=False, duration=30, loop=1)



