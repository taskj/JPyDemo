import cv2 #opencv默认读取的格式是BGR而非RGB

def init():
    img = cv2.imread('cat.jpg')
    #如果需要灰度图则添加下面的第二参数
    #img = cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)
    print(img.size) #获取图像的像素点个数
    print(img.shape) #获取图像的H,W,C值，如转换成灰度图则不存在C值
    print(img.dtype) #获取图像的数据类型

   
'''
保留BGR中的R通道,BG通道同理
@img : openvc读取的图片对象
012
BGR
'''
def saveR(img):
    cur_img = img.copy()
    cur_img[:,:,0] = 0
    cur_img[:,:,1] = 0
    cv_show('R',cur_img)

'''
提取图片颜色通道
@img : openvc读取的图片对象
'''
def getBgr(img):
    b,g,r = cv2.split(img)
    print(b,g,r)

'''
还原图片颜色通道
@img : openvc读取的图片对象
'''
def mergeBgr(img):
    b,g,r = cv2.split(img)
    img.merge((b,g,r))

'''
保存图片
@name : 自定义图片名字，如test.jpg
@img : openvc读取的图片对象
'''
def imgSave(name,img):
    cv2.imwrite(name,img)

'''
图像显示，可以创建多个窗口
@name : 自定义的窗口名字
@img : openvc读取的图片对象
'''
def cv_show(name,img):
    cv2.imshow(name,img)
    #图片展示的时间(ms)，0代表无限期
    cv2.waitKey(0)
    #销毁所有图片展示窗口
    cv2.destroyAllWindows()

'''
图像显示，可以创建多个窗口
p1 : 自定义的窗口名字
p2 : openvc读取的图片对象
'''
def imgCut(img):
    pic = img[0:50,0:200]
    cv_show('pic',pic)


if __name__ == "__main__":
    init()