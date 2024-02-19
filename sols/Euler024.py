# Python

def lexicographic_permutations(n: int) -> str:
    result = ''
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = n - 1
    for i in range(10, 0, -1):
        fact = 1
        for j in range(1, i):
            fact *= j
        idx = x // fact
        result += str(digits[idx])
        digits.pop(idx)
        x -= idx * fact
    return result

# Start translation now

# C++

string lexicographicPermutations(int n) {
    string result = "";
    vector<int> digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int x = n - 1;
    for (int i = 10; i > 0; i--) {
        int fact = 1;
        for (int j = 1; j < i; j++) {
            fact *= j;
        }
        int idx = x / fact;
        result += to_string(digits[idx]);
        digits.erase(digits.begin() + idx);
        x -= idx * fact;
    }
    return result;
}

# C#

class Global {
    public static string LexicographicPermutations(int n) {
        string result = "";
        List<int> digits = new List<int> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int x = n - 1;
        for (int i = 10; i > 0; i--) {
            int fact = 1;
            for (int j = 1; j < i; j++) {
                fact *= j;
            }
            int idx = x / fact;
            result += digits[idx].ToString();
            digits.RemoveAt(idx);
            x -= idx * fact;
        }
        return result;
    }
}

# Go

func LexicographicPermutations(n int) string {
    result := ""
    digits := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    x := n - 1
    for i := 10; i > 0; i-- {
        fact := 1
        for j := 1; j < i; j++ {
            fact *= j
        }
        idx := x / fact
        result += strconv.Itoa(digits[idx])
        digits = append(digits[:idx], digits[idx+1:]...)
        x -= idx * fact
    }
    return result
}

# Java

class Global {
    public static String lexicographicPermutations(int n) {
        String result = "";
        List<Integer> digits = new ArrayList<>(Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9));
        int x = n - 1;
        for (int i = 10; i > 0; i--) {
            int fact = 1;
            for (int j = 1; j < i; j++) {
                fact *= j;
            }
            int idx = x / fact;
            result += digits.get(idx);
            digits.remove(idx);
            x -= idx * fact;
        }
        return result;
    }
}

# JavaScript

const lexicographicPermutations = (n) => {
    let result = "";
    let digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let x = n - 1;
    for (let i = 10; i > 0; i--) {
        let fact = 1;
        for (let j = 1; j < i; j++) {
            fact *= j;
        }
        let idx = Math.floor(x / fact);
        result += digits[idx];
        digits.splice(idx, 1);
        x -= idx * fact;
    }
    return result;
}

# Kotlin

fun lexicographicPermutations(n: Int): String {
    var result = ""
    var digits = mutableListOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    var x = n - 1
    for (i in 10 downTo 1) {
        var fact = 1
        for (j in 1 until i) {
            fact *= j
        }
        var idx = x / fact
        result += digits[idx]
        digits.removeAt(idx)
        x -= idx * fact
    }
    return result
}

# PHP

function lexicographicPermutations($n) {
    $result = "";
    $digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    $x = $n - 1;
    for ($i = 10; $i > 0; $i--) {
        $fact = 1;
        for ($j = 1; $j < $i; $j++) {
            $fact *= $j;
        }
        $idx = floor($x / $fact);
        $result .= $digits[$idx];
        array_splice($digits, $idx, 1);
        $x -= $idx * $fact;
    }
    return $result;
}

# Ruby

def lexicographic_permutations(n)
    result = ""
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = n - 1
    10.downto(1) do |i|
        fact = 1
        (1...i).each do |j|
            fact *= j
        end
        idx = x / fact
        result += digits[idx].to_s
        digits.delete_at(idx)
        x -= idx * fact
    end
    result
end

# Rust

fn lexicographic_permutations(n: i32) -> String {
    let mut result = String::new();
    let mut digits = vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let mut x = n - 1;
    for i in (1..11).rev() {
        let mut fact = 1;
        for j in 1..i {
            fact *= j;
        }
        let idx = x / fact;
        result.push_str(&digits[idx as usize].to_string());
        digits.remove(idx as usize);
        x -= idx * fact;
    }
    result
}

# Scala

def lexicographicPermutations(n: Int): String = {
    var result = ""
    var digits = List(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    var x = n - 1
    for (i <- 10 to 1 by -1) {
        var fact = 1
        for (j <- 1 until i) {
            fact *= j
        }
        var idx = x / fact
        result += digits(idx)
        digits = digits.patch(idx, Nil, 1)
        x -= idx * fact
    }
    result
}
