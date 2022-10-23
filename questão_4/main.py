from functools import reduce


multiples_of_3_or_5 = lambda number: number % 3 == 0 or number % 5 == 0
sum_all = lambda a, b: a + b

if __name__ == "__main__":
    numbers = list(range(0, 11))

    multiples = list(filter(multiples_of_3_or_5, numbers))
    print(multiples)

    multiples_sum = reduce(sum_all, multiples)
    print(multiples_sum)
