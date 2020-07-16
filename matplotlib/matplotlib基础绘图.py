from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,16,26,23,25,14,12,23,13,4,21,36]

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)

#绘图
plt.plot(x,y)

#设置x轴的刻度
plt.xticks(x)

#展示图形
plt.show()

#保存图片
#plt.savefig("./t1.png")