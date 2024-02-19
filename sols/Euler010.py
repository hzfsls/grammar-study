# Python

def summation_of_primes(n: int) -> int:
    primes = [2]
    i = 3
    while i <= n:
        for p in primes:
            if i % p == 0:
                break
            if p * p > i:
                primes.append(i)
                break
        i += 2
    result = 0
    for prime in primes:
        result += prime
    return result

# Start translation now

# C++

int summationOfPrimes(int n) {
    vector<int> primes = {2};
    int i = 3;
    while (i <= n) {
        for (int p : primes) {
            if (i % p == 0) {
                break;
            }
            if (p * p > i) {
                primes.push_back(i);
                break;
            }
        }
        i += 2;
    }
    int result = 0;
    for (int prime : primes) {
        result += prime;
    }
    return result;
}

# C#

class Global {
    public static int SummationOfPrimes(int n) {
        List<int> primes = new List<int> {2};
        int i = 3;
        while (i <= n) {
            foreach (int p in primes) {
                if (i % p == 0) {
                    break;
                }
                if (p * p > i) {
                    primes.Add(i);
                    break;
                }
            }
            i += 2;
        }
        int result = 0;
        foreach (int prime in primes) {
            result += prime;
        }
        return result;
    }
}

# Go

func SummationOfPrimes(n int) int {
    primes := []int{2}
    i := 3
    for i <= n {
        for _, p := range primes {
            if i % p == 0 {
                break
            }
            if p * p > i {
                primes = append(primes, i)
                break
            }
        }
        i += 2
    }
    result := 0
    for _, prime := range primes {
        result += prime
    }
    return result
}

# Java

class Global {
    public static int summationOfPrimes(int n) {
        List<Integer> primes = new ArrayList<Integer>();
        primes.add(2);
        int i = 3;
        while (i <= n) {
            for (int p : primes) {
                if (i % p == 0) {
                    break;
                }
                if (p * p > i) {
                    primes.add(i);
                    break;
                }
            }
            i += 2;
        }
        int result = 0;
        for (int prime : primes) {
            result += prime;
        }
        return result;
    }
}

# JavaScript

const summationOfPrimes = (n) => {
    const primes = [2];
    let i = 3;
    while (i <= n) {
        for (let p of primes) {
            if (i % p === 0) {
                break;
            }
            if (p * p > i) {
                primes.push(i);
                break;
            }
        }
        i += 2;
    }
    let result = 0;
    for (let prime of primes) {
        result += prime;
    }
    return result;
}

# Kotlin

fun summationOfPrimes(n: Int): Int {
    val primes = mutableListOf(2)
    var i = 3
    while (i <= n) {
        for (p in primes) {
            if (i % p == 0) {
                break
            }
            if (p * p > i) {
                primes.add(i)
                break
            }
        }
        i += 2
    }
    var result = 0
    for (prime in primes) {
        result += prime
    }
    return result
}

# PHP

function summationOfPrimes($n) {
    $primes = [2];
    $i = 3;
    while ($i <= $n) {
        foreach ($primes as $p) {
            if ($i % $p == 0) {
                break;
            }
            if ($p * $p > $i) {
                $primes[] = $i;
                break;
            }
        }
        $i += 2;
    }
    $result = 0;
    foreach ($primes as $prime) {
        $result += $prime;
    }
    return $result;
}

# Ruby

def summation_of_primes(n)
    primes = [2]
    i = 3
    while i <= n
        primes.each do |p|
            if i % p == 0
                break
            end
            if p * p > i
                primes.push(i)
                break
            end
        end
        i += 2
    end
    result = 0
    primes.each do |prime|
        result += prime
    end
    return result
end

# Rust

fn summation_of_primes(n: i32) -> i32 {
    let mut primes = vec![2];
    let mut i = 3;
    while i <= n {
        for p in &primes {
            if i % p == 0 {
                break;
            }
            if p * p > i {
                primes.push(i);
                break;
            }
        }
        i += 2;
    }
    let mut result = 0;
    for prime in &primes {
        result += prime;
    }
    result
}

# Scala

def summationOfPrimes(n: Int): Int = {
    var primes = ArrayBuffer(2)
    var i = 3
    while (i <= n) {
        var isPrime = true
        breakable {
            for (p <- primes) {
                if (i % p == 0) {
                    isPrime = false
                    break
                }
                if (p * p > i) {
                    break
                }
            }
        }
        if (isPrime) {
            primes += i
        }
        i += 2
    }
    var result = 0
    for (prime <- primes) {
        result += prime
    }
    result
}