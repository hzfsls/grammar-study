# Python

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

# Start translation now

# C++

bool isPalindrome(string s) {
    for (int i = 0; i < s.length() / 2; i++) {
        if (s[i] != s[s.length() - i - 1]) {
            return false;
        }
    }
    return true;
}

int largestPalindromeProduct(int n) {
    int result = 0;
    for (int i = 100; i < 1000; i++) {
        for (int j = i; j < 1000; j++) {
            int prod = i * j;
            if (isPalindrome(to_string(prod)) && prod > result && prod < n) {
                result = prod;
            }
        }
    }
    return result;
}

# C#

class Global {
    public static bool IsPalindrome(string s) {
        for (int i = 0; i < s.Length / 2; i++) {
            if (s[i] != s[s.Length - i - 1]) {
                return false;
            }
        }
        return true;
    }

    public static int LargestPalindromeProduct(int n) {
        int result = 0;
        for (int i = 100; i < 1000; i++) {
            for (int j = i; j < 1000; j++) {
                int prod = i * j;
                if (IsPalindrome(prod.ToString()) && prod > result && prod < n) {
                    result = prod;
                }
            }
        }
        return result;
    }
}

# Go

func IsPalindrome(s string) bool {
    for i := 0; i < len(s) / 2; i++ {
        if s[i] != s[len(s) - i - 1] {
            return false
        }
    }
    return true
}

func LargestPalindromeProduct(n int) int {
    result := 0
    for i := 100; i < 1000; i++ {
        for j := i; j < 1000; j++ {
            prod := i * j
            if IsPalindrome(strconv.Itoa(prod)) && prod > result && prod < n {
                result = prod
            }
        }
    }
    return result
}

# Java

class Global {
    public static boolean isPalindrome(String s) {
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }

    public static int largestPalindromeProduct(int n) {
        int result = 0;
        for (int i = 100; i < 1000; i++) {
            for (int j = i; j < 1000; j++) {
                int prod = i * j;
                if (isPalindrome(Integer.toString(prod)) && prod > result && prod < n) {
                    result = prod;
                }
            }
        }
        return result;
    }
}

# JavaScript

const isPalindrome = (s) => {
    for (let i = 0; i < s.length / 2; i++) {
        if (s[i] !== s[s.length - i - 1]) {
            return false;
        }
    }
    return true;
}

const largestPalindromeProduct = (n) => {
    let result = 0;
    for (let i = 100; i < 1000; i++) {
        for (let j = i; j < 1000; j++) {
            let prod = i * j;
            if (isPalindrome(prod.toString()) && prod > result && prod < n) {
                result = prod;
            }
        }
    }
    return result;
}

# Kotlin

fun isPalindrome(s: String): Boolean {
    for (i in 0 until s.length / 2) {
        if (s[i] != s[s.length - i - 1]) {
            return false
        }
    }
    return true
}

fun largestPalindromeProduct(n: Int): Int {
    var result = 0
    for (i in 100 until 1000) {
        for (j in i until 1000) {
            val prod = i * j
            if (isPalindrome(prod.toString()) && prod > result && prod < n) {
                result = prod
            }
        }
    }
    return result
}

# PHP

function isPalindrome($s) {
    for ($i = 0; $i < strlen($s) / 2; $i++) {
        if ($s[$i] !== $s[strlen($s) - $i - 1]) {
            return false;
        }
    }
    return true;
}

function largestPalindromeProduct($n) {
    $result = 0;
    for ($i = 100; $i < 1000; $i++) {
        for ($j = $i; $j < 1000; $j++) {
            $prod = $i * $j;
            if (isPalindrome((string)$prod) && $prod > $result && $prod < $n) {
                $result = $prod;
            }
        }
    }
    return $result;
}

# Ruby

def is_palindrome(s)
    (0...s.length / 2).each do |i|
        if s[i] != s[s.length - i - 1]
            return false
        end
    end
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
    return result
end

# Rust

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

# Scala

def isPalindrome(s: String): Boolean = {
    for (i <- 0 until s.length / 2) {
        if (s(i) != s(s.length - i - 1)) {
            return false
        }
    }
    true
}

def largestPalindromeProduct(n: Int): Int = {
    var result = 0
    for (i <- 100 until 1000) {
        for (j <- i until 1000) {
            val prod = i * j
            if (isPalindrome(prod.toString) && prod > result && prod < n) {
                result = prod
            }
        }
    }
    result
}


