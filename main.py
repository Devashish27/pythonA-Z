# import tkinter
# import cv2  # pip install opencv-python
# import PIL.Image, PIL.ImageTk  # pip install pillow
# from functools import partial
# import threading
# import time
# import imutils
#
#
# def play(speed):
#     print(f"You Clicked On PLay. Speed is {speed}")
#     if speed<0:
#       # Play The Video In Reverse
#           
#
#
# def pending(decision):
#     # 1. Display Decision Pending Image.
#     frame = cv2.cvtColor(cv2.imread("Decision.jpg"), cv2.COLOR_XYZ2RGB)
#     frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
#     frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
#     canvas.image = frame
#     canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
#
#     # 2. Wait For A Second.
#     time.sleep(1)
#
#     # 3. Display Sponsor Image.
#     frame = cv2.cvtColor(cv2.imread("sponsers.jpg"), cv2.COLOR_YUV2GRAY_YV12)
#     frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
#     frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
#     canvas.image = frame
#     canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
#
#     # 4. Wait For 1.5 Second.
#     time.sleep(1.5)
#
#     # 5. Display Out/Not Out Image.
#     if decision == 'out':
#         decisionImg = "out.jpg"
#     else:
#         decisionImg = "not_out.jpg"
#
#     frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BAYER_BG2RGB_EA)
#     frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
#     frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
#     canvas.image = frame
#     canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
#
#     # 6. Wait For 1.5 Second.
#     time.sleep(1.5)
#
#
# def out():
#     thread = threading.Thread(target=pending, args="out")
#     thread.daemon = 1
#     thread.start()
#     print("Player Is Out")
#
#
# def not_out():
#     thread = threading.Thread(target=pending, args="not out")
#     thread.daemon = 1
#     thread.start()
#     print("Player Is Not Out")
#
#
# # Width And Height Of Our Main Screen...!!
# SET_WIDTH = 480
# SET_HEIGHT = 350
#
# # Tkinter GUI Starts Here...!!
# window = tkinter.Tk()
# window.title("Tyro As Being Third Empire For All Cricket Matches")
# window.configure(bg='#002266')
# cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2LAB)
# canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
# photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
# image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
# canvas.pack()
#
# # Buttons To Control Playback..!!
# btn = tkinter.Button(window, text="<< Previous (Fast)", width=15, command=partial(play, -25))
# btn.pack()
#
# btn = tkinter.Button(window, text="<< Previous (Slow)", width=15, command=partial(play, -2))
# btn.pack()
#
# btn = tkinter.Button(window, text=">> Next (Slow)", width=15, command=partial(play, 2))
# btn.pack()
#
# btn = tkinter.Button(window, text=">> Next (Fast)", width=15, command=partial(play, 25))
# btn.pack()
#
# btn = tkinter.Button(window, text="-- Giving Umpire Out --", width=20, command=out)
# btn.pack()
#
# btn = tkinter.Button(window, text="++ Giving Umpire Not Out ++", width=20, command=not_out)
# btn.pack()
#
# window.mainloop()


# All media file is available for download as a zip file (See description)
import tkinter
import cv2  # pip install opencv-python
import PIL.Image, PIL.ImageTk  # pip install pillow
from functools import partial
import threading
import time
import imutils  # pip install imutils

stream = cv2.VideoCapture("clip.mp4")
flag = True


def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag


def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("Decision.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
    time.sleep(1.5)

    # 3. Display sponsor image
    frame = cv2.cvtColor(cv2.imread("sponsers.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
    time.sleep(2.5)
    # 5. Display out/notout image
    if decision == 'out':
        decisionImg = "out.jpg"
    else:
        decisionImg = "not_out.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")


# Width and height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368

# Tkinter gui starts here
window = tkinter.Tk()
window.title("CodeWithHarry Third Umpire Decision Review Kit")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

# Buttons to control playback
btn = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
btn.pack()
window.mainloop()


