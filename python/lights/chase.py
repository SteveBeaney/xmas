import requests
import time

if __name__ == '__main__':

    print(time.time())
    url = 'http://192.168.1.197/led/'
    l = [(None, None, None)] * 500
    pitch = 12

    for j in range(490):
        for i in range(500):
            l[i] = (20, 20, 20)
        for k in range(10):
            l[j+k] = (40, 0, 0)
        a = ''
        for rgb in l:
            a += str.format('{:02X}{:02X}{:02X}', rgb[0], rgb[1], rgb[2])
        x = requests.post(url, data=a)
        # time.sleep(0.01)
    print(time.time())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
