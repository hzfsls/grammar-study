# Start Euler001

def multiples_of_3_and_5(n: int) -> int:
    result = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

# End Euler001

# Start Euler002

def even_fibonacci_numbers(n: int) -> int:
    result = 0
    a = 1
    b = 2
    while a < n:
        if a % 2 == 0:
            result += a
        tmp = a
        a = b
        b = tmp + b
    return result

# End Euler002

# Start Euler003

def largest_prime_factor(n: int) -> int:
    result = n
    i = 2
    while i * i <= result:
        if result % i:
            i += 1
        else:
            result //= i
    return result

# End Euler003

# Start Euler004

def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def largest_palindrome_product(n: int) -> int:
    result = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            prod = i * j
            if is_palindrome(str(prod)) and prod > result and prod < n:
                result = prod
    return result

# End Euler004

# Start Euler005

def smallest_multiple(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        if result % i != 0:
            for j in range(1, n + 1):
                if (result * j) % i == 0:
                    result *= j
                    break
    return result

# End Euler005

# Start Euler006

def sum_square_difference(n: int) -> int:
    sqr_sum = 0
    num_sum = 0
    for i in range(1, n + 1):
        sqr_sum += i * i
        num_sum += i
    return num_sum * num_sum - sqr_sum

# End Euler006

# Start Euler007

def nth_prime(n: int) -> int:
    primes = [2]
    i = 3
    while len(primes) < n:
        for p in primes:
            if i % p == 0:
                break
            if p * p > i:
                primes.append(i)
                break
        i += 2
    return primes[-1]

# End Euler007

# Start Euler008

def largest_product_in_a_series(s: str, k: int) -> int:
    result = 0
    for i in range(len(s) - k):
        product = 1
        for j in range(k):
            product *= int(s[i + j])
        result = max(result, product)
    return result

# End Euler008

# Start Euler009

def special_pythagorean_triplet(n: int) -> int:
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if a * a + b * b == c * c:
                return a * b * c
    return -1

# End Euler009

# Start Euler010

def summation_of_primes(n: int) -> int:
    primes = [2]
    i = 3
    while i <= n:
        for p in primes:
            if i % p == 0:
                break
            if p * p > i:
                primes.append(i)
                break
        i += 2
    result = 0
    for prime in primes:
        result += prime
    return result

# End Euler010

# Start Euler011

def largest_product_in_a_grid(grid: list[list[int]]) -> int:
    result = 0
    for i in range(len(grid) - 3):
        for j in range(len(grid[i]) - 3):
            p1, p2, p3, p4 = 1, 1, 1, 1
            for k in range(4):
                p1 *= grid[i + k][j]
            for k in range(4):
                p2 *= grid[i][j + k]
            for k in range(4):
                p3 *= grid[i + k][j + k]
            for k in range(4):
                p4 *= grid[i + k][j + 3 - k]
            result = max(result, p1, p2, p3, p4)
    return result

# End Euler011

# Start Euler012

def highly_divisible_triangular_number(n: int) -> int:
    for i in range(1, 100000000):
        result = i * (i + 1) // 2
        count = 0
        for j in range(1, int(math.sqrt(result)) + 1):
            if result % j == 0:
                count += 2
            if j * j == result:
                count -= 1
        if count > n:
            return result
    return -1

# End Euler012

# Start Euler013

def large_sum(numbers: list[str]) -> str:
    digits = [0] * 60
    for i in range(50):
        tmp = 0
        for num in numbers:
            tmp += int(num[49 - i])
        for j in range(i, 60):
            digits[j] += tmp % 10
            if digits[j] >= 10:
                digits[j + 1] += digits[j] // 10
                digits[j] %= 10
            tmp //= 10
            if tmp == 0:
                break
    for i in range(59, -1, -1):
        if digits[i] != 0:
            result = ''
            for j in range(i, i - 10, -1):
                result += str(digits[j])
            return result

# End Euler013

# Start Euler014

def longest_collatz_sequence(n: int) -> int:
    longest = 0
    result = 0
    for i in range(1, n):
        chain = 1
        num = i
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            chain += 1
        if chain > longest:
            longest = chain
            result = i
    return result

# End Euler014

# Start Euler015

def lattice_paths(m: int, n: int) -> int:
    grid = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        grid[i][0] = 1
    for j in range(n + 1):
        grid[0][j] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[m][n]

# End Euler015

# Start Euler016

def power_digit_sum(n: int) -> int:
    digits = [2]
    for _ in range(1, n):
        carry = 0
        for j in range(len(digits)):
            temp = digits[j] * 2 + carry
            digits[j] = temp % 10
            carry = temp // 10
        if carry:
            digits.append(carry)
    result = 0
    for digit in digits:
        result += digit
    return result

# End Euler016

# Start Euler017

def number_to_words(n: int) -> str:
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n == 1000:
        return "one thousand"
    elif n >= 100:
        if n % 100 == 0:
            return ones[n // 100] + " hundred"
        else:
            return ones[n // 100] + " hundred and " + number_to_words(n % 100)
    elif n >= 20:
        suf = ""
        if n % 10 != 0:
            suf = " " + ones[n % 10]
        return tens[n // 10] + suf
    elif n >= 10:
        return teens[n - 10]
    else:
        return ones[n]

# End Euler017

# Start Euler018

def maximum_path_sum_i(triangle: list[list[int]]) -> int:
    curr = triangle[-1].copy()
    for i in range(len(triangle) - 2, -1, -1):
        next = triangle[i].copy()
        for j in range(len(next)):
            next[j] += max(curr[j], curr[j + 1])
        curr = next
    return curr[0]

# End Euler018

# Start Euler019

def counting_sundays(y1: int, y2: int) -> int:
    day = 0
    count = 0
    for year in range(1900, y2 + 1):
        for month in range(1, 13):
            if year >= y1 and day % 7 == 6:
                count += 1
            if month in [4, 6, 9, 11]:
                day += 30
            elif month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    day += 29
                else:
                    day += 28
            else:
                day += 31
    return count

# End Euler019

# Start Euler020

def factorial_digit_sum(n: int) -> int:
    digits = [1]
    for i in range(1, n+1):
        carry = 0
        for j in range(len(digits)):
            digits[j] = digits[j] * i + carry
            carry = digits[j] // 10
            digits[j] %= 10
        while carry:
            digits.append(carry % 10)
            carry //= 10
    result = 0
    for digit in digits:
        result += digit
    return result

# End Euler020

# Start Euler021

def d(n: int) -> int:
    result = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result += i
            if i != n // i:
                result += n // i
    return result

def amicable_numbers(n: int) -> int:
    result = 0
    for a in range(2, n):
        b = d(a)
        if a != b and a == d(b):
            result += a
    return result

# End Euler021

# Start Euler022

def names_scores(names: list[str], queries: list[str]) -> int:
    s_names = sorted(names)
    result = 0
    for i, name in enumerate(s_names):
        x = 0
        for c in name:
            x += ord(c) - 64
        if name in queries:
            result += x * (i + 1)
    return result

# End Euler022

# Start Euler023

def is_abundant(n: int) -> bool:
    if n < 12:
        return False
    sum_divisors = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors > n

def non_abundant_sums(n: int) -> int:
    abundants = []
    for i in range(12, n):
        if is_abundant(i):
            abundants.append(i)
    abundant_sums = set()
    for i in abundants:
        for j in abundants:
            abundant_sums.add(i + j)
    result = 0
    for i in range(n):
        if i not in abundant_sums:
            result += i
    return result

# End Euler023

# Start Euler024

def lexicographic_permutations(n: int) -> str:
    result = ''
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = n - 1
    for i in range(10, 0, -1):
        fact = 1
        for j in range(1, i):
            fact *= j
        idx = x // fact
        result += str(digits[idx])
        digits.pop(idx)
        x -= idx * fact
    return result

# End Euler024

# Start Euler025

def n_digit_fibonacci_number(n: int) -> int:
    a = [1]
    b = [1]
    i = 2
    while len(b) < n:
        carry = 0
        c = b.copy()
        for j in range(len(b)):
            if j < len(a):
                b[j] = a[j] + b[j] + carry
            else:
                b[j] = b[j] + carry
            carry = b[j] // 10
            b[j] = b[j] % 10
        if carry:
            b.append(carry)
        a = c
        i = i + 1
    return i

# End Euler025

# Start Euler026

def reciprocal_cycles(n: int) -> int:
    result = 0
    max_length = 0
    for i in range(1, n):
        remainders = []
        remainder = 1
        while remainder != 0 and remainder not in remainders:
            remainders.append(remainder)
            remainder = (remainder * 10) % i
        length = 0
        if remainder != 0:
            length = len(remainders) - remainders.index(remainder)
        if length > max_length:
            max_length = length
            result = i
    return result

# End Euler026

# Start Euler027

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def quadratic_primes(n: int) -> int:
    max_primes = 0
    result = 0
    for a in range(-n + 1, n, 2):
        for b in range(-n + 1, n, 2):
            x = 0
            while True:
                if x * x + a * x + b < 2:
                    break
                if not is_prime(x * x + a * x + b):
                    break
                x += 1
            if x > max_primes:
                max_primes = x
                result = a * b
    return result

# End Euler027

# Start Euler028

def number_spiral_diagonals(n: int) -> int:
    result = 1
    for i in range(3, n + 1, 2):
        result += 4 * i * i - 6 * i + 6
    return result

# End Euler028

# Start Euler029

def distinct_powers(n: int) -> int:
    result = 0
    xs = set()
    for i in range(2, n + 1):
        primes = [2, 3, 5, 7]
        powers = [0, 0, 0, 0]
        num = i
        for j in range(len(primes)):
            while num % primes[j] == 0:
                num //= primes[j]
                powers[j] += 1
        if num != 1:
            result += n - 1
            continue
        for j in range(2, n + 1):
            pstr = f"{powers[0] * j}-{powers[1] * j}-{powers[2] * j}-{powers[3] * j}"
            xs.add(pstr)
    result += len(xs)
    return result

# End Euler029

# Start Euler030

def digit_nth_powers(n: int) -> int:
    result = 0
    for i in range(2, 4 * 10 ** n):
        digits_sum = 0
        for digit in str(i):
            digits_sum += int(digit) ** n
        if i == digits_sum:
            result += i
    return result

# End Euler030

# Start Euler031

def coin_sums(n: int) -> int:
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (n + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            ways[i] += ways[i - coin]
    return ways[n]

# End Euler031

# Start Euler032

def pandigital_products(n: int) -> int:
    products = set()
    s = ''.join(str(i) for i in range(1, n+1))
    for a in range(1, 100):
        for b in range(1, 10000):
            c = a * b
            chars = list(str(a) + str(b) + str(c))
            chars.sort()
            if ''.join(chars) == s:
                products.add(c)
    result = 0
    for product in products:
        result += product
    return result

# End Euler032

# Start Euler033

def digit_canceling_fractions(m: int) -> int:
    numer = 1
    denom = 1
    for d in range(10, m):
        for n in range(10, d):
            n0, n1 = n % 10, n // 10
            d0, d1 = d % 10, d // 10
            if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
                numer *= n
                denom *= d
    a, b = numer, denom
    while b:
        a, b = b, a % b
    return denom // a

# End Euler033

# Start Euler034

def digit_factorials(n: int) -> int:
    result = 0
    for i in range(3, n):
        fact_sum = 0
        for digit in str(i):
            fact = 1
            for j in range(1, int(digit) + 1):
                fact *= j
            fact_sum += fact
        if i == fact_sum:
            result += i
    return result

# End Euler034

# Start Euler035

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def circular_primes(n: int) -> int:
    count = 0
    for i in range(2, n):
        if is_prime(i):
            rotations = set()
            si = str(i)
            for j in range(len(si)):
                rotations.add(int(si[j:] + si[:j]))
            flag = True
            for x in rotations:
                if not is_prime(x):
                    flag = False
                    break
            if flag:
                count += 1
    return count

# End Euler035

# Start Euler036

def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

def double_base_palindromes(n: int) -> int:
    result = 0
    for i in range(1, n):
        str_i = str(i)
        bin_i = str(bin(i)[2:])
        if is_palindrome(str_i) and is_palindrome(bin_i):
            result += i
    return result

# End Euler036

# Start Euler037

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def truncatable_primes(n: int) -> int:
    result = 0
    for i in range(10, n):
        if is_prime(i):
            si = str(i)
            flag = True
            for j in range(1, len(si)):
                p1 = int(si[j:])
                p2 = int(si[:-j])
                if not is_prime(p1) or not is_prime(p2):
                    flag = False
                    break
            if flag:
                result += i
    return result

# End Euler037

# Start Euler038

def pandigital_multiples(n: int) -> int:
    result = -1
    for i in range(2, n + 1):
        cprod = ''
        for j in range(1, 10):
            cprod += str(i * j)
            if len(cprod) == 9:
                if ''.join(sorted(cprod)) == '123456789':
                    result = max(result, int(cprod))
                    break
            elif len(cprod) > 9:
                break
    return result

# End Euler038

# Start Euler039

def integer_right_triangles(n: int) -> int:
    max_sol = 0
    result = 0
    for p in range(3, n + 1):
        sol = 0
        for a in range(1, p // 2):
            for b in range(a, p // 2):
                c = p - a - b
                if a * a + b * b == c * c:
                    sol += 1
        if sol > max_sol:
            max_sol = sol
            result = p
    return result

# End Euler039

# Start Euler040

def champernowne_constant(b: int) -> int:
    s = ''
    for i in range(1, b**6):
        s += str(i)
    result = 1
    for i in range(7):
        result *= int(s[b**i - 1])
    return result

# End Euler040

# Start Euler041

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def pandigital_prime(n: int) -> int:
    for i in range(n-1, 0, -1):
        if is_prime(i):
            si = str(i)
            length = len(si)
            flag = True
            for j in range(1, length + 1):
                if str(j) not in si:
                    flag = False
                    break
            if flag:
                return i
    return -1

# End Euler041

# Start Euler042

def coded_triangle_numbers(words: list[str]) -> int:
    result = 0
    for word in words:
        value = 0
        for c in word:
            value += ord(c) - 64
        n = int(math.sqrt(value * 2))
        if n * (n + 1) == value * 2:
            result += 1
    return result

# End Euler042

# Start Euler043

def gen_permutations(s: str) -> list[str]:
    if len(s) <= 1:
        return s
    result = []
    for perm in gen_permutations(s[1:]):
        for i in range(len(s)):
            result.append(perm[:i] + s[0:1] + perm[i:])
    return result


def sub_string_divisibility(n: int) -> int:
    result = 0
    primes = [2, 3, 5, 7, 11, 13, 17]
    s = ''.join(str(i) for i in range(n + 1))
    for i in gen_permutations(s):
        flag = True
        for j in range(1, n - 1):
            if int(i[j:j + 3]) % primes[j - 1] != 0:
                flag = False
                break
        if flag:
            result += int(i)
    return result

# End Euler043

# Start Euler044

def pentagon_numbers(n: int) -> int:
    pentagon = set()
    for i in range(1, n):
        pentagon.add(i * (3 * i - 1) // 2)
    result = -1
    for j in pentagon:
        for k in pentagon:
            if j + k in pentagon and k - j in pentagon:
                if result == -1 or k - j < result:
                    result = k - j
    return result

# End Euler044

# Start Euler045

def triangular_pentagonal_and_hexagonal(n: int) -> int:
    ps = set()
    i = 1
    c = 0.5 * i * (3 * i - 1)
    while c < n:
        i += 1
        ps.add(c)
        c = 0.5 * i * (3 * i - 1)     
    i = 1
    c = i * (2 * i - 1)
    result = -1
    while c < n:
        i += 1
        if c in ps:
            result = c
        c = i * (2 * i - 1)
    return result

# End Euler045

# Start Euler046

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def goldbachs_other_conjecture(n: int) -> int:
    result = -1
    for i in range(9999, n, -2):
        upper = int(math.sqrt(i // 2))
        flag = False
        for j in range(0, upper + 1):
            if is_prime(i - 2 * j * j):
                flag = True
                break
        if not flag:
            result = i
    return result

# End Euler046

# Start Euler047

def prime_factors(n: int) -> int:
    num = n
    factors = []
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return len(set(factors))

def distinct_primes_factors(n: int) -> int:
    for i in range(n, 1000000):
        if prime_factors(i) == 4 and prime_factors(i + 1) == 4 and prime_factors(i + 2) == 4 and prime_factors(i + 3) == 4:
            return i
    return -1

# End Euler047

# Start Euler048

def self_powers(n: int) -> str:
    digits = [0] * 10
    for i in range(1, n + 1):
        temp_digits = [0] * 10
        temp_digits[0] = 1
        for j in range(i):
            carry = 0
            for k in range(10):
                temp_digits[k] = temp_digits[k] * i + carry
                carry = temp_digits[k] // 10
                temp_digits[k] %= 10
        for j in range(10):
            digits[j] += temp_digits[j]
            if digits[j] >= 10:
                digits[j] -= 10
                if j < 9:
                    digits[j + 1] += 1
    result = ""
    for i in range(9, -1, -1):
        result += str(digits[i])
    return result

# End Euler048

# Start Euler049

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def gen_permutations(s: str) -> list[str]:
    if len(s) <= 1:
        return s
    result = []
    for perm in gen_permutations(s[1:]):
        for i in range(len(s)):
            result.append(perm[:i] + s[0:1] + perm[i:])
    return result

def prime_permutations(n: int) -> str:
    for i in range(n, 999, -1):
        if is_prime(i):
            permutations = gen_permutations(str(i))
            candidates = set()
            for j in permutations:
                candidate = int(j)
                if candidate > i and is_prime(candidate):
                    candidates.add(candidate)
            for m in candidates:
                if m + (m - i) in candidates:
                    return str(i) + str(m) + str(m + (m - i))
    return ''

# End Euler049

# Start Euler050

def consecutive_prime_sum(limit: int) -> int:
    sieve = [True] * limit
    primes = []
    for i in range(2, limit):
        if sieve[i]:
            primes.append(i)
            for j in range(i * 2, limit, i):
                sieve[j] = False
    max_length = 0
    max_prime = 0
    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            s = sum(primes[i:j])
            if s >= limit:
                break
            if sieve[s] and j - i > max_length:
                max_length = j - i
                max_prime = s
    return max_prime

# End Euler050

