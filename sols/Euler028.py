# Python

def number_spiral_diagonals(n: int) -> int:
    result = 1
    for i in range(3, n + 1, 2):
        result += 4 * i * i - 6 * i + 6
    return result

# Start translation now

# C++

int numberSpiralDiagonals(int n) {
    int result = 1;
    for (int i = 3; i <= n; i += 2) {
        result += 4 * i * i - 6 * i + 6;
    }
    return result;
}

# C#

class Global {
    public static int NumberSpiralDiagonals(int n) {
        int result = 1;
        for (int i = 3; i <= n; i += 2) {
            result += 4 * i * i - 6 * i + 6;
        }
        return result;
    }
}

# Go

func NumberSpiralDiagonals(n int) int {
    result := 1
    for i := 3; i <= n; i += 2 {
        result += 4 * i * i - 6 * i + 6
    }
    return result
}

# Java

class Global {
    public static int numberSpiralDiagonals(int n) {
        int result = 1;
        for (int i = 3; i <= n; i += 2) {
            result += 4 * i * i - 6 * i + 6;
        }
        return result;
    }
}

# JavaScript

const numberSpiralDiagonals = (n) => {
    let result = 1;
    for (let i = 3; i <= n; i += 2) {
        result += 4 * i * i - 6 * i + 6;
    }
    return result;
}

# Kotlin

fun numberSpiralDiagonals(n: Int): Int {
    var result = 1
    for (i in 3..n step 2) {
        result += 4 * i * i - 6 * i + 6
    }
    return result
}

# PHP

function numberSpiralDiagonals($n) {
    $result = 1;
    for ($i = 3; $i <= $n; $i += 2) {
        $result += 4 * $i * $i - 6 * $i + 6;
    }
    return $result;
}

# Ruby

def number_spiral_diagonals(n)
    result = 1
    (3..n).step(2) do |i|
        result += 4 * i * i - 6 * i + 6
    end
    result
end

# Rust

fn number_spiral_diagonals(n: i32) -> i32 {
    let mut result = 1;
    for i in (3..=n).step_by(2) {
        result += 4 * i * i - 6 * i + 6;
    }
    result
}

# Scala

def numberSpiralDiagonals(n: Int): Int = {
    var result = 1
    for (i <- 3 to n by 2) {
        result += 4 * i * i - 6 * i + 6
    }
    result
}


