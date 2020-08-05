import exifread
import re

#查找图片GPS
def find_gps_image(pic_path):
    GPS = {}
    date = ''

    with open(pic_path,'rb') as f:
        tags = exifread.process_file(f)
        for tag,value in tags.items():
            if re.match('GPS GPSLatitudeRef',tag):
                #纬度
                GPS['GPSLatitudeRef'] = str(value)
            elif re.match('GPS GPSLongitudeRef',tag):
                #经度
                GPS['GPSLongitudeRef'] = str(value)
            elif re.match('GPS GPSAltitudeRef',tag):
                #海拔
                GPS['GPSAltitudeRef'] = str(value)
            elif re.match('GPS GPSAltitudeRef',tag):
                #海拔
                GPS['GPSLatitude'] = str(value)
            elif re.match('GPS GPSLatitude', tag):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]',str(value)).group()
                    GPS['GPSLatitude'] = int(match_result[0],match_result[1],match_result[2])
                except:
                    pass

        #输出获得结果的键值对，如设备型号
        for tag1,value1 in tags.items():
            if tag1 == "Image Model":
                print(value1)

if __name__ == '__main__':
    find_gps_image('gps_test1.jpg')