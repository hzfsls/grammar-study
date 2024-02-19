# Python

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

# Start translation now

# C++

string largeSum(const vector<string>& numbers) {
    vector<int> digits(60, 0);
    for (int i = 0; i < 50; i++) {
        int tmp = 0;
        for (auto num : numbers) {
            tmp += num[49 - i] - '0';
        }
        for (int j = i; j < 60; j++) {
            digits[j] += tmp % 10;
            if (digits[j] >= 10) {
                digits[j + 1] += digits[j] / 10;
                digits[j] %= 10;
            }
            tmp /= 10;
            if (tmp == 0) {
                break;
            }
        }
    }
    for (int i = 59; i >= 0; i--) {
        if (digits[i] != 0) {
            string result;
            for (int j = i; j > i - 10; j--) {
                result += to_string(digits[j]);
            }
            return result;
        }
    }
    return "";
}

# C#

class Global {
    public static string LargeSum(IList<string> numbers) {
        int[] digits = new int[60];
        for (int i = 0; i < 50; i++) {
            int tmp = 0;
            foreach (var num in numbers) {
                tmp += num[49 - i] - '0';
            }
            for (int j = i; j < 60; j++) {
                digits[j] += tmp % 10;
                if (digits[j] >= 10) {
                    digits[j + 1] += digits[j] / 10;
                    digits[j] %= 10;
                }
                tmp /= 10;
                if (tmp == 0) {
                    break;
                }
            }
        }
        for (int i = 59; i >= 0; i--) {
            if (digits[i] != 0) {
                string result = "";
                for (int j = i; j > i - 10; j--) {
                    result += digits[j].ToString();
                }
                return result;
            }
        }
        return "";
    }
}

# Go

func LargeSum(numbers []string) string {
    digits := make([]int, 60)
    for i := 0; i < 50; i++ {
        tmp := 0
        for _, num := range numbers {
            tmp += int(num[49 - i] - '0')
        }
        for j := i; j < 60; j++ {
            digits[j] += tmp % 10
            if digits[j] >= 10 {
                digits[j + 1] += digits[j] / 10
                digits[j] %= 10
            }
            tmp /= 10
            if tmp == 0 {
                break
            }
        }
    }
    for i := 59; i >= 0; i-- {
        if digits[i] != 0 {
            result := ""
            for j := i; j > i - 10; j-- {
                result += strconv.Itoa(digits[j])
            }
            return result
        }
    }
    return ""
}

# Java

class Global {
    public static String largeSum(List<String> numbers) {
        int[] digits = new int[60];
        for (int i = 0; i < 50; i++) {
            int tmp = 0;
            for (String num : numbers) {
                tmp += num.charAt(49 - i) - '0';
            }
            for (int j = i; j < 60; j++) {
                digits[j] += tmp % 10;
                if (digits[j] >= 10) {
                    digits[j + 1] += digits[j] / 10;
                    digits[j] %= 10;
                }
                tmp /= 10;
                if (tmp == 0) {
                    break;
                }
            }
        }
        for (int i = 59; i >= 0; i--) {
            if (digits[i] != 0) {
                StringBuilder result = new StringBuilder();
                for (int j = i; j > i - 10; j--) {
                    result.append(digits[j]);
                }
                return result.toString();
            }
        }
        return "";
    }
}

# JavaScript

const largeSum = (numbers) => {
    const digits = Array(60).fill(0);
    for (let i = 0; i < 50; i++) {
        let tmp = 0;
        for (let num of numbers) {
            tmp += parseInt(num[49 - i]);
        }
        for (let j = i; j < 60; j++) {
            digits[j] += tmp % 10;
            if (digits[j] >= 10) {
                digits[j + 1] += Math.floor(digits[j] / 10);
                digits[j] %= 10;
            }
            tmp = Math.floor(tmp / 10);
            if (tmp == 0) {
                break;
            }
        }
    }
    for (let i = 59; i >= 0; i--) {
        if (digits[i] != 0) {
            let result = '';
            for (let j = i; j > i - 10; j--) {
                result += digits[j];
            }
            return result;
        }
    }
    return '';
}

# Kotlin

fun largeSum(numbers: List<String>): String {
    val digits = Array(60) { 0 }
    for (i in 0 until 50) {
        var tmp = 0
        for (num in numbers) {
            tmp += num[49 - i] - '0'
        }
        for (j in i until 60) {
            digits[j] += tmp % 10
            if (digits[j] >= 10) {
                digits[j + 1] += digits[j] / 10
                digits[j] %= 10
            }
            tmp /= 10
            if (tmp == 0) {
                break
            }
        }
    }
    for (i in 59 downTo 0) {
        if (digits[i] != 0) {
            val result = StringBuilder()
            for (j in i downTo i - 9) {
                result.append(digits[j])
            }
            return result.toString()
        }
    }
    return ""
}

# PHP

function largeSum($numbers) {
    $digits = array_fill(0, 60, 0);
    for ($i = 0; $i < 50; $i++) {
        $tmp = 0;
        foreach ($numbers as $num) {
            $tmp += (int)$num[49 - $i];
        }
        for ($j = $i; $j < 60; $j++) {
            $digits[$j] += $tmp % 10;
            if ($digits[$j] >= 10) {
                $digits[$j + 1] += intdiv($digits[$j], 10);
                $digits[$j] %= 10;
            }
            $tmp = intdiv($tmp, 10);
            if ($tmp == 0) {
                break;
            }
        }
    }
    for ($i = 59; $i >= 0; $i--) {
        if ($digits[$i] != 0) {
            $result = '';
            for ($j = $i; $j > $i - 10; $j--) {
                $result .= $digits[$j];
            }
            return $result;
        }
    }
    return '';
}

# Ruby

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

# Rust

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

# Scala

def largeSum(numbers: Seq[String]): String = {
    val digits = Array.fill(60)(0)
    for (i <- 0 until 50) {
        var tmp = 0
        for (num <- numbers) {
            tmp += num(49 - i).asDigit
        }
        breakable {
            for (j <- i until 60) {
                digits(j) += tmp % 10
                if (digits(j) >= 10) {
                    digits(j + 1) += digits(j) / 10
                    digits(j) %= 10
                }
                tmp /= 10
                if (tmp == 0) {
                    break
                }
            }
        }
    }
    for (i <- 59 to 0 by -1) {
        if (digits(i) != 0) {
            val result = new StringBuilder
            for (j <- i to i - 9 by -1) {
                result.append(digits(j))
            }
            return result.toString
        }
    }
    ""
}

