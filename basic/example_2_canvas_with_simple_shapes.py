"""
Purpose of this script is to demo an example of a canvas

"""

from tkinter import Canvas, Tk, Frame


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Example 2 : Lines')
        self.pack()

        canvas = Canvas(self)
        # create a solid horizontal line
        canvas.create_line(15, 25, 200, 25)
        # create a dashed vertical line
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        # create a triangle
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        canvas.pack()



root = Tk()

ex = Example()
root.geometry('400x250+300+300')
root.mainloop()

