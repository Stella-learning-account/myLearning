import multiprocessing as mp
def jod(q):
    res = 0
    for i in range(10000):
        res = i + i**2 + i**3
    q.put(res)
if __name__=='__main__':
    q=mp.Queue()
    p1=mp.Process(target=jod,args=(q,))
    p2=mp.Process(target=jod,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res=q.get()
    print(res)