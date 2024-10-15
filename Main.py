from tkinter import *
from Functions import *


def inputFile():
    inputText = text0.get('1.0', 'end-1c')
    root.txt0.set("Input File Name: \"" + inputText + ".csv\"")


def funcft():
    global selFunc
    selFunc = "ft"
    root.txt1c.set("Function Selected: \"Find Tag\"")


def funcss():
    global selFunc
    selFunc = "ss"
    root.txt1c.set("Function Selected: \"Select Section\"")


def funcdi():
    global selFunc
    selFunc = "di"
    root.txt1c.set("Function Selected: \"Create DI Tags\"")


def functe():
    global selFunc
    selFunc = "te"
    root.txt1c.set("Function Selected: \"Create TESYS Tags\"")


def outputFile():
    outputText = text2.get('1.0', 'end-1c')
    root.txt2.set("Output File Name: \"" + outputText + ".csv\"")


class HST(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.txt0 = StringVar()
        self.txt1c = StringVar()
        self.txt2 = StringVar()

        global text0
        global text2

        frame0 = Frame(self)
        frame0.grid(row=0, column=0)
        Label(
            frame0, text="Enter Input File Name:").grid(column=0, row=0)
        text0 = Text(frame0, height=1)
        text0.grid(column=0, row=1)
        Button(frame0, text="Enter", command=inputFile).grid(
            column=0, row=2)
        Label(frame0, textvariable=self.txt0).grid(
            column=0, row=3)
        Label(frame0, text="").grid(column=0, row=4)

        frame1a = Frame(self)
        frame1a.grid(row=1, column=0)
        frame1b = Frame(self)
        frame1b.grid(row=2, column=0)
        frame1c = Frame(self)
        frame1c.grid(row=3, column=0)
        Label(
            frame1a, text="Select Function:").grid(column=0, row=0)
        Button(frame1b, text="Find Tag", command=funcft).grid(
            column=0, row=0)
        Button(frame1b, text="Select Section",
               command=funcss).grid(column=1, row=0)
        Button(frame1b, text="Create DI", command=funcdi).grid(
            column=2, row=0)
        Button(frame1b, text="Create TESYS",
               command=functe).grid(column=3, row=0)
        Label(frame1c, textvariable=self.txt1c).grid(column=0, row=0)
        Label(frame1c, text="").grid(column=0, row=1)

        frame2 = Frame(self)
        frame2.grid(row=4, column=0)
        Label(
            frame0, text="Enter Output File Name:").grid(column=0, row=0)
        text2 = Text(frame2, height=1)
        text2.grid(column=0, row=1)
        Button(frame2, text="Enter", command=outputFile).grid(
            column=0, row=2)
        Label(frame2, textvariable=self.txt2).grid(
            column=0, row=3)
        Label(frame2, text="").grid(column=0, row=4)

    def startwindow():
        root = Tk()
        root.title("Database Functions")
        root.resizable(False, False)

        frame1 = createframe1(root)
        frame1.grid(column=0, row=0)
        frame2 = createframe2(root)
        frame2.grid(column=0, row=1)
        frame3 = createframe3(root)
        frame3.grid(column=0, row=2)


root = HST()
root.mainloop()
