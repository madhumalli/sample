import multiprocessing
import cli as cl

if __name__ == '__main__':
    for i in range(2):
        p = multiprocessing.Process(target = cl.callapi('output_4sh_2B_1.json'))

        p.start()

        p.join()