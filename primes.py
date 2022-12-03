def primes(number_of_primes):

    list = []
    n = 2

    if (number_of_primes <= 0):
        raise ValueError(f"numberOfPrimes = {number_of_primes} should be positive.")

    else:
        while (len(list) < number_of_primes):
            for i in range(2, n):
                if n % i == 0:
                    n += 1
                    break
            else:
                list.append(n)
                n += 1
                
    print(list)
    return list
