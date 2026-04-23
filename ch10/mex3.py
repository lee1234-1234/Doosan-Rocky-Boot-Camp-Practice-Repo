from mex1 import plus
from mex1 import Cvalue
# from mex1 import p1

from mex1 import *

p3 = Cvalue()
p3.add(100)
p3.add(200)
p3.fprint()
# aaa = plus(1000, 2000)    # from을 썻기 때문에 mex1 모듈명 없이 plus만
# print(aaa)

plus(100, 200)
print("--------------")
print("--------------")
print(__name__)
print("mex3의 이름:", __name__)