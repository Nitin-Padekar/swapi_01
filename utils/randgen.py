import random


def random_list(start=1, stop=82):
    return (random.randint(start, stop) for i in range(1,16))


if __name__=="__main__":
    print(__name__)
    print("from randgen.py")
