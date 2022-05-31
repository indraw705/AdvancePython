import threading
import time

print("Testing Threading here")


def fun(number):
    for i in range(number):
        print(i)
        time.sleep(4)


def gun(number):
    for i in range(number):
        print(i)


if __name__ == '__main__':
    num = 5
    thread1 = threading.Thread(target=fun, args=(num,))
    thread2 = threading.Thread(target=gun, args=(num,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
