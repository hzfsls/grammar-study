# Python

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def circular_primes(n: int) -> int:
    count = 0
    for i in range(2, n):
        if is_prime(i):
            rotations = set()
            si = str(i)
            for j in range(len(si)):
                rotations.add(int(si[j:] + si[:j]))
            flag = True
            for x in rotations:
                if not is_prime(x):
                    flag = False
                    break
            if flag:
                count += 1
    return count

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

int circularPrimes(int n) {
    int count = 0;
    for (int i = 2; i < n; i++) {
        if (isPrime(i)) {
            unordered_set<int> rotations;
            string si = to_string(i);
            for (int j = 0; j < str.size(); j++) {
                rotations.insert(stoi(si.substr(j) + si.substr(0, j)));
            }
            bool flag = true;
            for (int x : rotations) {
                if (!isPrime(x)) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                count++;
            }
        }
    }
    return count;
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

    public static int CircularPrimes(int n) {
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (IsPrime(i)) {
                HashSet<int> rotations = new HashSet<int>();
                string si = i.ToString();
                for (int j = 0; j < si.Length; j++) {
                    rotations.Add(int.Parse(si.Substring(j) + si.Substring(0, j)));
                }
                bool flag = true;
                foreach (int x in rotations) {
                    if (!IsPrime(x)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    count++;
                }
            }
        }
        return count;
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

func CircularPrimes(n int) int {
    count := 0
    for i := 2; i < n; i++ {
        if IsPrime(i) {
            rotations := make(map[int]bool)
            si := strconv.Itoa(i)
            for j := 0; j < len(si); j++ {
                x, _ := strconv.Atoi(si[j:] + si[:j])
                rotations[x] = true
            }
            flag := true
            for x := range rotations {
                if !IsPrime(x) {
                    flag = false
                    break
                }
            }
            if flag {
                count++
            }
        }
    }
    return count
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

    public static int circularPrimes(int n) {
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                HashSet<Integer> rotations = new HashSet<Integer>();
                String str = Integer.toString(i);
                for (int j = 0; j < str.length(); j++) {
                    rotations.add(Integer.parseInt(str.substring(j) + str.substring(0, j)));
                }
                boolean flag = true;
                for (int x : rotations) {
                    if (!isPrime(x)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    count++;
                }
            }
        }
        return count;
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

const circularPrimes = (n) => {
    let count = 0;
    for (let i = 2; i < n; i++) {
        if (isPrime(i)) {
            const rotations = new Set();
            const str = i.toString();
            for (let j = 0; j < str.length; j++) {
                rotations.add(parseInt(str.substring(j) + str.substring(0, j)));
            }
            let flag = true;
            for (let x of rotations) {
                if (!isPrime(x)) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                count++;
            }
        }
    }
    return count;
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

fun circularPrimes(n: Int): Int {
    var count = 0
    for (i in 2 until n) {
        if (isPrime(i)) {
            val rotations = HashSet<Int>()
            val str = i.toString()
            for (j in 0 until str.length) {
                rotations.add((str.substring(j) + str.substring(0, j)).toInt())
            }
            var flag = true
            for (x in rotations) {
                if (!isPrime(x)) {
                    flag = false
                    break
                }
            }
            if (flag) {
                count++
            }
        }
    }
    return count
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

function circularPrimes($n) {
    $count = 0;
    for ($i = 2; $i < $n; $i++) {
        if (isPrime($i)) {
            $rotations = [];
            $str = strval($i);
            for ($j = 0; $j < strlen($str); $j++) {
                $rotations[] = intval(substr($str, $j) . substr($str, 0, $j));
            }
            $flag = true;
            foreach ($rotations as $x) {
                if (!isPrime($x)) {
                    $flag = false;
                    break;
                }
            }
            if ($flag) {
                $count++;
            }
        }
    }
    return $count;
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

def circular_primes(n)
    count = 0
    (2...n).each do |i|
        if is_prime(i)
            rotations = Set.new
            str = i.to_s
            (0...str.length).each do |j|
                rotations.add((str[j...str.length] + str[0...j]).to_i)
            end
            flag = true
            rotations.each do |x|
                if !is_prime(x)
                    flag = false
                    break
                end
            end
            if flag
                count += 1
            end
        end
    end
    return count
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
    for i in (3..=(n as f64).sqrt() as i32).step_by(2) {
        if n % i == 0 {
            return false;
        }
    }
    return true;
}

fn circular_primes(n: i32) -> i32 {
    let mut count = 0;
    for i in 2..n {
        if is_prime(i) {
            let mut rotations = HashSet::new();
            let str = i.to_string();
            for j in 0..str.len() {
                rotations.insert(format!("{}{}", &str[j..], &str[..j]).parse().unwrap());
            }
            let mut flag = true;
            for x in rotations {
                if !is_prime(x) {
                    flag = false;
                    break;
                }
            }
            if flag {
                count += 1;
            }
        }
    }
    return count;
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
    for (i <- 3 to math.sqrt(n).toInt by 2) {
        if (n % i == 0) {
            return false
        }
    }
    return true
}

def circularPrimes(n: Int): Int = {
    var count = 0
    for (i <- 2 until n) {
        if (isPrime(i)) {
            val rotations = HashSet[Int]()
            val str = i.toString
            for (j <- 0 until str.length) {
                rotations.add((str.substring(j) + str.substring(0, j)).toInt)
            }
            var flag = true
            breakable {
                for (x <- rotations) {
                    if (!isPrime(x)) {
                        flag = false
                        break
                    }
                }
            }
            if (flag) {
                count += 1
            }
        }
    }
    return count
}
