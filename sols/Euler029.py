# Python

def distinct_powers(n: int) -> int:
    result = 0
    xs = set()
    for i in range(2, n + 1):
        primes = [2, 3, 5, 7]
        powers = [0, 0, 0, 0]
        num = i
        for j in range(len(primes)):
            while num % primes[j] == 0:
                num //= primes[j]
                powers[j] += 1
        if num != 1:
            result += n - 1
            continue
        for j in range(2, n + 1):
            pstr = f"{powers[0] * j}-{powers[1] * j}-{powers[2] * j}-{powers[3] * j}"
            xs.add(pstr)
    result += len(xs)
    return result

# Start translation now

# C++

int distinctPowers(int n) {
    int result = 0;
    unordered_set<string> xs;
    for (int i = 2; i <= n; i++) {
        vector<int> primes = {2, 3, 5, 7};
        vector<int> powers = {0, 0, 0, 0};
        int num = i;
        for (int j = 0; j < primes.size(); j++) {
            while (num % primes[j] == 0) {
                num /= primes[j];
                powers[j] += 1;
            }
        }
        if (num != 1) {
            result += n - 1;
            continue;
        }
        for (int j = 2; j <= n; j++) {
            string pstr = format("{}-{}-{}-{}", powers[0] * j, powers[1] * j, powers[2] * j, powers[3] * j);
            xs.insert(pstr);
        }
    }
    result += xs.size();
    return result;
}

# C#

class Global {
    public static int DistinctPowers(int n) {
        int result = 0;
        HashSet<string> xs = new HashSet<string>();
        for (int i = 2; i <= n; i++) {
            List<int> primes = new List<int> {2, 3, 5, 7};
            List<int> powers = new List<int> {0, 0, 0, 0};
            int num = i;
            for (int j = 0; j < primes.Count; j++) {
                while (num % primes[j] == 0) {
                    num /= primes[j];
                    powers[j] += 1;
                }
            }
            if (num != 1) {
                result += n - 1;
                continue;
            }
            for (int j = 2; j <= n; j++) {
                string pstr = string.Format("{0}-{1}-{2}-{3}", powers[0] * j, powers[1] * j, powers[2] * j, powers[3] * j);
                xs.Add(pstr);
            }
        }
        result += xs.Count;
        return result;
    }
}

# Go

func DistinctPowers(n int) int {
    result := 0
    xs := make(map[string]bool)
    for i := 2; i <= n; i++ {
        primes := []int{2, 3, 5, 7}
        powers := []int{0, 0, 0, 0}
        num := i
        for j := 0; j < len(primes); j++ {
            for num % primes[j] == 0 {
                num /= primes[j]
                powers[j] += 1
            }
        }
        if num != 1 {
            result += n - 1
            continue
        }
        for j := 2; j <= n; j++ {
            pstr := fmt.Sprintf("%d-%d-%d-%d", powers[0] * j, powers[1] * j, powers[2] * j, powers[3] * j)
            xs[pstr] = true
        }
    }
    result += len(xs)
    return result
}

# Java

class Global {
    public static int distinctPowers(int n) {
        int result = 0;
        HashSet<String> xs = new HashSet<String>();
        for (int i = 2; i <= n; i++) {
            List<Integer> primes = new ArrayList<Integer>(Arrays.asList(2, 3, 5, 7));
            List<Integer> powers = new ArrayList<Integer>(Arrays.asList(0, 0, 0, 0));
            int num = i;
            for (int j = 0; j < primes.size(); j++) {
                while (num % primes.get(j) == 0) {
                    num /= primes.get(j);
                    powers.set(j, powers.get(j) + 1);
                }
            }
            if (num != 1) {
                result += n - 1;
                continue;
            }
            for (int j = 2; j <= n; j++) {
                String pstr = String.format("%d-%d-%d-%d", powers.get(0) * j, powers.get(1) * j, powers.get(2) * j, powers.get(3) * j);
                xs.add(pstr);
            }
        }
        result += xs.size();
        return result;
    }
}

# JavaScript

const distinctPowers = (n) => {
    let result = 0;
    let xs = new Set();
    for (let i = 2; i <= n; i++) {
        let primes = [2, 3, 5, 7];
        let powers = [0, 0, 0, 0];
        let num = i;
        for (let j = 0; j < primes.length; j++) {
            while (num % primes[j] == 0) {
                num /= primes[j];
                powers[j] += 1;
            }
        }
        if (num != 1) {
            result += n - 1;
            continue;
        }
        for (let j = 2; j <= n; j++) {
            let pstr = `${powers[0] * j}-${powers[1] * j}-${powers[2] * j}-${powers[3] * j}`;
            xs.add(pstr);
        }
    }
    result += xs.size;
    return result;
}

# Kotlin

fun distinctPowers(n: Int): Int {
    var result = 0
    val xs = mutableSetOf<String>()
    for (i in 2..n) {
        val primes = listOf(2, 3, 5, 7)
        val powers = mutableListOf(0, 0, 0, 0)
        var num = i
        for (j in primes.indices) {
            while (num % primes[j] == 0) {
                num /= primes[j]
                powers[j] += 1
            }
        }
        if (num != 1) {
            result += n - 1
            continue
        }
        for (j in 2..n) {
            val pstr = "${powers[0] * j}-${powers[1] * j}-${powers[2] * j}-${powers[3] * j}"
            xs.add(pstr)
        }
    }
    result += xs.size
    return result
}

# PHP

function distinctPowers($n) {
    $result = 0;
    $xs = [];
    for ($i = 2; $i <= $n; $i++) {
        $primes = [2, 3, 5, 7];
        $powers = [0, 0, 0, 0];
        $num = $i;
        for ($j = 0; $j < count($primes); $j++) {
            while ($num % $primes[$j] == 0) {
                $num /= $primes[$j];
                $powers[$j] += 1;
            }
        }
        if ($num != 1) {
            $result += $n - 1;
            continue;
        }
        for ($j = 2; $j <= $n; $j++) {
            $pstr = sprintf("%d-%d-%d-%d", $powers[0] * $j, $powers[1] * $j, $powers[2] * $j, $powers[3] * $j);
            $xs[$pstr] = true;
        }
    }
    $result += count($xs);
    return $result;
}

# Ruby

def distinct_powers(n)
    result = 0
    xs = Set.new
    (2..n).each do |i|
        primes = [2, 3, 5, 7]
        powers = [0, 0, 0, 0]
        num = i
        primes.each_with_index do |p, j|
            while num % p == 0
                num /= p
                powers[j] += 1
            end
        end
        if num != 1
            result += n - 1
            next
        end
        (2..n).each do |j|
            pstr = "#{powers[0] * j}-#{powers[1] * j}-#{powers[2] * j}-#{powers[3] * j}"
            xs.add(pstr)
        end
    end
    result += xs.size
    result
end

# Rust

fn distinct_powers(n: i32) -> i32 {
    let mut result = 0;
    let mut xs = HashSet::new();
    for i in 2..=n {
        let primes = vec![2, 3, 5, 7];
        let mut powers = vec![0, 0, 0, 0];
        let mut num = i;
        for j in 0..primes.len() {
            while num % primes[j] == 0 {
                num /= primes[j];
                powers[j] += 1;
            }
        }
        if num != 1 {
            result += n - 1;
            continue;
        }
        for j in 2..=n {
            let pstr = format!("{}-{}-{}-{}", powers[0] * j, powers[1] * j, powers[2] * j, powers[3] * j);
            xs.insert(pstr);
        }
    }
    result += xs.len() as i32;
    result
}

# Scala

def distinctPowers(n: Int): Int = {
    var result = 0
    val xs = mutable.Set[String]()
    for (i <- 2 to n) {
        val primes = List(2, 3, 5, 7)
        val powers = ArrayBuffer(0, 0, 0, 0)
        var num = i
        for (j <- primes.indices) {
            while (num % primes(j) == 0) {
                num /= primes(j)
                powers(j) += 1
            }
        }
        if (num != 1) {
            result += n - 1
        } else {
            for (j <- 2 to n) {
                val pstr = s"${powers(0) * j}-${powers(1) * j}-${powers(2) * j}-${powers(3) * j}"
                xs.add(pstr)
            }
        }
    }
    result += xs.size
    result
}