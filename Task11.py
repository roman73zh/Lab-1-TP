class Summator():
    def transform(self, n):
        return n

    def sum(self, n):
        result = 0
        for i in range(1, n + 1):
            result += self.transform(i)
        return result


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3


summator = Summator()
squareSummator = SquareSummator()
cubeSummator = CubeSummator()
print(summator.sum(n=5))
print(squareSummator.sum(n=5))
print(cubeSummator.sum(n=5))
