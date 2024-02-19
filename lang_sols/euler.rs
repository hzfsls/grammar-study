// Start Euler001

fn multiples_of_3_and_5(n: i32) -> i32 {
    let mut result = 0;
    for i in 0..n {
        if i % 3 == 0 || i % 5 == 0 {
            result += i;
        }
    }
    result
}

// End Euler001

// Start Euler002

fn even_fibonacci_numbers(n: i32) -> i32 {
    let mut result = 0;
    let mut a = 1;
    let mut b = 2;
    while a < n {
        if a % 2 == 0 {
            result += a;
        }
        let tmp = a;
        a = b;
        b = tmp + b;
    }
    result
}

// End Euler002

// Start Euler003

fn largest_prime_factor(n: i32) -> i32 {
    let mut result = n;
    let mut i = 2;
    while i * i <= result {
        if result % i != 0 {
            i += 1;
        } else {
            result /= i;
        }
    }
    result
}

// End Euler003

// Start Euler004

fn is_palindrome(s: &String) -> bool {
    for i in 0..s.len() / 2 {
        if s.chars().nth(i).unwrap() != s.chars().nth(s.len() - i - 1).unwrap() {
            return false;
        }
    }
    true
}

fn largest_palindrome_product(n: i32) -> i32 {
    let mut result = 0;
    for i in 100..1000 {
        for j in i..1000 {
            let prod = i * j;
            if is_palindrome(&prod.to_string()) && prod > result && prod < n {
                result = prod;
            }
        }
    }
    result
}

// End Euler004

// Start Euler005

fn smallest_multiple(n: i32) -> i32 {
    let mut result = 1;
    for i in 1..=n {
        if result % i != 0 {
            for j in 1..=n {
                if (result * j) % i == 0 {
                    result *= j;
                    break;
                }
            }
        }
    }
    result
}

// End Euler005

// Start Euler006

fn sum_square_difference(n: i32) -> i32 {
    let mut sqr_sum = 0;
    let mut num_sum = 0;
    for i in 1..=n {
        sqr_sum += i * i;
        num_sum += i;
    }
    num_sum * num_sum - sqr_sum
}

// End Euler006

// Start Euler007

fn nth_prime(n: i32) -> i32 {
    let mut primes = vec![2];
    let mut i = 3;
    while primes.len() < n as usize {
        for p in &primes {
            if i % p == 0 {
                break;
            }
            if p * p > i {
                primes.push(i);
                break;
            }
        }
        i += 2;
    }
    primes[primes.len() - 1]
}

// End Euler007

// Start Euler008

fn largest_product_in_a_series(s: &String, k: i32) -> i32 {
    let mut result = 0;
    for i in 0..s.len() - k as usize {
        let mut product = 1;
        for j in 0..k as usize {
            product *= s.chars().nth(i + j).unwrap().to_digit(10).unwrap() as i32;
        }
        result = result.max(product);
    }
    result
}

// End Euler008

// Start Euler009

fn special_pythagorean_triplet(n: i32) -> i32 {
    for a in 1..n {
        for b in a..n {
            let c = n - a - b;
            if a * a + b * b == c * c {
                return a * b * c;
            }
        }
    }
    -1
}

// End Euler009

// Start Euler010

fn summation_of_primes(n: i32) -> i32 {
    let mut primes = vec![2];
    let mut i = 3;
    while i <= n {
        for p in &primes {
            if i % p == 0 {
                break;
            }
            if p * p > i {
                primes.push(i);
                break;
            }
        }
        i += 2;
    }
    let mut result = 0;
    for prime in &primes {
        result += prime;
    }
    result
}

// End Euler010

// Start Euler011

fn largest_product_in_a_grid(grid: &Vec<Vec<i32>>) -> i32 {
    let mut result = 0;
    for i in 0..grid.len() - 3 {
        for j in 0..grid[i].len() - 3 {
            let mut p1 = 1;
            let mut p2 = 1;
            let mut p3 = 1;
            let mut p4 = 1;
            for k in 0..4 {
                p1 *= grid[i + k][j];
            }
            for k in 0..4 {
                p2 *= grid[i][j + k];
            }
            for k in 0..4 {
                p3 *= grid[i + k][j + k];
            }
            for k in 0..4 {
                p4 *= grid[i + k][j + 3 - k];
            }
            result = vec![result, p1, p2, p3, p4].into_iter().max().unwrap();
        }
    }
    result
}

// End Euler011

// Start Euler012

fn highly_divisible_triangular_number(n: i32) -> i32 {
    for i in 1..100000000 {
        let result = i * (i + 1) / 2;
        let mut count = 0;
        for j in 1..=(result as f64).sqrt() as i32 {
            if result % j == 0 {
                count += 2;
            }
            if j * j == result {
                count -= 1;
            }
        }
        if count > n {
            return result;
        }
    }
    -1
}

// End Euler012

// Start Euler013

fn large_sum(numbers: &Vec<String>) -> String {
    let mut digits = vec![0; 60];
    for i in 0..50 {
        let mut tmp = 0;
        for num in numbers.iter() {
            tmp += num.chars().nth(49 - i).unwrap().to_digit(10).unwrap();
        }
        for j in i..60 {
            digits[j] += tmp % 10;
            if digits[j] >= 10 {
                digits[j + 1] += digits[j] / 10;
                digits[j] %= 10;
            }
            tmp /= 10;
            if tmp == 0 {
                break;
            }
        }
    }
    for i in (0..60).rev() {
        if digits[i] != 0 {
            let mut result = String::new();
            for j in (i - 9..=i).rev() {
                result += &digits[j].to_string();
            }
            return result;
        }
    }
    String::new()
}

// End Euler013

// Start Euler014

fn longest_collatz_sequence(n: i32) -> i32 {
    let mut longest = 0;
    let mut result = 0;
    for i in 1..n {
        let mut chain = 1;
        let mut num = i;
        while num != 1 {
            if num % 2 == 0 {
                num = num / 2;
            } else {
                num = 3 * num + 1;
            }
            chain += 1;
        }
        if chain > longest {
            longest = chain;
            result = i;
        }
    }
    result
}

// End Euler014

// Start Euler015

fn lattice_paths(m: i32, n: i32) -> i32 {
    let mut grid = vec![vec![0; (n + 1) as usize]; (m + 1) as usize];
    for i in 0..=m {
        grid[i as usize][0] = 1;
    }
    for j in 0..=n {
        grid[0][j as usize] = 1;
    }
    for i in 1..=m {
        for j in 1..=n {
            grid[i as usize][j as usize] = grid[(i - 1) as usize][j as usize] + grid[i as usize][(j - 1) as usize];
        }
    }
    grid[m as usize][n as usize]
}

// End Euler015

// Start Euler016

fn power_digit_sum(n: i32) -> i32 {
    let mut digits = vec![2];
    for _ in 1..n {
        let mut carry = 0;
        for j in 0..digits.len() {
            let temp = digits[j] * 2 + carry;
            digits[j] = temp % 10;
            carry = temp / 10;
        }
        if carry != 0 {
            digits.push(carry);
        }
    }
    let mut result = 0;
    for digit in digits {
        result += digit;
    }
    result
}

// End Euler016

// Start Euler017

fn number_to_words(n: i32) -> String {
    let ones = vec!["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let teens = vec!["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
    let tens = vec!["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
    if n == 1000 {
        "one thousand".to_string()
    } else if n >= 100 {
        if n % 100 == 0 {
            ones[(n / 100) as usize].to_string() + " hundred"
        } else {
            ones[(n / 100) as usize].to_string() + " hundred and " + &number_to_words(n % 100)
        }
    } else if n >= 20 {
        let mut suf = "".to_string();
        if n % 10 != 0 {
            suf = " ".to_string() + &ones[(n % 10) as usize];
        }
        tens[(n / 10) as usize].to_string() + &suf
    } else if n >= 10 {
        teens[(n - 10) as usize].to_string()
    } else {
        ones[n as usize].to_string()
    }
}

// End Euler017

// Start Euler018

fn maximum_path_sum_i(triangle: &Vec<Vec<i32>>) -> i32 {
    let mut curr = triangle.last().unwrap().clone();
    for i in (0..triangle.len() - 1).rev() {
        let mut next = triangle[i].clone();
        for j in 0..next.len() {
            next[j] += curr[j].max(curr[j + 1]);
        }
        curr = next;
    }
    curr[0]
}

// End Euler018

// Start Euler019

fn counting_sundays(y1: i32, y2: i32) -> i32 {
    let mut day = 0;
    let mut count = 0;
    for year in 1900..=y2 {
        for month in 1..=12 {
            if year >= y1 && day % 7 == 6 {
                count += 1;
            }
            if month == 4 || month == 6 || month == 9 || month == 11 {
                day += 30;
            } else if month == 2 {
                if year % 4 == 0 && (year % 100 != 0 || year % 400 == 0) {
                    day += 29;
                } else {
                    day += 28;
                }
            } else {
                day += 31;
            }
        }
    }
    count
}

// End Euler019

// Start Euler020

fn factorial_digit_sum(n: i32) -> i32 {
    let mut digits = vec![1];
    for i in 1..=n {
        let mut carry = 0;
        for j in 0..digits.len() {
            digits[j] = digits[j] * i + carry;
            carry = digits[j] / 10;
            digits[j] %= 10;
        }
        while carry != 0 {
            digits.push(carry % 10);
            carry /= 10;
        }
    }
    let mut result = 0;
    for digit in digits {
        result += digit;
    }
    result
}

// End Euler020

// Start Euler021

fn d(n: i32) -> i32 {
    let mut result = 1;
    for i in 2..=(n as f64).sqrt() as i32 {
        if n % i == 0 {
            result += i;
            if i != n / i {
                result += n / i;
            }
        }
    }
    result
}

fn amicable_numbers(n: i32) -> i32 {
    let mut result = 0;
    for a in 2..n {
        let b = d(a);
        if a != b && a == d(b) {
            result += a;
        }
    }
    result
}

// End Euler021

// Start Euler022

fn names_scores(names: &Vec<String>, queries: &Vec<String>) -> i32 {
    let mut s_names = names.clone();
    s_names.sort();
    let mut result = 0;
    for (i, name) in s_names.iter().enumerate() {
        let mut x = 0;
        for c in name.chars() {
            x += c as i32 - 64;
        }
        if queries.contains(name) {
            result += x * (i as i32 + 1);
        }
    }
    result
}

// End Euler022

// Start Euler023

fn is_abundant(n: i32) -> bool {
    if n < 12 {
        return false;
    }
    let mut sum_divisors = 1;
    for i in 2..=(n as f64).sqrt() as i32 {
        if n % i == 0 {
            sum_divisors += i;
            if i != n / i {
                sum_divisors += n / i;
            }
        }
    }
    sum_divisors > n
}

fn non_abundant_sums(n: i32) -> i32 {
    let mut abundants = vec![];
    for i in 12..n {
        if is_abundant(i) {
            abundants.push(i);
        }
    }
    let mut abundant_sums = vec![];
    for i in &abundants {
        for j in &abundants {
            abundant_sums.push(i + j);
        }
    }
    let mut result = 0;
    for i in 0..n {
        if !abundant_sums.contains(&i) {
            result += i;
        }
    }
    result
}

// End Euler023

// Start Euler024

fn lexicographic_permutations(n: i32) -> String {
    let mut result = String::new();
    let mut digits = vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let mut x = n - 1;
    for i in (1..11).rev() {
        let mut fact = 1;
        for j in 1..i {
            fact *= j;
        }
        let idx = x / fact;
        result.push_str(&digits[idx as usize].to_string());
        digits.remove(idx as usize);
        x -= idx * fact;
    }
    result
}

// End Euler024

// Start Euler025

fn n_digit_fibonacci_number(n: i32) -> i32 {
    let mut a = vec![1];
    let mut b = vec![1];
    let mut i = 2;
    while b.len() < n as usize {
        let mut carry = 0;
        let c = b.clone();
        for j in 0..b.len() {
            if j < a.len() {
                b[j] = a[j] + b[j] + carry;
            } else {
                b[j] = b[j] + carry;
            }
            carry = b[j] / 10;
            b[j] = b[j] % 10;
        }
        if carry != 0 {
            b.push(carry);
        }
        a = c;
        i = i + 1;
    }
    i
}

// End Euler025

// Start Euler026

fn reciprocal_cycles(n: i32) -> i32 {
    let mut result = 0;
    let mut max_length = 0;
    for i in 1..n {
        let mut remainders = vec![];
        let mut remainder = 1;
        while remainder != 0 && !remainders.contains(&remainder) {
            remainders.push(remainder);
            remainder = (remainder * 10) % i;
        }
        let mut length = 0;
        if remainder != 0 {
            length = remainders.len() - remainders.iter().position(|&x| x == remainder).unwrap();
        }
        if length > max_length {
            max_length = length;
            result = i;
        }
    }
    result
}

// End Euler026

// Start Euler027

fn is_prime(n: i32) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    for i in (3..=(n as f64).sqrt() as i32).step_by(2) {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn quadratic_primes(n: i32) -> i32 {
    let mut max_primes = 0;
    let mut result = 0;
    for a in (-n + 1..n).step_by(2) {
        for b in (-n + 1..n).step_by(2) {
            let mut x = 0;
            while x * x + a * x + b >= 2 {
                if !is_prime(x * x + a * x + b) {
                    break;
                }
                x += 1;
            }
            if x > max_primes {
                max_primes = x;
                result = a * b;
            }
        }
    }
    result
}

// End Euler027

// Start Euler028

fn number_spiral_diagonals(n: i32) -> i32 {
    let mut result = 1;
    for i in (3..=n).step_by(2) {
        result += 4 * i * i - 6 * i + 6;
    }
    result
}

// End Euler028

// Start Euler029

fn distinct_powers(n: i32) -> i32 {
    let mut result = 0;
    let mut xs = HashSet::new();
    for i in 2..=n {
        let primes = vec![2, 3, 5, 7];
        let mut powers = vec![0, 0, 0, 0];
        let mut num = i;
        for j in 0..primes.len() {
            while num % primes[j] == 0 {
                num /= primes[j];
                powers[j] += 1;
            }
        }
        if num != 1 {
            result += n - 1;
            continue;
        }
        for j in 2..=n {
            let pstr = format!("{}-{}-{}-{}", powers[0] * j, powers[1] * j, powers[2] * j, powers[3] * j);
            xs.insert(pstr);
        }
    }
    result += xs.len() as i32;
    result
}

// End Euler029

// Start Euler030

fn digit_nth_powers(n: i32) -> i32 {
    let mut result = 0;
    for i in 2..4 * (10 as i32).pow(n as u32) {
        let mut digits_sum = 0;
        for digit in i.to_string().chars() {
            digits_sum += (digit.to_digit(10).unwrap() as i32).pow(n as u32);
        }
        if i == digits_sum {
            result += i;
        }
    }
    result
}

// End Euler030

// Start Euler031

fn coin_sums(n: i32) -> i32 {
    let coins = vec![1, 2, 5, 10, 20, 50, 100, 200];
    let mut ways = vec![0; (n + 1) as usize];
    ways[0] = 1;
    for coin in coins {
        for i in coin..=n {
            ways[i as usize] += ways[(i - coin) as usize];
        }
    }
    ways[n as usize]
}

// End Euler031

// Start Euler032

fn pandigital_products(n: i32) -> i32 {
    let mut products = HashSet::new();
    let mut s = String::new();
    for i in 1..=n {
        s.push_str(&i.to_string());
    }
    for a in 1..100 {
        for b in 1..10000 {
            let c = a * b;
            let mut chars = (a.to_string() + &b.to_string() + &c.to_string()).chars().collect::<Vec<char>>();
            chars.sort();
            if chars.into_iter().collect::<String>() == s {
                products.insert(c);
            }
        }
    }
    let mut result = 0;
    for product in products {
        result += product;
    }
    result
}

// End Euler032

// Start Euler033

fn digit_canceling_fractions(m: i32) -> i32 {
    let mut numer = 1;
    let mut denom = 1;
    for d in 10..m {
        for n in 10..d {
            let n0 = n % 10;
            let n1 = n / 10;
            let d0 = d % 10;
            let d1 = d / 10;
            if (n1 == d0 && n0 * d == n * d1) || (n0 == d1 && n1 * d == n * d0) {
                numer *= n;
                denom *= d;
            }
        }
    }
    let mut a = numer;
    let mut b = denom;
    while b != 0 {
        let temp = b;
        b = a % b;
        a = temp;
    }
    denom / a
}

// End Euler033

// Start Euler034

fn digit_factorials(n: i32) -> i32 {
    let mut result = 0;
    for i in 3..n {
        let mut fact_sum = 0;
        for digit in i.to_string().chars() {
            let mut fact = 1;
            for j in 1..=digit.to_digit(10).unwrap() {
                fact *= j;
            }
            fact_sum += fact;
        }
        if i == fact_sum as i32 {
            result += i;
        }
    }
    result
}

// End Euler034

// Start Euler035

fn is_prime(n: i32) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    for i in (3..=(n as f64).sqrt() as i32).step_by(2) {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn circular_primes(n: i32) -> i32 {
    let mut count = 0;
    for i in 2..n {
        if is_prime(i) {
            let mut rotations = HashSet::new();
            let si = i.to_string();
            for j in 0..si.len() {
                rotations.insert((si[j..].to_string() + &si[..j]).parse().unwrap());
            }
            let mut flag = true;
            for x in rotations {
                if !is_prime(x) {
                    flag = false;
                    break;
                }
            }
            if flag {
                count += 1;
            }
        }
    }
    count
}

// End Euler035

// Start Euler036

fn is_palindrome(s: &String) -> bool {
    for i in 0..s.len() / 2 {
        if s.chars().nth(i).unwrap() != s.chars().nth(s.len() - i - 1).unwrap() {
            return false;
        }
    }
    true
}

fn double_base_palindromes(n: i32) -> i32 {
    let mut result = 0;
    for i in 1..n {
        let str_i = i.to_string();
        let bin_i = format!("{:b}", i);
        if is_palindrome(&str_i) && is_palindrome(&bin_i) {
            result += i;
        }
    }
    result
}

// End Euler036

// Start Euler037

fn is_prime(n: i32) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    for i in (3..=(n as f64).sqrt() as i32).step_by(2) {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn truncatable_primes(n: i32) -> i32 {
    let mut result = 0;
    for i in 10..n {
        if is_prime(i) {
            let si = i.to_string();
            let mut flag = true;
            for j in 1..si.len() {
                let p1 = si[j..].parse().unwrap();
                let p2 = si[..si.len() - j].parse().unwrap();
                if !is_prime(p1) || !is_prime(p2) {
                    flag = false;
                    break;
                }
            }
            if flag {
                result += i;
            }
        }
    }
    result
}

// End Euler037

// Start Euler038

fn pandigital_multiples(n: i32) -> i32 {
    let mut result = -1;
    for i in 2..=n {
        let mut cprod = String::new();
        for j in 1..10 {
            cprod += &(i * j).to_string();
            if cprod.len() == 9 {
                let mut chars: Vec<char> = cprod.chars().collect();
                chars.sort();
                if chars.iter().collect::<String>() == "123456789" {
                    result = result.max(cprod.parse::<i32>().unwrap());
                    break;
                }
            } else if cprod.len() > 9 {
                break;
            }
        }
    }
    result
}

// End Euler038

// Start Euler039

fn integer_right_triangles(n: i32) -> i32 {
    let mut max_sol = 0;
    let mut result = 0;
    for p in 3..=n {
        let mut sol = 0;
        for a in 1..p / 2 {
            for b in a..p / 2 {
                let c = p - a - b;
                if a * a + b * b == c * c {
                    sol += 1;
                }
            }
        }
        if sol > max_sol {
            max_sol = sol;
            result = p;
        }
    }
    result
}

// End Euler039

// Start Euler040

fn champernowne_constant(b: i32) -> i32 {
    let mut s = String::new();
    for i in 1..i32::pow(b, 6) {
        s += &i.to_string();
    }
    let mut result = 1;
    for i in 0..7 {
        result *= s.chars().nth(i32::pow(b, i) as usize - 1).unwrap().to_digit(10).unwrap() as i32;
    }
    result
}

// End Euler040

// Start Euler041

fn is_prime(n: i32) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    for i in (3..=(n as f64).sqrt() as i32).step_by(2) {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn pandigital_prime(n: i32) -> i32 {
    for i in (1..n).rev() {
        if is_prime(i) {
            let si = i.to_string();
            let length = si.len();
            let mut flag = true;
            for j in 1..=length {
                if !si.contains(&j.to_string()) {
                    flag = false;
                    break;
                }
            }
            if flag {
                return i;
            }
        }
    }
    -1
}

// End Euler041

// Start Euler042

fn coded_triangle_numbers(words: &Vec<String>) -> i32 {
    let mut result = 0;
    for word in words {
        let mut value = 0;
        for c in word.chars() {
            value += c as i32 - 64;
        }
        let n = ((value * 2) as f64).sqrt() as i32;
        if n * (n + 1) == value * 2 {
            result += 1;
        }
    }
    result
}

// End Euler042

// Start Euler043

fn gen_permutations(s: &String) -> Vec<String> {
    if s.len() <= 1 {
        return vec![s.clone()];
    }
    let mut result = vec![];
    for perm in gen_permutations(&s[1..].to_string()) {
        for i in 0..s.len() {
            result.push(perm[..i].to_string() + &s[0..1] + &perm[i..]);
        }
    }
    result
}

fn sub_string_divisibility(n: i32) -> i32 {
    let mut result = 0;
    let primes = vec![2, 3, 5, 7, 11, 13, 17];
    let mut s = String::new();
    for i in 0..=n {
        s += &i.to_string();
    }
    for i in gen_permutations(&s) {
        let mut flag = true;
        for j in 1..(n - 1) as usize {
            if i[j..j + 3].parse::<i32>().unwrap() % primes[j - 1] != 0 {
                flag = false;
                break;
            }
        }
        if flag {
            result += i.parse::<i32>().unwrap();
        }
    }
    result
}

// End Euler043

// Start Euler044

fn pentagon_numbers(n: i32) -> i32 {
    let mut pentagon = HashSet::new();
    for i in 1..n {
        pentagon.insert(i * (3 * i - 1) / 2);
    }
    let mut result = -1;
    for &j in &pentagon {
        for &k in &pentagon {
            if pentagon.contains(&(j + k)) && pentagon.contains(&(k - j)) {
                if result == -1 || k - j < result {
                    result = k - j;
                }
            }
        }
    }
    result
}

// End Euler044

// Start Euler045

fn triangular_pentagonal_and_hexagonal(n: i32) -> i32 {
    let mut ps = HashSet::new();
    let mut i = 1;
    let mut c = (0.5 * i as f64 * (3 * i - 1) as f64) as i32;
    while c < n {
        i += 1;
        ps.insert(c);
        c = (0.5 * i as f64 * (3 * i - 1) as f64) as i32;
    }
    i = 1;
    c = i * (2 * i - 1);
    let mut result = -1;
    while c < n {
        i += 1;
        if ps.contains(&c) {
            result = c;
        }
        c = i * (2 * i - 1);
    }
    result
}

// End Euler045

// Start Euler046

fn is_prime(n: i32) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    for i in (3..=(n as f64).sqrt() as i32).step_by(2) {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn goldbachs_other_conjecture(n: i32) -> i32 {
    let mut result = -1;
    for i in (n + 1..=9999).rev().step_by(2) {
        let upper = ((i / 2) as f64).sqrt() as i32;
        let mut flag = false;
        for j in 0..=upper {
            if is_prime(i - 2 * j * j) {
                flag = true;
                break;
            }
        }
        if !flag {
            result = i;
        }
    }
    result
}

// End Euler046

// Start Euler047

fn prime_factors(n: i32) -> i32 {
    let mut num = n;
    let mut factors = vec![];
    let mut i = 2;
    while i * i <= num {
        if num % i != 0 {
            i += 1;
        } else {
            num /= i;
            factors.push(i);
        }
    }
    if num > 1 {
        factors.push(num);
    }
    factors.into_iter().collect::<HashSet<_>>().len() as i32
}

fn distinct_primes_factors(n: i32) -> i32 {
    for i in n..1000000 {
        if prime_factors(i) == 4 && prime_factors(i + 1) == 4 && prime_factors(i + 2) == 4 && prime_factors(i + 3) == 4 {
            return i;
        }
    }
    -1
}

// End Euler047

// Start Euler048

fn self_powers(n: i32) -> String {
    let mut digits = [0; 10];
    for i in 1..=n {
        let mut temp_digits = [0; 10];
        temp_digits[0] = 1;
        for j in 0..i {
            let mut carry = 0;
            for k in 0..10 {
                temp_digits[k] = temp_digits[k] * i + carry;
                carry = temp_digits[k] / 10;
                temp_digits[k] %= 10;
            }
        }
        for j in 0..10 {
            digits[j] += temp_digits[j];
            if digits[j] >= 10 {
                digits[j] -= 10;
                if j < 9 {
                    digits[j + 1] += 1;
                }
            }
        }
    }
    let mut result = String::new();
    for i in (0..10).rev() {
        result += &digits[i].to_string();
    }
    result
}

// End Euler048

// Start Euler049

fn is_prime(n: i32) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    for i in (3..=(n as f64).sqrt() as i32).step_by(2) {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn gen_permutations(s: &String) -> Vec<String> {
    if s.len() <= 1 {
        return vec![s.clone()];
    }
    let mut result = vec![];
    for perm in gen_permutations(&s[1..].to_string()) {
        for i in 0..s.len() {
            result.push(perm[..i].to_string() + &s[0..1] + &perm[i..]);
        }
    }
    result
}

fn prime_permutations(n: i32) -> String {
    for i in (999..n).rev() {
        if is_prime(i) {
            let permutations = gen_permutations(&i.to_string());
            let mut candidates = std::collections::HashSet::new();
            for j in permutations {
                let candidate = j.parse::<i32>().unwrap();
                if candidate > i && is_prime(candidate) {
                    candidates.insert(candidate);
                }
            }
            for m in &candidates {
                if candidates.contains(&(m + (m - i))) {
                    return i.to_string() + &m.to_string() + &(m + (m - i)).to_string();
                }
            }
        }
    }
    "".to_string()
}

// End Euler049

// Start Euler050

fn consecutive_prime_sum(limit: i32) -> i32 {
    let mut sieve = vec![true; limit as usize];
    let mut primes = vec![];
    for i in 2..limit {
        if sieve[i as usize] {
            primes.push(i);
            for j in (i * 2..limit).step_by(i as usize) {
                sieve[j as usize] = false;
            }
        }
    }
    let mut max_length = 0;
    let mut max_prime = 0;
    for i in 0..primes.len() {
        for j in i + max_length..primes.len() {
            let mut s = 0;
            for k in i..j {
                s += primes[k];
            }
            if s >= limit {
                break;
            }
            if sieve[s as usize] && j - i > max_length {
                max_length = j - i;
                max_prime = s;
            }
        }
    }
    max_prime
}

// End Euler050

