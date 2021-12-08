import requests
import time
import colorsys

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

url = 'http://192.168.1.197/led/'
l = [(None, None, None)] * 500

for j in range(3000):
    for i in range( 100):
        c = hsv2rgb(i/100,  1.0,  0.03 )
        for k in range(500):
            l[k] = c
        a = ''
        for rgb in l:
            a += str.format('{:02X}{:02X}{:02X}', rgb[0], rgb[1], rgb[2])
        x = requests.post(url, data=a)

