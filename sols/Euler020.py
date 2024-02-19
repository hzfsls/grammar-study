# Python

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

# Start translation now

# C++

int factorialDigitSum(int n) {
    vector<int> digits = {1};
    for (int i = 1; i <= n; i++) {
        int carry = 0;
        for (int j = 0; j < digits.size(); j++) {
            digits[j] = digits[j] * i + carry;
            carry = digits[j] / 10;
            digits[j] %= 10;
        }
        while (carry) {
            digits.push_back(carry % 10);
            carry /= 10;
        }
    }
    int result = 0;
    for (int digit : digits) {
        result += digit;
    }
    return result;
}

# C#

class Global {
    public static int FactorialDigitSum(int n) {
        List<int> digits = new List<int> {1};
        for (int i = 1; i <= n; i++) {
            int carry = 0;
            for (int j = 0; j < digits.Count; j++) {
                digits[j] = digits[j] * i + carry;
                carry = digits[j] / 10;
                digits[j] %= 10;
            }
            while (carry != 0) {
                digits.Add(carry % 10);
                carry /= 10;
            }
        }
        int result = 0;
        foreach (int digit in digits) {
            result += digit;
        }
        return result;
    }
}

# Go

func FactorialDigitSum(n int) int {
    digits := []int{1}
    for i := 1; i <= n; i++ {
        carry := 0
        for j := 0; j < len(digits); j++ {
            digits[j] = digits[j] * i + carry
            carry = digits[j] / 10
            digits[j] %= 10
        }
        for carry != 0 {
            digits = append(digits, carry % 10)
            carry /= 10
        }
    }
    result := 0
    for _, digit := range digits {
        result += digit
    }
    return result
}

# Java

class Global {
    public static int factorialDigitSum(int n) {
        List<Integer> digits = new ArrayList<Integer>();
        digits.add(1);
        for (int i = 1; i <= n; i++) {
            int carry = 0;
            for (int j = 0; j < digits.size(); j++) {
                digits.set(j, digits.get(j) * i + carry);
                carry = digits.get(j) / 10;
                digits.set(j, digits.get(j) % 10);
            }
            while (carry != 0) {
                digits.add(carry % 10);
                carry /= 10;
            }
        }
        int result = 0;
        for (int digit : digits) {
            result += digit;
        }
        return result;
    }
}

# JavaScript

const factorialDigitSum = (n) => {
    let digits = [1];
    for (let i = 1; i <= n; i++) {
        let carry = 0;
        for (let j = 0; j < digits.length; j++) {
            digits[j] = digits[j] * i + carry;
            carry = Math.floor(digits[j] / 10);
            digits[j] %= 10;
        }
        while (carry !== 0) {
            digits.push(carry % 10);
            carry = Math.floor(carry / 10);
        }
    }
    let result = 0;
    for (let digit of digits) {
        result += digit;
    }
    return result;
}

# Kotlin

fun factorialDigitSum(n: Int): Int {
    val digits = mutableListOf(1)
    for (i in 1..n) {
        var carry = 0
        for (j in digits.indices) {
            digits[j] = digits[j] * i + carry
            carry = digits[j] / 10
            digits[j] %= 10
        }
        while (carry != 0) {
            digits.add(carry % 10)
            carry /= 10
        }
    }
    var result = 0
    for (digit in digits) {
        result += digit
    }
    return result
}

# PHP

function factorialDigitSum($n) {
    $digits = [1];
    for ($i = 1; $i <= $n; $i++) {
        $carry = 0;
        for ($j = 0; $j < count($digits); $j++) {
            $digits[$j] = $digits[$j] * $i + $carry;
            $carry = (int)($digits[$j] / 10);
            $digits[$j] %= 10;
        }
        while ($carry !== 0) {
            $digits[] = $carry % 10;
            $carry = (int)($carry / 10);
        }
    }
    $result = 0;
    foreach ($digits as $digit) {
        $result += $digit;
    }
    return $result;
}

# Ruby

def factorial_digit_sum(n)
    digits = [1]
    for i in 1..n
        carry = 0
        for j in 0...digits.length
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
    return result
end

# Rust

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

# Scala

def factorialDigitSum(n: Int): Int = {
    var digits = ArrayBuffer(1)
    for (i <- 1 to n) {
        var carry = 0
        for (j <- digits.indices) {
            digits(j) = digits(j) * i + carry
            carry = digits(j) / 10
            digits(j) = digits(j) % 10
        }
        while (carry != 0) {
            digits += carry % 10
            carry /= 10
        }
    }
    var result = 0
    for (digit <- digits) {
        result += digit
    }
    result
}
