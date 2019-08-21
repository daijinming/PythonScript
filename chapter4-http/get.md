```
import requests
import time
import threading

'''
r0 = requests.get("http://localhost")
print(r0)
'''

def run(num):
    print(num + 1)
    r0 = requests.get("http://127.0.0.1")
    print(r0)

if __name__ == '__main__':
    print("主线程%s启动..."%(threading.current_thread().name))
    for i in range(50):
        # 创建子线程
        
        t = threading.Thread(target = run,args = (i,))
        t.start()
        t.join()
        
        #run(i)
    print("主线程%s结束..."%(threading.current_thread().name))


```
