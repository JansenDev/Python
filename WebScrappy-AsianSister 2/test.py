# from multiprocessing import Lock, Process, Queue, current_process
# import time
# import queue # imported for using queue.Empty exception
from queue import Queue
from threading import Thread
import time
import os

print(os.cpu_count())


# def do_stuff(q):
#   while True:
#     print (q.get())
#     time.sleep(0.5)
#     q.task_done()

# q = Queue(maxsize=0)
# num_threads = 5

# for i in range(num_threads):
#   worker = Thread(target=do_stuff, args=(q,))
#   worker.setDaemon(True)
#   worker.start()

# for x in range(101):
#   q.put(x)

# q.join()

# def do_job(tasks_to_accomplish, tasks_that_are_done):
#     while True:
#         try:
#             '''
#                 try to get task from the queue. get_nowait() function will 
#                 raise queue.Empty exception if the queue is empty. 
#                 queue(False) function would do the same task also.
#             '''
#             task = tasks_to_accomplish.get_nowait()
#         except queue.Empty:

#             break
#         else:
#             '''
#                 if no exception has been raised, add the task completion 
#                 message to task_that_are_done queue
#             '''
#             print(task)
#             tasks_that_are_done.put(task + ' is done by ' + current_process().name)
#             time.sleep(.5)
#     return True


# def main():
#     number_of_task = 10
#     number_of_processes = 4
#     tasks_to_accomplish = Queue()
#     tasks_that_are_done = Queue()
#     processes = []

#     for i in range(number_of_task):
#         tasks_to_accomplish.put("Task no " + str(i))

#     # creating processes
#     for w in range(number_of_processes):
#         p = Process(target=do_job, args=(tasks_to_accomplish, tasks_that_are_done))
#         processes.append(p)
#         p.start()

#     # completing process
#     for p in processes:
#         p.join()

#     # print the output
#     while not tasks_that_are_done.empty():
#         print(tasks_that_are_done.get())

#     return True


# if __name__ == '__main__':
#     main()


# def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
#     """
#     Call in a loop to create terminal progress bar
#     @params:
#         iteration   - Required  : current iteration (Int)
#         total       - Required  : total iterations (Int)
#         prefix      - Optional  : prefix string (Str)
#         suffix      - Optional  : suffix string (Str)
#         decimals    - Optional  : positive number of decimals in percent complete (Int)
#         length      - Optional  : character length of bar (Int)
#         fill        - Optional  : bar fill character (Str)
#         printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
#     """
#     percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
#     filledLength = int(length * iteration // total)
#     bar = fill * filledLength + '-' * (length - filledLength)
#     print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
#     # Print New Line on Complete
#     if iteration == total: 
#         print()


# # A List of Items
# items = list(range(0, 57))
# l = len(items)

# # Initial call to print 0% progress
# printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
# for i, item in enumerate(items):
#     # Do stuff...
#     time.sleep(0.1)
#     # Update Progress Bar
#     printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)


# lista = [1,23,4,5,]

# for index, item in enumerate(lista):
#     print(item)

##TESTS
# for i in range(5) :

#     texto = "pene: {}".format(i)
#     print(f'\b{texto}',end='\r' )
#     time.sleep(1)

##END TEST

# def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
#     """
#     Call in a loop to create terminal progress bar
#     @params:
#         iteration   - Required  : current iteration (Int)
#         total       - Required  : total iterations (Int)
#         prefix      - Optional  : prefix string (Str)
#         suffix      - Optional  : suffix string (Str)
#         decimals    - Optional  : positive number of decimals in percent complete (Int)
#         length      - Optional  : character length of bar (Int)
#         fill        - Optional  : bar fill character (Str)
#         printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
#     """
#     total = len(iterable)
#     # Progress Bar Printing Function
#     def printProgressBar (iteration):
#         percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
#         filledLength = int(length * iteration // total)
#         bar = fill * filledLength + '-' * (length - filledLength)
#         print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
#     # Initial Call
#     printProgressBar(0)
#     # Update Progress Bar
#     for i, item in enumerate(iterable):
#         yield item
#         printProgressBar(i + 1)
#     # Print New Line on Complete
#     print()

# for i in progressBar(range(200),'progress:'):
#     time.sleep(0.1)

# for index, i in enumerate(progressBar(range(10),prefix='Progress',suffix='Complete')):
#     time.sleep(0.3)

#     print(i,"\n")
