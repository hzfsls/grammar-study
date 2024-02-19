# Python

def champernowne_constant(b: int) -> int:
    s = ''
    for i in range(1, b**6):
        s += str(i)
    result = 1
    for i in range(7):
        result *= int(s[b**i - 1])
    return result

# Start translation now

# C++

int champernowneConstant(int b) {
    string s = "";
    for (int i = 1; i < pow(b, 6); i++) {
        s += to_string(i);
    }
    int result = 1;
    for (int i = 0; i < 7; i++) {
        result *= s[pow(b, i) - 1] - '0';
    }
    return result;
}

# C#

class Global {
    public static int ChampernowneConstant(int b) {
        string s = "";
        for (int i = 1; i < Math.Pow(b, 6); i++) {
            s += i.ToString();
        }
        int result = 1;
        for (int i = 0; i < 7; i++) {
            result *= s[(int)Math.Pow(b, i) - 1] - '0';
        }
        return result;
    }
}

# Go

func ChampernowneConstant(b int) int {
    s := ""
    for i := 1; i < int(math.Pow(float64(b), 6)); i++ {
        s += strconv.Itoa(i)
    }
    result := 1
    for i := 0; i < 7; i++ {
        n, _ := strconv.Atoi(string(s[int(math.Pow(float64(b), float64(i))) - 1]))
        result *= n
    }
    return result
}

# Java

class Global {
    public static int champernowneConstant(int b) {
        String s = "";
        for (int i = 1; i < Math.pow(b, 6); i++) {
            s += Integer.toString(i);
        }
        int result = 1;
        for (int i = 0; i < 7; i++) {
            result *= s.charAt((int)Math.pow(b, i) - 1) - '0';
        }
        return result;
    }
}

# JavaScript

const champernowneConstant = (b) => {
    let s = "";
    for (let i = 1; i < Math.pow(b, 6); i++) {
        s += i.toString();
    }
    let result = 1;
    for (let i = 0; i < 7; i++) {
        result *= parseInt(s[Math.pow(b, i) - 1]);
    }
    return result;
}

# Kotlin

fun champernowneConstant(b: Int): Int {
    var s = ""
    for (i in 1 until b.toDouble().pow(6).toInt()) {
        s += i.toString()
    }
    var result = 1
    for (i in 0 until 7) {
        result *= s[b.toDouble().pow(i).toInt() - 1] - '0'
    }
    return result
}

# PHP

function champernowneConstant($b) {
    $s = "";
    for ($i = 1; $i < pow($b, 6); $i++) {
        $s .= strval($i);
    }
    $result = 1;
    for ($i = 0; $i < 7; $i++) {
        $result *= intval($s[pow($b, $i) - 1]);
    }
    return $result;
}

# Ruby

def champernowne_constant(b)
    s = ""
    (1..b**6).each do |i|
        s += i.to_s
    end
    result = 1
    (0..6).each do |i|
        result *= s[b**i - 1].to_i
    end
    result
end

# Rust

fn champernowne_constant(b: i32) -> i32 {
    let mut s = String::new();
    for i in 1..i32::pow(b, 6) {
        s += &i.to_string();
    }
    let mut result = 1;
    for i in 0..7 {
        result *= s.chars().nth(i32::pow(b, i) as usize - 1).unwrap().to_digit(10).unwrap() as i32;
    }
    result
}

# Scala

def champernowneConstant(b: Int): Int = {
    var s = ""
    for (i <- 1 until math.pow(b, 6).toInt) {
        s += i.toString
    }
    var result = 1
    for (i <- 0 until 7) {
        result *= s(math.pow(b, i).toInt - 1).asDigit
    }
    result
}


