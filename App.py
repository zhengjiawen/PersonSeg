from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk


class App:
    def __init__(self):
        root = Tk()
        self.create_canvas(root)
        root.title("people segmentation")
        root.update()
        # root.resizable(False, False) 调用方法会禁止根窗体改变大小
        # 以下方法用来计算并设置窗体显示时，在屏幕中心居中
        curWidth = root.winfo_width()  # get current width
        curHeight = root.winfo_height()  # get current height
        scnWidth, scnHeight = root.maxsize()  # get screen width and height
        tmpcnf = '+%d+%d' % ((scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        root.geometry(tmpcnf)
        # root.geometry('1024x1280')
        root.mainloop()




    def create_canvas(self, root):
        lf = ttk.LabelFrame(root, text = 'origin image')
        lf.pack(fill=Y, padx=15, pady=8, side=LEFT)
        left_frame = Frame(lf)
        left_frame.pack(fill=Y, expand=YES, side=LEFT, padx=15, pady=8)
        left_frame.grid_rowconfigure(0, weight=1)
        left_frame.grid_columnconfigure(0, weight=1)
        xscroll = Scrollbar(left_frame, orient=HORIZONTAL)
        xscroll.grid(row=1, column=0, sticky=E + W)
        yscroll = Scrollbar(left_frame)
        yscroll.grid(row=0, column=1, sticky=N + S)
        canvas = Canvas(left_frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        canvas.grid(row=0, column=0, sticky=N + S + E + W)

        lf_right = ttk.LabelFrame(root, text='segmentation image')
        lf_right.pack(fill=Y, padx=15, pady=8, side=RIGHT)
        right_frame = Frame(lf_right)
        right_frame.pack(fill=Y, expand=YES, side=RIGHT, padx=15, pady=8)
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)
        xscroll2 = Scrollbar(right_frame, orient=HORIZONTAL)
        xscroll2.grid(row=1, column=0, sticky=E + W)
        yscroll2 = Scrollbar(right_frame)
        yscroll2.grid(row=0, column=1, sticky=N + S)
        canvas2 = Canvas(right_frame, bd=0, xscrollcommand=xscroll2.set, yscrollcommand=yscroll2.set)
        canvas2.grid(row=0, column=0, sticky=N + S + E + W)

        # function to be called when mouse is clicked
        def printcoords():
            File = filedialog.askopenfilename(parent=root, initialdir="C:/", title='Choose an image.')
            filename = ImageTk.PhotoImage(Image.open(File))
            canvas.image = filename  # <--- keep reference of your image
            canvas.create_image(0, 0, anchor='nw', image=filename)

        def printcoords2():
            File = filedialog.askopenfilename(parent=root, initialdir="C:/", title='Choose an image.')
            filename = ImageTk.PhotoImage(Image.open(File))
            canvas2.image = filename  # <--- keep reference of your image
            canvas2.create_image(0, 0, anchor='nw', image=filename)

        bottom_frame = Frame(root)
        Button(bottom_frame, text='choose', command=printcoords).pack(padx=10, pady=10)
        Button(bottom_frame, text='segmentation', command=printcoords2).pack(padx=10, pady=10)
        bottom_frame.pack()








if __name__ == '__main__':
    App()
