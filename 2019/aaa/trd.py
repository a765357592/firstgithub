import multiprocessing as mp
import time

def job(x):
    print(x * x)

if __name__ =='__name__':
    
    t1 = time.time()
    pool = mp.Pool()
    res = pool.map(job,range(1000))
    print(res)
    t2 = time.time()
    print(t2-t1)

    res = pool.apply_async(job,(2))
    print(res.get())
    
    #p1 = mp.Process(target=job,args=(1,2))
    #p1.start()
    #p1.join()