# generator2.py

import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = [longtime_job() for i in range(5)]
print(list_job[0])
print(list_job)

print('__iter__' in dir(list_job))
print('__next__' in dir(list_job))