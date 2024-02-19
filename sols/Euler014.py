# Python

def longest_collatz_sequence(n: int) -> int:
    longest = 0
    result = 0
    for i in range(1, n):
        chain = 1
        num = i
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            chain += 1
        if chain > longest:
            longest = chain
            result = i
    return result

# Start translation now

# C++

int longestCollatzSequence(int n) {
    int longest = 0;
    int result = 0;
    for (int i = 1; i < n; i++) {
        int chain = 1;
        int num = i;
        while (num != 1) {
            if (num % 2 == 0) {
                num = num / 2;
            } else {
                num = 3 * num + 1;
            }
            chain++;
        }
        if (chain > longest) {
            longest = chain;
            result = i;
        }
    }
    return result;
}

# C#

class Global {
    public static int LongestCollatzSequence(int n) {
        int longest = 0;
        int result = 0;
        for (int i = 1; i < n; i++) {
            int chain = 1;
            int num = i;
            while (num != 1) {
                if (num % 2 == 0) {
                    num = num / 2;
                } else {
                    num = 3 * num + 1;
                }
                chain++;
            }
            if (chain > longest) {
                longest = chain;
                result = i;
            }
        }
        return result;
    }
}

# Go

func LongestCollatzSequence(n int) int {
    longest := 0
    result := 0
    for i := 1; i < n; i++ {
        chain := 1
        num := i
        for num != 1 {
            if num % 2 == 0 {
                num = num / 2
            } else {
                num = 3 * num + 1
            }
            chain++
        }
        if chain > longest {
            longest = chain
            result = i
        }
    }
    return result
}

# Java

class Global {
    public static int longestCollatzSequence(int n) {
        int longest = 0;
        int result = 0;
        for (int i = 1; i < n; i++) {
            int chain = 1;
            int num = i;
            while (num != 1) {
                if (num % 2 == 0) {
                    num = num / 2;
                } else {
                    num = 3 * num + 1;
                }
                chain++;
            }
            if (chain > longest) {
                longest = chain;
                result = i;
            }
        }
        return result;
    }
}

# JavaScript

const longestCollatzSequence = (n) => {
    let longest = 0;
    let result = 0;
    for (let i = 1; i < n; i++) {
        let chain = 1;
        let num = i;
        while (num != 1) {
            if (num % 2 == 0) {
                num = num / 2;
            } else {
                num = 3 * num + 1;
            }
            chain++;
        }
        if (chain > longest) {
            longest = chain;
            result = i;
        }
    }
    return result;
}

# Kotlin

fun longestCollatzSequence(n: Int): Int {
    var longest = 0
    var result = 0
    for (i in 1 until n) {
        var chain = 1
        var num = i
        while (num != 1) {
            if (num % 2 == 0) {
                num = num / 2
            } else {
                num = 3 * num + 1
            }
            chain++
        }
        if (chain > longest) {
            longest = chain
            result = i
        }
    }
    return result
}

# PHP

function longestCollatzSequence($n) {
    $longest = 0;
    $result = 0;
    for ($i = 1; $i < $n; $i++) {
        $chain = 1;
        $num = $i;
        while ($num != 1) {
            if ($num % 2 == 0) {
                $num = $num / 2;
            } else {
                $num = 3 * $num + 1;
            }
            $chain++;
        }
        if ($chain > $longest) {
            $longest = $chain;
            $result = $i;
        }
    }
    return $result;
}

# Ruby

def longest_collatz_sequence(n)
    longest = 0
    result = 0
    for i in 1...n
        chain = 1
        num = i
        while num != 1
            if num % 2 == 0
                num = num / 2
            else
                num = 3 * num + 1
            end
            chain += 1
        end
        if chain > longest
            longest = chain
            result = i
        end
    end
    result
end

# Rust

fn longest_collatz_sequence(n: i32) -> i32 {
    let mut longest = 0;
    let mut result = 0;
    for i in 1..n {
        let mut chain = 1;
        let mut num = i;
        while num != 1 {
            if num % 2 == 0 {
                num = num / 2;
            } else {
                num = 3 * num + 1;
            }
            chain += 1;
        }
        if chain > longest {
            longest = chain;
            result = i;
        }
    }
    result
}

# Scala

def longestCollatzSequence(n: Int): Int = {
    var longest = 0
    var result = 0
    for (i <- 1 until n) {
        var chain = 1
        var num = i
        while (num != 1) {
            if (num % 2 == 0) {
                num = num / 2
            } else {
                num = 3 * num + 1
            }
            chain += 1
        }
        if (chain > longest) {
            longest = chain
            result = i
        }
    }
    result
}
