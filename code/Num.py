import math
import random
from Utils import *
import Utils

class Num:
    def __init__(self, c=0, s=""):
        self.n = 0  # items seen
        self.at = c  # column  position
        self.name = s  # column name
        self._has = {}  # kept data
        self.lo = float('inf')  # lowest seen
        self.hi = -float('inf')  # highest seen
        self.isSorted = True  # no updates since last sort of data
    

    def nums(self):
        return self._has

    def add(self, v):
        if v != "?":
            self.n += 1
            self.lo = min(self.lo, v)
            self.hi = max(self.hi, v)
            if len(self._has) < Utils.the['nums']:
                pos = 1 + len(self._has)
            elif random.random() < Utils.the['nums'] / self.n:
                pos = random.randint(1, len(self._has))
            if pos:
                self.isSorted = False
                self._has[pos] = int(v)

    def div(self):
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1)) / 2.58

    def mid(self):
        print(self.nums())
        return per(self.nums(), 0.5)
