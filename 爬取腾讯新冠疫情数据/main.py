import requests
import json
'''
爬取页面地址
https://news.qq.com/zt2020/page/feiyan.htm#/
页面数据接口地址
https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5
'''

#http请求头
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
res = requests.get(url,headers)
d = json.loads(res.text)
data_all = json.loads(d["data"])

'''
print(data_all.keys())
dict_keys(['lastUpdateTime', 'chinaTotal', 'chinaAdd', 'isShowAdd', 'showAddSwitch', 'areaTree'])
print(data_all["lastUpdateTime"]) #上次数据更新时间
print(data_all['chinaTotal']) #当前汇总数据
print(data_all['chinaAdd']) #中国新增数据
print(data_all['areaTree']) #数据树结构
areaTree : -name 中国数据
           -today
           -total
           -chirldren:-name #省级列表数据
                      -today
                      -total
        
                      -children:-name #市级列表数据             
'''
details = [] #当日的详细数据
update_time = data_all['lastUpdateTime']
data_country = data_all['areaTree']
data_province = data_country[0]['children']

for pro_infos in data_province:
    province = pro_infos['name']
    for city_infos in pro_infos['children']:
        city = city_infos['name']
        confirm = city_infos['total']['confirm']
        confirm_add = city_infos['today']['confirm']
        heal = city_infos['total']['heal']
        dead = city_infos['total']['dead']
        details.append([update_time,province,city,confirm,confirm_add,heal,dead])

print(details)








