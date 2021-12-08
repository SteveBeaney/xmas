import requests
import time

if __name__ == '__main__':


    url = 'http://192.168.1.197/led/'
    l = [(None, None, None)] * 500
    pitch = 12
    for k in range(400):
        for j in range(500):
            for i1 in range(pitch):
                for i in range(len(l)):
                    if (i + i1) % pitch == 0:
                        l[i] = (30, 30, 10)
                    else:
                        l[i] = (20, 20, 0)
                a = ''
                for rgb in l:
                    a += str.format('{:02X}{:02X}{:02X}', rgb[0], rgb[1], rgb[2])
                x = requests.post(url, data=a)

                time.sleep(0.2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
