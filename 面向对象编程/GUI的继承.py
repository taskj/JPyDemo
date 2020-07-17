from tkinter import *
from tkinter.ttk import *

#创建GUI的基类
class GUIBase:
    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("600x600+700+150")
        self.frame.resizable(0,0)
        self.frame["bg"] = "lightgray"

        #配置style
        self.frame.Style01 = Style()
        self.frame.Style01.configure("TPaneWindows",background="lightcyan")
        self.frame.Style01.configure("TButton",font=("微软雅黑",12,"bold"))
        #添加pane容器
        self.frame.Pane_Detail = PanedWindow(self.frame,width=588,height=420)
        self.frame.Pane_Detail.place(x=6,y=110)
        #添加下面的关闭按钮
        self.frame.Button_close = Button(self.frame,text="关闭",width=10,command=self.close)
        self.frame.Button_close.place(x=480,y=550)

    def show(self):
        self.frame.mainloop()

    def close(self):
        self.frame.destroy()


#创建GUI派生类
class GUI01(GUIBase):
    def __init__(self):
        GUIBase.__init__(self)

        #修改GUI01的内容
        self.frame.Button_GUI01 = Button(self.frame,text="GUI01",width=10,command=self.close)
        self.frame.Button_GUI01.place(x=40, y=130)

if __name__ == '__main__':
    this = GUI01()
    this.show()