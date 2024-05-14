class ProductOfNumbers:

    def __init__(self):
        self.stream = deque()
        self.K = 0

    def add(self, num: int) -> None:
        self.stream.append(num)        

    def getProduct(self, k: int) -> int:
        tmp_stream = deepcopy(self.stream)
        product = 1
        while k > 0:
            
            product = product * tmp_stream.pop()
            k -= 1
        return product

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
