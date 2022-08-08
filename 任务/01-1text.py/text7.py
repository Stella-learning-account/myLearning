import multiprocessing
import random


def add(a):
    url = [str(a) + 'undhiewci']
    dic = {str(a):random.randint(4,19)}
    return dic


if __name__ == '__main__':
    pool = multiprocessing.Pool(2)  # 两个进程执行
    multi_result = []
    # 开始运行
    li = [3,1,5,5,1,3,1]
    for i in li:
        multi_result.append(pool.apply_async(func=add, args=(i, )))
    pool.close()
    pool.join()
    listw = []
    dic = {}
    # 打印结果
    for _r in multi_result:
        # print(str(_r.get()))
        listw.append((_r.get()))
        dic |= _r.get()
    print(_r.get())
    print(listw)
    print(dic)
    d = {}
    for i in listw:
        print(i)
        for a,b in i.items():
            for j in  [3,1,5]:
                if a == f'{j}':
                    d.setdefault(j, []).append(f"{b}")
    print(d)
    










# s = '1,战狼2,175.4万,1.05亿,36.6,吴京,吴京,余男,弗兰克·格里罗,张翰,卢靖姗,2017-07-27,100分钟,中国大陆,剧情,动作,战争'
# print(s.split(',',2)[0]+s.split(',',2)[1],s.split(',',2)[2])

# lst = [[[1],[2]],[['a','b']]]
# for part in lst:
#         for row in part:
#             print(row[0])