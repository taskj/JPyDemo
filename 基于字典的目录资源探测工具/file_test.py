with open("dic.txt","r") as f:
    line_list = f.readlines()
    print(len(line_list))
    print(type(line_list))
    for line in line_list:
        print(line.strip())