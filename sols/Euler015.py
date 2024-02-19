# Python

def lattice_paths(m: int, n: int) -> int:
    grid = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        grid[i][0] = 1
    for j in range(n + 1):
        grid[0][j] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[m][n]

# Start translation now

# C++

int latticePaths(int m, int n) {
    vector<vector<int>> grid(m + 1, vector<int>(n + 1, 0));
    for (int i = 0; i <= m; i++) {
        grid[i][0] = 1;
    }
    for (int j = 0; j <= n; j++) {
        grid[0][j] = 1;
    }
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1];
        }
    }
    return grid[m][n];
}

# C#

class Global {
    public static int LatticePaths(int m, int n) {
        int[,] grid = new int[m + 1, n + 1];
        for (int i = 0; i <= m; i++) {
            grid[i, 0] = 1;
        }
        for (int j = 0; j <= n; j++) {
            grid[0, j] = 1;
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                grid[i, j] = grid[i - 1, j] + grid[i, j - 1];
            }
        }
        return grid[m, n];
    }
}

# Go

func LatticePaths(m int, n int) int {
    grid := make([][]int, m + 1)
    for i := 0; i <= m; i++ {
        grid[i] = make([]int, n + 1)
        grid[i][0] = 1
    }
    for j := 0; j <= n; j++ {
        grid[0][j] = 1
    }
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        }
    }
    return grid[m][n]
}

# Java

class Global {
    public static int latticePaths(int m, int n) {
        int[][] grid = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) {
            grid[i][0] = 1;
        }
        for (int j = 0; j <= n; j++) {
            grid[0][j] = 1;
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1];
            }
        }
        return grid[m][n];
    }
}

# JavaScript

const latticePaths = (m, n) => {
    const grid = new Array(m + 1).fill(0).map(() => new Array(n + 1).fill(0));
    for (let i = 0; i <= m; i++) {
        grid[i][0] = 1;
    }
    for (let j = 0; j <= n; j++) {
        grid[0][j] = 1;
    }
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1];
        }
    }
    return grid[m][n];
}

# Kotlin

fun latticePaths(m: Int, n: Int): Int {
    val grid = Array(m + 1) { IntArray(n + 1) { 0 } }
    for (i in 0..m) {
        grid[i][0] = 1
    }
    for (j in 0..n) {
        grid[0][j] = 1
    }
    for (i in 1..m) {
        for (j in 1..n) {
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        }
    }
    return grid[m][n]
}

# PHP

function latticePaths($m, $n) {
    $grid = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
    for ($i = 0; $i <= $m; $i++) {
        $grid[$i][0] = 1;
    }
    for ($j = 0; $j <= $n; $j++) {
        $grid[0][$j] = 1;
    }
    for ($i = 1; $i <= $m; $i++) {
        for ($j = 1; $j <= $n; $j++) {
            $grid[$i][$j] = $grid[$i - 1][$j] + $grid[$i][$j - 1];
        }
    }
    return $grid[$m][$n];
}

# Ruby

def lattice_paths(m, n)
    grid = Array.new(m + 1) { Array.new(n + 1, 0) }
    for i in 0..m
        grid[i][0] = 1
    end
    for j in 0..n
        grid[0][j] = 1
    end
    for i in 1..m
        for j in 1..n
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        end
    end
    return grid[m][n]
end

# Rust

fn lattice_paths(m: i32, n: i32) -> i32 {
    let mut grid = vec![vec![0; (n + 1) as usize]; (m + 1) as usize];
    for i in 0..=m {
        grid[i as usize][0] = 1;
    }
    for j in 0..=n {
        grid[0][j as usize] = 1;
    }
    for i in 1..=m {
        for j in 1..=n {
            grid[i as usize][j as usize] = grid[(i - 1) as usize][j as usize] + grid[i as usize][(j - 1) as usize];
        }
    }
    grid[m as usize][n as usize]
}

# Scala

def latticePaths(m: Int, n: Int): Int = {
    val grid = Array.ofDim[Int](m + 1, n + 1)
    for (i <- 0 to m) {
        grid(i)(0) = 1
    }
    for (j <- 0 to n) {
        grid(0)(j) = 1
    }
    for (i <- 1 to m) {
        for (j <- 1 to n) {
            grid(i)(j) = grid(i - 1)(j) + grid(i)(j - 1)
        }
    }
    grid(m)(n)
}


