'''
实现学生明细的GUI，由basedetail派生而来
'''
from basedetail import *

class StudentDetail(BaseDetail):
    def __init__(self):
        super().__init__()
        #修改title
        self.Label_Title["text"] = "学生明细信息"
        #修改style
        self.Style01.configure("TLabel",font=("微软雅黑",12),forground="Navy")
        #添加StudentDetail内容
        #学号
        self.Label_sno = Label(self.Pane_detail,text="学号:")
        self.Label_sno.place(x=140,y=40)
        self.Entry_sno = Entry(self.Pane_detail,font=("微软雅黑",14,"bold"),width=10)
        self.Entry_sno.place(x=210,y=38)
        #姓名
        self.Label_name = Label(self.Pane_detail, text="姓名:")
        self.Label_name.place(x=140, y=90)
        self.Entry_name = Entry(self.Pane_detail, font=("微软雅黑", 14, "bold"), width=10)
        self.Entry_name.place(x=210, y=88)
        #性别
        self.Label_gender = Label(self.Pane_detail, text="性别:")
        self.Label_gender.place(x=140, y=140)
        self.var_gender = IntVar()
        self.Radiu_man = Radiobutton(self.Pane_detail,text="男",variable=self.var_gender,value=1)
        self.Radiu_man.place(x=220,y=140)
        self.Radiu_woman = Radiobutton(self.Pane_detail, text="女",variable=self.var_gender, value=2)
        self.Radiu_woman.place(x=300, y=140)
        #出生日期
        self.Label_birthday = Label(self.Pane_detail, text="出生日期:")
        self.Label_birthday.place(x=100, y=190)
        self.Label_birthday = Entry(self.Pane_detail, font=("微软雅黑", 14, "bold"), width=10)
        self.Label_birthday.place(x=210, y=188)
        #手机号码
        self.Label_mobile = Label(self.Pane_detail, text="手机号码:")
        self.Label_mobile.place(x=100, y=240)
        self.Label_mobile = Entry(self.Pane_detail, font=("微软雅黑", 14, "bold"), width=10)
        self.Label_mobile.place(x=210, y=238)
        #邮箱地址
        self.Label_email = Label(self.Pane_detail, text="邮箱地址:")
        self.Label_email.place(x=100, y=290)
        self.Label_email = Entry(self.Pane_detail, font=("微软雅黑", 14, "bold"), width=10)
        self.Label_email.place(x=210, y=288)
        #所学专业
        self.Label_profession = Label(self.Pane_detail, text="所学专业:")
        self.Label_profession.place(x=100, y=340)
        self.Label_profession = Entry(self.Pane_detail, font=("微软雅黑", 14, "bold"), width=10)
        self.Label_profession.place(x=210, y=338)
        #入学时间
        self.Label_study_time = Label(self.Pane_detail, text="入学时间:")
        self.Label_study_time.place(x=100, y=390)
        self.Label_study_time = Entry(self.Pane_detail, font=("微软雅黑", 14, "bold"), width=10)
        self.Label_study_time.place(x=210, y=388)

if __name__ == '__main__':
    student = StudentDetail()
    student.mainloop()