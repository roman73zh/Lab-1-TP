class Summator():
    def transform(self, n):
        return n

    def sum(self, n):
        result = 0
        for i in range(1, n + 1):
            result += self.transform(i)
        return result


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)


powersummator = PowerSummator(4)
summator = Summator()
squareSummator = SquareSummator()
cubeSummator = CubeSummator()
print(summator.sum(n=5))
print(squareSummator.sum(n=5))
print(cubeSummator.sum(n=5))
print(powersummator.sum(n=5))
