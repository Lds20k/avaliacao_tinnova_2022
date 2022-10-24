from functools import reduce


multiples_of_3_or_5 = lambda number: number % 3 == 0 or number % 5 == 0
sum_all = lambda a, b: a + b

if __name__ == "__main__":
    flag = True
    max_range = 0
    while flag:
        x_input = input("Digite um valor inteiro para X: ")        
        if x_input.isnumeric():
            flag = False
            max_range = int(x_input)

    numbers = list(range(1, max_range))

    multiples = list(filter(multiples_of_3_or_5, numbers))
    print(multiples)

    if not multiples:
        print("Sem múltiplos de 3 ou 5")
        exit()

    multiples_sum = reduce(sum_all, multiples)
    print(multiples_sum)
