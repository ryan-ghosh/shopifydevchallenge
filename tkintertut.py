from tkinter import *
from PIL import ImageTk, Image

## create root widget
root = Tk()
root.title('image repository')

def forward(img_num:int):
    global button_back
    global button_forward
    global my_label

    my_label.grid_forget()
    my_label = Label(image=imagelist[img_num-1])
    button_forward = Button(root, text='>>', command=lambda: forward(img_num+1))
    button_back = Button(root, text='<<', command=lambda: back(img_num-1))

    if img_num==len(imagelist):
        button_forward = Button(root, text='>>', state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(img_num:int):
    global button_back
    global button_forward
    global my_label

    my_label.grid_forget()
    my_label = Label(image=imagelist[img_num-1])
    button_forward = Button(root, text='>>', command=lambda: forward(img_num+1))
    button_back = Button(root, text='<<', command=lambda: back(img_num-1))

    if img_num==1:
        button_back = Button(root, text='<<', state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    



img1 = ImageTk.PhotoImage(Image.open('resume.PNG'))
img2 = ImageTk.PhotoImage(Image.open('transcript.PNG'))
img3 = ImageTk.PhotoImage(Image.open('resume.PNG'))
img4 = ImageTk.PhotoImage(Image.open('resume.PNG'))
img5 = ImageTk.PhotoImage(Image.open('resume.PNG'))

imagelist = [img1, img2, img3, img4, img5]

my_label = Label(image=img1)
my_label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='EXIT PROGRAM', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

## create event loop
root.mainloop()


