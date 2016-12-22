#Python has a number of different concurrency constructs such as threading, queues, and and multiprocessing
#  The threading module used to be the primary way of accomplishing concurrency however a few years ago
#  the multiprocessing module was added to the Python standard library

#using threads
import random
import time
import os
import urllib.request
from threading import Thread

class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        amount = random.randint(3, 15)
        time.sleep(amount)
        msg = '%s is running' % self.name
        print(msg)

class DownloadThread(Thread):
    """
    A Threading example that can download a file
    """
    def __init__(self, url, name):
        Thread.__init__(self)
        self.name = name
        self.url = url

    def run(self):
        """Run the thread"""
        handle = urllib.request.urlopen(self.url)
        fname = os.path.basename(self.url)
        with open(fname, 'wb') as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        msg = '%s has finished downloading %s' % (self.name, self.url)
        print(msg)

def main(urls):
    """
    Run the program
    :param urls:
    :return:
    """
    for item, url in enumerate(urls):
        name = 'Thread %s' % (item + 1)
        thread = DownloadThread(url, name)
        thread.start()

def create_threads():
    """
    create a group of threads
    :return:
    """
    for i in range(5):
        name = 'Thread #%s' % (i+1)
        my_thread = MyThread(name)
        my_thread.start()

if __name__ == '__main__':
    #create_threads()

    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]

    main(urls)

