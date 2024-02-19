# Python

def maximum_path_sum_i(triangle: list[list[int]]) -> int:
    curr = triangle[-1].copy()
    for i in range(len(triangle) - 2, -1, -1):
        next = triangle[i].copy()
        for j in range(len(next)):
            next[j] += max(curr[j], curr[j + 1])
        curr = next
    return curr[0]

# Start translation now

# C++

int maximumPathSumI(const vector<vector<int>>& triangle) {
    vector<int> curr = triangle.back();
    for (int i = triangle.size() - 2; i >= 0; i--) {
        vector<int> next = triangle[i];
        for (int j = 0; j < next.size(); j++) {
            next[j] += max(curr[j], curr[j + 1]);
        }
        curr = next;
    }
    return curr[0];
}

# C#

class Global {
    public static int MaximumPathSumI(IList<IList<int>> triangle) {
        List<int> curr = triangle.Last().ToList();
        for (int i = triangle.Count - 2; i >= 0; i--) {
            List<int> next = triangle[i].ToList();
            for (int j = 0; j < next.Count; j++) {
                next[j] += Math.Max(curr[j], curr[j + 1]);
            }
            curr = next;
        }
        return curr[0];
    }
}

# Go

func MaximumPathSumI(triangle [][]int) int {
    curr := make([]int, len(triangle[len(triangle) - 1]))
    copy(curr, triangle[len(triangle) - 1])
    for i := len(triangle) - 2; i >= 0; i-- {
        next := make([]int, len(triangle[i]))
        copy(next, triangle[i])
        for j := 0; j < len(next); j++ {
            next[j] += int(math.Max(float64(curr[j]), float64(curr[j + 1])))
        }
        curr = next
    }
    return curr[0]
}

# Java

class Global {
    public static int maximumPathSumI(List<List<Integer>> triangle) {
        List<Integer> curr = new ArrayList<>(triangle.get(triangle.size() - 1));
        for (int i = triangle.size() - 2; i >= 0; i--) {
            List<Integer> next = new ArrayList<>(triangle.get(i));
            for (int j = 0; j < next.size(); j++) {
                next.set(j, next.get(j) + Math.max(curr.get(j), curr.get(j + 1)));
            }
            curr = next;
        }
        return curr.get(0);
    }
}

# JavaScript

const maximumPathSumI = (triangle) => {
    let curr = triangle[triangle.length - 1].slice();
    for (let i = triangle.length - 2; i >= 0; i--) {
        let next = triangle[i].slice();
        for (let j = 0; j < next.length; j++) {
            next[j] += Math.max(curr[j], curr[j + 1]);
        }
        curr = next;
    }
    return curr[0];
}

# Kotlin

fun maximumPathSumI(triangle: List<List<Int>>): Int {
    var curr = triangle.last().toMutableList()
    for (i in triangle.size - 2 downTo 0) {
        val next = triangle[i].toMutableList()
        for (j in 0 until next.size) {
            next[j] += max(curr[j], curr[j + 1])
        }
        curr = next
    }
    return curr[0]
}

# PHP

function maximumPathSumI($triangle) {
    $curr = end($triangle);
    for ($i = count($triangle) - 2; $i >= 0; $i--) {
        $next = $triangle[$i];
        for ($j = 0; $j < count($next); $j++) {
            $next[$j] += max($curr[$j], $curr[$j + 1]);
        }
        $curr = $next;
    }
    return $curr[0];
}

# Ruby

def maximum_path_sum_i(triangle)
    curr = triangle.last.dup
    (triangle.size - 2).downto(0) do |i|
        next_ = triangle[i].dup
        next_.each_with_index do |_, j|
            next_[j] += [curr[j], curr[j + 1]].max
        end
        curr = next_
    end
    curr[0]
end

# Rust

fn maximum_path_sum_i(triangle: &Vec<Vec<i32>>) -> i32 {
    let mut curr = triangle.last().unwrap().clone();
    for i in (0..triangle.len() - 1).rev() {
        let mut next = triangle[i].clone();
        for j in 0..next.len() {
            next[j] += curr[j].max(curr[j + 1]);
        }
        curr = next;
    }
    curr[0]
}

# Scala

def maximumPathSumI(triangle: Seq[Seq[Int]]): Int = {
    var curr = triangle.last.to(ArrayBuffer)
    for (i <- triangle.length - 2 to 0 by -1) {
        val next = triangle(i).to(ArrayBuffer)
        for (j <- 0 until next.length) {
            next(j) += curr(j).max(curr(j + 1))
        }
        curr = next
    }
    curr.head
}

