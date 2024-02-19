# Python

def d(n: int) -> int:
    result = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            result += i
            if i != n // i:
                result += n // i
    return result

def amicable_numbers(n: int) -> int:
    result = 0
    for a in range(2, n):
        b = d(a)
        if a != b and a == d(b):
            result += a
    return result

# Start translation now

# C++

int d(int n) {
    int result = 1;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            result += i;
            if (i != n / i) {
                result += n / i;
            }
        }
    }
    return result;
}

int amicableNumbers(int n) {
    int result = 0;
    for (int a = 2; a < n; a++) {
        int b = d(a);
        if (a != b && a == d(b)) {
            result += a;
        }
    }
    return result;
}

# C#

class Global {
    public static int D(int n) {
        int result = 1;
        for (int i = 2; i <= Math.Sqrt(n); i++) {
            if (n % i == 0) {
                result += i;
                if (i != n / i) {
                    result += n / i;
                }
            }
        }
        return result;
    }

    public static int AmicableNumbers(int n) {
        int result = 0;
        for (int a = 2; a < n; a++) {
            int b = D(a);
            if (a != b && a == D(b)) {
                result += a;
            }
        }
        return result;
    }
}

# Go

func D(n int) int {
    result := 1
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            result += i
            if i != n / i {
                result += n / i
            }
        }
    }
    return result
}

func AmicableNumbers(n int) int {
    result := 0
    for a := 2; a < n; a++ {
        b := D(a)
        if a != b && a == D(b) {
            result += a
        }
    }
    return result
}

# Java

class Global {
    public static int d(int n) {
        int result = 1;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                result += i;
                if (i != n / i) {
                    result += n / i;
                }
            }
        }
        return result;
    }

    public static int amicableNumbers(int n) {
        int result = 0;
        for (int a = 2; a < n; a++) {
            int b = d(a);
            if (a != b && a == d(b)) {
                result += a;
            }
        }
        return result;
    }
}

# JavaScript

const d = (n) => {
    let result = 1;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            result += i;
            if (i !== n / i) {
                result += n / i;
            }
        }
    }
    return result;
}

const amicableNumbers = (n) => {
    let result = 0;
    for (let a = 2; a < n; a++) {
        let b = d(a);
        if (a !== b && a === d(b)) {
            result += a;
        }
    }
    return result;
}

# Kotlin

fun d(n: Int): Int {
    var result = 1
    for (i in 2..sqrt(n.toDouble()).toInt()) {
        if (n % i == 0) {
            result += i
            if (i != n / i) {
                result += n / i
            }
        }
    }
    return result
}

fun amicableNumbers(n: Int): Int {
    var result = 0
    for (a in 2 until n) {
        val b = d(a)
        if (a != b && a == d(b)) {
            result += a
        }
    }
    return result
}

# PHP

function d($n) {
    $result = 1;
    for ($i = 2; $i <= sqrt($n); $i++) {
        if ($n % $i == 0) {
            $result += $i;
            if ($i != $n / $i) {
                $result += $n / $i;
            }
        }
    }
    return $result;
}

function amicableNumbers($n) {
    $result = 0;
    for ($a = 2; $a < $n; $a++) {
        $b = d($a);
        if ($a != $b && $a == d($b)) {
            $result += $a;
        }
    }
    return $result;
}

# Ruby

def d(n)
    result = 1
    (2..Math.sqrt(n)).each do |i|
        if n % i == 0
            result += i
            result += n / i if i != n / i
        end
    end
    result
end

def amicable_numbers(n)
    result = 0
    (2...n).each do |a|
        b = d(a)
        result += a if a != b && a == d(b)
    end
    result
end

# Rust

fn d(n: i32) -> i32 {
    let mut result = 1;
    for i in 2..=(n as f64).sqrt() as i32 {
        if n % i == 0 {
            result += i;
            if i != n / i {
                result += n / i;
            }
        }
    }
    result
}

fn amicable_numbers(n: i32) -> i32 {
    let mut result = 0;
    for a in 2..n {
        let b = d(a);
        if a != b && a == d(b) {
            result += a;
        }
    }
    result
}

# Scala

def d(n: Int): Int = {
    var result = 1
    for (i <- 2 to math.sqrt(n).toInt) {
        if (n % i == 0) {
            result += i
            if (i != n / i) {
                result += n / i
            }
        }
    }
    result
}

def amicableNumbers(n: Int): Int = {
    var result = 0
    for (a <- 2 until n) {
        val b = d(a)
        if (a != b && a == d(b)) {
            result += a
        }
    }
    result
}



