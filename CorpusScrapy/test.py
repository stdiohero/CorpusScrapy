#!/user/bin/env python3
# -*- coding: utf-8 -*-
# Created by Wang Haoyu on 2017/11/13

import datetime

main_domain = 'http://www.chinanews.com/scroll-news/'
def url_generator(start_date=datetime.date(2017, 11, 1)):
    end_date = datetime.date.today()
    cur_date = start_date

    while cur_date <= end_date:
        temp = str(cur_date).split('-')
        url = '%s/%s/%s%s/news.shtml' % (main_domain,
                                         temp[0], temp[1], temp[2])
        yield url
        cur_date += datetime.timedelta(1)

#for url in url_generator():
#    print(url)


#a = [1, 2, 3, 4]
#b = [5, 6, 7, 8]
#for x, y in zip(a, b):
#    print('%d, %d' % (x, y))

def A(c):
    print(c)
    c += 2
def B(func):
    func()

#c = 1
#B(func= lambda: A(c))

#p = ['a', 'b', 'c']
#print(''.join(p))

import re
a = 'I\xa0\xa0T'
print(re.sub(r'\s', '', a))

