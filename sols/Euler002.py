# Python

def even_fibonacci_numbers(n: int) -> int:
    result = 0
    a = 1
    b = 2
    while a < n:
        if a % 2 == 0:
            result += a
        tmp = a
        a = b
        b = tmp + b
    return result

# Start translation now

# C++

int evenFibonacciNumbers(int n) {
    int result = 0;
    int a = 1;
    int b = 2;
    while (a < n) {
        if (a % 2 == 0) {
            result += a;
        }
        int tmp = a;
        a = b;
        b = tmp + b;
    }
    return result;
}

# C#

class Global {
    public static int EvenFibonacciNumbers(int n) {
        int result = 0;
        int a = 1;
        int b = 2;
        while (a < n) {
            if (a % 2 == 0) {
                result += a;
            }
            int tmp = a;
            a = b;
            b = tmp + b;
        }
        return result;
    }
}

# Go

func EvenFibonacciNumbers(n int) int {
    result := 0
    a := 1
    b := 2
    for a < n {
        if a % 2 == 0 {
            result += a
        }
        tmp := a
        a = b
        b = tmp + b
    }
    return result
}

# Java

class Global {
    public static int evenFibonacciNumbers(int n) {
        int result = 0;
        int a = 1;
        int b = 2;
        while (a < n) {
            if (a % 2 == 0) {
                result += a;
            }
            int tmp = a;
            a = b;
            b = tmp + b;
        }
        return result;
    }
}

# JavaScript

const evenFibonacciNumbers = (n) => {
    let result = 0;
    let a = 1;
    let b = 2;
    while (a < n) {
        if (a % 2 == 0) {
            result += a;
        }
        const tmp = a;
        a = b;
        b = tmp + b;
    }
    return result;
}

# Kotlin

fun evenFibonacciNumbers(n: Int): Int {
    var result = 0
    var a = 1
    var b = 2
    while (a < n) {
        if (a % 2 == 0) {
            result += a
        }
        val tmp = a
        a = b
        b = tmp + b
    }
    return result
}

# PHP

function evenFibonacciNumbers($n) {
    $result = 0;
    $a = 1;
    $b = 2;
    while ($a < $n) {
        if ($a % 2 == 0) {
            $result += $a;
        }
        $tmp = $a;
        $a = $b;
        $b = $tmp + $b;
    }
    return $result;
}

# Ruby

def even_fibonacci_numbers(n)
    result = 0
    a = 1
    b = 2
    while a < n
        if a % 2 == 0
            result += a
        end
        tmp = a
        a = b
        b = tmp + b
    end
    result
end

# Rust

fn even_fibonacci_numbers(n: i32) -> i32 {
    let mut result = 0;
    let mut a = 1;
    let mut b = 2;
    while a < n {
        if a % 2 == 0 {
            result += a;
        }
        let tmp = a;
        a = b;
        b = tmp + b;
    }
    result
}

# Scala

def evenFibonacciNumbers(n: Int): Int = {
    var result = 0
    var a = 1
    var b = 2
    while (a < n) {
        if (a % 2 == 0) {
            result += a
        }
        val tmp = a
        a = b
        b = tmp + b
    }
    result
}