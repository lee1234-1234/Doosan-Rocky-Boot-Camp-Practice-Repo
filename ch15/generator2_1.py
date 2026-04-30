# generator2_1.py
# 제너레이터 컴프리핸션 사용 예제

# 차이점:
# 1. 실행 "타이밍"이 다름
# 2. 중간에 정지 가능

import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

gen_job = (longtime_job() for i in range(5))
print(next(gen_job))


print('__iter__' in dir(gen_job))
print('__next__' in dir(gen_job))