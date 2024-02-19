# Python

def largest_product_in_a_grid(grid: list[list[int]]) -> int:
    result = 0
    for i in range(len(grid) - 3):
        for j in range(len(grid[i]) - 3):
            p1, p2, p3, p4 = 1, 1, 1, 1
            for k in range(4):
                p1 *= grid[i + k][j]
            for k in range(4):
                p2 *= grid[i][j + k]
            for k in range(4):
                p3 *= grid[i + k][j + k]
            for k in range(4):
                p4 *= grid[i + k][j + 3 - k]
            result = max(result, p1, p2, p3, p4)
    return result

# Start translation now

# C++

int largestProductInAGrid(const vector<vector<int>>& grid) {
    int result = 0;
    for (int i = 0; i < grid.size() - 3; i++) {
        for (int j = 0; j < grid[i].size() - 3; j++) {
            int p1 = 1, p2 = 1, p3 = 1, p4 = 1;
            for (int k = 0; k < 4; k++) {
                p1 *= grid[i + k][j];
            }
            for (int k = 0; k < 4; k++) {
                p2 *= grid[i][j + k];
            }
            for (int k = 0; k < 4; k++) {
                p3 *= grid[i + k][j + k];
            }
            for (int k = 0; k < 4; k++) {
                p4 *= grid[i + k][j + 3 - k];
            }
            result = max({result, p1, p2, p3, p4});
        }
    }
    return result;
}

# C#

class Global {
    public static int LargestProductInAGrid(IList<IList<int>> grid) {
        int result = 0;
        for (int i = 0; i < grid.Count - 3; i++) {
            for (int j = 0; j < grid[i].Count - 3; j++) {
                int p1 = 1, p2 = 1, p3 = 1, p4 = 1;
                for (int k = 0; k < 4; k++) {
                    p1 *= grid[i + k][j];
                }
                for (int k = 0; k < 4; k++) {
                    p2 *= grid[i][j + k];
                }
                for (int k = 0; k < 4; k++) {
                    p3 *= grid[i + k][j + k];
                }
                for (int k = 0; k < 4; k++) {
                    p4 *= grid[i + k][j + 3 - k];
                }
                result = new int[] {result, p1, p2, p3, p4}.Max();
            }
        }
        return result;
    }
}

# Go

func LargestProductInAGrid(grid [][]int) int {
    result := 0
    for i := 0; i < len(grid) - 3; i++ {
        for j := 0; j < len(grid[i]) - 3; j++ {
            p1, p2, p3, p4 := 1, 1, 1, 1
            for k := 0; k < 4; k++ {
                p1 *= grid[i + k][j]
            }
            for k := 0; k < 4; k++ {
                p2 *= grid[i][j + k]
            }
            for k := 0; k < 4; k++ {
                p3 *= grid[i + k][j + k]
            }
            for k := 0; k < 4; k++ {
                p4 *= grid[i + k][j + 3 - k]
            }
            result = max(result, p1, p2, p3, p4)
        }
    }
    return result
}

# Java

class Global {
    public static int largestProductInAGrid(List<List<Integer>> grid) {
        int result = 0;
        for (int i = 0; i < grid.size() - 3; i++) {
            for (int j = 0; j < grid.get(i).size() - 3; j++) {
                int p1 = 1, p2 = 1, p3 = 1, p4 = 1;
                for (int k = 0; k < 4; k++) {
                    p1 *= grid.get(i + k).get(j);
                }
                for (int k = 0; k < 4; k++) {
                    p2 *= grid.get(i).get(j + k);
                }
                for (int k = 0; k < 4; k++) {
                    p3 *= grid.get(i + k).get(j + k);
                }
                for (int k = 0; k < 4; k++) {
                    p4 *= grid.get(i + k).get(j + 3 - k);
                }
                result = Collections.max(Arrays.asList(result, p1, p2, p3, p4));
            }
        }
        return result;
    }
}

# JavaScript

const largestProductInAGrid = (grid) => {
    let result = 0;
    for (let i = 0; i < grid.length - 3; i++) {
        for (let j = 0; j < grid[i].length - 3; j++) {
            let p1 = 1, p2 = 1, p3 = 1, p4 = 1;
            for (let k = 0; k < 4; k++) {
                p1 *= grid[i + k][j];
            }
            for (let k = 0; k < 4; k++) {
                p2 *= grid[i][j + k];
            }
            for (let k = 0; k < 4; k++) {
                p3 *= grid[i + k][j + k];
            }
            for (let k = 0; k < 4; k++) {
                p4 *= grid[i + k][j + 3 - k];
            }
            result = Math.max(result, p1, p2, p3, p4);
        }
    }
    return result;
}

# Kotlin

fun largestProductInAGrid(grid: List<List<Int>>): Int {
    var result = 0
    for (i in 0 until grid.size - 3) {
        for (j in 0 until grid[i].size - 3) {
            var p1 = 1
            var p2 = 1
            var p3 = 1
            var p4 = 1
            for (k in 0 until 4) {
                p1 *= grid[i + k][j]
            }
            for (k in 0 until 4) {
                p2 *= grid[i][j + k]
            }
            for (k in 0 until 4) {
                p3 *= grid[i + k][j + k]
            }
            for (k in 0 until 4) {
                p4 *= grid[i + k][j + 3 - k]
            }
            result = maxOf(result, p1, p2, p3, p4)
        }
    }
    return result
}

# PHP

function largestProductInAGrid($grid) {
    $result = 0;
    for ($i = 0; $i < count($grid) - 3; $i++) {
        for ($j = 0; $j < count($grid[$i]) - 3; $j++) {
            $p1 = 1;
            $p2 = 1;
            $p3 = 1;
            $p4 = 1;
            for ($k = 0; $k < 4; $k++) {
                $p1 *= $grid[$i + $k][$j];
            }
            for ($k = 0; $k < 4; $k++) {
                $p2 *= $grid[$i][$j + $k];
            }
            for ($k = 0; $k < 4; $k++) {
                $p3 *= $grid[$i + $k][$j + $k];
            }
            for ($k = 0; $k < 4; $k++) {
                $p4 *= $grid[$i + $k][$j + 3 - $k];
            }
            $result = max($result, $p1, $p2, $p3, $p4);
        }
    }
    return $result;
}

# Ruby

def largest_product_in_a_grid(grid)
    result = 0
    (0...grid.length - 3).each do |i|
        (0...grid[i].length - 3).each do |j|
            p1, p2, p3, p4 = 1, 1, 1, 1
            (0...4).each do |k|
                p1 *= grid[i + k][j]
            end
            (0...4).each do |k|
                p2 *= grid[i][j + k]
            end
            (0...4).each do |k|
                p3 *= grid[i + k][j + k]
            end
            (0...4).each do |k|
                p4 *= grid[i + k][j + 3 - k]
            end
            result = [result, p1, p2, p3, p4].max
        end
    end
    result
end

# Rust

fn largest_product_in_a_grid(grid: &Vec<Vec<i32>>) -> i32 {
    let mut result = 0;
    for i in 0..grid.len() - 3 {
        for j in 0..grid[i].len() - 3 {
            let mut p1 = 1;
            let mut p2 = 1;
            let mut p3 = 1;
            let mut p4 = 1;
            for k in 0..4 {
                p1 *= grid[i + k][j];
            }
            for k in 0..4 {
                p2 *= grid[i][j + k];
            }
            for k in 0..4 {
                p3 *= grid[i + k][j + k];
            }
            for k in 0..4 {
                p4 *= grid[i + k][j + 3 - k];
            }
            result = vec![result, p1, p2, p3, p4].into_iter().max().unwrap();
        }
    }
    result
}

# Scala

def largestProductInAGrid(grid: Seq[Seq[Int]]): Int = {
    var result = 0
    for (i <- 0 until grid.length - 3) {
        for (j <- 0 until grid(i).length - 3) {
            var p1 = 1
            var p2 = 1
            var p3 = 1
            var p4 = 1
            for (k <- 0 until 4) {
                p1 *= grid(i + k)(j)
            }
            for (k <- 0 until 4) {
                p2 *= grid(i)(j + k)
            }
            for (k <- 0 until 4) {
                p3 *= grid(i + k)(j + k)
            }
            for (k <- 0 until 4) {
                p4 *= grid(i + k)(j + 3 - k)
            }
            result = List(result, p1, p2, p3, p4).max
        }
    }
    result
}