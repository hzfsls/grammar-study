# Python

def consecutive_prime_sum(limit: int) -> int:
    sieve = [True] * limit
    primes = []
    for i in range(2, limit):
        if sieve[i]:
            primes.append(i)
            for j in range(i * 2, limit, i):
                sieve[j] = False
    max_length = 0
    max_prime = 0
    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            s = sum(primes[i:j])
            if s >= limit:
                break
            if sieve[s] and j - i > max_length:
                max_length = j - i
                max_prime = s
    return max_prime

# Start translation now

# C++

int consecutivePrimeSum(int limit) {
    vector<bool> sieve(limit, true);
    vector<int> primes;
    for (int i = 2; i < limit; i++) {
        if (sieve[i]) {
            primes.push_back(i);
            for (int j = i * 2; j < limit; j += i) {
                sieve[j] = false;
            }
        }
    }
    int max_length = 0;
    int max_prime = 0;
    for (int i = 0; i < primes.size(); i++) {
        for (int j = i + max_length; j < primes.size(); j++) {
            int s = 0;
            for (int k = i; k < j; k++) {
                s += primes[k];
            }
            if (s >= limit) {
                break;
            }
            if (sieve[s] && j - i > max_length) {
                max_length = j - i;
                max_prime = s;
            }
        }
    }
    return max_prime;
}

# C#

class Global {
    public static int ConsecutivePrimeSum(int limit) {
        bool[] sieve = new bool[limit];
        Array.Fill(sieve, true);
        List<int> primes = new List<int>();
        for (int i = 2; i < limit; i++) {
            if (sieve[i]) {
                primes.Add(i);
                for (int j = i * 2; j < limit; j += i) {
                    sieve[j] = false;
                }
            }
        }
        int maxLength = 0;
        int maxPrime = 0;
        for (int i = 0; i < primes.Count; i++) {
            for (int j = i + maxLength; j < primes.Count; j++) {
                int s = 0;
                for (int k = i; k < j; k++) {
                    s += primes[k];
                }
                if (s >= limit) {
                    break;
                }
                if (sieve[s] && j - i > maxLength) {
                    maxLength = j - i;
                    maxPrime = s;
                }
            }
        }
        return maxPrime;
    }
}

# Go

func ConsecutivePrimeSum(limit int) int {
    sieve := make([]bool, limit)
    for i := range sieve {
        sieve[i] = true
    }
    primes := []int{}
    for i := 2; i < limit; i++ {
        if sieve[i] {
            primes = append(primes, i)
            for j := i * 2; j < limit; j += i {
                sieve[j] = false
            }
        }
    }
    maxLength := 0
    maxPrime := 0
    for i := 0; i < len(primes); i++ {
        for j := i + maxLength; j < len(primes); j++ {
            s := 0
            for k := i; k < j; k++ {
                s += primes[k]
            }
            if s >= limit {
                break
            }
            if sieve[s] && j - i > maxLength {
                maxLength = j - i
                maxPrime = s
            }
        }
    }
    return maxPrime
}

# Java

class Global {
    public static int consecutivePrimeSum(int limit) {
        boolean[] sieve = new boolean[limit];
        Arrays.fill(sieve, true);
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i < limit; i++) {
            if (sieve[i]) {
                primes.add(i);
                for (int j = i * 2; j < limit; j += i) {
                    sieve[j] = false;
                }
            }
        }
        int maxLength = 0;
        int maxPrime = 0;
        for (int i = 0; i < primes.size(); i++) {
            for (int j = i + maxLength; j < primes.size(); j++) {
                int s = 0;
                for (int k = i; k < j; k++) {
                    s += primes.get(k);
                }
                if (s >= limit) {
                    break;
                }
                if (sieve[s] && j - i > maxLength) {
                    maxLength = j - i;
                    maxPrime = s;
                }
            }
        }
        return maxPrime;
    }
}

# JavaScript

const consecutivePrimeSum = (limit) => {
    const sieve = Array(limit).fill(true);
    const primes = [];
    for (let i = 2; i < limit; i++) {
        if (sieve[i]) {
            primes.push(i);
            for (let j = i * 2; j < limit; j += i) {
                sieve[j] = false;
            }
        }
    }
    let maxLength = 0;
    let maxPrime = 0;
    for (let i = 0; i < primes.length; i++) {
        for (let j = i + maxLength; j < primes.length; j++) {
            let s = 0;
            for (let k = i; k < j; k++) {
                s += primes[k];
            }
            if (s >= limit) {
                break;
            }
            if (sieve[s] && j - i > maxLength) {
                maxLength = j - i;
                maxPrime = s;
            }
        }
    }
    return maxPrime;
}

# Kotlin

fun consecutivePrimeSum(limit: Int): Int {
    val sieve = BooleanArray(limit) { true }
    val primes = mutableListOf<Int>()
    for (i in 2 until limit) {
        if (sieve[i]) {
            primes.add(i)
            for (j in i * 2 until limit step i) {
                sieve[j] = false
            }
        }
    }
    var maxLength = 0
    var maxPrime = 0
    for (i in primes.indices) {
        for (j in i + maxLength until primes.size) {
            var s = 0
            for (k in i until j) {
                s += primes[k]
            }
            if (s >= limit) {
                break
            }
            if (sieve[s] && j - i > maxLength) {
                maxLength = j - i
                maxPrime = s
            }
        }
    }
    return maxPrime
}

# PHP

function consecutivePrimeSum($limit) {
    $sieve = array_fill(0, $limit, true);
    $primes = [];
    for ($i = 2; $i < $limit; $i++) {
        if ($sieve[$i]) {
            $primes[] = $i;
            for ($j = $i * 2; $j < $limit; $j += $i) {
                $sieve[$j] = false;
            }
        }
    }
    $maxLength = 0;
    $maxPrime = 0;
    for ($i = 0; $i < count($primes); $i++) {
        for ($j = $i + $maxLength; $j < count($primes); $j++) {
            $s = 0;
            for ($k = $i; $k < $j; $k++) {
                $s += $primes[$k];
            }
            if ($s >= $limit) {
                break;
            }
            if ($sieve[$s] && $j - $i > $maxLength) {
                $maxLength = $j - $i;
                $maxPrime = $s;
            }
        }
    }
    return $maxPrime;
}

# Ruby

def consecutive_prime_sum(limit)
    sieve = Array.new(limit, true)
    primes = []
    (2...limit).each do |i|
        if sieve[i]
            primes.push(i)
            (i * 2...limit).step(i) do |j|
                sieve[j] = false
            end
        end
    end
    max_length = 0
    max_prime = 0
    primes.each_with_index do |_, i|
        (i + max_length...primes.length).each do |j|
            s = 0
            (i...j).each do |k|
                s += primes[k]
            end
            if s >= limit
                break
            end
            if sieve[s] && j - i > max_length
                max_length = j - i
                max_prime = s
            end
        end
    end
    max_prime
end

# Rust

fn consecutive_prime_sum(limit: i32) -> i32 {
    let mut sieve = vec![true; limit as usize];
    let mut primes = vec![];
    for i in 2..limit {
        if sieve[i as usize] {
            primes.push(i);
            for j in (i * 2..limit).step_by(i as usize) {
                sieve[j as usize] = false;
            }
        }
    }
    let mut max_length = 0;
    let mut max_prime = 0;
    for i in 0..primes.len() {
        for j in i + max_length..primes.len() {
            let mut s = 0;
            for k in i..j {
                s += primes[k];
            }
            if s >= limit {
                break;
            }
            if sieve[s as usize] && j - i > max_length {
                max_length = j - i;
                max_prime = s;
            }
        }
    }
    max_prime
}

# Scala

def consecutivePrimeSum(limit: Int): Int = {
    val sieve = Array.fill(limit)(true)
    val primes = ArrayBuffer[Int]()
    for (i <- 2 until limit) {
        if (sieve(i)) {
            primes += i
            for (j <- i * 2 until limit by i) {
                sieve(j) = false
            }
        }
    }
    var maxLength = 0
    var maxPrime = 0
    for (i <- primes.indices) {
        breakable {
            for (j <- i + maxLength until primes.length) {
                var s = 0
                for (k <- i until j) {
                    s += primes(k)
                }
                if (s >= limit) {
                    break
                }
                if (sieve(s) && j - i > maxLength) {
                    maxLength = j - i
                    maxPrime = s
                }
            }
        }
    }
    maxPrime
}
