import os

class Files:
    def __init__(self):

        #记录学生信息的文件路径
        self.student_path = "student.txt"
        #记录教师信息的文件路径
        self.teacher_path = "teacher.txt"
        #定义学生存储所用的List
        self.list_student_all = []
        #定义老师存储所用的List = []
        self.list_teacher_all = []

    def read_from_file(self):
        #读取学生信息
        try:
            with open(self.student_path,encoding="utf-8",mode="r") as fd_student:
                #逐行读取
                current_line = fd_student.readline()
                #判断是否有数据
                while current_line:
                    #分割成数组
                    student_list = current_line.split(",")
                    #直接添加
                    self.list_student_all.append(student_list)
                    #读取下一行
                    current_line = fd_student.readline()
        except Exception as e:
            raise e
        #读取教师信息
        try:
            with open(self.teacher_path,encoding="utf-8",mode="r") as fd_teacher:
                #逐行读取
                current_line = fd_teacher.readline()
                #判断是否有数据
                while current_line:
                    #分割成数组
                    teacher_list = current_line.split(",")
                    #直接添加
                    self.list_teacher_all.append(teacher_list)
                    #读取下一行
                    current_line = fd_teacher.readline()
        except Exception as e:
            raise e

if __name__ == '__main__':
    file = Files()
    file.read_from_file()
    print(file.list_teacher_all)
