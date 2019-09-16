# import modules
import threading
import time

# target function
def action(thread_name, delay):
    for i in range(5):
        time.sleep(delay)
        print(thread_name, time.time())


if __name__ == '__main__':

    # instantiating threads objects
    t1  = threading.Thread(target=action, args=('Thread 1', 1))
    t2  = threading.Thread(target=action, args=('Thread 2', 2))

    # start first thread
    t1.start()

    # start second thread
    t2.start()

    # wait until first thread is finished
    t1.join()

    # wait until second thread is finished
    t2.join()

    print('Finish')
