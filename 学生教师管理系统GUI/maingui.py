from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from fileoperator import *

class MainGUI(Tk):
    def __init__(self):
        super().__init__() #初始化基类的构造方法
        self.title("学生教师信息管理")
        self.geometry("1400x600+100+100")
        self.resizable(0,0)
        
        #实例化File类,把教师和学生信息读取到系统
        self.file_info = Files()
        self.student_all = self.file_info.list_student_all
        self.teacher_all = self.file_info.list_teacher_all
        print(self.student_all)
        #定义style
        self.Style01 = Style()
        self.Style01.configure("TLabel",font=("微软雅黑",14,"bold"),foreground="Navy")

        #学生和老师的标签
        self.label_student = Label(self,text="学生信息列表:")
        self.label_student.place(x=40,y=60)
        self.lable_teacher = Label(self,text="教师信息列表:")
        self.lable_teacher.place(x=720,y=60)

        #添加学生表格
        self.student_gui()
        #添加老师表格
        self.teacher_gui()

        # 自动加载学生和教师信息到表格
        self.load_student_treeview()
        self.load_teacher_treeview()

    def student_gui(self):
        #添加tree_view控件
        self.Tree_student = Treeview(self,columns = ("sno","name","gender","profession","mobile","email"),show="headings",height=20)
        #设置每一列的对齐方式
        self.Tree_student.column("sno",width=80,anchor="center")
        self.Tree_student.column("name", width=80, anchor="center")
        self.Tree_student.column("gender", width=60, anchor="center")
        self.Tree_student.column("profession", width=120, anchor="center")
        self.Tree_student.column("mobile", width=150, anchor="center")
        self.Tree_student.column("email", width=150, anchor="center")
        #设置每个列的标题
        self.Tree_student.heading("sno",text="学号")
        self.Tree_student.heading("name", text="姓名")
        self.Tree_student.heading("gender", text="性别")
        self.Tree_student.heading("profession", text="专业")
        self.Tree_student.heading("mobile", text="手机号码")
        self.Tree_student.heading("email", text="邮箱")

        self.Tree_student.place(x=35,y=95)

        #添加按钮
        self.Button_add_student = Button(self,text="添加",width=10)
        self.Button_add_student.place(x=400,y=550)

        #修改按钮
        self.Button_update_student = Button(self,text="修改",width=10)
        self.Button_update_student.place(x=500,y=550)

        #删除按钮
        self.Button_del_student = Button(self,text="删除",width=10)
        self.Button_del_student.place(x=600,y=550)


    def teacher_gui(self):
        # 添加tree_view控件
        self.Tree_teacher = Treeview(self, columns=("tid", "name", "gender", "title", "college", "mobile"),show="headings", height=20)
        self.Tree_teacher.column("tid", width=80, anchor="center")
        self.Tree_teacher.column("name", width=80, anchor="center")
        self.Tree_teacher.column("gender", width=60, anchor="center")
        self.Tree_teacher.column("title", width=120, anchor="center")
        self.Tree_teacher.column("college", width=150, anchor="center")
        self.Tree_teacher.column("mobile", width=150, anchor="center")

        #设置每个列的标题
        self.Tree_teacher.heading("tid",text="编号")
        self.Tree_teacher.heading("name", text="姓名")
        self.Tree_teacher.heading("gender", text="性别")
        self.Tree_teacher.heading("title", text="职称")
        self.Tree_teacher.heading("college", text="毕业院校")
        self.Tree_teacher.heading("mobile", text="手机号码")

        self.Tree_teacher.place(x=700, y=95)

    def load_student_treeview(self):
        #1 先把当前Treeview内容清空
        for index in self.Tree_student.get_children():
            self.Tree_student.delete(index)
        #2 加载list中的数据
        if len(self.student_all) == 0:
            showinfo("系统消息","没有任何学生信息需要加载")
        else:
            for index in range(len(self.student_all)):
                self.Tree_student.insert("",index,values=(
                    self.student_all[index][0],
                    self.student_all[index][1],
                    self.student_all[index][2],
                    self.student_all[index][6],
                    self.student_all[index][4],
                    self.student_all[index][5]
                    )
                )

    def load_teacher_treeview(self):
        # 1 先把当前Treeview内容清空
        for index in self.Tree_teacher.get_children():
            self.Tree_teacher.delete(index)
        # 2 加载list中的数据
        if len(self.teacher_all) == 0:
            showinfo("系统消息", "没有任何教师信息需要加载")
        else:
            for index in range(len(self.teacher_all)):
                self.Tree_teacher.insert("", index, values=(
                    self.teacher_all[index][0],
                    self.teacher_all[index][1],
                    self.teacher_all[index][2],
                    self.teacher_all[index][6],
                    self.teacher_all[index][7],
                    self.teacher_all[index][4]
                )
                                         )


if __name__ == '__main__':
    main = MainGUI()
    main.mainloop()
