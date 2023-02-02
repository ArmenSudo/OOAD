import numpy as np


class BitSet:
    def __init__(self, size):
        self.__arr = np.zeros((size // 64 + 1), dtype=np.uint)

    def get_array(self):
        return self.__arr

    def set_bit(self, place: int) -> None:
        y = np.uint64(1 << place % 64)
        if self.__arr[len(self.__arr) - place // 64 - 1] & y > 0:
            print("Its already add")
            return
        self.__arr[len(self.__arr) - place // 64 - 1] |= y

    def reset_bit(self, place):
        y = np.uint64(1 << place % 64)
        if self.__arr[len(self.__arr) - place // 64 - 1] & y > 0:
            self.__arr[len(self.__arr) - place // 64 - 1] ^= y
            return
        print("Its not add")


bitset1 = BitSet(200)

bitset1.set_bit(0)
bitset1.set_bit(12)
bitset1.reset_bit(45)
bitset1.set_bit(190)

print(bitset1.get_array())
