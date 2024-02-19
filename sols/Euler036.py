# Python

def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

def double_base_palindromes(n: int) -> int:
    result = 0
    for i in range(1, n):
        str_i = str(i)
        bin_i = str(bin(i)[2:])
        if is_palindrome(str_i) and is_palindrome(bin_i):
            result += i
    return result

# Start translation now

# C++

bool isPalindrome(const string& s) {
    for (int i = 0; i < s.size() / 2; i++) {
        if (s[i] != s[s.size() - (i + 1)]) {
            return false;
        }
    }
    return true;
}

int doubleBasePalindromes(int n) {
    int result = 0;
    for (int i = 1; i < n; i++) {
        string strI = to_string(i);
        string binI = bitset<32>(i).to_string();
        binI.erase(0, min(binI.find_first_not_of('0'), binI.size() - 1));
        if (isPalindrome(strI) && isPalindrome(binI)) {
            result += i;
        }
    }
    return result;
}

# C#

class Global {
    public static bool IsPalindrome(string s) {
        for (int i = 0; i < s.Length / 2; i++) {
            if (s[i] != s[s.Length - (i + 1)]) {
                return false;
            }
        }
        return true;
    }

    public static int DoubleBasePalindromes(int n) {
        int result = 0;
        for (int i = 1; i < n; i++) {
            string strI = i.ToString();
            string binI = Convert.ToString(i, 2);
            if (IsPalindrome(strI) && IsPalindrome(binI)) {
                result += i;
            }
        }
        return result;
    }
}

# Go

func IsPalindrome(s string) bool {
    for i := 0; i < len(s) / 2; i++ {
        if s[i] != s[len(s) - (i + 1)] {
            return false
        }
    }
    return true
}

func DoubleBasePalindromes(n int) int {
    result := 0
    for i := 1; i < n; i++ {
        strI := strconv.Itoa(i)
        binI := strconv.FormatInt(int64(i), 2)
        if IsPalindrome(strI) && IsPalindrome(binI) {
            result += i
        }
    }
    return result
}

# Java

class Global {
    public static boolean isPalindrome(String s) {
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - (i + 1))) {
                return false;
            }
        }
        return true;
    }

    public static int doubleBasePalindromes(int n) {
        int result = 0;
        for (int i = 1; i < n; i++) {
            String strI = Integer.toString(i);
            String binI = Integer.toBinaryString(i);
            if (isPalindrome(strI) && isPalindrome(binI)) {
                result += i;
            }
        }
        return result;
    }
}

# JavaScript

const isPalindrome = (s) => {
    for (let i = 0; i < s.length / 2; i++) {
        if (s[i] !== s[s.length - (i + 1)]) {
            return false;
        }
    }
    return true;
}

const doubleBasePalindromes = (n) => {
    let result = 0;
    for (let i = 1; i < n; i++) {
        const strI = i.toString();
        const binI = i.toString(2);
        if (isPalindrome(strI) && isPalindrome(binI)) {
            result += i;
        }
    }
    return result;
}

# Kotlin

fun isPalindrome(s: String): Boolean {
    for (i in 0 until s.length / 2) {
        if (s[i] != s[s.length - (i + 1)]) {
            return false
        }
    }
    return true
}

fun doubleBasePalindromes(n: Int): Int {
    var result = 0
    for (i in 1 until n) {
        val strI = i.toString()
        val binI = Integer.toBinaryString(i)
        if (isPalindrome(strI) && isPalindrome(binI)) {
            result += i
        }
    }
    return result
}

# PHP

function isPalindrome($s) {
    for ($i = 0; $i < strlen($s) / 2; $i++) {
        if ($s[$i] !== $s[strlen($s) - ($i + 1)]) {
            return false;
        }
    }
    return true;
}

function doubleBasePalindromes($n) {
    $result = 0;
    for ($i = 1; $i < $n; $i++) {
        $strI = strval($i);
        $binI = decbin($i);
        if (isPalindrome($strI) && isPalindrome($binI)) {
            $result += $i;
        }
    }
    return $result;
}

# Ruby

def is_palindrome(s)
    for i in 0...s.length / 2
        if s[i] != s[s.length - (i + 1)]
            return false
        end
    end
    true
end

def double_base_palindromes(n)
    result = 0
    for i in 1...n
        str_i = i.to_s
        bin_i = i.to_s(2)
        if is_palindrome(str_i) && is_palindrome(bin_i)
            result += i
        end
    end
    result
end

# Rust

fn is_palindrome(s: &String) -> bool {
    for i in 0..s.len() / 2 {
        if s.as_bytes()[i] != s.as_bytes()[s.len() - (i + 1)] {
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

# Scala

def isPalindrome(s: String): Boolean = {
    for (i <- 0 until s.length / 2) {
        if (s(i) != s(s.length - (i + 1))) {
            return false
        }
    }
    true
}

def doubleBasePalindromes(n: Int): Int = {
    var result = 0
    for (i <- 1 until n) {
        val strI = i.toString
        val binI = i.toBinaryString
        if (isPalindrome(strI) && isPalindrome(binI)) {
            result += i
        }
    }
    result
}


