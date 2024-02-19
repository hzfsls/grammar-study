# Python

def largest_product_in_a_series(s: str, k: int) -> int:
    result = 0
    for i in range(len(s) - k):
        product = 1
        for j in range(k):
            product *= int(s[i + j])
        result = max(result, product)
    return result

# Start translation now

# C++

int largestProductInASeries(const string& s, int k) {
    int result = 0;
    for (int i = 0; i < s.length() - k; i++) {
        int product = 1;
        for (int j = 0; j < k; j++) {
            product *= s[i + j] - '0';
        }
        result = max(result, product);
    }
    return result;
}

# C#

class Global {
    public static int LargestProductInASeries(string s, int k) {
        int result = 0;
        for (int i = 0; i < s.Length - k; i++) {
            int product = 1;
            for (int j = 0; j < k; j++) {
                product *= s[i + j] - '0';
            }
            result = Math.Max(result, product);
        }
        return result;
    }
}

# Go

func LargestProductInASeries(s string, k int) int {
    result := 0
    for i := 0; i < len(s) - k; i++ {
        product := 1
        for j := 0; j < k; j++ {
            product *= int(s[i + j] - '0')
        }
        result = max(result, product)
    }
    return result
}

# Java

class Global {
    public static int largestProductInASeries(String s, int k) {
        int result = 0;
        for (int i = 0; i < s.length() - k; i++) {
            int product = 1;
            for (int j = 0; j < k; j++) {
                product *= s.charAt(i + j) - '0';
            }
            result = Math.max(result, product);
        }
        return result;
    }
}

# JavaScript

const largestProductInASeries = (s, k) => {
    let result = 0;
    for (let i = 0; i < s.length - k; i++) {
        let product = 1;
        for (let j = 0; j < k; j++) {
            product *= parseInt(s[i + j]);
        }
        result = Math.max(result, product);
    }
    return result;
}

# Kotlin

fun largestProductInASeries(s: String, k: Int): Int {
    var result = 0
    for (i in 0 until s.length - k) {
        var product = 1
        for (j in 0 until k) {
            product *= s[i + j].digitToInt()
        }
        result = maxOf(result, product)
    }
    return result
}

# PHP

function largestProductInASeries($s, $k) {
    $result = 0;
    for ($i = 0; $i < strlen($s) - $k; $i++) {
        $product = 1;
        for ($j = 0; $j < $k; $j++) {
            $product *= intval($s[$i + $j]);
        }
        $result = max($result, $product);
    }
    return $result;
}

# Ruby

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

# Rust

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

# Scala

def largestProductInASeries(s: String, k: Int): Int = {
    var result = 0
    for (i <- 0 until s.length - k) {
        var product = 1
        for (j <- 0 until k) {
            product *= s(i + j).asDigit
        }
        result = result.max(product)
    }
    result
}