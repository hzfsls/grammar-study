# Python

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def quadratic_primes(n: int) -> int:
    max_primes = 0
    result = 0
    for a in range(-n + 1, n, 2):
        for b in range(-n + 1, n, 2):
            x = 0
            while True:
                if x * x + a * x + b < 2:
                    break
                if not is_prime(x * x + a * x + b):
                    break
                x += 1
            if x > max_primes:
                max_primes = x
                result = a * b
    return result

# Start translation now

# C++

bool isPrime(int n) {
    if (n < 2) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (int i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int quadraticPrimes(int n) {
    int maxPrimes = 0;
    int result = 0;
    for (int a = -n + 1; a < n; a += 2) {
        for (int b = -n + 1; b < n; b += 2) {
            int x = 0;
            while (true) {
                if (x * x + a * x + b < 2) {
                    break;
                }
                if (!isPrime(x * x + a * x + b)) {
                    break;
                }
                x++;
            }
            if (x > maxPrimes) {
                maxPrimes = x;
                result = a * b;
            }
        }
    }
    return result;
}

# C#

class Global {
    public static bool IsPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= Math.Sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int QuadraticPrimes(int n) {
        int maxPrimes = 0;
        int result = 0;
        for (int a = -n + 1; a < n; a += 2) {
            for (int b = -n + 1; b < n; b += 2) {
                int x = 0;
                while (true) {
                    if (x * x + a * x + b < 2) {
                        break;
                    }
                    if (!IsPrime(x * x + a * x + b)) {
                        break;
                    }
                    x++;
                }
                if (x > maxPrimes) {
                    maxPrimes = x;
                    result = a * b;
                }
            }
        }
        return result;
    }
}

# Go

func IsPrime(n int) bool {
    if n < 2 {
        return false
    }
    if n == 2 {
        return true
    }
    if n % 2 == 0 {
        return false
    }
    for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func QuadraticPrimes(n int) int {
    maxPrimes := 0
    result := 0
    for a := -n + 1; a < n; a += 2 {
        for b := -n + 1; b < n; b += 2 {
            x := 0
            for {
                if x*x+a*x+b < 2 {
                    break
                }
                if !IsPrime(x*x+a*x+b) {
                    break
                }
                x++
            }
            if x > maxPrimes {
                maxPrimes = x
                result = a * b
            }
        }
    }
    return result
}

# Java

class Global {
    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int quadraticPrimes(int n) {
        int maxPrimes = 0;
        int result = 0;
        for (int a = -n + 1; a < n; a += 2) {
            for (int b = -n + 1; b < n; b += 2) {
                int x = 0;
                while (true) {
                    if (x * x + a * x + b < 2) {
                        break;
                    }
                    if (!isPrime(x * x + a * x + b)) {
                        break;
                    }
                    x++;
                }
                if (x > maxPrimes) {
                    maxPrimes = x;
                    result = a * b;
                }
            }
        }
        return result;
    }
}

# JavaScript

const isPrime = (n) => {
    if (n < 2) {
        return false;
    }
    if (n === 2) {
        return true;
    }
    if (n % 2 === 0) {
        return false;
    }
    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

const quadraticPrimes = (n) => {
    let maxPrimes = 0;
    let result = 0;
    for (let a = -n + 1; a < n; a += 2) {
        for (let b = -n + 1; b < n; b += 2) {
            let x = 0;
            while (true) {
                if (x * x + a * x + b < 2) {
                    break;
                }
                if (!isPrime(x * x + a * x + b)) {
                    break;
                }
                x++;
            }
            if (x > maxPrimes) {
                maxPrimes = x;
                result = a * b;
            }
        }
    }
    return result;
}

# Kotlin

fun isPrime(n: Int): Boolean {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i in 3..Math.sqrt(n.toDouble()).toInt() step 2) {
        if (n % i == 0) {
            return false
        }
    }
    return true
}

fun quadraticPrimes(n: Int): Int {
    var maxPrimes = 0
    var result = 0
    for (a in -n + 1 until n step 2) {
        for (b in -n + 1 until n step 2) {
            var x = 0
            while (true) {
                if (x * x + a * x + b < 2) {
                    break
                }
                if (!isPrime(x * x + a * x + b)) {
                    break
                }
                x++
            }
            if (x > maxPrimes) {
                maxPrimes = x
                result = a * b
            }
        }
    }
    return result
}

# PHP

function isPrime($n) {
    if ($n < 2) {
        return false;
    }
    if ($n == 2) {
        return true;
    }
    if ($n % 2 == 0) {
        return false;
    }
    for ($i = 3; $i <= sqrt($n); $i += 2) {
        if ($n % $i == 0) {
            return false;
        }
    }
    return true;
}

function quadraticPrimes($n) {
    $maxPrimes = 0;
    $result = 0;
    for ($a = -$n + 1; $a < $n; $a += 2) {
        for ($b = -$n + 1; $b < $n; $b += 2) {
            $x = 0;
            while (true) {
                if ($x * $x + $a * $x + $b < 2) {
                    break;
                }
                if (!isPrime($x * $x + $a * $x + $b)) {
                    break;
                }
                $x++;
            }
            if ($x > $maxPrimes) {
                $maxPrimes = $x;
                $result = $a * $b;
            }
        }
    }
    return $result;
}

# Ruby

def is_prime(n)
    if n < 2
        return false
    end
    if n == 2
        return true
    end
    if n % 2 == 0
        return false
    end
    (3..Math.sqrt(n)).step(2) do |i|
        if n % i == 0
            return false
        end
    end
    return true
end

def quadratic_primes(n)
    max_primes = 0
    result = 0
    (-n + 1...n).step(2) do |a|
        (-n + 1...n).step(2) do |b|
            x = 0
            while true
                if x * x + a * x + b < 2
                    break
                end
                if !is_prime(x * x + a * x + b)
                    break
                end
                x += 1
            end
            if x > max_primes
                max_primes = x
                result = a * b
            end
        end
    end
    result
end

# Rust

fn is_prime(n: i32) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    for i in 3..=(n as f64).sqrt() as i32 {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn quadratic_primes(n: i32) -> i32 {
    let mut max_primes = 0;
    let mut result = 0;
    for a in (-n + 1..n).step_by(2) {
        for b in (-n + 1..n).step_by(2) {
            let mut x = 0;
            while x * x + a * x + b >= 2 {
                if !is_prime(x * x + a * x + b) {
                    break;
                }
                x += 1;
            }
            if x > max_primes {
                max_primes = x;
                result = a * b;
            }
        }
    }
    result
}

# Scala

def isPrime(n: Int): Boolean = {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i <- 3 to Math.sqrt(n).toInt by 2) {
        if (n % i == 0) {
            return false
        }
    }
    true
}

def quadraticPrimes(n: Int): Int = {
    var maxPrimes = 0
    var result = 0
    for (a <- -n + 1 until n by 2) {
        for (b <- -n + 1 until n by 2) {
            var x = 0
            breakable {
                while (x * x + a * x + b >= 2) {
                    if (!isPrime(x * x + a * x + b)) {
                        break
                    }
                    x += 1
                }
            }
            if (x > maxPrimes) {
                maxPrimes = x
                result = a * b
            }
        }
    }
    result
}