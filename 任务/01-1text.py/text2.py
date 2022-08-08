import time
import os
from multiprocessing import Process
 
 
def demo_one(num):
    print("start" + str(num))
    time.sleep(1)
    print(os.getpid(), os.getppid(), num)  # 子进程和父进程的pid
    print("end" + str(num))
 
 
if __name__ == '__main__':
    p_list = []
    for i in range(5):
        p = Process(target=demo_one, args=(i, ))  # 进程执行带参数的函数
        p.start()
        p_list.append(p)
    # for循环内添加join()  线程会按照顺序执行
    for p in p_list:
        p.join()
    print("mian")