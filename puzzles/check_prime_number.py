from math import sqrt
class PrimeUtil:

    def isPrime(self, A):
        if A == 1:
            return 0
        upper_limit = int(sqrt(A))
        for i in range(2, upper_limit + 1):
            if A % i == 0:
                return 0
        return 1