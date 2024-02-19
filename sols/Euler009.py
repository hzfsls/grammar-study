# Python

def special_pythagorean_triplet(n: int) -> int:
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if a * a + b * b == c * c:
                return a * b * c
    return -1

# Start translation now

# C++

int specialPythagoreanTriplet(int n) {
    for (int a = 1; a < n; a++) {
        for (int b = a; b < n; b++) {
            int c = n - a - b;
            if (a * a + b * b == c * c) {
                return a * b * c;
            }
        }
    }
    return -1;
}

# C#

class Global {
    public static int SpecialPythagoreanTriplet(int n) {
        for (int a = 1; a < n; a++) {
            for (int b = a; b < n; b++) {
                int c = n - a - b;
                if (a * a + b * b == c * c) {
                    return a * b * c;
                }
            }
        }
        return -1;
    }
}

# Go

func SpecialPythagoreanTriplet(n int) int {
    for a := 1; a < n; a++ {
        for b := a; b < n; b++ {
            c := n - a - b
            if a * a + b * b == c * c {
                return a * b * c
            }
        }
    }
    return -1
}

# Java

class Global {
    public static int specialPythagoreanTriplet(int n) {
        for (int a = 1; a < n; a++) {
            for (int b = a; b < n; b++) {
                int c = n - a - b;
                if (a * a + b * b == c * c) {
                    return a * b * c;
                }
            }
        }
        return -1;
    }
}

# JavaScript

const specialPythagoreanTriplet = (n) => {
    for (let a = 1; a < n; a++) {
        for (let b = a; b < n; b++) {
            let c = n - a - b;
            if (a * a + b * b == c * c) {
                return a * b * c;
            }
        }
    }
    return -1;
}

# Kotlin

fun specialPythagoreanTriplet(n: Int): Int {
    for (a in 1 until n) {
        for (b in a until n) {
            val c = n - a - b
            if (a * a + b * b == c * c) {
                return a * b * c
            }
        }
    }
    return -1
}

# PHP

function specialPythagoreanTriplet($n) {
    for ($a = 1; $a < $n; $a++) {
        for ($b = $a; $b < $n; $b++) {
            $c = $n - $a - $b;
            if ($a * $a + $b * $b == $c * $c) {
                return $a * $b * $c;
            }
        }
    }
    return -1;
}

# Ruby

def special_pythagorean_triplet(n)
    (1...n).each do |a|
        (a...n).each do |b|
            c = n - a - b
            return a * b * c if a * a + b * b == c * c
        end
    end
end

# Rust

fn special_pythagorean_triplet(n: i32) -> i32 {
    for a in 1..n {
        for b in a..n {
            let c = n - a - b;
            if a * a + b * b == c * c {
                return a * b * c;
            }
        }
    }
    -1
}

# Scala

def specialPythagoreanTriplet(n: Int): Int = {
    for (a <- 1 until n) {
        for (b <- a until n) {
            val c = n - a - b
            if (a * a + b * b == c * c) {
                return a * b * c
            }
        }
    }
    -1
}

