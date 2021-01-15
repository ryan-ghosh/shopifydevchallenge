from classes import *
from tkinter import *
from PIL import ImageTk, Image

## create root widget
root = Tk()
root.title('image repository')
repo = repository()
imge1 = image('forest mountain', 125.00, "mountain forest green water")
imge2 = image('river valley', 100.00, "river water blue sky nature")
imge3 = image('reflection', 678.00, "reflection water mountain clear")
imge4 = image('lighthouse', 500.00, "trail coast scenery ocean")
imge5 = image('flower trail', 170.00, "flowers green trail")
imge6 = image('sky valley', 255.00, "sky valley mountain rocks")
imge7 = image('top of the world', 346.00, "valley mountain forest green")
imge8 = image('London', 932.00, "city roads Europe dawn")
imge9 = image('desolate plain', 100.00, "flat shrub green mountain sky")
imge10 = image('island paradise', 120.00, "island ocean vacation rocks")
imge11 = image('tangerine dream', 250.00, "pink swamp jungle")
imge12 = image('castle in the sky', 1000.00, "reflection castle water mountain")
imge13 = image('this land', 800.00, "cave waterfall green scenery")
imge14 = image('peaceful dusk', 177.00, "dusk city scenery")
imge15 = image('Rio', 133.00, "city ocean tourist")
imge16 = image('Dubai', 147.00, "roads tower city")
imge17 = image('sunset', 138.00, "sunset city buildings background")
imge18 = image('Sydney', 277.00, "water city architecture")
imge19 = image('aurora', 950.00, "rocks sky night lights north stars")
imge20 = image('cold clear reflection', 1500.00, "snow cold ice reflection water sky clear")

imglist = [imge1, imge2, imge3, imge4, imge5, imge6, imge7, imge8, imge9, imge10, imge11, imge12, imge13, imge14, imge15, imge16, imge17, imge18, imge19, imge20]
repo.inventory = {imge1:1, imge2:1, imge3:1, imge4:1, imge5:1, imge6:1, imge7:1, imge8:1, imge9:1, imge10:1, imge11:1, imge12:1, imge13:1, imge14:1, imge15:1, imge16:1, imge17:1, imge18:1, imge19:1, imge20:1}

def forward(img_num:int):
    global button_back
    global button_forward
    global my_label
    global text_label

    my_label.grid_forget()
    my_label = Label(image=imagelist[img_num-1])
    button_forward = Button(root, text='>>', command=lambda: forward(img_num+1))
    button_back = Button(root, text='<<', command=lambda: back(img_num-1))
    

    if img_num==len(imagelist):
        button_forward = Button(root, text='>>', state=DISABLED)
        text_label = Text(root, height=1)
        text_label.insert(INSERT, imglist[len(imglist)-1].gettag())
    else:
        text_label = Text(root, height=1)
        text_label.insert(INSERT, "{}: ${}".format(imglist[img_num-1].gettag(), imglist[img_num-1].getprice()))
    text_label.grid(row=1,column=1)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=2, column=0)
    button_forward.grid(row=2, column=2)

def back(img_num:int):
    global button_back
    global button_forward
    global my_label
    global text_label

    my_label.grid_forget()
    my_label = Label(image=imagelist[img_num-1])
    button_forward = Button(root, text='>>', command=lambda: forward(img_num+1))
    button_back = Button(root, text='<<', command=lambda: back(img_num-1))
    
    if img_num==1:
        button_back = Button(root, text='<<', state=DISABLED)
        text_label = Text(root, height=1)
        text_label.insert(INSERT, "{}: ${}".format(imglist[img_num-1].gettag(), imglist[img_num-1].getprice()))
    else:
        text_label = Text(root, height=1)
        text_label.insert(INSERT, imglist[img_num-1].gettag())
    text_label.grid(row=1,column=1)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=2, column=0)
    button_forward.grid(row=2, column=2)
    

img1 = ImageTk.PhotoImage(Image.open('images/img1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('images/img2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('images/img3.jpeg'))
img4 = ImageTk.PhotoImage(Image.open('images/img4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('images/img5.jpg'))
img6 = ImageTk.PhotoImage(Image.open('images/img6.jpg'))
img7 = ImageTk.PhotoImage(Image.open('images/img7.jpg'))
img8 = ImageTk.PhotoImage(Image.open('images/img8.jpg'))
img9 = ImageTk.PhotoImage(Image.open('images/img9.jpg'))
img10 = ImageTk.PhotoImage(Image.open('images/img10.jpg'))
img11 = ImageTk.PhotoImage(Image.open('images/img11.jpg'))
img12 = ImageTk.PhotoImage(Image.open('images/img12.jpg'))
img13 = ImageTk.PhotoImage(Image.open('images/img13.jpg'))
img14 = ImageTk.PhotoImage(Image.open('images/img14.jpg'))
img15 = ImageTk.PhotoImage(Image.open('images/img15.jpg'))
img16 = ImageTk.PhotoImage(Image.open('images/img16.jpg'))
img17 = ImageTk.PhotoImage(Image.open('images/img17.png'))
img18 = ImageTk.PhotoImage(Image.open('images/img18.jpg'))
img19 = ImageTk.PhotoImage(Image.open('images/img19.jpg'))
img20 = ImageTk.PhotoImage(Image.open('images/img20.jpg'))

imagelist = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15, img16, img17, img18, img19, img20]


my_label = Label(image=img1)
my_label.grid(row=0, column=0, columnspan=3)
text_label = Text(root, height=1)
text_label.insert(INSERT, "{}: ${}".format(imge1.gettag(), imge1.getprice()))
text_label.grid(row=1, column=1)

button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='EXIT PROGRAM', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=2, column=0)
button_exit.grid(row=2, column=1)
button_forward.grid(row=2, column=2)


print("Hello, welcome to Picture Inc.")
print()
while True:
    print('possible commands: ')
    print('     - show inventory')
    print('     - buy')
    print('     - sell')
    print('     - search')
    print('     - exit')
    print('Enter command: ')
    command = input().split()
    if command[0] == 'show':
        try:
            print(repo)
        except TypeError:
            pass
    elif command[0] == 'buy':
        print("Enter name of picture: ")
        name = input()
        print("Enter price: ")
        price = float(input())
        print("Enter description")
        description = input()
        repo.buy(name, price, description)
    elif command[0] == 'sell':
        print("Enter name of picture: ")
        name = input()
        print("Enter discount if applicable or 0 if none: ")
        discount = float(input())
        repo.sell(name, discount)
    elif command[0] == 'search':
        print('Enter description: ')
        des = input()
        repo.search(des)
    elif command[0] == 'exit':
        print("Goodbye!")
        root.quit()
        break
    else:
        print('Invalid command')
    print()
    print('Remaining balances: {}'.format(repo.capital))
    print()

## create event loop
root.mainloop()


