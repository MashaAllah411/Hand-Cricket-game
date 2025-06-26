import threading
import time


def red():
    time.sleep(1)
    print("Red Light:Stop")

def yellow():
    time.sleep(3)
    print("Yellow Light: Ready to go")
    
def green():
    time.sleep(5)
    print("green light: Go")
    
    
res=threading.Thread(target=red)
res2=threading.Thread(target=yellow)
res3=threading.Thread(target=green)

res.start()
res2.start()
res3.start()

res.join()
res2.join()
res3.join()
time.sleep(1)
print("obey Traffic rules")

#Multithreading is not a vice choice for traffic rules just for an example