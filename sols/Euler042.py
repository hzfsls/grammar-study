# Python

def coded_triangle_numbers(words: list[str]) -> int:
    result = 0
    for word in words:
        value = 0
        for c in word:
            value += ord(c) - 64
        n = int((value * 2) ** 0.5)
        if n * (n + 1) == value * 2:
            result += 1
    return result

# Start translation now

# C++

int codedTriangleNumbers(const vector<string>& words) {
    int result = 0;
    for (const string& word : words) {
        int value = 0;
        for (char c : word) {
            value += c - 64;
        }
        int n = int(sqrt(value * 2));
        if (n * (n + 1) == value * 2) {
            result++;
        }
    }
    return result;
}

# C#

class Global {
    public static int CodedTriangleNumbers(IList<string> words) {
        int result = 0;
        foreach (string word in words) {
            int value = 0;
            foreach (char c in word) {
                value += c - 64;
            }
            int n = (int)Math.Sqrt(value * 2);
            if (n * (n + 1) == value * 2) {
                result++;
            }
        }
        return result;
    }
}

# Go

func CodedTriangleNumbers(words []string) int {
    result := 0
    for _, word := range words {
        value := 0
        for _, c := range word {
            value += int(c) - 64
        }
        n := int(math.Sqrt(float64(value * 2)))
        if n * (n + 1) == value * 2 {
            result++
        }
    }
    return result
}

# Java

class Global {
    public static int codedTriangleNumbers(List<String> words) {
        int result = 0;
        for (String word : words) {
            int value = 0;
            for (char c : word.toCharArray()) {
                value += c - 64;
            }
            int n = (int)Math.sqrt(value * 2);
            if (n * (n + 1) == value * 2) {
                result++;
            }
        }
        return result;
    }
}

# JavaScript

const codedTriangleNumbers = (words) => {
    let result = 0;
    for (let word of words) {
        let value = 0;
        for (let c of word) {
            value += c.charCodeAt(0) - 64;
        }
        let n = parseInt(Math.sqrt(value * 2));
        if (n * (n + 1) === value * 2) {
            result++;
        }
    }
    return result;
}

# Kotlin

fun codedTriangleNumbers(words: List<String>): Int {
    var result = 0
    for (word in words) {
        var value = 0
        for (c in word) {
            value += c.toInt() - 64
        }
        val n = Math.sqrt((value * 2).toDouble()).toInt()
        if (n * (n + 1) == value * 2) {
            result++
        }
    }
    return result
}

# PHP

function codedTriangleNumbers($words) {
    $result = 0;
    foreach ($words as $word) {
        $value = 0;
        for ($i = 0; $i < strlen($word); $i++) {
            $value += ord($word[$i]) - 64;
        }
        $n = intval(sqrt($value * 2));
        if ($n * ($n + 1) == $value * 2) {
            $result++;
        }
    }
    return $result;
}

# Ruby

def coded_triangle_numbers(words)
    result = 0
    words.each do |word|
        value = 0
        word.each_char do |c|
            value += c.ord - 64
        end
        n = Math.sqrt(value * 2).to_i
        if n * (n + 1) == value * 2
            result += 1
        end
    end
    result
end

# Rust

fn coded_triangle_numbers(words: &Vec<String>) -> i32 {
    let mut result = 0;
    for word in words {
        let mut value = 0;
        for c in word.chars() {
            value += c as i32 - 64;
        }
        let n = ((value * 2) as f64).sqrt() as i32;
        if n * (n + 1) == value * 2 {
            result += 1;
        }
    }
    result
}

# Scala

def codedTriangleNumbers(words: Seq[String]): Int = {
    var result = 0
    for (word <- words) {
        var value = 0
        for (c <- word) {
            value += c.toInt - 64
        }
        val n = math.sqrt(value * 2).toInt
        if (n * (n + 1) == value * 2) {
            result += 1
        }
    }
    result
}
