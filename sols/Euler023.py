# Python

def is_abundant(n: int) -> bool:
    if n < 12:
        return False
    sum_divisors = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors > n

def non_abundant_sums(n: int) -> int:
    abundants = []
    for i in range(12, n):
        if is_abundant(i):
            abundants.append(i)
    abundant_sums = set()
    for i in abundants:
        for j in abundants:
            abundant_sums.add(i + j)
    result = 0
    for i in range(n):
        if i not in abundant_sums:
            result += i
    return result

# Start translation now

# C++

bool isAbundant(int n) {
    if (n < 12) {
        return false;
    }
    int sumDivisors = 1;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            sumDivisors += i;
            if (i != n / i) {
                sumDivisors += n / i;
            }
        }
    }
    return sumDivisors > n;
}

int nonAbundantSums(int n) {
    vector<int> abundants;
    for (int i = 12; i < n; i++) {
        if (isAbundant(i)) {
            abundants.push_back(i);
        }
    }
    set<int> abundantSums;
    for (int i : abundants) {
        for (int j : abundants) {
            abundantSums.insert(i + j);
        }
    }
    int result = 0;
    for (int i = 0; i < n; i++) {
        if (abundantSums.find(i) == abundantSums.end()) {
            result += i;
        }
    }
    return result;
}

# C#

class Global {
    public static bool IsAbundant(int n) {
        if (n < 12) {
            return false;
        }
        int sumDivisors = 1;
        for (int i = 2; i <= Math.Sqrt(n); i++) {
            if (n % i == 0) {
                sumDivisors += i;
                if (i != n / i) {
                    sumDivisors += n / i;
                }
            }
        }
        return sumDivisors > n;
    }

    public static int NonAbundantSums(int n) {
        List<int> abundants = new List<int>();
        for (int i = 12; i < n; i++) {
            if (IsAbundant(i)) {
                abundants.Add(i);
            }
        }
        HashSet<int> abundantSums = new HashSet<int>();
        foreach (int i in abundants) {
            foreach (int j in abundants) {
                abundantSums.Add(i + j);
            }
        }
        int result = 0;
        for (int i = 0; i < n; i++) {
            if (!abundantSums.Contains(i)) {
                result += i;
            }
        }
        return result;
    }
}

# Go

func IsAbundant(n int) bool {
    if n < 12 {
        return false
    }
    sumDivisors := 1
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            sumDivisors += i
            if i != n / i {
                sumDivisors += n / i
            }
        }
    }
    return sumDivisors > n
}

func NonAbundantSums(n int) int {
    abundants := []int{}
    for i := 12; i < n; i++ {
        if IsAbundant(i) {
            abundants = append(abundants, i)
        }
    }
    abundantSums := map[int]bool{}
    for _, i := range abundants {
        for _, j := range abundants {
            abundantSums[i + j] = true
        }
    }
    result := 0
    for i := 0; i < n; i++ {
        if !abundantSums[i] {
            result += i
        }
    }
    return result
}

# Java

class Global {
    public static boolean isAbundant(int n) {
        if (n < 12) {
            return false;
        }
        int sumDivisors = 1;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                sumDivisors += i;
                if (i != n / i) {
                    sumDivisors += n / i;
                }
            }
        }
        return sumDivisors > n;
    }

    public static int nonAbundantSums(int n) {
        List<Integer> abundants = new ArrayList<>();
        for (int i = 12; i < n; i++) {
            if (isAbundant(i)) {
                abundants.add(i);
            }
        }
        Set<Integer> abundantSums = new HashSet<>();
        for (int i : abundants) {
            for (int j : abundants) {
                abundantSums.add(i + j);
            }
        }
        int result = 0;
        for (int i = 0; i < n; i++) {
            if (!abundantSums.contains(i)) {
                result += i;
            }
        }
        return result;
    }
}

# JavaScript

const isAbundant = (n) => {
    if (n < 12) {
        return false;
    }
    let sumDivisors = 1;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            sumDivisors += i;
            if (i !== n / i) {
                sumDivisors += n / i;
            }
        }
    }
    return sumDivisors > n;
}

const nonAbundantSums = (n) => {
    const abundants = [];
    for (let i = 12; i < n; i++) {
        if (isAbundant(i)) {
            abundants.push(i);
        }
    }
    const abundantSums = new Set();
    for (let i of abundants) {
        for (let j of abundants) {
            abundantSums.add(i + j);
        }
    }
    let result = 0;
    for (let i = 0; i < n; i++) {
        if (!abundantSums.has(i)) {
            result += i;
        }
    }
    return result;
}

# Kotlin

fun isAbundant(n: Int): Boolean {
    if (n < 12) {
        return false
    }
    var sumDivisors = 1
    for (i in 2..sqrt(n.toDouble()).toInt()) {
        if (n % i == 0) {
            sumDivisors += i
            if (i != n / i) {
                sumDivisors += n / i
            }
        }
    }
    return sumDivisors > n
}

fun nonAbundantSums(n: Int): Int {
    val abundants = mutableListOf<Int>()
    for (i in 12 until n) {
        if (isAbundant(i)) {
            abundants.add(i)
        }
    }
    val abundantSums = mutableSetOf<Int>()
    for (i in abundants) {
        for (j in abundants) {
            abundantSums.add(i + j)
        }
    }
    var result = 0
    for (i in 0 until n) {
        if (i !in abundantSums) {
            result += i
        }
    }
    return result
}

# PHP

function isAbundant($n) {
    if ($n < 12) {
        return false;
    }
    $sumDivisors = 1;
    for ($i = 2; $i <= sqrt($n); $i++) {
        if ($n % $i == 0) {
            $sumDivisors += $i;
            if ($i != $n / $i) {
                $sumDivisors += $n / $i;
            }
        }
    }
    return $sumDivisors > $n;
}

function nonAbundantSums($n) {
    $abundants = [];
    for ($i = 12; $i < $n; $i++) {
        if (isAbundant($i)) {
            $abundants[] = $i;
        }
    }
    $abundantSums = [];
    foreach ($abundants as $i) {
        foreach ($abundants as $j) {
            $abundantSums[] = $i + $j;
        }
    }
    $result = 0;
    for ($i = 0; $i < $n; $i++) {
        if (!in_array($i, $abundantSums)) {
            $result += $i;
        }
    }
    return $result;
}

# Ruby

def is_abundant(n)
    if n < 12
        return false
    end
    sum_divisors = 1
    (2..Math.sqrt(n)).each do |i|
        if n % i == 0
            sum_divisors += i
            sum_divisors += n / i if i != n / i
        end
    end
    sum_divisors > n
end

def non_abundant_sums(n)
    abundants = []
    (12...n).each do |i|
        abundants.push(i) if is_abundant(i)
    end
    abundant_sums = []
    abundants.each do |i|
        abundants.each do |j|
            abundant_sums.push(i + j)
        end
    end
    result = 0
    (0...n).each do |i|
        result += i if !abundant_sums.include?(i)
    end
    result
end

# Rust

fn is_abundant(n: i32) -> bool {
    if n < 12 {
        return false;
    }
    let mut sum_divisors = 1;
    for i in 2..=(n as f64).sqrt() as i32 {
        if n % i == 0 {
            sum_divisors += i;
            if i != n / i {
                sum_divisors += n / i;
            }
        }
    }
    sum_divisors > n
}

fn non_abundant_sums(n: i32) -> i32 {
    let mut abundants = vec![];
    for i in 12..n {
        if is_abundant(i) {
            abundants.push(i);
        }
    }
    let mut abundant_sums = vec![];
    for i in &abundants {
        for j in &abundants {
            abundant_sums.push(i + j);
        }
    }
    let mut result = 0;
    for i in 0..n {
        if !abundant_sums.contains(&i) {
            result += i;
        }
    }
    result
}

# Scala

def isAbundant(n: Int): Boolean = {
    if (n < 12) {
        return false
    }
    var sumDivisors = 1
    for (i <- 2 to math.sqrt(n).toInt) {
        if (n % i == 0) {
            sumDivisors += i
            if (i != n / i) {
                sumDivisors += n / i
            }
        }
    }
    sumDivisors > n
}

def nonAbundantSums(n: Int): Int = {
    val abundants = ArrayBuffer[Int]()
    for (i <- 12 until n) {
        if (isAbundant(i)) {
            abundants += i
        }
    }
    val abundantSums = ArrayBuffer[Int]()
    for (i <- abundants) {
        for (j <- abundants) {
            abundantSums += i + j
        }
    }
    var result = 0
    for (i <- 0 until n) {
        if (!abundantSums.contains(i)) {
            result += i
        }
    }
    result
}


