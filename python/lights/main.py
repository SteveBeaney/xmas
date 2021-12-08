import requests
import time

if __name__ == '__main__':


    url = 'http://192.168.1.197/led/'
    l = [(None, None, None)] * 500
    for i in range(2):
        for j in range(1,499):
            l[j] = (0, 0, 0)
        l[0]=(255,255,255)
        l[499]=(255,255,255)
        l[490]=(255,255,255)
        l[480]=(255,255,255)
        a = ''
        for rgb in l:
            a += str.format('{:02X}{:02X}{:02X}', rgb[0], rgb[1], rgb[2])
        x = requests.post(url, data=a)
