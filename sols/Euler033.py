# Python

def digit_canceling_fractions(m: int) -> int:
    numer = 1
    denom = 1
    for d in range(10, m):
        for n in range(10, d):
            n0, n1 = n % 10, n // 10
            d0, d1 = d % 10, d // 10
            if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
                numer *= n
                denom *= d
    a, b = numer, denom
    while b:
        a, b = b, a % b
    return denom // a

# Start translation now

# C++

int digitCancelingFractions(int m) {
    int numer = 1;
    int denom = 1;
    for (int d = 10; d < m; d++) {
        for (int n = 10; n < d; n++) {
            int n0 = n % 10;
            int n1 = n / 10;
            int d0 = d % 10;
            int d1 = d / 10;
            if ((n1 == d0 && n0 * d == n * d1) || (n0 == d1 && n1 * d == n * d0)) {
                numer *= n;
                denom *= d;
            }
        }
    }
    int a = numer;
    int b = denom;
    while (b) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return denom / a;
}

# C#

class Global {
    public static int DigitCancelingFractions(int m) {
        int numer = 1;
        int denom = 1;
        for (int d = 10; d < m; d++) {
            for (int n = 10; n < d; n++) {
                int n0 = n % 10;
                int n1 = n / 10;
                int d0 = d % 10;
                int d1 = d / 10;
                if ((n1 == d0 && n0 * d == n * d1) || (n0 == d1 && n1 * d == n * d0)) {
                    numer *= n;
                    denom *= d;
                }
            }
        }
        int a = numer;
        int b = denom;
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return denom / a;
    }
}

# Go

func DigitCancelingFractions(m int) int {
    numer := 1
    denom := 1
    for d := 10; d < m; d++ {
        for n := 10; n < d; n++ {
            n0 := n % 10
            n1 := n / 10
            d0 := d % 10
            d1 := d / 10
            if (n1 == d0 && n0 * d == n * d1) || (n0 == d1 && n1 * d == n * d0) {
                numer *= n
                denom *= d
            }
        }
    }
    a := numer
    b := denom
    for b != 0 {
        temp := b
        b = a % b
        a = temp
    }
    return denom / a
}

# Java

class Global {
    public static int digitCancelingFractions(int m) {
        int numer = 1;
        int denom = 1;
        for (int d = 10; d < m; d++) {
            for (int n = 10; n < d; n++) {
                int n0 = n % 10;
                int n1 = n / 10;
                int d0 = d % 10;
                int d1 = d / 10;
                if ((n1 == d0 && n0 * d == n * d1) || (n0 == d1 && n1 * d == n * d0)) {
                    numer *= n;
                    denom *= d;
                }
            }
        }
        int a = numer;
        int b = denom;
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return denom / a;
    }
}

# JavaScript

const digitCancelingFractions = (m) => {
    let numer = 1;
    let denom = 1;
    for (let d = 10; d < m; d++) {
        for (let n = 10; n < d; n++) {
            let n0 = n % 10;
            let n1 = Math.floor(n / 10);
            let d0 = d % 10;
            let d1 = Math.floor(d / 10);
            if ((n1 === d0 && n0 * d === n * d1) || (n0 === d1 && n1 * d === n * d0)) {
                numer *= n;
                denom *= d;
            }
        }
    }
    let a = numer;
    let b = denom;
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return denom / a;
}

# Kotlin

fun digitCancelingFractions(m: Int): Int {
    var numer = 1
    var denom = 1
    for (d in 10 until m) {
        for (n in 10 until d) {
            val n0 = n % 10
            val n1 = n / 10
            val d0 = d % 10
            val d1 = d / 10
            if ((n1 == d0 && n0 * d == n * d1) || (n0 == d1 && n1 * d == n * d0)) {
                numer *= n
                denom *= d
            }
        }
    }
    var a = numer
    var b = denom
    while (b != 0) {
        val temp = b
        b = a % b
        a = temp
    }
    return denom / a
}

# PHP

function digitCancelingFractions($m) {
    $numer = 1;
    $denom = 1;
    for ($d = 10; $d < $m; $d++) {
        for ($n = 10; $n < $d; $n++) {
            $n0 = $n % 10;
            $n1 = intdiv($n, 10);
            $d0 = $d % 10;
            $d1 = intdiv($d, 10);
            if (($n1 == $d0 && $n0 * $d == $n * $d1) || ($n0 == $d1 && $n1 * $d == $n * $d0)) {
                $numer *= $n;
                $denom *= $d;
            }
        }
    }
    $a = $numer;
    $b = $denom;
    while ($b != 0) {
        $temp = $b;
        $b = $a % $b;
        $a = $temp;
    }
    return intdiv($denom, $a);
}

# Ruby

def digit_canceling_fractions(m)
    numer = 1
    denom = 1
    for d in 10...m
        for n in 10...d
            n0 = n % 10
            n1 = n / 10
            d0 = d % 10
            d1 = d / 10
            if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0)
                numer *= n
                denom *= d
            end
        end
    end
    a, b = numer, denom
    while b != 0
        a, b = b, a % b
    end
    return denom / a
end

# Rust

fn digit_canceling_fractions(m: i32) -> i32 {
    let mut numer = 1;
    let mut denom = 1;
    for d in 10..m {
        for n in 10..d {
            let n0 = n % 10;
            let n1 = n / 10;
            let d0 = d % 10;
            let d1 = d / 10;
            if (n1 == d0 && n0 * d == n * d1) || (n0 == d1 && n1 * d == n * d0) {
                numer *= n;
                denom *= d;
            }
        }
    }
    let mut a = numer;
    let mut b = denom;
    while b != 0 {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return denom / a;
}

# Scala

def digitCancelingFractions(m: Int): Int = {
    var numer = 1
    var denom = 1
    for (d <- 10 until m) {
        for (n <- 10 until d) {
            val n0 = n % 10
            val n1 = n / 10
            val d0 = d % 10
            val d1 = d / 10
            if ((n1 == d0 && n0 * d == n * d1) || (n0 == d1 && n1 * d == n * d0)) {
                numer *= n
                denom *= d
            }
        }
    }
    var a = numer
    var b = denom
    while (b != 0) {
        val temp = b
        b = a % b
        a = temp
    }
    denom / a
}
