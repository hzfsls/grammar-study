# Python

def integer_right_triangles(n: int) -> int:
    max_sol = 0
    result = 0
    for p in range(3, n + 1):
        sol = 0
        for a in range(1, p // 2):
            for b in range(a, p // 2):
                c = p - a - b
                if a * a + b * b == c * c:
                    sol += 1
        if sol > max_sol:
            max_sol = sol
            result = p
    return result

# Start translation now

# C++

int integerRightTriangles(int n) {
    int max_sol = 0;
    int result = 0;
    for (int p = 3; p <= n; p++) {
        int sol = 0;
        for (int a = 1; a < p / 2; a++) {
            for (int b = a; b < p / 2; b++) {
                int c = p - a - b;
                if (a * a + b * b == c * c) {
                    sol++;
                }
            }
        }
        if (sol > max_sol) {
            max_sol = sol;
            result = p;
        }
    }
    return result;
}

# C#

class Global {
    public static int IntegerRightTriangles(int n) {
        int maxSol = 0;
        int result = 0;
        for (int p = 3; p <= n; p++) {
            int sol = 0;
            for (int a = 1; a < p / 2; a++) {
                for (int b = a; b < p / 2; b++) {
                    int c = p - a - b;
                    if (a * a + b * b == c * c) {
                        sol++;
                    }
                }
            }
            if (sol > maxSol) {
                maxSol = sol;
                result = p;
            }
        }
        return result;
    }
}

# Go

func IntegerRightTriangles(n int) int {
    maxSol := 0
    result := 0
    for p := 3; p <= n; p++ {
        sol := 0
        for a := 1; a < p / 2; a++ {
            for b := a; b < p / 2; b++ {
                c := p - a - b
                if a * a + b * b == c * c {
                    sol++
                }
            }
        }
        if sol > maxSol {
            maxSol = sol
            result = p
        }
    }
    return result
}

# Java

class Global {
    public static int integerRightTriangles(int n) {
        int maxSol = 0;
        int result = 0;
        for (int p = 3; p <= n; p++) {
            int sol = 0;
            for (int a = 1; a < p / 2; a++) {
                for (int b = a; b < p / 2; b++) {
                    int c = p - a - b;
                    if (a * a + b * b == c * c) {
                        sol++;
                    }
                }
            }
            if (sol > maxSol) {
                maxSol = sol;
                result = p;
            }
        }
        return result;
    }
}

# JavaScript

const integerRightTriangles = (n) => {
    let maxSol = 0;
    let result = 0;
    for (let p = 3; p <= n; p++) {
        let sol = 0;
        for (let a = 1; a < p / 2; a++) {
            for (let b = a; b < p / 2; b++) {
                let c = p - a - b;
                if (a * a + b * b == c * c) {
                    sol++;
                }
            }
        }
        if (sol > maxSol) {
            maxSol = sol;
            result = p;
        }
    }
    return result;
}

# Kotlin

fun integerRightTriangles(n: Int): Int {
    var maxSol = 0
    var result = 0
    for (p in 3..n) {
        var sol = 0
        for (a in 1 until p / 2) {
            for (b in a until p / 2) {
                val c = p - a - b
                if (a * a + b * b == c * c) {
                    sol++
                }
            }
        }
        if (sol > maxSol) {
            maxSol = sol
            result = p
        }
    }
    return result
}

# PHP

function integerRightTriangles($n) {
    $maxSol = 0;
    $result = 0;
    for ($p = 3; $p <= $n; $p++) {
        $sol = 0;
        for ($a = 1; $a < $p / 2; $a++) {
            for ($b = $a; $b < $p / 2; $b++) {
                $c = $p - $a - $b;
                if ($a * $a + $b * $b == $c * $c) {
                    $sol++;
                }
            }
        }
        if ($sol > $maxSol) {
            $maxSol = $sol;
            $result = $p;
        }
    }
    return $result;
}

# Ruby

def integer_right_triangles(n)
    max_sol = 0
    result = 0
    for p in 3..n
        sol = 0
        for a in 1...p / 2
            for b in a...p / 2
                c = p - a - b
                if a * a + b * b == c * c
                    sol += 1
                end
            end
        end
        if sol > max_sol
            max_sol = sol
            result = p
        end
    end
    return result
end

# Rust

fn integer_right_triangles(n: i32) -> i32 {
    let mut max_sol = 0;
    let mut result = 0;
    for p in 3..=n {
        let mut sol = 0;
        for a in 1..p / 2 {
            for b in a..p / 2 {
                let c = p - a - b;
                if a * a + b * b == c * c {
                    sol += 1;
                }
            }
        }
        if sol > max_sol {
            max_sol = sol;
            result = p;
        }
    }
    result
}

# Scala

def integerRightTriangles(n: Int): Int = {
    var maxSol = 0
    var result = 0
    for (p <- 3 to n) {
        var sol = 0
        for (a <- 1 until p / 2) {
            for (b <- a until p / 2) {
                val c = p - a - b
                if (a * a + b * b == c * c) {
                    sol += 1
                }
            }
        }
        if (sol > maxSol) {
            maxSol = sol
            result = p
        }
    }
    result
}
