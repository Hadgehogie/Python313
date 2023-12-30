import random

tlp_1 = ()
tlp_2 = ()


def func():
    tlp_1 = (random.randint(0, 5) for i in range(10))
    tlp_2 = (random.randint(-5, 0) for J in range(10))

    return func()


print(tlp_1)
print(tlp_2)

# tlp_sum = tlp_1 + tlp_2

