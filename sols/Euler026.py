# Python

def reciprocal_cycles(n: int) -> int:
    result = 0
    max_length = 0
    for i in range(1, n):
        remainders = []
        remainder = 1
        while remainder != 0 and remainder not in remainders:
            remainders.append(remainder)
            remainder = (remainder * 10) % i
        length = 0
        if remainder != 0:
            length = len(remainders) - remainders.index(remainder)
        if length > max_length:
            max_length = length
            result = i
    return result

# Start translation now

# C++

int reciprocalCycles(int n) {
    int result = 0;
    int max_length = 0;
    for (int i = 1; i < n; i++) {
        vector<int> remainders;
        int remainder = 1;
        while (remainder != 0 && find(remainders.begin(), remainders.end(), remainder) == remainders.end()) {
            remainders.push_back(remainder);
            remainder = (remainder * 10) % i;
        }
        int length = 0;
        if (remainder != 0) {
            length = remainders.size() - (find(remainders.begin(), remainders.end(), remainder) - remainders.begin());
        }
        if (length > max_length) {
            max_length = length;
            result = i;
        }
    }
    return result;
}

# C#

class Global {
    public static int ReciprocalCycles(int n) {
        int result = 0;
        int max_length = 0;
        for (int i = 1; i < n; i++) {
            List<int> remainders = new List<int>();
            int remainder = 1;
            while (remainder != 0 && !remainders.Contains(remainder)) {
                remainders.Add(remainder);
                remainder = (remainder * 10) % i;
            }
            int length = 0;
            if (remainder != 0) {
                length = remainders.Count - remainders.IndexOf(remainder);
            }
            if (length > max_length) {
                max_length = length;
                result = i;
            }
        }
        return result;
    }
}

# Go

func ReciprocalCycles(n int) int {
    result := 0
    max_length := 0
    for i := 1; i < n; i++ {
        remainders := []int{}
        remainder := 1
        for remainder != 0 && !slices.Contains(remainders, remainder) {
            remainders = append(remainders, remainder)
            remainder = (remainder * 10) % i
        }
        length := 0
        if remainder != 0 {
            length = len(remainders) - slices.Index(remainders, remainder)
        }
        if length > max_length {
            max_length = length
            result = i
        }
    }
    return result
}

# Java

class Global {
    public static int reciprocalCycles(int n) {
        int result = 0;
        int max_length = 0;
        for (int i = 1; i < n; i++) {
            List<Integer> remainders = new ArrayList<Integer>();
            int remainder = 1;
            while (remainder != 0 && !remainders.contains(remainder)) {
                remainders.add(remainder);
                remainder = (remainder * 10) % i;
            }
            int length = 0;
            if (remainder != 0) {
                length = remainders.size() - remainders.indexOf(remainder);
            }
            if (length > max_length) {
                max_length = length;
                result = i;
            }
        }
        return result;
    }
}

# JavaScript

const reciprocalCycles = (n) => {
    let result = 0;
    let max_length = 0;
    for (let i = 1; i < n; i++) {
        let remainders = [];
        let remainder = 1;
        while (remainder !== 0 && !remainders.includes(remainder)) {
            remainders.push(remainder);
            remainder = (remainder * 10) % i;
        }
        let length = 0;
        if (remainder !== 0) {
            length = remainders.length - remainders.indexOf(remainder);
        }
        if (length > max_length) {
            max_length = length;
            result = i;
        }
    }
    return result;
}

# Kotlin

fun reciprocalCycles(n: Int): Int {
    var result = 0
    var max_length = 0
    for (i in 1 until n) {
        val remainders = mutableListOf<Int>()
        var remainder = 1
        while (remainder != 0 && !remainders.contains(remainder)) {
            remainders.add(remainder)
            remainder = (remainder * 10) % i
        }
        var length = 0
        if (remainder != 0) {
            length = remainders.size - remainders.indexOf(remainder)
        }
        if (length > max_length) {
            max_length = length
            result = i
        }
    }
    return result
}

# PHP

function reciprocalCycles($n) {
    $result = 0;
    $max_length = 0;
    for ($i = 1; $i < $n; $i++) {
        $remainders = [];
        $remainder = 1;
        while ($remainder != 0 && !in_array($remainder, $remainders)) {
            array_push($remainders, $remainder);
            $remainder = ($remainder * 10) % $i;
        }
        $length = 0;
        if ($remainder != 0) {
            $length = count($remainders) - array_search($remainder, $remainders);
        }
        if ($length > $max_length) {
            $max_length = $length;
            $result = $i;
        }
    }
    return $result;
}

# Ruby

def reciprocal_cycles(n)
    result = 0
    max_length = 0
    for i in 1...n
        remainders = []
        remainder = 1
        while remainder != 0 && !remainders.include?(remainder)
            remainders.push(remainder)
            remainder = (remainder * 10) % i
        end
        length = 0
        if remainder != 0
            length = remainders.length - remainders.index(remainder)
        end
        if length > max_length
            max_length = length
            result = i
        end
    end
    result
end

# Rust

fn reciprocal_cycles(n: i32) -> i32 {
    let mut result = 0;
    let mut max_length = 0;
    for i in 1..n {
        let mut remainders = vec![];
        let mut remainder = 1;
        while remainder != 0 && !remainders.contains(&remainder) {
            remainders.push(remainder);
            remainder = (remainder * 10) % i;
        }
        let mut length = 0;
        if remainder != 0 {
            length = remainders.len() - remainders.iter().position(|&x| x == remainder).unwrap();
        }
        if length > max_length {
            max_length = length;
            result = i;
        }
    }
    result
}

# Scala

def reciprocalCycles(n: Int): Int = {
    var result = 0
    var maxLength = 0
    for (i <- 1 until n) {
        val remainders = ArrayBuffer[Int]()
        var remainder = 1
        while (remainder != 0 && !remainders.contains(remainder)) {
            remainders += remainder
            remainder = (remainder * 10) % i
        }
        var length = 0
        if (remainder != 0) {
            length = remainders.length - remainders.indexOf(remainder)
        }
        if (length > maxLength) {
            maxLength = length
            result = i
        }
    }
    result
}
