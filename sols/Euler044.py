# Python

def pentagon_numbers(n: int) -> int:
    pentagon = set()
    for i in range(1, n):
        pentagon.add(i * (3 * i - 1) // 2)
    result = -1
    for j in pentagon:
        for k in pentagon:
            if j + k in pentagon and k - j in pentagon:
                if result == -1 or k - j < result:
                    result = k - j
    return result

# Start translation now

# C++

int pentagonNumbers(int n) {
    unordered_set<int> pentagon;
    for (int i = 1; i < n; i++) {
        pentagon.insert(i * (3 * i - 1) / 2);
    }
    int result = -1;
    for (int j : pentagon) {
        for (int k : pentagon) {
            if (pentagon.count(j + k) && pentagon.count(k - j)) {
                if (result == -1 || k - j < result) {
                    result = k - j;
                }
            }
        }
    }
    return result;
}

# C#

class Global {
    public static int PentagonNumbers(int n) {
        HashSet<int> pentagon = new HashSet<int>();
        for (int i = 1; i < n; i++) {
            pentagon.Add(i * (3 * i - 1) / 2);
        }
        int result = -1;
        foreach (int j in pentagon) {
            foreach (int k in pentagon) {
                if (pentagon.Contains(j + k) && pentagon.Contains(k - j)) {
                    if (result == -1 || k - j < result) {
                        result = k - j;
                    }
                }
            }
        }
        return result;
    }
}

# Go

func PentagonNumbers(n int) int {
    pentagon := make(map[int]bool)
    for i := 1; i < n; i++ {
        pentagon[i * (3 * i - 1) / 2] = true
    }
    result := -1
    for j := range pentagon {
        for k := range pentagon {
            if pentagon[j + k] && pentagon[k - j] {
                if result == -1 || k - j < result {
                    result = k - j
                }
            }
        }
    }
    return result
}

# Java

class Global {
    public static int pentagonNumbers(int n) {
        Set<Integer> pentagon = new HashSet<>();
        for (int i = 1; i < n; i++) {
            pentagon.add(i * (3 * i - 1) / 2);
        }
        int result = -1;
        for (int j : pentagon) {
            for (int k : pentagon) {
                if (pentagon.contains(j + k) && pentagon.contains(k - j)) {
                    if (result == -1 || k - j < result) {
                        result = k - j;
                    }
                }
            }
        }
        return result;
    }
}

# JavaScript

const pentagonNumbers = (n) => {
    const pentagon = new Set();
    for (let i = 1; i < n; i++) {
        pentagon.add(i * (3 * i - 1) / 2);
    }
    let result = -1;
    for (let j of pentagon) {
        for (let k of pentagon) {
            if (pentagon.has(j + k) && pentagon.has(k - j)) {
                if (result == -1 || k - j < result) {
                    result = k - j;
                }
            }
        }
    }
    return result;
}

# Kotlin

fun pentagonNumbers(n: Int): Int {
    val pentagon = HashSet<Int>()
    for (i in 1 until n) {
        pentagon.add(i * (3 * i - 1) / 2)
    }
    var result = -1
    for (j in pentagon) {
        for (k in pentagon) {
            if (pentagon.contains(j + k) && pentagon.contains(k - j)) {
                if (result == -1 || k - j < result) {
                    result = k - j
                }
            }
        }
    }
    return result
}

# PHP

function pentagonNumbers($n) {
    $pentagon = array();
    for ($i = 1; $i < $n; $i++) {
        $pentagon[$i * (3 * $i - 1) / 2] = true;
    }
    $result = -1;
    foreach ($pentagon as $j => $value) {
        foreach ($pentagon as $k => $value) {
            if (isset($pentagon[$j + $k]) && isset($pentagon[$k - $j])) {
                if ($result == -1 || $k - $j < $result) {
                    $result = $k - $j;
                }
            }
        }
    }
    return $result;
}

# Ruby

def pentagon_numbers(n)
    pentagon = {}
    (1...n).each do |i|
        pentagon[i * (3 * i - 1) / 2] = true
    end
    result = -1
    pentagon.each do |j, _|
        pentagon.each do |k, _|
            if pentagon[j + k] && pentagon[k - j]
                if result == -1 || k - j < result
                    result = k - j
                end
            end
        end
    end
    result
end

# Rust

fn pentagon_numbers(n: i32) -> i32 {
    let mut pentagon = HashSet::new();
    for i in 1..n {
        pentagon.insert(i * (3 * i - 1) / 2);
    }
    let mut result = -1;
    for &j in &pentagon {
        for &k in &pentagon {
            if pentagon.contains(&(j + k)) && pentagon.contains(&(k - j)) {
                if result == -1 || k - j < result {
                    result = k - j;
                }
            }
        }
    }
    result
}

# Scala

def pentagonNumbers(n: Int): Int = {
    val pentagon = mutable.HashSet[Int]()
    for (i <- 1 until n) {
        pentagon.add(i * (3 * i - 1) / 2)
    }
    var result = -1
    for (j <- pentagon) {
        for (k <- pentagon) {
            if (pentagon.contains(j + k) && pentagon.contains(k - j)) {
                if (result == -1 || k - j < result) {
                    result = k - j
                }
            }
        }
    }
    result
}



