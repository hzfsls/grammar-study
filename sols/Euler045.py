# Python

def triangular_pentagonal_and_hexagonal(n: int) -> int:
    ps = set()
    i = 1
    c = 0.5 * i * (3 * i - 1)
    while c < n:
        i += 1
        ps.add(c)
        c = 0.5 * i * (3 * i - 1)     
    i = 1
    c = i * (2 * i - 1)
    result = -1
    while c < n:
        i += 1
        if c in ps:
            result = c
        c = i * (2 * i - 1)
    return result

# Start translation now

# C++

int triangularPentagonalAndHexagonal(int n) {
    unordered_set<int> ps;
    int i = 1;
    int c = 0.5 * i * (3 * i - 1);
    while (c < n) {
        i++;
        ps.insert(c);
        c = 0.5 * i * (3 * i - 1);
    }
    i = 1;
    c = i * (2 * i - 1);
    int result = -1;
    while (c < n) {
        i++;
        if (ps.find(c) != ps.end()) {
            result = c;
        }
        c = i * (2 * i - 1);
    }
    return result;
}

# C#

class Global {
    public static int TriangularPentagonalAndHexagonal(int n) {
        HashSet<int> ps = new HashSet<int>();
        int i = 1;
        int c = (int)(0.5 * i * (3 * i - 1));
        while (c < n) {
            i++;
            ps.Add(c);
            c = (int)(0.5 * i * (3 * i - 1));
        }
        i = 1;
        c = i * (2 * i - 1);
        int result = -1;
        while (c < n) {
            i++;
            if (ps.Contains(c)) {
                result = c;
            }
            c = i * (2 * i - 1);
        }
        return result;
    }
}

# Go

func TriangularPentagonalAndHexagonal(n int) int {
    ps := make(map[int]bool)
    i := 1
    c := int(0.5 * float64(i) * (3 * float64(i) - 1))
    for c < n {
        i++
        ps[c] = true
        c = int(0.5 * float64(i) * (3 * float64(i) - 1))
    }
    i = 1
    c = i * (2 * i - 1)
    result := -1
    for c < n {
        i++
        if ps[c] {
            result = c
        }
        c = i * (2 * i - 1)
    }
    return result
}

# Java

class Global {
    public static int triangularPentagonalAndHexagonal(int n) {
        HashSet<Integer> ps = new HashSet<Integer>();
        int i = 1;
        int c = (int)(0.5 * i * (3 * i - 1));
        while (c < n) {
            i++;
            ps.add(c);
            c = (int)(0.5 * i * (3 * i - 1));
        }
        i = 1;
        c = i * (2 * i - 1);
        int result = -1;
        while (c < n) {
            i++;
            if (ps.contains(c)) {
                result = c;
            }
            c = i * (2 * i - 1);
        }
        return result;
    }
}

# JavaScript

const triangularPentagonalAndHexagonal = (n) => {
    const ps = new Set();
    let i = 1;
    let c = 0.5 * i * (3 * i - 1);
    while (c < n) {
        i++;
        ps.add(c);
        c = 0.5 * i * (3 * i - 1);
    }
    i = 1;
    c = i * (2 * i - 1);
    let result = -1;
    while (c < n) {
        i++;
        if (ps.has(c)) {
            result = c;
        }
        c = i * (2 * i - 1);
    }
    return result;
}

# Kotlin

fun triangularPentagonalAndHexagonal(n: Int): Int {
    val ps = HashSet<Int>()
    var i = 1
    var c = (0.5 * i * (3 * i - 1)).toInt()
    while (c < n) {
        i++
        ps.add(c)
        c = (0.5 * i * (3 * i - 1)).toInt()
    }
    i = 1
    c = i * (2 * i - 1)
    var result = -1
    while (c < n) {
        i++
        if (ps.contains(c)) {
            result = c
        }
        c = i * (2 * i - 1)
    }
    return result
}

# PHP

function triangularPentagonalAndHexagonal($n) {
    $ps = [];
    $i = 1;
    $c = 0.5 * $i * (3 * $i - 1);
    while ($c < $n) {
        $i++;
        $ps[$c] = true;
        $c = 0.5 * $i * (3 * $i - 1);
    }
    $i = 1;
    $c = $i * (2 * $i - 1);
    $result = -1;
    while ($c < $n) {
        $i++;
        if (isset($ps[$c])) {
            $result = $c;
        }
        $c = $i * (2 * $i - 1);
    }
    return $result;
}

# Ruby

def triangular_pentagonal_and_hexagonal(n)
    ps = Set.new
    i = 1
    c = (0.5 * i * (3 * i - 1)).to_i
    while c < n
        i += 1
        ps.add(c)
        c = (0.5 * i * (3 * i - 1)).to_i
    end
    i = 1
    c = i * (2 * i - 1)
    result = -1
    while c < n
        i += 1
        if ps.include?(c)
            result = c
        end
        c = i * (2 * i - 1)
    end
    return result
end

# Rust

fn triangular_pentagonal_and_hexagonal(n: i32) -> i32 {
    let mut ps = HashSet::new();
    let mut i = 1;
    let mut c = (0.5 * i as f64 * (3 * i - 1) as f64) as i32;
    while c < n {
        i += 1;
        ps.insert(c);
        c = (0.5 * i as f64 * (3 * i - 1) as f64) as i32;
    }
    i = 1;
    c = i * (2 * i - 1);
    let mut result = -1;
    while c < n {
        i += 1;
        if ps.contains(&c) {
            result = c;
        }
        c = i * (2 * i - 1);
    }
    result
}

# Scala

def triangularPentagonalAndHexagonal(n: Int): Int = {
    val ps = HashSet[Int]()
    var i = 1
    var c = (0.5 * i * (3 * i - 1)).toInt
    while (c < n) {
        i += 1
        ps.add(c)
        c = (0.5 * i * (3 * i - 1)).toInt
    }
    i = 1
    c = i * (2 * i - 1)
    var result = -1
    while (c < n) {
        i += 1
        if (ps.contains(c)) {
            result = c
        }
        c = i * (2 * i - 1)
    }
    result
}