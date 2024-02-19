# Python

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

# Start translation now

# C++

int powerDigitSum(int n) {
    vector<int> digits = {2};
    for (int i = 1; i < n; i++) {
        int carry = 0;
        for (int j = 0; j < digits.size(); j++) {
            int temp = digits[j] * 2 + carry;
            digits[j] = temp % 10;
            carry = temp / 10;
        }
        if (carry) {
            digits.push_back(carry);
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
    public static int PowerDigitSum(int n) {
        List<int> digits = new List<int> {2};
        for (int i = 1; i < n; i++) {
            int carry = 0;
            for (int j = 0; j < digits.Count; j++) {
                int temp = digits[j] * 2 + carry;
                digits[j] = temp % 10;
                carry = temp / 10;
            }
            if (carry != 0) {
                digits.Add(carry);
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

func PowerDigitSum(n int) int {
    digits := []int{2}
    for i := 1; i < n; i++ {
        carry := 0
        for j := 0; j < len(digits); j++ {
            temp := digits[j]*2 + carry
            digits[j] = temp % 10
            carry = temp / 10
        }
        if carry != 0 {
            digits = append(digits, carry)
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
    public static int powerDigitSum(int n) {
        List<Integer> digits = new ArrayList<>(List.of(2));
        for (int i = 1; i < n; i++) {
            int carry = 0;
            for (int j = 0; j < digits.size(); j++) {
                int temp = digits.get(j) * 2 + carry;
                digits.set(j, temp % 10);
                carry = temp / 10;
            }
            if (carry != 0) {
                digits.add(carry);
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

const powerDigitSum = (n) => {
    let digits = [2];
    for (let i = 1; i < n; i++) {
        let carry = 0;
        for (let j = 0; j < digits.length; j++) {
            let temp = digits[j] * 2 + carry;
            digits[j] = temp % 10;
            carry = Math.floor(temp / 10);
        }
        if (carry !== 0) {
            digits.push(carry);
        }
    }
    let result = 0;
    for (let digit of digits) {
        result += digit;
    }
    return result;
}

# Kotlin

fun powerDigitSum(n: Int): Int {
    val digits = mutableListOf(2)
    for (i in 1 until n) {
        var carry = 0
        for (j in digits.indices) {
            var temp = digits[j] * 2 + carry
            digits[j] = temp % 10
            carry = temp / 10
        }
        if (carry != 0) {
            digits.add(carry)
        }
    }
    var result = 0
    for (digit in digits) {
        result += digit
    }
    return result
}

# PHP

function powerDigitSum($n) {
    $digits = [2];
    for ($i = 1; $i < $n; $i++) {
        $carry = 0;
        for ($j = 0; $j < count($digits); $j++) {
            $temp = $digits[$j] * 2 + $carry;
            $digits[$j] = $temp % 10;
            $carry = intdiv($temp, 10);
        }
        if ($carry !== 0) {
            array_push($digits, $carry);
        }
    }
    $result = 0;
    foreach ($digits as $digit) {
        $result += $digit;
    }
    return $result;
}

# Ruby

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

# Rust

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

# Scala

def powerDigitSum(n: Int): Int = {
    var digits = ArrayBuffer(2)
    for (i <- 1 until n) {
        var carry = 0
        for (j <- digits.indices) {
            val temp = digits(j) * 2 + carry
            digits(j) = temp % 10
            carry = temp / 10
        }
        if (carry != 0) {
            digits += carry
        }
    }
    var result = 0
    for (digit <- digits) {
        result += digit
    }
    result
}


