import face_recognition
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
import matplotlib.image as mpimg
import matplotlib.patches as patches
import face_recognition as fr
import os
import datetime


# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

date_zero = datetime.datetime(2019, 6, 2)
date_today = datetime.datetime.now()

day_number = (date_today - date_zero).days

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a second sample picture and learn how to recognize it.
admin_image = face_recognition.load_image_file("Admin/admin.png")
admin_face_encoding = face_recognition.face_encodings(admin_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    admin_face_encoding
]
known_face_names = [
    "ADMIN"
]

def grab_frame(cap):
    ret,frame = cap.read()
    return cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

def plot_crosshairs(face_loc, ht, fig, ax, name="XXX-XXX-XXX"):
    
    fac = 0.05
    x1 = face_loc[3] - fac*ht
    x2 = face_loc[1] + fac*ht
    y1 = face_loc[2] + fac*ht
    y2 = face_loc[0] - fac*ht

    col = "white"

    if (name == "ADMIN"):
        col = "yellow"

    #rect = patches.Rectangle((x2 ,y2 - fac*ht),(x1-x2),(y1-y2),linewidth=2,linestyle="--",edgecolor=col,facecolor='none')
    rect.set_x(x2)
    rect.set_y(y2 - fac*ht)
    rect.set_width(x1-x2)
    rect.set_height(y1-y2)
    rect.set_edgecolor(col)
    #plt.scatter([(x1+x2)/2.0, (x1+x2)/2.0],[y1 - 1.3*fac*ht, y2 - 0.6*fac*ht], marker="|", c=col)
    e1.set_xdata((x1+x2)/2.0)
    e1.set_ydata(y1 - 1.3*fac*ht)
    e1.set_color(col)
    e2.set_xdata((x1+x2)/2.0)
    e2.set_ydata(y2 - 0.6*fac*ht)
    e2.set_color(col)
    #plt.scatter([x1 + 0.4*fac*ht,x2 - 0.4*fac*ht],[(y1+y2-2*fac*ht)/2.0, (y1+y2-2*fac*ht)/2.0], marker="_", c=col)
    e3.set_xdata(x1 + 0.4*fac*ht)
    e3.set_ydata((y1+y2-2*fac*ht)/2.0)
    e3.set_color(col)
    e4.set_xdata(x2 - 0.4*fac*ht)
    e4.set_ydata((y1+y2-2*fac*ht)/2.0)
    e4.set_color(col)
    #plt.scatter(x1 + 0.2*fac*ht, y2 - 0.1*fac*ht ,marker="$\u231c$",c=col, s=700)
    c1.set_xdata(x1 + 0.2*fac*ht)
    c1.set_ydata(y2 - 0.05*fac*ht)
    c1.set_color(col)
    #plt.scatter(x2 - 0.45*fac*ht, y2 - 0.1*fac*ht ,marker="$\u231d$",c=col, s=700)
    c2.set_xdata(x2 - 0.45*fac*ht)
    c2.set_ydata(y2 - 0.05*fac*ht)
    c2.set_color(col)
    #plt.scatter(x1 + 0.2*fac*ht, y1 - 1.4*fac*ht,marker="$\u231e$",c=col, s=200)
    c3.set_xdata(x1 + 0.2*fac*ht)
    c3.set_ydata(y1 - 1.4*fac*ht)
    c3.set_color(col)
    #plt.scatter(x2 - 0.45*fac*ht, y1 - 1.4*fac*ht,marker="$\u231f$",c=col, s=200)
    c4.set_xdata(x2 - 0.4*fac*ht)
    c4.set_ydata(y1 - 1.4*fac*ht)
    c4.set_color(col)
    name_text.set_x(x2 + fac*ht)
    name_text.set_y(y2)
    name_text.set_text(name)
    ax.add_patch(rect)
    
    return 0

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

plt.ion()

fig, ax = plt.subplots(1)
fpath = "/home/arvind/.local/share/fonts/BerkeliumIIHGR.ttf"
prop = fm.FontProperties(fname=fpath)
fname = os.path.split(fpath)[1]

im = ax.imshow(grab_frame(video_capture))
ht = np.shape(grab_frame(video_capture))[0]
rect = patches.Rectangle((0,0),0,0, linewidth=2, linestyle="--", edgecolor='none', facecolor='none')
e1, = plt.plot(np.array([]),np.array([]), marker="|", c='none')
e2, = plt.plot(np.array([]),np.array([]), marker="|", c='none')
e3, = plt.plot(np.array([]),np.array([]), marker="_", c='none')
e4, = plt.plot(np.array([]),np.array([]), marker="_", c='none')
c1, = plt.plot(np.array([]), np.array([]) ,marker="$\u231c$",c='none', markersize=28)
c2, = plt.plot(np.array([]), np.array([]) ,marker="$\u231d$",c='none', markersize=28)
c3, = plt.plot(np.array([]), np.array([]) ,marker="$\u231e$",c='none', markersize=15)
c4, = plt.plot(np.array([]), np.array([]) ,marker="$\u231f$",c='none', markersize=15)
ax.text(ht-30, ht-30, "DAY {d:0.0f}".format(d=day_number), fontproperties=prop, color="white")

name_text = ax.text(0, 0, "", fontproperties=prop, color="white")

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if (name == "ADMIN"):
            plot_crosshairs((4*top, 4*right, 4*bottom, 4*left), np.shape(frame)[0], fig, ax, name=name)
        else :
            plot_crosshairs((4*top, 4*right, 4*bottom, 4*left), np.shape(frame)[0], fig, ax, name=name)
    # Display the resulting image
    im.set_data(grab_frame(video_capture))
    plt.pause(0.2)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        video_capture.release()
        break

# Release handle to the webcam
plt.ioff()
plt.axis('off')
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
plt.margins(0,0)
plt.show()
video_capture.release()
