# Python

def coin_sums(n: int) -> int:
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (n + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            ways[i] += ways[i - coin]
    return ways[n]

# Start translation now

# C++

int coinSums(int n) {
    vector<int> coins = {1, 2, 5, 10, 20, 50, 100, 200};
    vector<int> ways(n + 1, 0);
    ways[0] = 1;
    for (int coin : coins) {
        for (int i = coin; i <= n; i++) {
            ways[i] += ways[i - coin];
        }
    }
    return ways[n];
}

# C#

class Global {
    public static int CoinSums(int n) {
        int[] coins = {1, 2, 5, 10, 20, 50, 100, 200};
        int[] ways = new int[n + 1];
        ways[0] = 1;
        foreach (int coin in coins) {
            for (int i = coin; i <= n; i++) {
                ways[i] += ways[i - coin];
            }
        }
        return ways[n];
    }
}

# Go

func CoinSums(n int) int {
    coins := []int{1, 2, 5, 10, 20, 50, 100, 200}
    ways := make([]int, n + 1)
    ways[0] = 1
    for _, coin := range coins {
        for i := coin; i <= n; i++ {
            ways[i] += ways[i - coin]
        }
    }
    return ways[n]
}

# Java

class Global {
    public static int coinSums(int n) {
        int[] coins = {1, 2, 5, 10, 20, 50, 100, 200};
        int[] ways = new int[n + 1];
        ways[0] = 1;
        for (int coin : coins) {
            for (int i = coin; i <= n; i++) {
                ways[i] += ways[i - coin];
            }
        }
        return ways[n];
    }
}

# JavaScript

const coinSums = (n) => {
    const coins = [1, 2, 5, 10, 20, 50, 100, 200];
    const ways = new Array(n + 1).fill(0);
    ways[0] = 1;
    for (const coin of coins) {
        for (let i = coin; i <= n; i++) {
            ways[i] += ways[i - coin];
        }
    }
    return ways[n];
}

# Kotlin

fun coinSums(n: Int): Int {
    val coins = listOf(1, 2, 5, 10, 20, 50, 100, 200)
    val ways = IntArray(n + 1) { 0 }
    ways[0] = 1
    for (coin in coins) {
        for (i in coin..n) {
            ways[i] += ways[i - coin]
        }
    }
    return ways[n]
}

# PHP

function coinSums($n) {
    $coins = [1, 2, 5, 10, 20, 50, 100, 200];
    $ways = array_fill(0, $n + 1, 0);
    $ways[0] = 1;
    foreach ($coins as $coin) {
        for ($i = $coin; $i <= $n; $i++) {
            $ways[$i] += $ways[$i - $coin];
        }
    }
    return $ways[$n];
}

# Ruby

def coin_sums(n)
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (n + 1)
    ways[0] = 1
    coins.each do |coin|
        (coin..n).each do |i|
            ways[i] += ways[i - coin]
        end
    end
    ways[n]
end

# Rust

fn coin_sums(n: i32) -> i32 {
    let coins = vec![1, 2, 5, 10, 20, 50, 100, 200];
    let mut ways = vec![0; (n + 1) as usize];
    ways[0] = 1;
    for coin in coins {
        for i in coin..=n {
            ways[i as usize] += ways[(i - coin) as usize];
        }
    }
    ways[n as usize]
}

# Scala

def coinSums(n: Int): Int = {
    val coins = List(1, 2, 5, 10, 20, 50, 100, 200)
    val ways = Array.fill(n + 1)(0)
    ways(0) = 1
    for (coin <- coins) {
        for (i <- coin to n) {
            ways(i) += ways(i - coin)
        }
    }
    ways(n)
}


