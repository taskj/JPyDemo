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
                GPS['GPS GPSLatitudeRef'] = str(value)
            elif re.match('GPS GPSLongitudeRef',tag):
                #经度
                GPS['GPS GPSLongitudeRef'] = str(value)
            elif re.match('GPS GPSAltitudeRef',tag):
                #海拔
                GPS['GPS GPSAltitudeRef'] = str(value)
            elif re.match('GPS GPSAltitudeRef',tag):
                #海拔
                GPS['GPS GPSLatitude'] = str(value)

if __name__ == '__main__':
    find_gps_image('gps_test1.jpg')