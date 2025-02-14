# design a class which can scale the product of the last k elements

class ProductOfNumbers:
    def __init__(self):
        self.numbers = []
        self.products = [1]

    def add(self, num: int) -> None:
        self.numbers.append(num)
        if num == 0:
            self.products = [1] # clear the prefix product
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.products):
            return 0
        return self.products[-1] // self.products[-k-1] if k > 0 else self.products[-1]