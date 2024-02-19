# Python

def multiples_of_3_and_5(n: int) -> int:
    result = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

# Start translation now

# C++

int multiplesOf3And5(int n) {
    int result = 0;
    for (int i = 0; i < n; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            result += i;
        }
    }
    return result;
}

# C#

class Global {
    public static int MultiplesOf3And5(int n) {
        int result = 0;
        for (int i = 0; i < n; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                result += i;
            }
        }
        return result;
    }
}

# Go

func MultiplesOf3And5(n int) int {
    result := 0
    for i := 0; i < n; i++ {
        if i % 3 == 0 || i % 5 == 0 {
            result += i
        }
    }
    return result
}

# Java

class Global {
    public static int multiplesOf3And5(int n) {
        int result = 0;
        for (int i = 0; i < n; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                result += i;
            }
        }
        return result;
    }
}

# JavaScript

const multiplesOf3And5 = (n) => {
    let result = 0;
    for (let i = 0; i < n; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            result += i;
        }
    }
    return result;
}

# Kotlin

fun multiplesOf3And5(n: Int): Int {
    var result = 0
    for (i in 0 until n) {
        if (i % 3 == 0 || i % 5 == 0) {
            result += i
        }
    }
    return result
}

# PHP

function multiplesOf3And5($n) {
    $result = 0;
    for ($i = 0; $i < $n; $i++) {
        if ($i % 3 == 0 || $i % 5 == 0) {
            $result += $i;
        }
    }
    return $result;
}

# Ruby

def multiples_of_3_and_5(n)
    result = 0
    (0...n).each do |i|
        if i % 3 == 0 || i % 5 == 0
            result += i
        end
    end
    result
end

# Rust

fn multiples_of_3_and_5(n: i32) -> i32 {
    let mut result = 0;
    for i in 0..n {
        if i % 3 == 0 || i % 5 == 0 {
            result += i;
        }
    }
    result
}

# Scala

def multiplesOf3And5(n: Int): Int = {
    var result = 0
    for (i <- 0 until n) {
        if (i % 3 == 0 || i % 5 == 0) {
            result += i
        }
    }
    result
}


