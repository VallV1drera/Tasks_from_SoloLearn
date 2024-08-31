class Calculator:
    def _init_(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    @staticmethod
    def add(n1, n2):
        return n1 + n2
       
n1 = int(input())
n2 = int(input())

print(Calculator.add(n1, n2))
