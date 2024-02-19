# Start Euler001

def multiples_of_3_and_5(n)
    result = 0
    (0...n).each do |i|
        if i % 3 == 0 || i % 5 == 0
            result += i
        end
    end
    result
end

# End Euler001

# Start Euler002

def even_fibonacci_numbers(n)
    result = 0
    a = 1
    b = 2
    while a < n
        if a % 2 == 0
            result += a
        end
        tmp = a
        a = b
        b = tmp + b
    end
    result
end

# End Euler002

# Start Euler003

def largest_prime_factor(n)
    result = n
    i = 2
    while i * i <= result
        if result % i != 0
            i += 1
        else
            result /= i
        end
    end
    result
end

# End Euler003

# Start Euler004

def is_palindrome(s)
    (0...s.length / 2).each do |i|
        if s[i] != s[s.length - i - 1]
            return false
        end
    end
    true
end

def largest_palindrome_product(n)
    result = 0
    (100...1000).each do |i|
        (i...1000).each do |j|
            prod = i * j
            if is_palindrome(prod.to_s) && prod > result && prod < n
                result = prod
            end
        end
    end
    result
end

# End Euler004

# Start Euler005

def smallest_multiple(n)
    result = 1
    (1..n).each do |i|
        if result % i != 0
            (1..n).each do |j|
                if (result * j) % i == 0
                    result *= j
                    break
                end
            end
        end
    end
    result
end

# End Euler005

# Start Euler006

def sum_square_difference(n)
    sqr_sum = 0
    num_sum = 0
    (1..n).each do |i|
        sqr_sum += i * i
        num_sum += i
    end
    num_sum * num_sum - sqr_sum
end

# End Euler006

# Start Euler007

def nth_prime(n)
    primes = [2]
    i = 3
    while primes.length < n
        primes.each do |p|
            if i % p == 0
                break
            end
            if p * p > i
                primes.push(i)
                break
            end
        end
        i += 2
    end
    primes.last
end

# End Euler007

# Start Euler008

def largest_product_in_a_series(s, k)
    result = 0
    (0..s.length - k).each do |i|
        product = 1
        (0...k).each do |j|
            product *= s[i + j].to_i
        end
        result = [result, product].max
    end
    result
end

# End Euler008

# Start Euler009

def special_pythagorean_triplet(n)
    (1...n).each do |a|
        (a...n).each do |b|
            c = n - a - b
            return a * b * c if a * a + b * b == c * c
        end
    end
end

# End Euler009

# Start Euler010

def summation_of_primes(n)
    primes = [2]
    i = 3
    while i <= n
        primes.each do |p|
            if i % p == 0
                break
            end
            if p * p > i
                primes.push(i)
                break
            end
        end
        i += 2
    end
    result = 0
    primes.each do |prime|
        result += prime
    end
    result
end

# End Euler010

# Start Euler011

def largest_product_in_a_grid(grid)
    result = 0
    (0...grid.length - 3).each do |i|
        (0...grid[i].length - 3).each do |j|
            p1, p2, p3, p4 = 1, 1, 1, 1
            (0...4).each do |k|
                p1 *= grid[i + k][j]
            end
            (0...4).each do |k|
                p2 *= grid[i][j + k]
            end
            (0...4).each do |k|
                p3 *= grid[i + k][j + k]
            end
            (0...4).each do |k|
                p4 *= grid[i + k][j + 3 - k]
            end
            result = [result, p1, p2, p3, p4].max
        end
    end
    result
end

# End Euler011

# Start Euler012

def highly_divisible_triangular_number(n)
    (1...100000000).each do |i|
        result = i * (i + 1) / 2
        count = 0
        (1..Math.sqrt(result).to_i).each do |j|
            if result % j == 0
                count += 2
            end
            if j * j == result
                count -= 1
            end
        end
        if count > n
            return result
        end
    end
    -1
end

# End Euler012

# Start Euler013

def large_sum(numbers)
    digits = Array.new(60, 0)
    (0...50).each do |i|
        tmp = 0
        numbers.each do |num|
            tmp += num[49 - i].to_i
        end
        (i...60).each do |j|
            digits[j] += tmp % 10
            if digits[j] >= 10
                digits[j + 1] += digits[j] / 10
                digits[j] %= 10
            end
            tmp /= 10
            break if tmp == 0
        end
    end
    59.downto(0) do |i|
        next if digits[i] == 0
        result = ''
        i.downto(i - 9).each do |j|
            result += digits[j].to_s
        end
        return result
    end
end

# End Euler013

# Start Euler014

def longest_collatz_sequence(n)
    longest = 0
    result = 0
    (1...n).each do |i|
        chain = 1
        num = i
        while num != 1
            if num % 2 == 0
                num = num / 2
            else
                num = 3 * num + 1
            end
            chain += 1
        end
        if chain > longest
            longest = chain
            result = i
        end
    end
    result
end

# End Euler014

# Start Euler015

def lattice_paths(m, n)
    grid = Array.new(m + 1) { Array.new(n + 1, 0) }
    (0..m).each do |i|
        grid[i][0] = 1
    end
    (0..n).each do |j|
        grid[0][j] = 1
    end
    (1..m).each do |i|
        (1..n).each do |j|
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        end
    end
    grid[m][n]
end

# End Euler015

# Start Euler016

def power_digit_sum(n)
    digits = [2]
    (1...n).each do
        carry = 0
        digits.each_with_index do |_, j|
            temp = digits[j] * 2 + carry
            digits[j] = temp % 10
            carry = temp / 10
        end
        digits.push(carry) if carry != 0
    end
    result = 0
    digits.each { |digit| result += digit }
    result
end

# End Euler016

# Start Euler017

def number_to_words(n)
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n == 1000
        "one thousand"
    elsif n >= 100
        if n % 100 == 0
            ones[n / 100] + " hundred"
        else
            ones[n / 100] + " hundred and " + number_to_words(n % 100)
        end
    elsif n >= 20
        suf = ""
        if n % 10 != 0
            suf = " " + ones[n % 10]
        end
        tens[n / 10] + suf
    elsif n >= 10
        teens[n - 10]
    else
        ones[n]
    end
end

# End Euler017

# Start Euler018

def maximum_path_sum_i(triangle)
    curr = triangle.last.dup
    (triangle.size - 2).downto(0) do |i|
        next_ = triangle[i].dup
        next_.each_with_index do |_, j|
            next_[j] += [curr[j], curr[j + 1]].max
        end
        curr = next_
    end
    curr[0]
end

# End Euler018

# Start Euler019

def counting_sundays(y1, y2)
    day = 0
    count = 0
    (1900..y2).each do |year|
        (1..12).each do |month|
            if year >= y1 && day % 7 == 6
                count += 1
            end
            if [4, 6, 9, 11].include?(month)
                day += 30
            elsif month == 2
                if year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
                    day += 29
                else
                    day += 28
                end
            else
                day += 31
            end
        end
    end
    count
end

# End Euler019

# Start Euler020

def factorial_digit_sum(n)
    digits = [1]
    (1..n).each do |i|
        carry = 0
        (0...digits.length).each do |j|
            digits[j] = digits[j] * i + carry
            carry = digits[j] / 10
            digits[j] %= 10
        end
        while carry != 0
            digits.push(carry % 10)
            carry /= 10
        end
    end
    result = 0
    digits.each do |digit|
        result += digit
    end
    result
end

# End Euler020

# Start Euler021

def d(n)
    result = 1
    (2..Math.sqrt(n)).each do |i|
        if n % i == 0
            result += i
            result += n / i if i != n / i
        end
    end
    result
end

def amicable_numbers(n)
    result = 0
    (2...n).each do |a|
        b = d(a)
        result += a if a != b && a == d(b)
    end
    result
end

# End Euler021

# Start Euler022

def names_scores(names, queries)
    s_names = names.sort
    result = 0
    s_names.each_with_index do |name, i|
        x = 0
        name.each_char do |c|
            x += c.ord - 64
        end
        if queries.include?(name)
            result += x * (i + 1)
        end
    end
    result
end

# End Euler022

# Start Euler023

def is_abundant(n)
    if n < 12
        false
    end
    sum_divisors = 1
    (2..Math.sqrt(n)).each do |i|
        if n % i == 0
            sum_divisors += i
            sum_divisors += n / i if i != n / i
        end
    end
    sum_divisors > n
end

def non_abundant_sums(n)
    abundants = []
    (12...n).each do |i|
        abundants.push(i) if is_abundant(i)
    end
    abundant_sums = []
    abundants.each do |i|
        abundants.each do |j|
            abundant_sums.push(i + j)
        end
    end
    result = 0
    (0...n).each do |i|
        result += i if !abundant_sums.include?(i)
    end
    result
end

# End Euler023

# Start Euler024

def lexicographic_permutations(n)
    result = ""
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = n - 1
    10.downto(1) do |i|
        fact = 1
        (1...i).each do |j|
            fact *= j
        end
        idx = x / fact
        result += digits[idx].to_s
        digits.delete_at(idx)
        x -= idx * fact
    end
    result
end

# End Euler024

# Start Euler025

def n_digit_fibonacci_number(n)
    a = [1]
    b = [1]
    i = 2
    while b.length < n
        carry = 0
        c = b.clone
        b.each_with_index do |_, j|
            if j < a.length
                b[j] = a[j] + b[j] + carry
            else
                b[j] = b[j] + carry
            end
            carry = b[j] / 10
            b[j] = b[j] % 10
        end
        if carry != 0
            b.push(carry)
        end
        a = c
        i = i + 1
    end
    i
end

# End Euler025

# Start Euler026

def reciprocal_cycles(n)
    result = 0
    max_length = 0
    (1...n).each do |i|
        remainders = []
        remainder = 1
        while remainder != 0 && !remainders.include?(remainder)
            remainders.push(remainder)
            remainder = (remainder * 10) % i
        end
        length = 0
        if remainder != 0
            length = remainders.length - remainders.index(remainder)
        end
        if length > max_length
            max_length = length
            result = i
        end
    end
    result
end

# End Euler026

# Start Euler027

def is_prime(n)
    if n < 2
        return false
    end
    if n == 2
        return true
    end
    if n % 2 == 0
        return false
    end
    (3..Math.sqrt(n)).step(2) do |i|
        if n % i == 0
            return false
        end
    end
    true
end

def quadratic_primes(n)
    max_primes = 0
    result = 0
    (-n + 1...n).step(2) do |a|
        (-n + 1...n).step(2) do |b|
            x = 0
            while true
                if x * x + a * x + b < 2
                    break
                end
                if !is_prime(x * x + a * x + b)
                    break
                end
                x += 1
            end
            if x > max_primes
                max_primes = x
                result = a * b
            end
        end
    end
    result
end

# End Euler027

# Start Euler028

def number_spiral_diagonals(n)
    result = 1
    (3..n).step(2) do |i|
        result += 4 * i * i - 6 * i + 6
    end
    result
end

# End Euler028

# Start Euler029

def distinct_powers(n)
    result = 0
    xs = Set.new
    (2..n).each do |i|
        primes = [2, 3, 5, 7]
        powers = [0, 0, 0, 0]
        num = i
        primes.each_with_index do |p, j|
            while num % p == 0
                num /= p
                powers[j] += 1
            end
        end
        if num != 1
            result += n - 1
            next
        end
        (2..n).each do |j|
            pstr = "#{powers[0] * j}-#{powers[1] * j}-#{powers[2] * j}-#{powers[3] * j}"
            xs.add(pstr)
        end
    end
    result += xs.size
    result
end

# End Euler029

# Start Euler030

def digit_nth_powers(n)
    result = 0
    (2..4 * 10 ** n).each do |i|
        digits_sum = 0
        i.to_s.each_char do |digit|
            digits_sum += digit.to_i ** n
        end
        result += i if i == digits_sum
    end
    result
end

# End Euler030

# Start Euler031

def coin_sums(n)
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (n + 1)
    ways[0] = 1
    coins.each do |coin|
        (coin..n).each do |i|
            ways[i] += ways[i - coin]
        end
    end
    ways[n]
end

# End Euler031

# Start Euler032

def pandigital_products(n)
    products = Set.new
    s = ""
    (1..n).each do |i|
        s += i.to_s
    end
    (1...100).each do |a|
        (1...10000).each do |b|
            c = a * b
            chars = (a.to_s + b.to_s + c.to_s).chars
            chars.sort!
            if chars.join("") == s
                products.add(c)
            end
        end
    end
    result = 0
    products.each do |product|
        result += product
    end
    result
end

# End Euler032

# Start Euler033

def digit_canceling_fractions(m)
    numer = 1
    denom = 1
    (10...m).each do |d|
        (10...d).each do |n|
            n0 = n % 10
            n1 = n / 10
            d0 = d % 10
            d1 = d / 10
            if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0)
                numer *= n
                denom *= d
            end
        end
    end
    a, b = numer, denom
    while b != 0
        a, b = b, a % b
    end
    denom / a
end

# End Euler033

# Start Euler034

def digit_factorials(n)
    result = 0
    (3...n).each do |i|
        fact_sum = 0
        i.to_s.each_char do |digit|
            fact = 1
            (1..digit.to_i).each do |j|
                fact *= j
            end
            fact_sum += fact
        end
        if i == fact_sum
            result += i
        end
    end
    result
end

# End Euler034

# Start Euler035

def is_prime(n)
    if n < 2
        return false
    end
    if n == 2
        return true
    end
    if n % 2 == 0
        return false
    end
    (3..Math.sqrt(n)).step(2) do |i|
        if n % i == 0
            return false
        end
    end
    true
end

def circular_primes(n)
    count = 0
    (2...n).each do |i|
        if is_prime(i)
            rotations = Set.new
            si = i.to_s
            (0...si.length).each do |j|
                rotations.add((si[j..-1] + si[0...j]).to_i)
            end
            flag = true
            rotations.each do |x|
                if !is_prime(x)
                    flag = false
                    break
                end
            end
            if flag
                count += 1
            end
        end
    end
    count
end

# End Euler035

# Start Euler036

def is_palindrome(s)
    (0...s.length / 2).each do |i|
        if s[i] != s[s.length - i - 1]
            return false
        end
    end
    true
end

def double_base_palindromes(n)
    result = 0
    (1...n).each do |i|
        str_i = i.to_s
        bin_i = i.to_s(2)
        if is_palindrome(str_i) && is_palindrome(bin_i)
            result += i
        end
    end
    result
end

# End Euler036

# Start Euler037

def is_prime(n)
    if n < 2
        return false
    end
    if n == 2
        return true
    end
    if n % 2 == 0
        return false
    end
    (3..Math.sqrt(n)).step(2) do |i|
        if n % i == 0
            return false
        end
    end
    true
end

def truncatable_primes(n)
    result = 0
    (10...n).each do |i|
        if is_prime(i)
            si = i.to_s
            flag = true
            (1...si.length).each do |j|
                p1 = si[j..-1].to_i
                p2 = si[0...-j].to_i
                if !is_prime(p1) || !is_prime(p2)
                    flag = false
                    break
                end
            end
            if flag
                result += i
            end
        end
    end
    result
end

# End Euler037

# Start Euler038

def pandigital_multiples(n)
    result = -1
    (2..n).each do |i|
        cprod = ''
        (1...10).each do |j|
            cprod += (i * j).to_s
            if cprod.length == 9
                chars = cprod.split('').sort.join
                if chars == '123456789'
                    result = [result, cprod.to_i].max
                    break
                end
            elsif cprod.length > 9
                break
            end
        end
    end
    result
end

# End Euler038

# Start Euler039

def integer_right_triangles(n)
    max_sol = 0
    result = 0
    (3..n).each do |p|
        sol = 0
        (1...p / 2).each do |a|
            (a...p / 2).each do |b|
                c = p - a - b
                if a * a + b * b == c * c
                    sol += 1
                end
            end
        end
        if sol > max_sol
            max_sol = sol
            result = p
        end
    end
    result
end

# End Euler039

# Start Euler040

def champernowne_constant(b)
    s = ""
    (1..b**6).each do |i|
        s += i.to_s
    end
    result = 1
    (0..6).each do |i|
        result *= s[b**i - 1].to_i
    end
    result
end

# End Euler040

# Start Euler041

def is_prime(n)
    if n < 2
        return false
    end
    if n == 2
        return true
    end
    if n % 2 == 0
        return false
    end
    (3..Math.sqrt(n)).step(2) do |i|
        if n % i == 0
            return false
        end
    end
    true
end

def pandigital_prime(n)
    (n - 1).downto(1) do |i|
        if is_prime(i)
            si = i.to_s
            length = si.length
            flag = true
            (1..length).each do |j|
                if !si.include?(j.to_s)
                    flag = false
                    break
                end
            end
            if flag
                return i
            end
        end
    end
    -1
end

# End Euler041

# Start Euler042

def coded_triangle_numbers(words)
    result = 0
    words.each do |word|
        value = 0
        word.each_char do |c|
            value += c.ord - 64
        end
        n = Math.sqrt(value * 2).to_i
        if n * (n + 1) == value * 2
            result += 1
        end
    end
    result
end

# End Euler042

# Start Euler043

def gen_permutations(s)
    if s.length <= 1
        return [s]
    end
    result = []
    gen_permutations(s[1..-1]).each do |perm|
        (0...s.length).each do |i|
            result.push(perm[0...i] + s[0] + perm[i..-1])
        end
    end
    result
end


def sub_string_divisibility(n)
    result = 0
    primes = [2, 3, 5, 7, 11, 13, 17]
    s = ""
    (0..n).each do |i|
        s += i.to_s
    end
    gen_permutations(s).each do |i|
        flag = true
        (1...n - 1).each do |j|
            if i[j..j + 2].to_i % primes[j - 1] != 0
                flag = false
                break
            end
        end
        if flag
            result += i.to_i
        end
    end
    result
end

# End Euler043

# Start Euler044

def pentagon_numbers(n)
    pentagon = {}
    (1...n).each do |i|
        pentagon[i * (3 * i - 1) / 2] = true
    end
    result = -1
    pentagon.each do |j, _|
        pentagon.each do |k, _|
            if pentagon[j + k] && pentagon[k - j]
                if result == -1 || k - j < result
                    result = k - j
                end
            end
        end
    end
    result
end

# End Euler044

# Start Euler045

def triangular_pentagonal_and_hexagonal(n)
    ps = Set.new
    i = 1
    c = (0.5 * i * (3 * i - 1)).to_i
    while c < n
        i += 1
        ps.add(c)
        c = (0.5 * i * (3 * i - 1)).to_i
    end
    i = 1
    c = i * (2 * i - 1)
    result = -1
    while c < n
        i += 1
        if ps.include?(c)
            result = c
        end
        c = i * (2 * i - 1)
    end
    result
end

# End Euler045

# Start Euler046

def is_prime(n)
    if n < 2
        return false
    end
    if n == 2
        return true
    end
    if n % 2 == 0
        return false
    end
    (3..Math.sqrt(n)).step(2) do |i|
        if n % i == 0
            return false
        end
    end
    true
end

def goldbachs_other_conjecture(n)
    result = -1
    (9999...n).step(-2).each do |i|
        upper = Math.sqrt(i / 2).to_i
        flag = false
        (0..upper).each do |j|
            if is_prime(i - 2 * j * j)
                flag = true
                break
            end
        end
        if !flag
            result = i
        end
    end
    result
end

# End Euler046

# Start Euler047

def prime_factors(n)
    num = n
    factors = []
    i = 2
    while i * i <= num
        if num % i != 0
            i += 1
        else
            num /= i
            factors.push(i)
        end
    end
    if num > 1
        factors.push(num)
    end
    factors.uniq.length
end

def distinct_primes_factors(n)
    (n...1000000).each do |i|
        if prime_factors(i) == 4 && prime_factors(i + 1) == 4 && prime_factors(i + 2) == 4 && prime_factors(i + 3) == 4
            return i
        end
    end
    -1
end

# End Euler047

# Start Euler048

def self_powers(n)
    digits = [0] * 10
    (1..n).each do |i|
        temp_digits = [0] * 10
        temp_digits[0] = 1
        (0...i).each do |j|
            carry = 0
            (0...10).each do |k|
                temp_digits[k] = temp_digits[k] * i + carry
                carry = temp_digits[k] / 10
                temp_digits[k] %= 10
            end
        end
        (0...10).each do |j|
            digits[j] += temp_digits[j]
            if digits[j] >= 10
                digits[j] -= 10
                if j < 9
                    digits[j + 1] += 1
                end
            end
        end
    end
    result = ""
    (9).downto(0).each do |i|
        result += digits[i].to_s
    end
    result
end

# End Euler048

# Start Euler049

def is_prime(n)
    if n < 2
        return false
    end
    if n == 2
        return true
    end
    if n % 2 == 0
        return false
    end
    (3..Math.sqrt(n)).step(2) do |i|
        if n % i == 0
            return false
        end
    end
    true
end

def gen_permutations(s)
    if s.length <= 1
        return [s]
    end
    result = []
    gen_permutations(s[1..-1]).each do |perm|
        (0...s.length).each do |i|
            result.push(perm[0...i] + s[0] + perm[i..-1])
        end
    end
    result
end

def prime_permutations(n)
    (n).downto(999).each do |i|
        if is_prime(i)
            permutations = gen_permutations(i.to_s)
            candidates = Set.new
            permutations.each do |j|
                candidate = j.to_i
                if candidate > i && is_prime(candidate)
                    candidates.add(candidate)
                end
            end
            candidates.each do |m|
                if candidates.include?(m + (m - i))
                    return i.to_s + m.to_s + (m + (m - i)).to_s
                end
            end
        end
    end
    ""
end

# End Euler049

# Start Euler050

def consecutive_prime_sum(limit)
    sieve = Array.new(limit, true)
    primes = []
    (2...limit).each do |i|
        if sieve[i]
            primes.push(i)
            (i * 2...limit).step(i) do |j|
                sieve[j] = false
            end
        end
    end
    max_length = 0
    max_prime = 0
    primes.each_with_index do |_, i|
        (i + max_length...primes.length).each do |j|
            s = 0
            (i...j).each do |k|
                s += primes[k]
            end
            if s >= limit
                break
            end
            if sieve[s] && j - i > max_length
                max_length = j - i
                max_prime = s
            end
        end
    end
    max_prime
end

# End Euler050

