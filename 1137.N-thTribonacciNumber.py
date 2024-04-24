def tribonacci(n: int) -> int:
        if n == 2 or n == 1: return 1
        elif n == 0: return 0

        numsList= [0, 1, 1]
        for _ in range(n - 2):
            numsList.append(numsList[-1] + numsList[-2] + numsList[-3])

        return numsList[-1]

print(tribonacci(38))

