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

def truncatable_primes(n: int) -> int:
    result = 0
    for i in range(10, n):
        if is_prime(i):
            si = str(i)
            flag = True
            for j in range(1, len(si)):
                p1 = int(si[j:])
                p2 = int(si[:-j])
                if not is_prime(p1) or not is_prime(p2):
                    flag = False
                    break
            if flag:
                result += i
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

int truncatablePrimes(int n) {
    int result = 0;
    for (int i = 10; i < n; i++) {
        if (isPrime(i)) {
            string si = to_string(i);
            bool flag = true;
            for (int j = 1; j < si.size(); j++) {
                int p1 = stoi(si.substr(j));
                int p2 = stoi(si.substr(0, si.size() - j));
                if (!isPrime(p1) || !isPrime(p2)) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                result += i;
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

    public static int TruncatablePrimes(int n) {
        int result = 0;
        for (int i = 10; i < n; i++) {
            if (IsPrime(i)) {
                string si = i.ToString();
                bool flag = true;
                for (int j = 1; j < si.Length; j++) {
                    int p1 = int.Parse(si.Substring(j));
                    int p2 = int.Parse(si.Substring(0, si.Length - j));
                    if (!IsPrime(p1) || !IsPrime(p2)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    result += i;
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

func TruncatablePrimes(n int) int {
    result := 0
    for i := 10; i < n; i++ {
        if IsPrime(i) {
            si := strconv.Itoa(i)
            flag := true
            for j := 1; j < len(si); j++ {
                p1, _ := strconv.Atoi(si[j:])
                p2, _ := strconv.Atoi(si[:len(si) - j])
                if !IsPrime(p1) || !IsPrime(p2) {
                    flag = false
                    break
                }
            }
            if flag {
                result += i
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

    public static int truncatablePrimes(int n) {
        int result = 0;
        for (int i = 10; i < n; i++) {
            if (isPrime(i)) {
                String si = String.valueOf(i);
                boolean flag = true;
                for (int j = 1; j < si.length(); j++) {
                    int p1 = Integer.parseInt(si.substring(j));
                    int p2 = Integer.parseInt(si.substring(0, si.length() - j));
                    if (!isPrime(p1) || !isPrime(p2)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    result += i;
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

const truncatablePrimes = (n) => {
    let result = 0;
    for (let i = 10; i < n; i++) {
        if (isPrime(i)) {
            const si = i.toString();
            let flag = true;
            for (let j = 1; j < si.length; j++) {
                const p1 = parseInt(si.substring(j));
                const p2 = parseInt(si.substring(0, si.length - j));
                if (!isPrime(p1) || !isPrime(p2)) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                result += i;
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

fun truncatablePrimes(n: Int): Int {
    var result = 0
    for (i in 10 until n) {
        if (isPrime(i)) {
            val si = i.toString()
            var flag = true
            for (j in 1 until si.length) {
                val p1 = si.substring(j).toInt()
                val p2 = si.substring(0, si.length - j).toInt()
                if (!isPrime(p1) || !isPrime(p2)) {
                    flag = false
                    break
                }
            }
            if (flag) {
                result += i
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

function truncatablePrimes($n) {
    $result = 0;
    for ($i = 10; $i < $n; $i++) {
        if (isPrime($i)) {
            $si = strval($i);
            $flag = true;
            for ($j = 1; $j < strlen($si); $j++) {
                $p1 = intval(substr($si, $j));
                $p2 = intval(substr($si, 0, strlen($si) - $j));
                if (!isPrime($p1) || !isPrime($p2)) {
                    $flag = false;
                    break;
                }
            }
            if ($flag) {
                $result += $i;
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
    for i in 3..Math.sqrt(n).to_i
        if n % i == 0
            return false
        end
    end
    return true
end

def truncatable_primes(n)
    result = 0
    for i in 10...n
        if is_prime(i)
            si = i.to_s
            flag = true
            for j in 1...si.length
                p1 = si[j..-1].to_i
                p2 = si[0...-j].to_i
                if !is_prime(p1) || !is_prime(p2)
                    flag = false
                    break
                end
            end
            if flag
                result += i
            end
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

fn truncatable_primes(n: i32) -> i32 {
    let mut result = 0;
    for i in 10..n {
        if is_prime(i) {
            let si = i.to_string();
            let mut flag = true;
            for j in 1..si.len() {
                let p1 = si[j..].parse().unwrap();
                let p2 = si[..si.len() - j].parse().unwrap();
                if !is_prime(p1) || !is_prime(p2) {
                    flag = false;
                    break;
                }
            }
            if flag {
                result += i;
            }
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

def truncatablePrimes(n: Int): Int = {
    var result = 0;
    for (i <- 10 until n) {
        if (isPrime(i)) {
            val si = i.toString;
            var flag = true;
            breakable {
                for (j <- 1 until si.length) {
                    val p1 = si.substring(j).toInt;
                    val p2 = si.substring(0, si.length - j).toInt;
                    if (!isPrime(p1) || !isPrime(p2)) {
                        flag = false;
                        break;
                    }
                }
            }
            if (flag) {
                result += i;
            }
        }
    }
    return result;
}


