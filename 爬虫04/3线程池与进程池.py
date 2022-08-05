# 线程池：一次性开辟一些线程，我们用户直接给线程池提交任务，线程任务的调度交给线程池来完成
# 调动线程池：from concurrent.futures import ThreadPoolExecutor
# 调动进程池：from concurrent.futures import ProcessPoolExecutor

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def fn(name):
    for j in range(1000):
        print(name,j)


if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn,name=f'线程{i}')
    # 等待线程池中的任务全部执行完毕，才能继续执行(守护)
    print('123')


