from faker import Faker
from Crypto.Hash import *
import time
import random
import string


hash = SHA1.new()
fake = Faker('zh_TW')
time_arr = []
for i in range(100):
    str_test = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10 ** 6))

    x = time.time_ns()
    hash.update(str_test.encode("utf8"))
    y = time.time_ns()

    time_arr.append(y-x);
    print("{} \n> {}\n".format(hash.hexdigest(),y-x))

print((sum(time_arr)/len(time_arr))/(10 ** 9),end="")
print('秒')