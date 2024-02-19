# Python

def prime_factors(n: int) -> int:
    num = n
    factors = []
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return len(set(factors))

def distinct_primes_factors(n: int) -> int:
    for i in range(n, 1000000):
        if prime_factors(i) == 4 and prime_factors(i + 1) == 4 and prime_factors(i + 2) == 4 and prime_factors(i + 3) == 4:
            return i
    return -1

# Start translation now

# C++

int primeFactors(int n) {
    int num = n;
    vector<int> factors;
    int i = 2;
    while (i * i <= num) {
        if (num % i) {
            i++;
        } else {
            num /= i;
            factors.push_back(i);
        }
    }
    if (num > 1) {
        factors.push_back(num);
    }
    unordered_set<int> s(factors.begin(), factors.end());
    return s.size();
}

int distinctPrimesFactors(int n) {
    for (int i = n; i < 1000000; i++) {
        if (primeFactors(i) == 4 && primeFactors(i + 1) == 4 && primeFactors(i + 2) == 4 && primeFactors(i + 3) == 4) {
            return i;
        }
    }
    return -1;
}

# C#

class Global {
    public static int PrimeFactors(int n) {
        int num = n;
        List<int> factors = new List<int>();
        int i = 2;
        while (i * i <= num) {
            if (num % i != 0) {
                i++;
            } else {
                num /= i;
                factors.Add(i);
            }
        }
        if (num > 1) {
            factors.Add(num);
        }
        return factors.Distinct().Count();
    }

    public static int DistinctPrimesFactors(int n) {
        for (int i = n; i < 1000000; i++) {
            if (PrimeFactors(i) == 4 && PrimeFactors(i + 1) == 4 && PrimeFactors(i + 2) == 4 && PrimeFactors(i + 3) == 4) {
                return i;
            }
        }
        return -1;
    }
}

# Go

func PrimeFactors(n int) int {
    num := n
    factors := []int{}
    i := 2
    for i * i <= num {
        if num % i != 0 {
            i++
        } else {
            num /= i
            factors = append(factors, i)
        }
    }
    if num > 1 {
        factors = append(factors, num)
    }
    s := make(map[int]bool)
    for _, v := range factors {
        s[v] = true
    }
    return len(s)
}

func DistinctPrimesFactors(n int) int {
    for i := n; i < 1000000; i++ {
        if PrimeFactors(i) == 4 && PrimeFactors(i + 1) == 4 && PrimeFactors(i + 2) == 4 && PrimeFactors(i + 3) == 4 {
            return i
        }
    }
    return -1
}

# Java

class Global {
    public static int primeFactors(int n) {
        int num = n;
        List<Integer> factors = new ArrayList<Integer>();
        int i = 2;
        while (i * i <= num) {
            if (num % i != 0) {
                i++;
            } else {
                num /= i;
                factors.add(i);
            }
        }
        if (num > 1) {
            factors.add(num);
        }
        return new HashSet<Integer>(factors).size();
    }

    public static int distinctPrimesFactors(int n) {
        for (int i = n; i < 1000000; i++) {
            if (primeFactors(i) == 4 && primeFactors(i + 1) == 4 && primeFactors(i + 2) == 4 && primeFactors(i + 3) == 4) {
                return i;
            }
        }
        return -1;
    }
}

# JavaScript

const primeFactors = (n) => {
    let num = n;
    const factors = [];
    let i = 2;
    while (i * i <= num) {
        if (num % i != 0) {
            i++;
        } else {
            num /= i;
            factors.push(i);
        }
    }
    if (num > 1) {
        factors.push(num);
    }
    return new Set(factors).size;
}

const distinctPrimesFactors = (n) => {
    for (let i = n; i < 1000000; i++) {
        if (primeFactors(i) == 4 && primeFactors(i + 1) == 4 && primeFactors(i + 2) == 4 && primeFactors(i + 3) == 4) {
            return i;
        }
    }
    return -1;
}

# Kotlin

fun primeFactors(n: Int): Int {
    var num = n
    val factors = mutableListOf<Int>()
    var i = 2
    while (i * i <= num) {
        if (num % i != 0) {
            i++
        } else {
            num /= i
            factors.add(i)
        }
    }
    if (num > 1) {
        factors.add(num)
    }
    return factors.toSet().size
}

fun distinctPrimesFactors(n: Int): Int {
    for (i in n until 1000000) {
        if (primeFactors(i) == 4 && primeFactors(i + 1) == 4 && primeFactors(i + 2) == 4 && primeFactors(i + 3) == 4) {
            return i
        }
    }
    return -1
}

# PHP

function primeFactors($n) {
    $num = $n;
    $factors = [];
    $i = 2;
    while ($i * $i <= $num) {
        if ($num % $i != 0) {
            $i++;
        } else {
            $num /= $i;
            $factors[] = $i;
        }
    }
    if ($num > 1) {
        $factors[] = $num;
    }
    return count(array_unique($factors));
}

function distinctPrimesFactors($n) {
    for ($i = $n; $i < 1000000; $i++) {
        if (primeFactors($i) == 4 && primeFactors($i + 1) == 4 && primeFactors($i + 2) == 4 && primeFactors($i + 3) == 4) {
            return $i;
        }
    }
    return -1;
}

# Ruby

def prime_factors(n)
    num = n
    factors = []
    i = 2
    while i * i <= num
        if num % i != 0
            i += 1
        else
            num /= i
            factors.push(i)
        end
    end
    if num > 1
        factors.push(num)
    end
    factors.uniq.length
end

def distinct_primes_factors(n)
    for i in n...1000000
        if prime_factors(i) == 4 && prime_factors(i + 1) == 4 && prime_factors(i + 2) == 4 && prime_factors(i + 3) == 4
            return i
        end
    end
    -1
end

# Rust

fn prime_factors(n: i32) -> i32 {
    let mut num = n;
    let mut factors = vec![];
    let mut i = 2;
    while i * i <= num {
        if num % i != 0 {
            i += 1;
        } else {
            num /= i;
            factors.push(i);
        }
    }
    if num > 1 {
        factors.push(num);
    }
    factors.into_iter().collect::<HashSet<_>>().len() as i32
}

fn distinct_primes_factors(n: i32) -> i32 {
    for i in n..1000000 {
        if prime_factors(i) == 4 && prime_factors(i + 1) == 4 && prime_factors(i + 2) == 4 && prime_factors(i + 3) == 4 {
            return i;
        }
    }
    -1
}

# Scala

def primeFactors(n: Int): Int = {
    var num = n
    val factors = ArrayBuffer[Int]()
    var i = 2
    while (i * i <= num) {
        if (num % i != 0) {
            i += 1
        } else {
            num /= i
            factors += i
        }
    }
    if (num > 1) {
        factors += num
    }
    factors.toSet.size
}

def distinctPrimesFactors(n: Int): Int = {
    for (i <- n until 1000000) {
        if (primeFactors(i) == 4 && primeFactors(i + 1) == 4 && primeFactors(i + 2) == 4 && primeFactors(i + 3) == 4) {
            return i
        }
    }
    -1
}
