from faker import Faker
from Crypto.Hash import *
import time
import random
import string
import matplotlib.pyplot as plt
import numpy as np

# Add a basic title
plt.title("A 2D histogram")

hash = SHA384.new()
fake = Faker('zh_TW')
time_arr = []
for i in range(50):
    str_test = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(int(10 ** 5.5)))

    x = time.time_ns()
    hash.update(str_test.encode("utf8"))
    y = time.time_ns()

    time_arr.append(y - x)
    print("{} \n> {}\n".format(hash.hexdigest(), y - x))

time_arr = list(filter((0).__ne__, time_arr))
print((sum(time_arr) / len(time_arr)) / (10 ** 9), end="")
print('秒')

plt.plot(time_arr)
plt.show()
