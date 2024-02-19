# Python

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

# Start translation now

# C++

string selfPowers(int n) {
    int digits[10] = {0};
    for (int i = 1; i <= n; i++) {
        int temp_digits[10] = {0};
        temp_digits[0] = 1;
        for (int j = 0; j < i; j++) {
            int carry = 0;
            for (int k = 0; k < 10; k++) {
                temp_digits[k] = temp_digits[k] * i + carry;
                carry = temp_digits[k] / 10;
                temp_digits[k] %= 10;
            }
        }
        for (int j = 0; j < 10; j++) {
            digits[j] += temp_digits[j];
            if (digits[j] >= 10) {
                digits[j] -= 10;
                if (j < 9) {
                    digits[j + 1] += 1;
                }
            }
        }
    }
    string result = "";
    for (int i = 9; i >= 0; i--) {
        result += to_string(digits[i]);
    }
    return result;
}

# C#

class Global {
    public static string SelfPowers(int n) {
        int[] digits = new int[10];
        for (int i = 1; i <= n; i++) {
            int[] tempDigits = new int[10];
            tempDigits[0] = 1;
            for (int j = 0; j < i; j++) {
                int carry = 0;
                for (int k = 0; k < 10; k++) {
                    tempDigits[k] = tempDigits[k] * i + carry;
                    carry = tempDigits[k] / 10;
                    tempDigits[k] %= 10;
                }
            }
            for (int j = 0; j < 10; j++) {
                digits[j] += tempDigits[j];
                if (digits[j] >= 10) {
                    digits[j] -= 10;
                    if (j < 9) {
                        digits[j + 1] += 1;
                    }
                }
            }
        }
        string result = "";
        for (int i = 9; i >= 0; i--) {
            result += digits[i].ToString();
        }
        return result;
    }
}

# Go

func SelfPowers(n int) string {
    digits := [10]int{}
    for i := 1; i <= n; i++ {
        tempDigits := [10]int{}
        tempDigits[0] = 1
        for j := 0; j < i; j++ {
            carry := 0
            for k := 0; k < 10; k++ {
                tempDigits[k] = tempDigits[k] * i + carry
                carry = tempDigits[k] / 10
                tempDigits[k] %= 10
            }
        }
        for j := 0; j < 10; j++ {
            digits[j] += tempDigits[j]
            if digits[j] >= 10 {
                digits[j] -= 10
                if j < 9 {
                    digits[j + 1] += 1
                }
            }
        }
    }
    result := ""
    for i := 9; i >= 0; i-- {
        result += strconv.Itoa(digits[i])
    }
    return result
}

# Java

class Global {
    public static String selfPowers(int n) {
        int[] digits = new int[10];
        for (int i = 1; i <= n; i++) {
            int[] tempDigits = new int[10];
            tempDigits[0] = 1;
            for (int j = 0; j < i; j++) {
                int carry = 0;
                for (int k = 0; k < 10; k++) {
                    tempDigits[k] = tempDigits[k] * i + carry;
                    carry = tempDigits[k] / 10;
                    tempDigits[k] %= 10;
                }
            }
            for (int j = 0; j < 10; j++) {
                digits[j] += tempDigits[j];
                if (digits[j] >= 10) {
                    digits[j] -= 10;
                    if (j < 9) {
                        digits[j + 1] += 1;
                    }
                }
            }
        }
        String result = "";
        for (int i = 9; i >= 0; i--) {
            result += Integer.toString(digits[i]);
        }
        return result;
    }
}

# JavaScript

const selfPowers = (n) => {
    const digits = new Array(10).fill(0);
    for (let i = 1; i <= n; i++) {
        const tempDigits = new Array(10).fill(0);
        tempDigits[0] = 1;
        for (let j = 0; j < i; j++) {
            let carry = 0;
            for (let k = 0; k < 10; k++) {
                tempDigits[k] = tempDigits[k] * i + carry;
                carry = Math.floor(tempDigits[k] / 10);
                tempDigits[k] %= 10;
            }
        }
        for (let j = 0; j < 10; j++) {
            digits[j] += tempDigits[j];
            if (digits[j] >= 10) {
                digits[j] -= 10;
                if (j < 9) {
                    digits[j + 1] += 1;
                }
            }
        }
    }
    let result = "";
    for (let i = 9; i >= 0; i--) {
        result += digits[i].toString();
    }
    return result;
}

# Kotlin

fun selfPowers(n: Int): String {
    val digits = IntArray(10) { 0 }
    for (i in 1..n) {
        val tempDigits = IntArray(10) { 0 }
        tempDigits[0] = 1
        for (j in 0 until i) {
            var carry = 0
            for (k in 0 until 10) {
                tempDigits[k] = tempDigits[k] * i + carry
                carry = tempDigits[k] / 10
                tempDigits[k] %= 10
            }
        }
        for (j in 0 until 10) {
            digits[j] += tempDigits[j]
            if (digits[j] >= 10) {
                digits[j] -= 10
                if (j < 9) {
                    digits[j + 1] += 1
                }
            }
        }
    }
    var result = ""
    for (i in 9 downTo 0) {
        result += digits[i].toString()
    }
    return result
}

# PHP

function selfPowers($n) {
    $digits = array_fill(0, 10, 0);
    for ($i = 1; $i <= $n; $i++) {
        $tempDigits = array_fill(0, 10, 0);
        $tempDigits[0] = 1;
        for ($j = 0; $j < $i; $j++) {
            $carry = 0;
            for ($k = 0; $k < 10; $k++) {
                $tempDigits[$k] = $tempDigits[$k] * $i + $carry;
                $carry = intdiv($tempDigits[$k], 10);
                $tempDigits[$k] %= 10;
            }
        }
        for ($j = 0; $j < 10; $j++) {
            $digits[$j] += $tempDigits[$j];
            if ($digits[$j] >= 10) {
                $digits[$j] -= 10;
                if ($j < 9) {
                    $digits[$j + 1] += 1;
                }
            }
        }
    }
    $result = "";
    for ($i = 9; $i >= 0; $i--) {
        $result .= strval($digits[$i]);
    }
    return $result;
}

# Ruby

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

# Rust

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

# Scala

def selfPowers(n: Int): String = {
    val digits = Array.fill(10)(0)
    for (i <- 1 to n) {
        val tempDigits = Array.fill(10)(0)
        tempDigits(0) = 1
        for (j <- 0 until i) {
            var carry = 0
            for (k <- 0 until 10) {
                tempDigits(k) = tempDigits(k) * i + carry
                carry = tempDigits(k) / 10
                tempDigits(k) %= 10
            }
        }
        for (j <- 0 until 10) {
            digits(j) += tempDigits(j)
            if (digits(j) >= 10) {
                digits(j) -= 10
                if (j < 9) {
                    digits(j + 1) += 1
                }
            }
        }
    }
    var result = ""
    for (i <- 9 to 0 by -1) {
        result += digits(i).toString
    }
    result
}
