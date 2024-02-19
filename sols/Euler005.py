# Python

def smallest_multiple(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        if result % i != 0:
            for j in range(1, n + 1):
                if (result * j) % i == 0:
                    result *= j
                    break
    return result

# Start translation now

# C++

int smallestMultiple(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        if (result % i != 0) {
            for (int j = 1; j <= n; j++) {
                if ((result * j) % i == 0) {
                    result *= j;
                    break;
                }
            }
        }
    }
    return result;
}

# C#

class Global {
    public static int SmallestMultiple(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            if (result % i != 0) {
                for (int j = 1; j <= n; j++) {
                    if ((result * j) % i == 0) {
                        result *= j;
                        break;
                    }
                }
            }
        }
        return result;
    }
}

# Go

func SmallestMultiple(n int) int {
    result := 1
    for i := 1; i <= n; i++ {
        if result % i != 0 {
            for j := 1; j <= n; j++ {
                if (result * j) % i == 0 {
                    result *= j
                    break
                }
            }
        }
    }
    return result
}

# Java

class Global {
    public static int smallestMultiple(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            if (result % i != 0) {
                for (int j = 1; j <= n; j++) {
                    if ((result * j) % i == 0) {
                        result *= j;
                        break;
                    }
                }
            }
        }
        return result;
    }
}

# JavaScript

const smallestMultiple = (n) => {
    let result = 1;
    for (let i = 1; i <= n; i++) {
        if (result % i != 0) {
            for (let j = 1; j <= n; j++) {
                if ((result * j) % i == 0) {
                    result *= j;
                    break;
                }
            }
        }
    }
    return result;
}

# Kotlin

fun smallestMultiple(n: Int): Int {
    var result = 1
    for (i in 1..n) {
        if (result % i != 0) {
            for (j in 1..n) {
                if ((result * j) % i == 0) {
                    result *= j
                    break
                }
            }
        }
    }
    return result
}

# PHP

function smallestMultiple($n) {
    $result = 1;
    for ($i = 1; $i <= $n; $i++) {
        if ($result % $i != 0) {
            for ($j = 1; $j <= $n; $j++) {
                if (($result * $j) % $i == 0) {
                    $result *= $j;
                    break;
                }
            }
        }
    }
    return $result;
}

# Ruby

def smallest_multiple(n)
    result = 1
    (1..n).each do |i|
        if result % i != 0
            (1..n).each do |j|
                if (result * j) % i == 0
                    result *= j
                    break
                end
            end
        end
    end
    result
end

# Rust

fn smallest_multiple(n: i32) -> i32 {
    let mut result = 1;
    for i in 1..=n {
        if result % i != 0 {
            for j in 1..=n {
                if (result * j) % i == 0 {
                    result *= j;
                    break;
                }
            }
        }
    }
    result
}

# Scala

def smallestMultiple(n: Int): Int = {
    var result = 1
    for (i <- 1 to n) {
        if (result % i != 0) {
            breakable {
                for (j <- 1 to n) {
                    if ((result * j) % i == 0) {
                        result *= j
                        break
                    }
                }
            }
        }
    }
    result
}

