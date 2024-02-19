# Python

def nth_prime(n: int) -> int:
    primes = [2]
    i = 3
    while len(primes) < n:
        for p in primes:
            if i % p == 0:
                break
            if p * p > i:
                primes.append(i)
                break
        i += 2
    return primes[-1]

# Start translation now

# C++

int nthPrime(int n) {
    vector<int> primes = {2};
    int i = 3;
    while (primes.size() < n) {
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
    return primes.back();
}

# C#

class Global {
    public static int NthPrime(int n) {
        List<int> primes = new List<int> {2};
        int i = 3;
        while (primes.Count < n) {
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
        return primes.Last();
    }
}

# Go

func NthPrime(n int) int {
    primes := []int{2}
    i := 3
    for len(primes) < n {
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
    return primes[len(primes) - 1]
}

# Java

class Global {
    public static int nthPrime(int n) {
        List<Integer> primes = new ArrayList<>(Arrays.asList(2));
        int i = 3;
        while (primes.size() < n) {
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
        return primes.get(primes.size() - 1);
    }
}

# JavaScript

const nthPrime = (n) => {
    const primes = [2];
    let i = 3;
    while (primes.length < n) {
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
    return primes[primes.length - 1];
}

# Kotlin

fun nthPrime(n: Int): Int {
    val primes = mutableListOf(2)
    var i = 3
    while (primes.size < n) {
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
    return primes.last()
}

# PHP

function nthPrime($n) {
    $primes = [2];
    $i = 3;
    while (count($primes) < $n) {
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
    return end($primes);
}

# Ruby

def nth_prime(n)
    primes = [2]
    i = 3
    while primes.length < n
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
    primes.last
end

# Rust

fn nth_prime(n: i32) -> i32 {
    let mut primes = vec![2];
    let mut i = 3;
    while primes.len() < n as usize {
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
    primes[primes.len() - 1]
}

# Scala

def nthPrime(n: Int): Int = {
    var primes = ArrayBuffer(2)
    var i = 3
    while (primes.length < n) {
        breakable {
            for (p <- primes) {
                if (i % p == 0) {
                    break
                }
                if (p * p > i) {
                    primes += i
                    break
                }
            }
        }
        i += 2
    }
    primes.last
}


