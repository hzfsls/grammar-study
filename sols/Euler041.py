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


def pandigital_prime(n: int) -> int:
    for i in range(n-1, 0, -1):
        if is_prime(i):
            si = str(i)
            length = len(si)
            flag = True
            for j in range(1, length + 1):
                if str(j) not in si:
                    flag = False
                    break
            if flag:
                return i
    return -1

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

int pandigitalPrime(int n) {
    for (int i = n - 1; i > 0; i--) {
        if (isPrime(i)) {
            string si = to_string(i);
            int length = si.length();
            bool flag = true;
            for (int j = 1; j <= length; j++) {
                if (si.find(to_string(j)) == string::npos) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                return i;
            }
        }
    }
    return -1;
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

    public static int PandigitalPrime(int n) {
        for (int i = n - 1; i > 0; i--) {
            if (IsPrime(i)) {
                string si = i.ToString();
                int length = si.Length;
                bool flag = true;
                for (int j = 1; j <= length; j++) {
                    if (!si.Contains(j.ToString())) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    return i;
                }
            }
        }
        return -1;
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

func PandigitalPrime(n int) int {
    for i := n - 1; i > 0; i-- {
        if IsPrime(i) {
            si := strconv.Itoa(i)
            length := len(si)
            flag := true
            for j := 1; j <= length; j++ {
                if !strings.Contains(si, strconv.Itoa(j)) {
                    flag = false
                    break
                }
            }
            if flag {
                return i
            }
        }
    }
    return -1
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

    public static int pandigitalPrime(int n) {
        for (int i = n - 1; i > 0; i--) {
            if (isPrime(i)) {
                String si = Integer.toString(i);
                int length = si.length();
                boolean flag = true;
                for (int j = 1; j <= length; j++) {
                    if (si.indexOf(Integer.toString(j)) == -1) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    return i;
                }
            }
        }
        return -1;
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

const pandigitalPrime = (n) => {
    for (let i = n - 1; i > 0; i--) {
        if (isPrime(i)) {
            let si = i.toString();
            let length = si.length;
            let flag = true;
            for (let j = 1; j <= length; j++) {
                if (!si.includes(j.toString())) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                return i;
            }
        }
    }
    return -1;
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
    for (i in 3..sqrt(n.toDouble()).toInt() step 2) {
        if (n % i == 0) {
            return false
        }
    }
    return true
}

fun pandigitalPrime(n: Int): Int {
    for (i in n - 1 downTo 1) {
        if (isPrime(i)) {
            val si = i.toString()
            val length = si.length
            var flag = true
            for (j in 1..length) {
                if (!si.contains(j.toString())) {
                    flag = false
                    break
                }
            }
            if (flag) {
                return i
            }
        }
    }
    return -1
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

function pandigitalPrime($n) {
    for ($i = $n - 1; $i > 0; $i--) {
        if (isPrime($i)) {
            $si = strval($i);
            $length = strlen($si);
            $flag = true;
            for ($j = 1; $j <= $length; $j++) {
                if (strpos($si, strval($j)) === false) {
                    $flag = false;
                    break;
                }
            }
            if ($flag) {
                return $i;
            }
        }
    }
    return -1;
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

def pandigital_prime(n)
    for i in (n - 1).downto(1)
        if is_prime(i)
            si = i.to_s
            length = si.length
            flag = true
            for j in 1..length
                if !si.include?(j.to_s)
                    flag = false
                    break
                end
            end
            if flag
                return i
            end
        end
    end
    return -1
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

fn pandigital_prime(n: i32) -> i32 {
    for i in (1..n).rev() {
        if is_prime(i) {
            let si = i.to_string();
            let length = si.len();
            let mut flag = true;
            for j in 1..=length {
                if !si.contains(&j.to_string()) {
                    flag = false;
                    break;
                }
            }
            if flag {
                return i;
            }
        }
    }
    return -1;
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
    for (i <- 3 to math.sqrt(n).toInt by 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

def pandigitalPrime(n: Int): Int = {
    for (i <- n - 1 to 1 by -1) {
        if (isPrime(i)) {
            val si = i.toString;
            val length = si.length;
            var flag = true;
            breakable {
                for (j <- 1 to length) {
                    if (!si.contains(j.toString)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    return i;
                }
            }
        }
    }
    return -1;
}