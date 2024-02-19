# Python

def pandigital_products(n: int) -> int:
    products = set()
    s = ''.join(str(i) for i in range(1, n+1))
    for a in range(1, 100):
        for b in range(1, 10000):
            c = a * b
            chars = list(str(a) + str(b) + str(c))
            chars.sort()
            if ''.join(chars) == s:
                products.add(c)
    result = 0
    for product in products:
        result += product
    return result

# Start translation now

# C++

int pandigitalProducts(int n) {
    unordered_set<int> products;
    string s;
    for (int i = 1; i <= n; i++) {
        s += to_string(i);
    }
    for (int a = 1; a < 100; a++) {
        for (int b = 1; b < 10000; b++) {
            int c = a * b;
            string chars = to_string(a) + to_string(b) + to_string(c);
            sort(chars.begin(), chars.end());
            if (chars == s) {
                products.insert(c);
            }
        }
    }
    int result = 0;
    for (int product : products) {
        result += product;
    }
    return result;
}

# C#

class Global {
    public static int PandigitalProducts(int n) {
        HashSet<int> products = new HashSet<int>();
        string s = "";
        for (int i = 1; i <= n; i++) {
            s += i.ToString();
        }
        for (int a = 1; a < 100; a++) {
            for (int b = 1; b < 10000; b++) {
                int c = a * b;
                char[] chars = (a.ToString() + b.ToString() + c.ToString()).ToCharArray();
                Array.Sort(chars);
                if (new string(chars) == s) {
                    products.Add(c);
                }
            }
        }
        int result = 0;
        foreach (int product in products) {
            result += product;
        }
        return result;
    }
}

# Go

func PandigitalProducts(n int) int {
    products := make(map[int]bool)
    s := ""
    for i := 1; i <= n; i++ {
        s += strconv.Itoa(i)
    }
    for a := 1; a < 100; a++ {
        for b := 1; b < 10000; b++ {
            c := a * b
            chars := []rune(strconv.Itoa(a) + strconv.Itoa(b) + strconv.Itoa(c))
            slices.Sort(chars)
            if string(chars) == s {
                products[c] = true
            }
        }
    }
    result := 0
    for product := range products {
        result += product
    }
    return result
}

# Java

class Global {
    public static int pandigitalProducts(int n) {
        Set<Integer> products = new HashSet<>();
        String s = "";
        for (int i = 1; i <= n; i++) {
            s += i;
        }
        for (int a = 1; a < 100; a++) {
            for (int b = 1; b < 10000; b++) {
                int c = a * b;
                char[] chars = (Integer.toString(a) + Integer.toString(b) + Integer.toString(c)).toCharArray();
                Arrays.sort(chars);
                if (new String(chars).equals(s)) {
                    products.add(c);
                }
            }
        }
        int result = 0;
        for (int product : products) {
            result += product;
        }
        return result;
    }
}

# JavaScript

const pandigitalProducts = (n) => {
    const products = new Set();
    let s = "";
    for (let i = 1; i <= n; i++) {
        s += i;
    }
    for (let a = 1; a < 100; a++) {
        for (let b = 1; b < 10000; b++) {
            const c = a * b;
            let chars = (a.toString() + b.toString() + c.toString()).split("");
            chars.sort();
            if (chars.join("") === s) {
                products.add(c);
            }
        }
    }
    let result = 0;
    for (let product of products) {
        result += product;
    }
    return result;
}

# Kotlin

fun pandigitalProducts(n: Int): Int {
    val products = HashSet<Int>()
    var s = ""
    for (i in 1..n) {
        s += i
    }
    for (a in 1 until 100) {
        for (b in 1 until 10000) {
            val c = a * b
            var chars = (a.toString() + b.toString() + c.toString()).toCharArray()
            chars.sort()
            if (chars.joinToString("") == s) {
                products.add(c)
            }
        }
    }
    var result = 0
    for (product in products) {
        result += product
    }
    return result
}

# PHP

function pandigitalProducts($n) {
    $products = [];
    $s = "";
    for ($i = 1; $i <= $n; $i++) {
        $s .= $i;
    }
    for ($a = 1; $a < 100; $a++) {
        for ($b = 1; $b < 10000; $b++) {
            $c = $a * $b;
            $chars = str_split(strval($a) . strval($b) . strval($c));
            sort($chars);
            if (implode("", $chars) === $s) {
                $products[$c] = true;
            }
        }
    }
    $result = 0;
    foreach (array_keys($products) as $product) {
        $result += $product;
    }
    return $result;
}

# Ruby

def pandigital_products(n)
    products = Set.new
    s = ""
    for i in 1..n
        s += i.to_s
    end
    for a in 1...100
        for b in 1...10000
            c = a * b
            chars = (a.to_s + b.to_s + c.to_s).chars
            chars.sort!
            if chars.join("") == s
                products.add(c)
            end
        end
    end
    result = 0
    for product in products
        result += product
    end
    return result
end

# Rust

fn pandigital_products(n: i32) -> i32 {
    let mut products = HashSet::new();
    let mut s = String::new();
    for i in 1..=n {
        s.push_str(&i.to_string());
    }
    for a in 1..100 {
        for b in 1..10000 {
            let c = a * b;
            let mut chars = (a.to_string() + &b.to_string() + &c.to_string()).chars().collect::<Vec<char>>();
            chars.sort();
            if chars.into_iter().collect::<String>() == s {
                products.insert(c);
            }
        }
    }
    let mut result = 0;
    for product in products {
        result += product;
    }
    result
}

# Scala

def pandigitalProducts(n: Int): Int = {
    val products = HashSet[Int]()
    var s = ""
    for (i <- 1 to n) {
        s += i
    }
    for (a <- 1 until 100) {
        for (b <- 1 until 10000) {
            val c = a * b
            var chars = (a.toString + b.toString + c.toString).toCharArray
            chars = chars.sorted
            if (chars.mkString == s) {
                products.add(c)
            }
        }
    }
    var result = 0
    for (product <- products) {
        result += product
    }
    result
}


