# Python

def sum_square_difference(n: int) -> int:
    sqr_sum = 0
    num_sum = 0
    for i in range(1, n + 1):
        sqr_sum += i * i
        num_sum += i
    return num_sum * num_sum - sqr_sum

# Start translation now

# C++

int sumSquareDifference(int n) {
    int sqr_sum = 0;
    int num_sum = 0;
    for (int i = 1; i <= n; i++) {
        sqr_sum += i * i;
        num_sum += i;
    }
    return num_sum * num_sum - sqr_sum;
}

# C#

class Global {
    public static int SumSquareDifference(int n) {
        int sqrSum = 0;
        int numSum = 0;
        for (int i = 1; i <= n; i++) {
            sqrSum += i * i;
            numSum += i;
        }
        return numSum * numSum - sqrSum;
    }
}

# Go

func SumSquareDifference(n int) int {
    sqrSum := 0
    numSum := 0
    for i := 1; i <= n; i++ {
        sqrSum += i * i
        numSum += i
    }
    return numSum * numSum - sqrSum
}

# Java

class Global {
    public static int sumSquareDifference(int n) {
        int sqrSum = 0;
        int numSum = 0;
        for (int i = 1; i <= n; i++) {
            sqrSum += i * i;
            numSum += i;
        }
        return numSum * numSum - sqrSum;
    }
}

# JavaScript

const sumSquareDifference = (n) => {
    let sqrSum = 0;
    let numSum = 0;
    for (let i = 1; i <= n; i++) {
        sqrSum += i * i;
        numSum += i;
    }
    return numSum * numSum - sqrSum;
}

# Kotlin

fun sumSquareDifference(n: Int): Int {
    var sqrSum = 0
    var numSum = 0
    for (i in 1..n) {
        sqrSum += i * i
        numSum += i
    }
    return numSum * numSum - sqrSum
}

# PHP

function sumSquareDifference($n) {
    $sqrSum = 0;
    $numSum = 0;
    for ($i = 1; $i <= $n; $i++) {
        $sqrSum += $i * $i;
        $numSum += $i;
    }
    return $numSum * $numSum - $sqrSum;
}

# Ruby

def sum_square_difference(n)
    sqr_sum = 0
    num_sum = 0
    (1..n).each do |i|
        sqr_sum += i * i
        num_sum += i
    end
    num_sum * num_sum - sqr_sum
end

# Rust

fn sum_square_difference(n: i32) -> i32 {
    let mut sqr_sum = 0;
    let mut num_sum = 0;
    for i in 1..=n {
        sqr_sum += i * i;
        num_sum += i;
    }
    num_sum * num_sum - sqr_sum
}

# Scala

def sumSquareDifference(n: Int): Int = {
    var sqrSum = 0
    var numSum = 0
    for (i <- 1 to n) {
        sqrSum += i * i
        numSum += i
    }
    numSum * numSum - sqrSum
}
