# python爬虫之爬取百度图片

import requests, time, random

k = 1;
for i in range(100):
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%A6%8F%E5%AD%97&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E7%A6%8F%E5%AD%97&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={}&rn=30&gsm=1e&1518059971575='.format(i * 30)
    html = requests.get(url)
    html.encoding = 'utf-8'
    for j in range(30):
        image_url = html.json()['data'][j]['middleURL']
        data = requests.get(image_url).content
        with open('./pic/%d.jpg' % k, 'wb') as f:
            f.write(data)
        print('已经下载了%d张图片' % k)
        k += 1
        time.sleep(random.random())