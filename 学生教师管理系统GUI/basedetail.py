from tkinter import *
from tkinter.ttk import *

class BaseDetail(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("600x600+700+150")
        self.resizable(0,0)
        self["bg"] =  "lightgray"

        #准备一个style
        self.Style01 = Style()
        self.Style01.configure("Title.TLabel",font=("微软雅黑",18,"bold"),forground="Navy")
        self.Style01.configure("TPanedwindow",background="SkyBlue")
        self.Style01.configure("TButton",font=("微软雅黑",12,"bold"),forground="Navy")


        #加载一个标题label
        self.Label_Title = Label(self,text="学生明细",style="Title.TLabel")
        self.Label_Title.place(x=20,y=30)

        #准备一个Pane
        self.Pane_detail = PanedWindow(self,width=588,height=420)
        self.Pane_detail.place(x=6,y=110)

        #添加保存按钮
        self.Button_save = Button(self,text="保存",width=8)
        self.Button_save.place(x=350,y=540)

        # 添加关闭按钮
        self.Button_exit = Button(self, text="关闭", width=8)
        self.Button_exit.place(x=450, y=540)


if __name__ == '__main__':
    detail = BaseDetail()
    detail.mainloop()

