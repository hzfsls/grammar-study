# Python

def digit_nth_powers(n: int) -> int:
    result = 0
    for i in range(2, 4 * 10 ** n):
        digits_sum = 0
        for digit in str(i):
            digits_sum += int(digit) ** n
        if i == digits_sum:
            result += i
    return result

# Start translation now

# C++

int digitNthPowers(int n) {
    int result = 0;
    for (int i = 2; i < 4 * pow(10, n); i++) {
        int digit_sum = 0;
        for (char digit : to_string(i)) {
            digit_sum += pow(digit - '0', n);
        }
        if (i == digit_sum) {
            result += i;
        }
    }
    return result;
}

# C#

class Global {
    public static int DigitNthPowers(int n) {
        int result = 0;
        for (int i = 2; i < 4 * Math.Pow(10, n); i++) {
            int digitsSum = 0;
            foreach (char digit in i.ToString()) {
                digitsSum += (int)Math.Pow(digit - '0', n);
            }
            if (i == digitsSum) {
                result += i;
            }
        }
        return result;
    }
}

# Go

func DigitNthPowers(n int) int {
    result := 0
    for i := 2; i < 4 * int(math.Pow(10, float64(n))); i++ {
        digitsSum := 0
        for _, digit := range strconv.Itoa(i) {
            digitInt, _ := strconv.Atoi(string(digit))
            digitsSum += int(math.Pow(float64(digitInt), float64(n)))
        }
        if i == digitsSum {
            result += i
        }
    }
    return result
}

# Java

class Global {
    public static int digitNthPowers(int n) {
        int result = 0;
        for (int i = 2; i < 4 * Math.pow(10, n); i++) {
            int digitsSum = 0;
            for (char digit : String.valueOf(i).toCharArray()) {
                digitsSum += Math.pow(digit - '0', n);
            }
            if (i == digitsSum) {
                result += i;
            }
        }
        return result;
    }
}

# JavaScript

const digitNthPowers = (n) => {
    let result = 0;
    for (let i = 2; i < 4 * 10 ** n; i++) {
        let digitsSum = 0;
        for (const digit of i.toString()) {
            digitsSum += parseInt(digit) ** n;
        }
        if (i === digitsSum) {
            result += i;
        }
    }
    return result;
}

# Kotlin

fun digitNthPowers(n: Int): Int {
    var result = 0
    for (i in 2 until 4 * 10.0.pow(n).toInt()) {
        var digitsSum = 0
        for (digit in i.toString()) {
            digitsSum += digit.digitToInt().toDouble().pow(n).toInt()
        }
        if (i == digitsSum) {
            result += i
        }
    }
    return result
}

# PHP

function digitNthPowers($n) {
    $result = 0;
    for ($i = 2; $i < 4 * pow(10, $n); $i++) {
        $digitsSum = 0;
        foreach (str_split(strval($i)) as $digit) {
            $digitsSum += pow($digit, $n);
        }
        if ($i == $digitsSum) {
            $result += $i;
        }
    }
    return $result;
}

# Ruby

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

# Rust

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

# Scala

def digitNthPowers(n: Int): Int = {
    var result = 0
    for (i <- 2 until 4 * math.pow(10, n).toInt) {
        var digitsSum = 0
        for (digit <- i.toString) {
            digitsSum += math.pow(digit.asDigit, n).toInt
        }
        if (i == digitsSum) {
            result += i
        }
    }
    result
}


