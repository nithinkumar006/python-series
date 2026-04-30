import time
import sys
h=3
m=59
s=0
while True:
    sys.stdout.write("\r{0:2d} : {1:2d} : {2:2d}".format(h,m,s))
    sys.stdout.flush()
    time.sleep(1)
    s=s+1
    if s==60:
        s=0
        m=m+1
    if m==60:
        m=0
        h=h+1
    if h==13:
        h=1
