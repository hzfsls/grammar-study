# Python

def n_digit_fibonacci_number(n: int) -> int:
    a = [1]
    b = [1]
    i = 2
    while len(b) < n:
        carry = 0
        c = b.copy()
        for j in range(len(b)):
            if j < len(a):
                b[j] = a[j] + b[j] + carry
            else:
                b[j] = b[j] + carry
            carry = b[j] // 10
            b[j] = b[j] % 10
        if carry:
            b.append(carry)
        a = c
        i = i + 1
    return i

# Start translation now

# C++

int nDigitFibonacciNumber(int n) {
    vector<int> a = {1};
    vector<int> b = {1};
    int i = 2;
    while (b.size() < n) {
        int carry = 0;
        vector<int> c = b;
        for (int j = 0; j < b.size(); j++) {
            if (j < a.size()) {
                b[j] = a[j] + b[j] + carry;
            } else {
                b[j] = b[j] + carry;
            }
            carry = b[j] / 10;
            b[j] = b[j] % 10;
        }
        if (carry) {
            b.push_back(carry);
        }
        a = c;
        i = i + 1;
    }
    return i;
}

# C#

class Global {
    public static int NDigitFibonacciNumber(int n) {
        List<int> a = new List<int> {1};
        List<int> b = new List<int> {1};
        int i = 2;
        while (b.Count < n) {
            int carry = 0;
            List<int> c = new List<int>(b);
            for (int j = 0; j < b.Count; j++) {
                if (j < a.Count) {
                    b[j] = a[j] + b[j] + carry;
                } else {
                    b[j] = b[j] + carry;
                }
                carry = b[j] / 10;
                b[j] = b[j] % 10;
            }
            if (carry != 0) {
                b.Add(carry);
            }
            a = new List<int>(c);
            i = i + 1;
        }
        return i;
    }
}

# Go

func NDigitFibonacciNumber(n int) int {
    a := []int{1}
    b := []int{1}
    i := 2
    for len(b) < n {
        carry := 0
        c := make([]int, len(b))
        copy(c, b)
        for j := 0; j < len(b); j++ {
            if j < len(a) {
                b[j] = a[j] + b[j] + carry
            } else {
                b[j] = b[j] + carry
            }
            carry = b[j] / 10
            b[j] = b[j] % 10
        }
        if carry != 0 {
            b = append(b, carry)
        }
        a = make([]int, len(c))
        copy(a, c)
        i = i + 1
    }
    return i
}

# Java

class Global {
    public static int nDigitFibonacciNumber(int n) {
        List<Integer> a = new ArrayList<Integer>(Arrays.asList(1));
        List<Integer> b = new ArrayList<Integer>(Arrays.asList(1));
        int i = 2;
        while (b.size() < n) {
            int carry = 0;
            List<Integer> c = new ArrayList<Integer>(b);
            for (int j = 0; j < b.size(); j++) {
                if (j < a.size()) {
                    b.set(j, a.get(j) + b.get(j) + carry);
                } else {
                    b.set(j, b.get(j) + carry);
                }
                carry = b.get(j) / 10;
                b.set(j, b.get(j) % 10);
            }
            if (carry != 0) {
                b.add(carry);
            }
            a = new ArrayList<Integer>(c);
            i = i + 1;
        }
        return i;
    }
}

# JavaScript

const nDigitFibonacciNumber = (n) => {
    let a = [1];
    let b = [1];
    let i = 2;
    while (b.length < n) {
        let carry = 0;
        let c = b.slice();
        for (let j = 0; j < b.length; j++) {
            if (j < a.length) {
                b[j] = a[j] + b[j] + carry;
            } else {
                b[j] = b[j] + carry;
            }
            carry = Math.floor(b[j] / 10);
            b[j] = b[j] % 10;
        }
        if (carry) {
            b.push(carry);
        }
        a = c;
        i = i + 1;
    }
    return i;
}

# Kotlin

fun nDigitFibonacciNumber(n: Int): Int {
    var a = listOf(1)
    var b = listOf(1)
    var i = 2
    while (b.size < n) {
        var carry = 0
        val c = b.toMutableList()
        for (j in b.indices) {
            if (j < a.size) {
                b = b.toMutableList()
                b[j] = a[j] + b[j] + carry
            } else {
                b = b.toMutableList()
                b[j] = b[j] + carry
            }
            carry = b[j] / 10
            b = b.toMutableList()
            b[j] = b[j] % 10
        }
        if (carry != 0) {
            b = b.toMutableList()
            b = b + carry
        }
        a = c
        i = i + 1
    }
    return i
}

# PHP

function nDigitFibonacciNumber($n) {
    $a = [1];
    $b = [1];
    $i = 2;
    while (count($b) < $n) {
        $carry = 0;
        $c = $b;
        for ($j = 0; $j < count($b); $j++) {
            if ($j < count($a)) {
                $b[$j] = $a[$j] + $b[$j] + $carry;
            } else {
                $b[$j] = $b[$j] + $carry;
            }
            $carry = intdiv($b[$j], 10);
            $b[$j] = $b[$j] % 10;
        }
        if ($carry != 0) {
            array_push($b, $carry);
        }
        $a = $c;
        $i = $i + 1;
    }
    return $i;
}

# Ruby

def n_digit_fibonacci_number(n)
    a = [1]
    b = [1]
    i = 2
    while b.length < n
        carry = 0
        c = b.clone
        b.each_with_index do |_, j|
            if j < a.length
                b[j] = a[j] + b[j] + carry
            else
                b[j] = b[j] + carry
            end
            carry = b[j] / 10
            b[j] = b[j] % 10
        end
        if carry != 0
            b.push(carry)
        end
        a = c
        i = i + 1
    end
    i
end

# Rust

fn n_digit_fibonacci_number(n: i32) -> i32 {
    let mut a = vec![1];
    let mut b = vec![1];
    let mut i = 2;
    while b.len() < n as usize {
        let mut carry = 0;
        let c = b.clone();
        for j in 0..b.len() {
            if j < a.len() {
                b[j] = a[j] + b[j] + carry;
            } else {
                b[j] = b[j] + carry;
            }
            carry = b[j] / 10;
            b[j] = b[j] % 10;
        }
        if carry != 0 {
            b.push(carry);
        }
        a = c;
        i = i + 1;
    }
    i
}

# Scala

def nDigitFibonacciNumber(n: Int): Int = {
    val a = ArrayBuffer(1)
    val b = ArrayBuffer(1)
    var i = 2
    while (b.length < n) {
        var carry = 0
        val c = b.clone
        for (j <- b.indices) {
            if (j < a.length) {
                b(j) = a(j) + b(j) + carry
            } else {
                b(j) = b(j) + carry
            }
            carry = b(j) / 10
            b(j) = b(j) % 10
        }
        if (carry != 0) {
            b += carry
        }
        a.clear
        a ++= c
        i = i + 1
    }
    i
}


