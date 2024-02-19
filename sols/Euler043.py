# Python

def gen_permutations(s: str) -> list[str]:
    if len(s) <= 1:
        return s
    result = []
    for perm in gen_permutations(s[1:]):
        for i in range(len(s)):
            result.append(perm[:i] + s[0:1] + perm[i:])
    return result


def sub_string_divisibility(n: int) -> int:
    result = 0
    primes = [2, 3, 5, 7, 11, 13, 17]
    s = ''.join(str(i) for i in range(n + 1))
    for i in gen_permutations(s):
        flag = True
        for j in range(1, n - 1):
            if int(i[j:j + 3]) % primes[j - 1] != 0:
                flag = False
                break
        if flag:
            result += int(i)
    return result

# Start translation now

# C++

vector<string> genPermutations(const string& s) {
    if (s.size() <= 1) {
        return {s};
    }
    vector<string> result;
    for (const string& perm : genPermutations(s.substr(1))) {
        for (int i = 0; i < s.size(); i++) {
            result.push_back(perm.substr(0, i) + s[0] + perm.substr(i));
        }
    }
    return result;
}

int subStringDivisibility(int n) {
    int result = 0;
    vector<int> primes = {2, 3, 5, 7, 11, 13, 17};
    string s;
    for (int i = 0; i <= n; i++) {
        s += to_string(i);
    }
    for (const string& i : genPermutations(s)) {
        bool flag = true;
        for (int j = 1; j < n - 1; j++) {
            if (stoi(i.substr(j, 3)) % primes[j - 1] != 0) {
                flag = false;
                break;
            }
        }
        if (flag) {
            result += stoi(i);
        }
    }
    return result;
}

# C#

class Global {
    public static List<string> GenPermutations(string s) {
        if (s.Length <= 1) {
            return new List<string> { s };
        }
        List<string> result = new List<string>();
        foreach (string perm in GenPermutations(s.Substring(1))) {
            for (int i = 0; i < s.Length; i++) {
                result.Add(perm.Substring(0, i) + s[0] + perm.Substring(i));
            }
        }
        return result;
    }

    public static int SubStringDivisibility(int n) {
        int result = 0;
        List<int> primes = new List<int> { 2, 3, 5, 7, 11, 13, 17 };
        string s = "";
        for (int i = 0; i <= n; i++) {
            s += i.ToString();
        }
        foreach (string i in GenPermutations(s)) {
            bool flag = true;
            for (int j = 1; j < n - 1; j++) {
                if (int.Parse(i.Substring(j, 3)) % primes[j - 1] != 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                result += int.Parse(i);
            }
        }
        return result;
    }
}

# Go

func GenPermutations(s string) []string {
    if len(s) <= 1 {
        return []string{s}
    }
    result := []string{}
    for _, perm := range GenPermutations(s[1:]) {
        for i := 0; i < len(s); i++ {
            result = append(result, perm[:i] + s[:1] + perm[i:])
        }
    }
    return result
}

func SubStringDivisibility(n int) int {
    result := 0
    primes := []int{2, 3, 5, 7, 11, 13, 17}
    s := ""
    for i := 0; i <= n; i++ {
        s += strconv.Itoa(i)
    }
    for _, i := range GenPermutations(s) {
        flag := true
        for j := 1; j < n - 1; j++ {
            if n, _ := strconv.Atoi(i[j:j + 3]); n % primes[j - 1] != 0 {
                flag = false
                break
            }
        }
        if flag {
            s0, _ := strconv.Atoi(i)
            result += s0
        }
    }
    return result
}

# Java

class Global {
    public static List<String> genPermutations(String s) {
        if (s.length() <= 1) {
            return List.of(s);
        }
        List<String> result = new ArrayList<>();
        for (String perm : genPermutations(s.substring(1))) {
            for (int i = 0; i < s.length(); i++) {
                result.add(perm.substring(0, i) + s.charAt(0) + perm.substring(i));
            }
        }
        return result;
    }

    public static int subStringDivisibility(int n) {
        int result = 0;
        List<Integer> primes = List.of(2, 3, 5, 7, 11, 13, 17);
        String s = "";
        for (int i = 0; i <= n; i++) {
            s += i;
        }
        for (String i : genPermutations(s)) {
            boolean flag = true;
            for (int j = 1; j < n - 1; j++) {
                if (Integer.parseInt(i.substring(j, j + 3)) % primes.get(j - 1) != 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                result += Integer.parseInt(i);
            }
        }
        return result;
    }
}

# JavaScript

const genPermutations = (s) => {
    if (s.length <= 1) {
        return [s];
    }
    const result = [];
    for (const perm of genPermutations(s.substring(1))) {
        for (let i = 0; i < s.length; i++) {
            result.push(perm.substring(0, i) + s[0] + perm.substring(i));
        }
    }
    return result;
}

const subStringDivisibility = (n) => {
    let result = 0;
    const primes = [2, 3, 5, 7, 11, 13, 17];
    let s = "";
    for (let i = 0; i <= n; i++) {
        s += i;
    }
    for (const i of genPermutations(s)) {
        let flag = true;
        for (let j = 1; j < n - 1; j++) {
            if (parseInt(i.substring(j, j + 3)) % primes[j - 1] !== 0) {
                flag = false;
                break;
            }
        }
        if (flag) {
            result += parseInt(i);
        }
    }
    return result;
}

# Kotlin

fun genPermutations(s: String): List<String> {
    if (s.length <= 1) {
        return listOf(s);
    }
    val result = mutableListOf<String>()
    for (perm in genPermutations(s.substring(1))) {
        for (i in s.indices) {
            result.add(perm.substring(0, i) + s[0] + perm.substring(i))
        }
    }
    return result
}

fun subStringDivisibility(n: Int): Int {
    var result = 0
    val primes = listOf(2, 3, 5, 7, 11, 13, 17)
    var s = ""
    for (i in 0..n) {
        s += i
    }
    for (i in genPermutations(s)) {
        var flag = true
        for (j in 1 until n - 1) {
            if (i.substring(j, j + 3).toInt() % primes[j - 1] != 0) {
                flag = false
                break
            }
        }
        if (flag) {
            result += i.toInt()
        }
    }
    return result
}

# PHP

function genPermutations($s) {
    if (strlen($s) <= 1) {
        return [$s];
    }
    $result = [];
    foreach (genPermutations(substr($s, 1)) as $perm) {
        for ($i = 0; $i < strlen($s); $i++) {
            $result[] = substr($perm, 0, $i) . $s[0] . substr($perm, $i);
        }
    }
    return $result;
}

function subStringDivisibility($n) {
    $result = 0;
    $primes = [2, 3, 5, 7, 11, 13, 17];
    $s = "";
    for ($i = 0; $i <= $n; $i++) {
        $s .= $i;
    }
    foreach (genPermutations($s) as $i) {
        $flag = true;
        for ($j = 1; $j < $n - 1; $j++) {
            if (intval(substr($i, $j, 3)) % $primes[$j - 1] != 0) {
                $flag = false;
                break;
            }
        }
        if ($flag) {
            $result += intval($i);
        }
    }
    return $result;
}

# Ruby

def gen_permutations(s)
    if s.length <= 1
        return [s]
    end
    result = []
    gen_permutations(s[1..-1]).each do |perm|
        (0...s.length).each do |i|
            result.push(perm[0...i] + s[0] + perm[i..-1])
        end
    end
    result
end

def sub_string_divisibility(n)
    result = 0
    primes = [2, 3, 5, 7, 11, 13, 17]
    s = ""
    (0..n).each do |i|
        s += i.to_s
    end
    gen_permutations(s).each do |i|
        flag = true
        (1...n - 1).each do |j|
            if i[j..j + 2].to_i % primes[j - 1] != 0
                flag = false
                break
            end
        end
        if flag
            result += i.to_i
        end
    end
    result
end

# Rust

fn gen_permutations(s: &String) -> Vec<String> {
    if s.len() <= 1 {
        return vec![s.clone()];
    }
    let mut result = vec![];
    for perm in gen_permutations(&s[1..].to_string()) {
        for i in 0..s.len() {
            result.push(perm[0..i].to_string() + &s[0..1] + &perm[i..]);
        }
    }
    result
}

fn sub_string_divisibility(n: i32) -> i32 {
    let mut result = 0;
    let primes = vec![2, 3, 5, 7, 11, 13, 17];
    let mut s = String::new();
    for i in 0..=n {
        s += &i.to_string();
    }
    for i in gen_permutations(&s) {
        let mut flag = true;
        for j in 1..(n - 1) as usize {
            if i[j..j + 3].parse::<i32>().unwrap() % primes[j - 1] != 0 {
                flag = false;
                break;
            }
        }
        if flag {
            result += i.parse::<i32>().unwrap();
        }
    }
    result
}

# Scala

def genPermutations(s: String): Seq[String] = {
    if (s.length <= 1) {
        return Seq(s)
    }
    var result = Seq[String]()
    for (perm <- genPermutations(s.substring(1))) {
        for (i <- 0 until s.length) {
            result :+= perm.substring(0, i) + s(0) + perm.substring(i)
        }
    }
    result
}

def subStringDivisibility(n: Int): Int = {
    var result = 0
    val primes = Seq(2, 3, 5, 7, 11, 13, 17)
    var s = ""
    for (i <- 0 to n) {
        s += i
    }
    for (i <- genPermutations(s)) {
        var flag = true
            breakable {
            for (j <- 1 until n - 1) {
                if (i.substring(j, j + 3).toInt % primes(j - 1) != 0) {
                    flag = false
                    break
                }
            }
            if (flag) {
                result += i.toInt
            }
        }
    }
    result
}
