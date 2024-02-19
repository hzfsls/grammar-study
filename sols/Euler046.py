# Python

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def goldbachs_other_conjecture(n: int) -> int:
    result = -1
    for i in range(9999, n, -2):
        upper = int((i // 2)** 0.5)
        flag = False
        for j in range(0, upper + 1):
            if is_prime(i - 2 * j ** 2):
                flag = True
                break
        if not flag:
            result = i
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

int goldbachsOtherConjecture(int n) {
    int result = -1;
    for (int i = 9999; i > n; i -= 2) {
        int upper = sqrt(i / 2);
        bool flag = false;
        for (int j = 0; j <= upper; j++) {
            if (isPrime(i - 2 * j * j)) {
                flag = true;
                break;
            }
        }
        if (!flag) {
            result = i;
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

    public static int GoldbachsOtherConjecture(int n) {
        int result = -1;
        for (int i = 9999; i > n; i -= 2) {
            int upper = (int)Math.Sqrt(i / 2);
            bool flag = false;
            for (int j = 0; j <= upper; j++) {
                if (IsPrime(i - 2 * j * j)) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                result = i;
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

func GoldbachsOtherConjecture(n int) int {
    result := -1
    for i := 9999; i > n; i -= 2 {
        upper := int(math.Sqrt(float64(i / 2)))
        flag := false
        for j := 0; j <= upper; j++ {
            if IsPrime(i - 2 * j * j) {
                flag = true
                break
            }
        }
        if !flag {
            result = i
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

    public static int goldbachsOtherConjecture(int n) {
        int result = -1;
        for (int i = 9999; i > n; i -= 2) {
            int upper = (int)Math.sqrt(i / 2);
            boolean flag = false;
            for (int j = 0; j <= upper; j++) {
                if (isPrime(i - 2 * j * j)) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                result = i;
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
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

const goldbachsOtherConjecture = (n) => {
    let result = -1;
    for (let i = 9999; i > n; i -= 2) {
        let upper = parseInt(Math.sqrt(i / 2));
        let flag = false;
        for (let j = 0; j <= upper; j++) {
            if (isPrime(i - 2 * j * j)) {
                flag = true;
                break;
            }
        }
        if (!flag) {
            result = i;
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

fun goldbachsOtherConjecture(n: Int): Int {
    var result = -1
    for (i in 9999 downTo n + 1 step 2) {
        val upper = Math.sqrt(i / 2.0).toInt()
        var flag = false
        for (j in 0..upper) {
            if (isPrime(i - 2 * j * j)) {
                flag = true
                break
            }
        }
        if (!flag) {
            result = i
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

function goldbachsOtherConjecture($n) {
    $result = -1;
    for ($i = 9999; $i > $n; $i -= 2) {
        $upper = sqrt($i / 2);
        $flag = false;
        for ($j = 0; $j <= $upper; $j++) {
            if (isPrime($i - 2 * $j * $j)) {
                $flag = true;
                break;
            }
        }
        if (!$flag) {
            $result = $i;
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
    for i in 3..Math.sqrt(n).to_i
        if n % i == 0
            return false
        end
    end
    return true
end

def goldbachs_other_conjecture(n)
    result = -1
    (9999...n).step(-2).each do |i|
        upper = Math.sqrt(i / 2).to_i
        flag = false
        for j in 0..upper
            if is_prime(i - 2 * j * j)
                flag = true
                break
            end
        end
        if !flag
            result = i
        end
    end
    return result
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
    return true;
}

fn goldbachs_other_conjecture(n: i32) -> i32 {
    let mut result = -1;
    for i in (n + 1..=9999).rev().step_by(2) {
        let upper = ((i / 2) as f64).sqrt() as i32;
        let mut flag = false;
        for j in 0..=upper {
            if is_prime(i - 2 * j * j) {
                flag = true;
                break;
            }
        }
        if !flag {
            result = i;
        }
    }
    return result;
}

# Scala

def isPrime(n: Int): Boolean = {
    if (n < 2) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (i <- 3 to Math.sqrt(n).toInt by 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

def goldbachsOtherConjecture(n: Int): Int = {
    var result = -1;
    for (i <- 9999 until n by -2) {
        val upper = Math.sqrt(i / 2).toInt;
        var flag = false;
        breakable {
            for (j <- 0 to upper) {
                if (isPrime(i - 2 * j * j)) {
                    flag = true;
                    break;
                }
            }
        }
        if (!flag) {
            result = i;
        }
    }
    return result;
}



