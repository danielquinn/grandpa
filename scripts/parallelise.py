#!/usr/bin/env python3

import json
import subprocess
from multiprocessing.dummy import Pool as ThreadPool


class Paralleliser(object):

    def __init__(self):

        self.threads = int(subprocess.check_output(["nproc"]).strip())

        with open("queue.json") as f:
            self.queue = json.load(f)

    @staticmethod
    def run(command):
        print("Executing {}".format(command))
        subprocess.call(command, shell=True)

    def start(self):
        """
        Python parallelisation is amazeballs:
        http://stackoverflow.com/a/28463266/231670
        """

        # Make the Pool of workers
        pool = ThreadPool(self.threads)

        # Open the urls in their own threads
        pool.map(self.run, self.queue)

        # Close the pool and wait for the work to finish
        pool.close()
        pool.join()

if __name__ == "__main__":
    Paralleliser().start()
