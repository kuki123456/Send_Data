from multiprocessing import Pool
from script.send_data import main

import os, time, random
def worker(hehe):
    print("创建%s,pid:%s"%(hehe,os.getpid()))
if __name__=="__main__":
    po = Pool()
    for i in range(0,1000):
        po.apply_async(main,("e1dee5ee-4ad2-4d0f-ac39-b4e2ee70277f",30035,))
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后



