import requests
import time
import random

if __name__ == '__main__':

    vals = ( (  0,  0, 50,),
      (  0, 50, 0),
      (  0, 50, 50,),
      ( 50,  0, 0),
      ( 50,  0, 50,),
      ( 50, 50, 0),
      ( 50, 50, 50,),
      )
    url = 'http://192.168.1.197/led/'
    l = [(None, None, None)] * 500

    for j in range(5000):
        for k in range(500):
            i = vals[random.randint(0,6)]
            if k==0:
                l[k]=i
            else:
                while i == l[k-1]:
                    i = vals[random.randint(0, 6)]
                l[k] = i

        a = ''
        for rgb in l:
            a += str.format('{:02X}{:02X}{:02X}', rgb[0], rgb[1], rgb[2])
        x = requests.post(url, data=a)
        time.sleep(12)



