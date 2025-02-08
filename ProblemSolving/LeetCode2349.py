import heapq


class NumberContainer:
    def __init__(self):
        self.indexToNum = {}
        self.numToIndices = {}

    def change(self, index: int, number: int) -> None:
        self.indexToNum[index] = number
        if number not in self.numToIndices:
            self.numToIndices[number] = []
        heapq.heappush(self.numToIndices[number], index)

    def find(self, number: int) -> int:
        if number not in self.numToIndices:
            return -1
        pq = self.numToIndices[number]
        while pq:
            currIndex = pq[0]
            if self.indexToNum[currIndex] != number:
                heapq.heappop(pq)
            else:
                return currIndex
        return -1

obj = NumberContainer()
obj.change(2, 10)
obj.change(1, 10)
obj.change(3, 10)
obj.change(5, 10)
pra = obj.find(10)
obj.change(1, 10)
pre2 = obj.find(10)