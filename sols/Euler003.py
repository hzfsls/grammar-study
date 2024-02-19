# Python

def largest_prime_factor(n: int) -> int:
    result = n
    i = 2
    while i * i <= result:
        if result % i:
            i += 1
        else:
            result //= i
    return result

# Start translation now

# C++

int largestPrimeFactor(int n) {
    int result = n;
    int i = 2;
    while (i * i <= result) {
        if (result % i) {
            i += 1;
        } else {
            result /= i;
        }
    }
    return result;
}

# C#

class Global {
    public static int LargestPrimeFactor(int n) {
        int result = n;
        int i = 2;
        while (i * i <= result) {
            if (result % i != 0) {
                i += 1;
            } else {
                result /= i;
            }
        }
        return result;
    }
}

# Go

func LargestPrimeFactor(n int) int {
    result := n
    i := 2
    for i * i <= result {
        if result % i != 0 {
            i += 1
        } else {
            result /= i
        }
    }
    return result
}

# Java

class Global {
    public static int largestPrimeFactor(int n) {
        int result = n;
        int i = 2;
        while (i * i <= result) {
            if (result % i != 0) {
                i += 1;
            } else {
                result /= i;
            }
        }
        return result;
    }
}

# JavaScript

const largestPrimeFactor = (n) => {
    let result = n;
    let i = 2;
    while (i * i <= result) {
        if (result % i != 0) {
            i += 1;
        } else {
            result /= i;
        }
    }
    return result;
}

# Kotlin

fun largestPrimeFactor(n: Int): Int {
    var result = n
    var i = 2
    while (i * i <= result) {
        if (result % i != 0) {
            i += 1
        } else {
            result /= i
        }
    }
    return result
}

# PHP

function largestPrimeFactor($n) {
    $result = $n;
    $i = 2;
    while ($i * $i <= $result) {
        if ($result % $i != 0) {
            $i += 1;
        } else {
            $result /= $i;
        }
    }
    return $result;
}

# Ruby

def largest_prime_factor(n)
    result = n
    i = 2
    while i * i <= result
        if result % i != 0
            i += 1
        else
            result /= i
        end
    end
    result
end

# Rust

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

# Scala

def largestPrimeFactor(n: Int): Int = {
    var result = n
    var i = 2
    while (i * i <= result) {
        if (result % i != 0) {
            i += 1
        } else {
            result /= i
        }
    }
    result
}



