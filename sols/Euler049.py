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

def gen_permutations(s: str) -> list[str]:
    if len(s) <= 1:
        return s
    result = []
    for perm in gen_permutations(s[1:]):
        for i in range(len(s)):
            result.append(perm[:i] + s[0:1] + perm[i:])
    return result

def prime_permutations(n: int) -> str:
    for i in range(n, 999, -1):
        if is_prime(i):
            permutations = gen_permutations(str(i))
            candidates = set()
            for j in permutations:
                candidate = int(j)
                if candidate > i and is_prime(candidate):
                    candidates.add(candidate)
            for m in candidates:
                if m + (m - i) in candidates:
                    return str(i) + str(m) + str(m + (m - i))
    return ''

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
    for (int i = 3; i <= int(sqrt(n)); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

vector<string> genPermutations(string s) {
    if (s.size() <= 1) {
        return {s};
    }
    vector<string> result;
    for (string perm : genPermutations(s.substr(1))) {
        for (int i = 0; i < s.size(); ++i) {
            result.push_back(perm.substr(0, i) + s[0] + perm.substr(i));
        }
    }
    return result;
}

string primePermutations(int n) {
    for (int i = n; i > 999; --i) {
        if (isPrime(i)) {
            vector<string> permutations = genPermutations(to_string(i));
            unordered_set<int> candidates;
            for (string j : permutations) {
                int candidate = stoi(j);
                if (candidate > i && isPrime(candidate)) {
                    candidates.insert(candidate);
                }
            }
            for (int m : candidates) {
                if (candidates.count(m + (m - i))) {
                    return to_string(i) + to_string(m) + to_string(m + (m - i));
                }
            }
        }
    }
    return "";
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
        for (int i = 3; i <= (int)Math.Sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static IList<string> GenPermutations(string s) {
        if (s.Length <= 1) {
            return new List<string>{s};
        }
        var result = new List<string>();
        foreach (var perm in GenPermutations(s.Substring(1))) {
            for (int i = 0; i < s.Length; ++i) {
                result.Add(perm.Substring(0, i) + s[0] + perm.Substring(i));
            }
        }
        return result;
    }

    public static string PrimePermutations(int n) {
        for (int i = n; i > 999; --i) {
            if (IsPrime(i)) {
                var permutations = GenPermutations(i.ToString());
                var candidates = new HashSet<int>();
                foreach (var j in permutations) {
                    var candidate = int.Parse(j);
                    if (candidate > i && IsPrime(candidate)) {
                        candidates.Add(candidate);
                    }
                }
                foreach (var m in candidates) {
                    if (candidates.Contains(m + (m - i))) {
                        return i.ToString() + m.ToString() + (m + (m - i)).ToString();
                    }
                }
            }
        }
        return "";
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

func GenPermutations(s string) []string {
    if len(s) <= 1 {
        return []string{s}
    }
    result := []string{}
    for _, perm := range GenPermutations(s[1:]) {
        for i := 0; i < len(s); i++ {
            result = append(result, perm[:i] + string(s[0]) + perm[i:])
        }
    }
    return result
}

func PrimePermutations(n int) string {
    for i := n; i > 999; i-- {
        if IsPrime(i) {
            permutations := GenPermutations(strconv.Itoa(i))
            candidates := map[int]bool{}
            for _, j := range permutations {
                candidate, _ := strconv.Atoi(j)
                if candidate > i && IsPrime(candidate) {
                    candidates[candidate] = true
                }
            }
            for m := range candidates {
                if candidates[m + (m - i)] {
                    return strconv.Itoa(i) + strconv.Itoa(m) + strconv.Itoa(m + (m - i))
                }
            }
        }
    }
    return ""
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
        for (int i = 3; i <= (int)Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static List<String> genPermutations(String s) {
        if (s.length() <= 1) {
            return List.of(s);
        }
        List<String> result = new ArrayList<>();
        for (String perm : genPermutations(s.substring(1))) {
            for (int i = 0; i < s.length(); ++i) {
                result.add(perm.substring(0, i) + s.charAt(0) + perm.substring(i));
            }
        }
        return result;
    }

    public static String primePermutations(int n) {
        for (int i = n; i > 999; --i) {
            if (isPrime(i)) {
                List<String> permutations = genPermutations(String.valueOf(i));
                Set<Integer> candidates = new HashSet<>();
                for (String j : permutations) {
                    int candidate = Integer.parseInt(j);
                    if (candidate > i && isPrime(candidate)) {
                        candidates.add(candidate);
                    }
                }
                for (int m : candidates) {
                    if (candidates.contains(m + (m - i))) {
                        return Integer.toString(i) + Integer.toString(m) + Integer.toString(m + (m - i));
                    }
                }
            }
        }
        return "";
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
};

const genPermutations = (s) => {
    if (s.length <= 1) {
        return [s];
    }
    const result = [];
    for (const perm of genPermutations(s.slice(1))) {
        for (let i = 0; i < s.length; ++i) {
            result.push(perm.slice(0, i) + s[0] + perm.slice(i));
        }
    }
    return result;
};

const primePermutations = (n) => {
    for (let i = n; i > 999; --i) {
        if (isPrime(i)) {
            const permutations = genPermutations(i.toString());
            const candidates = new Set();
            for (const j of permutations) {
                const candidate = parseInt(j);
                if (candidate > i && isPrime(candidate)) {
                    candidates.add(candidate);
                }
            }
            for (const m of candidates) {
                if (candidates.has(m + (m - i))) {
                    return i.toString() + m.toString() + (m + (m - i)).toString();
                }
            }
        }
    }
    return "";
};

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
    for (i in 3..n / 2 step 2) {
        if (n % i == 0) {
            return false
        }
    }
    return true
}

fun genPermutations(s: String): List<String> {
    if (s.length <= 1) {
        return listOf(s)
    }
    val result = mutableListOf<String>()
    for (perm in genPermutations(s.substring(1))) {
        for (i in s.indices) {
            result.add(perm.substring(0, i) + s[0] + perm.substring(i))
        }
    }
    return result
}

fun primePermutations(n: Int): String {
    for (i in n downTo 999) {
        if (isPrime(i)) {
            val permutations = genPermutations(i.toString())
            val candidates = mutableSetOf<Int>()
            for (j in permutations) {
                val candidate = j.toInt()
                if (candidate > i && isPrime(candidate)) {
                    candidates.add(candidate)
                }
            }
            for (m in candidates) {
                if (candidates.contains(m + (m - i))) {
                    return i.toString() + m.toString() + (m + (m - i)).toString()
                }
            }
        }
    }
    return ""
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
    for ($i = 3; $i <= intval(sqrt($n)); $i += 2) {
        if ($n % $i == 0) {
            return false;
        }
    }
    return true;
}

function genPermutations($s) {
    if (strlen($s) <= 1) {
        return [$s];
    }
    $result = [];
    foreach (genPermutations(substr($s, 1)) as $perm) {
        for ($i = 0; $i < strlen($s); ++$i) {
            $result[] = substr($perm, 0, $i) . $s[0] . substr($perm, $i);
        }
    }
    return $result;
}

function primePermutations($n) {
    for ($i = $n; $i > 999; --$i) {
        if (isPrime($i)) {
            $permutations = genPermutations(strval($i));
            $candidates = [];
            foreach ($permutations as $j) {
                $candidate = intval($j);
                if ($candidate > $i && isPrime($candidate)) {
                    $candidates[] = $candidate;
                }
            }
            foreach ($candidates as $m) {
                if (in_array($m + ($m - $i), $candidates)) {
                    return strval($i) . strval($m) . strval($m + ($m - $i));
                }
            }
        }
    }
    return "";
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
    for i in 3..(n ** 0.5).to_i
        if n % i == 0
            return false
        end
    end
    return true
end

def gen_permutations(s)
    if s.length <= 1
        return [s]
    end
    result = []
    gen_permutations(s[1..-1]).each do |perm|
        (0..s.length - 1).each do |i|
            result << perm[0...i] + s[0] + perm[i..-1]
        end
    end
    result
end

def prime_permutations(n)
    (n).downto(999).each do |i|
        if is_prime(i)
            permutations = gen_permutations(i.to_s)
            candidates = Set.new
            permutations.each do |j|
                candidate = j.to_i
                if candidate > i && is_prime(candidate)
                    candidates.add(candidate)
                end
            end
            candidates.each do |m|
                if candidates.include?(m + (m - i))
                    return i.to_s + m.to_s + (m + (m - i)).to_s
                end
            end
        end
    end
    ""
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

fn gen_permutations(s: &str) -> Vec<String> {
    if s.len() <= 1 {
        return vec![s.to_string()];
    }
    let mut result = vec![];
    for perm in gen_permutations(&s[1..]) {
        for i in 0..s.len() {
            result.push(perm[..i].to_string() + &s[0..1] + &perm[i..]);
        }
    }
    result
}

fn prime_permutations(n: i32) -> String {
    for i in (999..n).rev() {
        if is_prime(i) {
            let permutations = gen_permutations(&i.to_string());
            let mut candidates = std::collections::HashSet::new();
            for j in permutations {
                let candidate = j.parse::<i32>().unwrap();
                if candidate > i && is_prime(candidate) {
                    candidates.insert(candidate);
                }
            }
            for m in &candidates {
                if candidates.contains(&(m + (m - i))) {
                    return i.to_string() + &m.to_string() + &(m + (m - i)).to_string();
                }
            }
        }
    }
    "".to_string()
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
    for (i <- 3 to n / 2 by 2) {
        if (n % i == 0) {
            return false
        }
    }
    true
}

def genPermutations(s: String): collection.Seq[String] = {
    if (s.length <= 1) {
        return Seq(s)
    }
    val result = collection.mutable.ArrayBuffer[String]()
    for (perm <- genPermutations(s.substring(1))) {
        for (i <- s.indices) {
            result += perm.substring(0, i) + s(0) + perm.substring(i)
        }
    }
    result
}

def primePermutations(n: Int): String = {
    for (i <- n to 999 by -1) {
        if (isPrime(i)) {
            val permutations = genPermutations(i.toString)
            val candidates = collection.mutable.Set[Int]()
            for (j <- permutations) {
                val candidate = j.toInt
                if (candidate > i && isPrime(candidate)) {
                    candidates += candidate
                }
            }
            for (m <- candidates) {
                if (candidates.contains(m + (m - i))) {
                    return i.toString + m.toString + (m + (m - i)).toString
                }
            }
        }
    }
    ""
}
