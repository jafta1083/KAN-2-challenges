def is_prime(user):
    if user <= 1:
        return False
    for i in range(2, int(user ** 0.5) + 1):
        if user % i == 0:
            return False
    else:
        return True
    
def get_factors(user):
    factors = []
    for i in range(1, user + 1):
        if user % i == 0:
            factors.append(i)

    return factors
            
def sum_of_digits(user):
    total = 0
    for i in range(1, user + 1):
        total += i
    return total
    
def main():

    user = int(input("Enter a number: "))

    prime_number = is_prime(user)
    print(f'Is_prime: {prime_number}')

    num_factors = get_factors(user)
    print(f'Factors: {num_factors}')

    sum_digits = sum_of_digits(user)
    print(f'Sum: {sum_digits}')

main()