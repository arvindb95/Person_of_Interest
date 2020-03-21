import numpy as np
import cv2
from matplotlib import font_manager as fm, rcParams
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import face_recognition as fr
import os
import datetime

"""
Day zero begins Jun 2 2019

Admin : Arvind 
"""

def plot_crosshairs(image, enc_num, fig, ax, name):
    face_loc = (fr.face_locations(image))[enc_num]
    ht = np.shape(image)[0]
    fac = 0.05
    x1 = face_loc[3] - fac*ht
    x2 = face_loc[1] + fac*ht
    y1 = face_loc[2] + fac*ht
    y2 = face_loc[0] - fac*ht

    fpath = "/home/arvind/.local/share/fonts/BerkeliumIIHGR.ttf"
    prop = fm.FontProperties(fname=fpath)
    fname = os.path.split(fpath)[1]
    
    if (name == "ADMIN"):
        col = 'yellow'
    else:
        col = 'white'

    rect = patches.Rectangle((x2 ,y2 - fac*ht),(x1-x2),(y1-y2),linewidth=2,linestyle="--",edgecolor=col,facecolor='none')
    plt.scatter([(x1+x2)/2.0, (x1+x2)/2.0],[y1 - 1.3*fac*ht, y2 - 0.6*fac*ht], marker="|", c=col)
    plt.scatter([x1 + 0.4*fac*ht,x2 - 0.4*fac*ht],[(y1+y2-2*fac*ht)/2.0, (y1+y2-2*fac*ht)/2.0], marker="_", c=col)
    plt.scatter(x1 + 0.2*fac*ht, y2 - 0.1*fac*ht ,marker="$\u231c$",c=col, s=700)
    plt.scatter(x2 - 0.45*fac*ht, y2 - 0.1*fac*ht ,marker="$\u231d$",c=col, s=700)
    plt.scatter(x1 + 0.2*fac*ht, y1 - 1.4*fac*ht,marker="$\u231e$",c=col, s=200)
    plt.scatter(x2 - 0.45*fac*ht, y1 - 1.4*fac*ht,marker="$\u231f$",c=col, s=200)
    ax.text(x2 + fac*ht, y2, name, fontproperties=prop, color="white")
    ax.text(ht-30, ht-30, "DAY {d:0.0f}".format(d=day_number), fontproperties=prop, color="white")
    ax.add_patch(rect)

    return 0

date_zero = datetime.datetime(2019, 6, 2)
date_today = datetime.datetime.now()

day_number = (date_today - date_zero).days

#question = input("Ask me something : ")

#question = question.lower()

#if ((question == "who am i?") or (question == "what is my name?")): 

print("***********CAPTURING IMAGE***********")
print("***********SAY CHEEEEESE!!***********")

video_capture = cv2.VideoCapture(0)
s, test_image = video_capture.read()
cv2.imwrite("test_image.png", test_image)

if not video_capture.isOpened():
    raise Exception("Could not open video device")
ret, frame = video_capture.read()
video_capture.release()

# Comparing captured face with database of admin faces

admin_face = fr.load_image_file("Admin/admin.png")
test_image = fr.load_image_file("test_image.png")

admin_enc = fr.face_encodings(admin_face)[0]
test_enc = np.array(fr.face_encodings(test_image))

fig2, ax2 = plt.subplots(1)
ax2.imshow(test_image)

for i in range(len(test_enc)):
    results = fr.compare_faces([admin_enc], test_enc[i])[0]
    if(results == True):
        name = "ADMIN"
        plot_crosshairs(test_image, i, fig2, ax2, name)
    else :
        name = "XXX-XXX-XXX"
        plot_crosshairs(test_image, i, fig2, ax2, name)
plt.show()

os.system("rm -rf test_image.png")

#else:
#    print("I haven't learnt so much yet!")

