import cv2
import matplotlib.pyplot as plt

def init():
    '''
    ret, dst = cv2.threshold(src,thresh,maxval,type)
    src: 输入图，只能输入单通道图像，通常来说是灰度图
    dst: 输出图
    thresh: 阈值
    maxval: 当像素超过了阈值或者小于阈值，根据type来决定，所赋予的值
    type: 二值化操作的类型
    cv2.THRESH_BINARY 超过阈值部分去maxval(最大值),否则取0
    cv2.THRESH_BINARY_INV THRESH_BINARY的反转
    cv2.THRESH_TRUNC 大于阈值的部分设为阈值，否则不变
    cv2.THRESH_TOZERO 大于阈值部分不改变，否则设为0
    cv2.THRESH_TOZERO_INV cv2.THRESH_TOZERO的反转
    '''


    img = cv2.imread('cat.jpg')
    img_gray = cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)
    ret, thresh1 = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

    for i in range(6):
        plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


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

if __name__ == '__main__':
    init()