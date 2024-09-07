def compute():
    def find_cycle(string):
        seq = []
        for i in string:
            if seq.pop(0) != i:
                seq.append(i)
            else:
                return
        return False

    for j in range(1, 20):
        num = str(1.0 / j).split(".")[1]
        print(num)
    return None


def compute1():
    max_cycle = 0
    max_d = 0

    for d in range(2, 1000):
        # Generate a long string of decimal digits
        remainders = {}
        value = 1
        position = 0
        decimal_digits = []

        while value != 0 and value not in remainders:
            remainders[value] = position
            value *= 10
            decimal_digits.append(str(value // d))
            value %= d
            position += 1
        if value != 0:  # We found a cycle
            cycle_start = remainders[value]
            cycle_length = position - cycle_start
            if cycle_length > max_cycle:
                max_cycle = cycle_length
                max_d = d
        return max_d


print(compute1())
