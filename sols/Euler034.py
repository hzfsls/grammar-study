# Python

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

# Start translation now

# C++

int digitFactorials(int n) {
    int result = 0;
    for (int i = 3; i < n; i++) {
        int factSum = 0;
        for (char digit : to_string(i)) {
            int fact = 1;
            for (int j = 1; j <= digit - '0'; j++) {
                fact *= j;
            }
            factSum += fact;
        }
        if (i == factSum) {
            result += i;
        }
    }
    return result;
}

# C#

class Global {
    public static int DigitFactorials(int n) {
        int result = 0;
        for (int i = 3; i < n; i++) {
            int factSum = 0;
            foreach (char digit in i.ToString()) {
                int fact = 1;
                for (int j = 1; j <= digit - '0'; j++) {
                    fact *= j;
                }
                factSum += fact;
            }
            if (i == factSum) {
                result += i;
            }
        }
        return result;
    }
}

# Go

func DigitFactorials(n int) int {
    result := 0
    for i := 3; i < n; i++ {
        factSum := 0
        for _, digit := range strconv.Itoa(i) {
            fact := 1
            for j := 1; j <= int(digit - '0'); j++ {
                fact *= j
            }
            factSum += fact
        }
        if i == factSum {
            result += i
        }
    }
    return result
}

# Java

class Global {
    public static int digitFactorials(int n) {
        int result = 0;
        for (int i = 3; i < n; i++) {
            int factSum = 0;
            for (char digit : Integer.toString(i).toCharArray()) {
                int fact = 1;
                for (int j = 1; j <= digit - '0'; j++) {
                    fact *= j;
                }
                factSum += fact;
            }
            if (i == factSum) {
                result += i;
            }
        }
        return result;
    }
}

# JavaScript

const digitFactorials = (n) => {
    let result = 0;
    for (let i = 3; i < n; i++) {
        let factSum = 0;
        for (let digit of i.toString()) {
            let fact = 1;
            for (let j = 1; j <= parseInt(digit); j++) {
                fact *= j;
            }
            factSum += fact;
        }
        if (i === factSum) {
            result += i;
        }
    }
    return result;
}

# Kotlin

fun digitFactorials(n: Int): Int {
    var result = 0
    for (i in 3 until n) {
        var factSum = 0
        for (digit in i.toString()) {
            var fact = 1
            for (j in 1..digit.toInt() - '0'.toInt()) {
                fact *= j
            }
            factSum += fact
        }
        if (i == factSum) {
            result += i
        }
    }
    return result
}

# PHP

function digitFactorials($n) {
    $result = 0;
    for ($i = 3; $i < $n; $i++) {
        $factSum = 0;
        foreach (str_split(strval($i)) as $digit) {
            $fact = 1;
            for ($j = 1; $j <= intval($digit); $j++) {
                $fact *= $j;
            }
            $factSum += $fact;
        }
        if ($i == $factSum) {
            $result += $i;
        }
    }
    return $result;
}

# Ruby

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

# Rust

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

# Scala

def digitFactorials(n: Int): Int = {
    var result = 0
    for (i <- 3 until n) {
        var factSum = 0
        for (digit <- i.toString) {
            var fact = 1
            for (j <- 1 to digit.asDigit) {
                fact *= j
            }
            factSum += fact
        }
        if (i == factSum) {
            result += i
        }
    }
    result
}


