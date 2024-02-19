# Python

def highly_divisible_triangular_number(n: int) -> int:
    for i in range(1, 100000000):
        result = i * (i + 1) // 2
        count = 0
        for j in range(1, int(math.sqrt(result)) + 1):
            if result % j == 0:
                count += 2
            if j ** 2 == result:
                count -= 1
        if count > n:
            return result
    return -1

# Start translation now

# C++

int highlyDivisibleTriangularNumber(int n) {
    for (int i = 1; i < 100000000; i++) {
        int result = i * (i + 1) / 2;
        int count = 0;
        for (int j = 1; j <= (int)sqrt(result); j++) {
            if (result % j == 0) {
                count += 2;
            }
            if (j * j == result) {
                count -= 1;
            }
        }
        if (count > n) {
            return result;
        }
    }
    return -1;
}

# C#

class Global {
    public static int HighlyDivisibleTriangularNumber(int n) {
        for (int i = 1; i < 100000000; i++) {
            int result = i * (i + 1) / 2;
            int count = 0;
            for (int j = 1; j <= (int)Math.Sqrt(result); j++) {
                if (result % j == 0) {
                    count += 2;
                }
                if (j * j == result) {
                    count -= 1;
                }
            }
            if (count > n) {
                return result;
            }
        }
        return -1;
    }    
}

# Go

func HighlyDivisibleTriangularNumber(n int) int {
    for i := 1; i < 100000000; i++ {
        result := i * (i + 1) / 2
        count := 0
        for j := 1; j <= int(math.Sqrt(float64(result))); j++ {
            if result % j == 0 {
                count += 2
            }
            if j * j == result {
                count -= 1
            }
        }
        if count > n {
            return result
        }
    }
    return -1
}

# Java

class Global {
    public static int highlyDivisibleTriangularNumber(int n) {
        for (int i = 1; i < 100000000; i++) {
            int result = i * (i + 1) / 2;
            int count = 0;
            for (int j = 1; j <= (int)Math.sqrt(result); j++) {
                if (result % j == 0) {
                    count += 2;
                }
                if (j * j == result) {
                    count -= 1;
                }
            }
            if (count > n) {
                return result;
            }
        }
        return -1;
    }
}

# JavaScript

const highlyDivisibleTriangularNumber = (n) => {
    for (let i = 1; i < 100000000; i++) {
        let result = i * (i + 1) / 2;
        let count = 0;
        for (let j = 1; j <= Math.trunc(Math.sqrt(result)); j++) {
            if (result % j == 0) {
                count += 2;
            }
            if (j * j == result) {
                count -= 1;
            }
        }
        if (count > n) {
            return result;
        }
    }
    return -1;
}

# Kotlin

fun highlyDivisibleTriangularNumber(n: Int): Int {
    for (i in 1 until 100000000) {
        val result = i * (i + 1) / 2
        var count = 0
        for (j in 1..sqrt(result.toDouble()).toInt()) {
            if (result % j == 0) {
                count += 2
            }
            if (j * j == result) {
                count -= 1
            }
        }
        if (count > n) {
            return result
        }
    }
    return -1
}

# PHP

function highlyDivisibleTriangularNumber($n) {
    for ($i = 1; $i < 100000000; $i++) {
        $result = $i * ($i + 1) / 2;
        $count = 0;
        for ($j = 1; $j <= intval(sqrt($result)); $j++) {
            if ($result % $j == 0) {
                $count += 2;
            }
            if ($j * $j == $result) {
                $count -= 1;
            }
        }
        if ($count > $n) {
            return $result;
        }
    }
    return -1;
}

# Ruby

def highly_divisible_triangular_number(n)
    for i in 1...100000000
        result = i * (i + 1) / 2
        count = 0
        for j in 1..Math.sqrt(result).to_i
            if result % j == 0
                count += 2
            end
            if j * j == result
                count -= 1
            end
        end
        if count > n
            return result
        end
    end
    -1
end

# Rust

fn highly_divisible_triangular_number(n: i32) -> i32 {
    for i in 1..100000000 {
        let result = i * (i + 1) / 2;
        let mut count = 0;
        for j in 1..=(result as f64).sqrt() as i32 {
            if result % j == 0 {
                count += 2;
            }
            if j * j == result {
                count -= 1;
            }
        }
        if count > n {
            return result;
        }
    }
    -1
}

# Scala

def highlyDivisibleTriangularNumber(n: Int): Int = {
    for (i <- 1 until 100000000) {
        val result = i * (i + 1) / 2
        var count = 0
        for (j <- 1 to Math.sqrt(result).toInt) {
            if (result % j == 0) {
                count += 2
            }
            if (j * j == result) {
                count -= 1
            }
        }
        if (count > n) {
            return result
        }
    }
    -1
}


