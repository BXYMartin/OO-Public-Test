from subprocess import Popen, PIPE
import multiprocessing
import os, sys, time, resource
import signal
import time
import re

def run(jar):
    filename = os.path.splitext(jar)[0]
    name="[{:>8s}] ".format(os.path.splitext(jar)[0])
    with open("./runtime/" + filename + ".res","wb") as out, open("./runtime/" + filename + ".err","wb") as err:
        path_runner = Popen(['java', '-jar', './test_jar/' + jar], stdin=PIPE, stdout=out, stderr=err, shell=False)
    start = time.time()
    check_content=""
    try:
        path_runner.stdin.write(write_content.encode())
        path_runner.stdin.flush()
        path_runner.stdin.close()
    except KeyboardInterrupt:
        print(name + "ERROR:\t Terminating...")
        os.kill(path_runner.pid, signal.SIGTERM)
    cut = resource.getrusage(resource.RUSAGE_CHILDREN)
    try:
        timeout = 10
        t_beginning = time.time()
        seconds_passed = 0
        while True:
            if path_runner.poll() is not None:
                break
            seconds_passed = time.time() - t_beginning
            if timeout and seconds_passed > timeout:
                path_runner.terminate()
                with open("./runtime/" + filename + ".err","w+") as err:
                    err.write(name + " Time Out: Elapsed For " + str(timeout) + " Seconds\n")
                print(name + "ERROR:\t Running Timeout!")
                raise TimeoutError("Elapsed For " + str(timeout) + " Seconds")
            time.sleep(0.5)
        ef = resource.getrusage(resource.RUSAGE_CHILDREN)
        elapsed = time.time() - start
    except ChildProcessError:
        print(name + "WARNING:\t Real Time Limit Exceeded!")
        with open("./runtime/" + filename + ".err","w+") as err:
            err.write(name + " Time Out: Elapsed For " + str(timeout) + " Seconds\n")
        os._exit(0)
    except KeyboardInterrupt:
        print(name + "ERROR:\t Terminating...")
        os.kill(path_runner.pid, signal.SIGTERM)
    if path_runner.poll() != 0:
        with open("./runtime/" + filename + ".err","w+") as err:
            err.write(name + " Exit Status: Return Code " + int(path_runner.poll()) + "\n")
        print(name + "ERROR:\t Error Status On Exit!")

    #print(name + "Baseline Refer:\t Base :{0:>7.3f}s | Upper:{1:>7.3f}MB".format(2.000, 768.000))
    #print(name + "SUML Processor:\t Real :{0:>7.3f}s | Total:{1:>7.3f}s | Memory:{2:>7.3f}MB".format(elapsed, ef.ru_utime - cut.ru_utime + ef.ru_stime - cut.ru_stime, ef.ru_maxrss / 1024 / 1024))
    print(name + "\t " + str((ef.ru_utime - cut.ru_utime + ef.ru_stime - cut.ru_stime)/2) + "s")
    if ef.ru_utime+ef.ru_stime-cut.ru_utime-cut.ru_stime > 5.000 or ef.ru_maxrss >= 768 * 1024 * 1024:
        with open("./runtime/" + filename + ".err","w+") as err:
            err.write(name + " Time Limit: CPU Time " + str(ef.ru_utime+ef.ru_stime-cut.ru_utime-cut.ru_stime) + "\n")

def batchRun(nprocess = 3):
    jars = os.listdir("./test_jar/")
    pool = multiprocessing.Pool(processes = nprocess)
    for each in jars:
        if each[0] != '.':
            pool.apply_async(run, (each, ))
    pool.close()
    pool.join()

write_content=""
while True:
    line = sys.stdin.readline()
    if line:
        write_content=write_content+line
    else:
        break

batchRun()
