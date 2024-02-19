// Start Euler001

fun multiplesOf3And5(n: Int): Int {
    var result = 0
    for (i in 0 until n) {
        if (i % 3 == 0 || i % 5 == 0) {
            result += i
        }
    }
    return result
}

// End Euler001

// Start Euler002

fun evenFibonacciNumbers(n: Int): Int {
    var result = 0
    var a = 1
    var b = 2
    while (a < n) {
        if (a % 2 == 0) {
            result += a
        }
        val tmp = a
        a = b
        b = tmp + b
    }
    return result
}

// End Euler002

// Start Euler003

fun largestPrimeFactor(n: Int): Int {
    var result = n
    var i = 2
    while (i * i <= result) {
        if (result % i != 0) {
            i += 1
        } else {
            result /= i
        }
    }
    return result
}

// End Euler003

// Start Euler004

fun isPalindrome(s: String): Boolean {
    for (i in 0 until s.length / 2) {
        if (s[i] != s[s.length - i - 1]) {
            return false
        }
    }
    return true
}

fun largestPalindromeProduct(n: Int): Int {
    var result = 0
    for (i in 100 until 1000) {
        for (j in i until 1000) {
            val prod = i * j
            if (isPalindrome(prod.toString()) && prod > result && prod < n) {
                result = prod
            }
        }
    }
    return result
}

// End Euler004

// Start Euler005

fun smallestMultiple(n: Int): Int {
    var result = 1
    for (i in 1..n) {
        if (result % i != 0) {
            for (j in 1..n) {
                if ((result * j) % i == 0) {
                    result *= j
                    break
                }
            }
        }
    }
    return result
}

// End Euler005

// Start Euler006

fun sumSquareDifference(n: Int): Int {
    var sqrSum = 0
    var numSum = 0
    for (i in 1..n) {
        sqrSum += i * i
        numSum += i
    }
    return numSum * numSum - sqrSum
}

// End Euler006

// Start Euler007

fun nthPrime(n: Int): Int {
    val primes = mutableListOf(2)
    var i = 3
    while (primes.size < n) {
        for (p in primes) {
            if (i % p == 0) {
                break
            }
            if (p * p > i) {
                primes.add(i)
                break
            }
        }
        i += 2
    }
    return primes.last()
}

// End Euler007

// Start Euler008

fun largestProductInASeries(s: String, k: Int): Int {
    var result = 0
    for (i in 0 until s.length - k) {
        var product = 1
        for (j in 0 until k) {
            product *= s[i + j].digitToInt()
        }
        result = maxOf(result, product)
    }
    return result
}

// End Euler008

// Start Euler009

fun specialPythagoreanTriplet(n: Int): Int {
    for (a in 1 until n) {
        for (b in a until n) {
            val c = n - a - b
            if (a * a + b * b == c * c) {
                return a * b * c
            }
        }
    }
    return -1
}

// End Euler009

// Start Euler010

fun summationOfPrimes(n: Int): Int {
    val primes = mutableListOf(2)
    var i = 3
    while (i <= n) {
        for (p in primes) {
            if (i % p == 0) {
                break
            }
            if (p * p > i) {
                primes.add(i)
                break
            }
        }
        i += 2
    }
    var result = 0
    for (prime in primes) {
        result += prime
    }
    return result
}

// End Euler010

// Start Euler011

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

// End Euler011

// Start Euler012

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

// End Euler012

// Start Euler013

fun largeSum(numbers: List<String>): String {
    val digits = Array(60) { 0 }
    for (i in 0 until 50) {
        var tmp = 0
        for (num in numbers) {
            tmp += num[49 - i] - '0'
        }
        for (j in i until 60) {
            digits[j] += tmp % 10
            if (digits[j] >= 10) {
                digits[j + 1] += digits[j] / 10
                digits[j] %= 10
            }
            tmp /= 10
            if (tmp == 0) {
                break
            }
        }
    }
    for (i in 59 downTo 0) {
        if (digits[i] != 0) {
            val result = StringBuilder()
            for (j in i downTo i - 9) {
                result.append(digits[j])
            }
            return result.toString()
        }
    }
    return ""
}

// End Euler013

// Start Euler014

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

// End Euler014

// Start Euler015

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

// End Euler015

// Start Euler016

fun powerDigitSum(n: Int): Int {
    val digits = mutableListOf(2)
    for (i in 1 until n) {
        var carry = 0
        for (j in digits.indices) {
            var temp = digits[j] * 2 + carry
            digits[j] = temp % 10
            carry = temp / 10
        }
        if (carry != 0) {
            digits.add(carry)
        }
    }
    var result = 0
    for (digit in digits) {
        result += digit
    }
    return result
}

// End Euler016

// Start Euler017

fun numberToWords(n: Int): String {
    val ones = listOf("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    val teens = listOf("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
    val tens = listOf("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
    if (n == 1000) {
        return "one thousand"
    } else if (n >= 100) {
        if (n % 100 == 0) {
            return ones[n / 100] + " hundred"
        } else {
            return ones[n / 100] + " hundred and " + numberToWords(n % 100)
        }
    } else if (n >= 20) {
        var suf = ""
        if (n % 10 != 0) {
            suf = " " + ones[n % 10]
        }
        return tens[n / 10] + suf
    } else if (n >= 10) {
        return teens[n - 10]
    } else {
        return ones[n]
    }
}

// End Euler017

// Start Euler018

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

// End Euler018

// Start Euler019

fun countingSundays(y1: Int, y2: Int): Int {
    var day = 0
    var count = 0
    for (year in 1900..y2) {
        for (month in 1..12) {
            if (year >= y1 && day % 7 == 6) {
                count++
            }
            if (month == 4 || month == 6 || month == 9 || month == 11) {
                day += 30
            } else if (month == 2) {
                if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
                    day += 29
                } else {
                    day += 28
                }
            } else {
                day += 31
            }
        }
    }
    return count
}

// End Euler019

// Start Euler020

fun factorialDigitSum(n: Int): Int {
    val digits = mutableListOf(1)
    for (i in 1..n) {
        var carry = 0
        for (j in digits.indices) {
            digits[j] = digits[j] * i + carry
            carry = digits[j] / 10
            digits[j] %= 10
        }
        while (carry != 0) {
            digits.add(carry % 10)
            carry /= 10
        }
    }
    var result = 0
    for (digit in digits) {
        result += digit
    }
    return result
}

// End Euler020

// Start Euler021

fun d(n: Int): Int {
    var result = 1
    for (i in 2..sqrt(n.toDouble()).toInt()) {
        if (n % i == 0) {
            result += i
            if (i != n / i) {
                result += n / i
            }
        }
    }
    return result
}

fun amicableNumbers(n: Int): Int {
    var result = 0
    for (a in 2 until n) {
        val b = d(a)
        if (a != b && a == d(b)) {
            result += a
        }
    }
    return result
}

// End Euler021

// Start Euler022

fun namesScores(names: List<String>, queries: List<String>): Int {
    val sNames = names.sorted().toMutableList()
    var result = 0
    for ((i, name) in sNames.withIndex()) {
        var x = 0
        for (c in name) {
            x += c.toInt() - 64
        }
        if (name in queries) {
            result += x * (i + 1)
        }
    }
    return result
}

// End Euler022

// Start Euler023

fun isAbundant(n: Int): Boolean {
    if (n < 12) {
        return false
    }
    var sumDivisors = 1
    for (i in 2..sqrt(n.toDouble()).toInt()) {
        if (n % i == 0) {
            sumDivisors += i
            if (i != n / i) {
                sumDivisors += n / i
            }
        }
    }
    return sumDivisors > n
}

fun nonAbundantSums(n: Int): Int {
    val abundants = mutableListOf<Int>()
    for (i in 12 until n) {
        if (isAbundant(i)) {
            abundants.add(i)
        }
    }
    val abundantSums = mutableSetOf<Int>()
    for (i in abundants) {
        for (j in abundants) {
            abundantSums.add(i + j)
        }
    }
    var result = 0
    for (i in 0 until n) {
        if (i !in abundantSums) {
            result += i
        }
    }
    return result
}

// End Euler023

// Start Euler024

fun lexicographicPermutations(n: Int): String {
    var result = ""
    var digits = mutableListOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    var x = n - 1
    for (i in 10 downTo 1) {
        var fact = 1
        for (j in 1 until i) {
            fact *= j
        }
        var idx = x / fact
        result += digits[idx]
        digits.removeAt(idx)
        x -= idx * fact
    }
    return result
}

// End Euler024

// Start Euler025

fun nDigitFibonacciNumber(n: Int): Int {
    var a = listOf(1)
    var b = listOf(1)
    var i = 2
    while (b.size < n) {
        var carry = 0
        val c = b.toMutableList()
        for (j in b.indices) {
            if (j < a.size) {
                b = b.toMutableList()
                b[j] = a[j] + b[j] + carry
            } else {
                b = b.toMutableList()
                b[j] = b[j] + carry
            }
            carry = b[j] / 10
            b = b.toMutableList()
            b[j] = b[j] % 10
        }
        if (carry != 0) {
            b = b.toMutableList()
            b = b + carry
        }
        a = c
        i = i + 1
    }
    return i
}

// End Euler025

// Start Euler026

fun reciprocalCycles(n: Int): Int {
    var result = 0
    var maxLength = 0
    for (i in 1 until n) {
        val remainders = mutableListOf<Int>()
        var remainder = 1
        while (remainder != 0 && !remainders.contains(remainder)) {
            remainders.add(remainder)
            remainder = (remainder * 10) % i
        }
        var length = 0
        if (remainder != 0) {
            length = remainders.size - remainders.indexOf(remainder)
        }
        if (length > maxLength) {
            maxLength = length
            result = i
        }
    }
    return result
}

// End Euler026

// Start Euler027

fun isPrime(n: Int): Boolean {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i in 3..sqrt(n.toDouble()).toInt() step 2) {
        if (n % i == 0) {
            return false
        }
    }
    return true
}

fun quadraticPrimes(n: Int): Int {
    var maxPrimes = 0
    var result = 0
    for (a in -n + 1 until n step 2) {
        for (b in -n + 1 until n step 2) {
            var x = 0
            while (true) {
                if (x * x + a * x + b < 2) {
                    break
                }
                if (!isPrime(x * x + a * x + b)) {
                    break
                }
                x++
            }
            if (x > maxPrimes) {
                maxPrimes = x
                result = a * b
            }
        }
    }
    return result
}

// End Euler027

// Start Euler028

fun numberSpiralDiagonals(n: Int): Int {
    var result = 1
    for (i in 3..n step 2) {
        result += 4 * i * i - 6 * i + 6
    }
    return result
}

// End Euler028

// Start Euler029

fun distinctPowers(n: Int): Int {
    var result = 0
    val xs = mutableSetOf<String>()
    for (i in 2..n) {
        val primes = listOf(2, 3, 5, 7)
        val powers = mutableListOf(0, 0, 0, 0)
        var num = i
        for (j in primes.indices) {
            while (num % primes[j] == 0) {
                num /= primes[j]
                powers[j] += 1
            }
        }
        if (num != 1) {
            result += n - 1
            continue
        }
        for (j in 2..n) {
            val pstr = "${powers[0] * j}-${powers[1] * j}-${powers[2] * j}-${powers[3] * j}"
            xs.add(pstr)
        }
    }
    result += xs.size
    return result
}

// End Euler029

// Start Euler030

fun digitNthPowers(n: Int): Int {
    var result = 0
    for (i in 2 until 4 * 10.0.pow(n).toInt()) {
        var digitsSum = 0
        for (digit in i.toString()) {
            digitsSum += digit.digitToInt().toDouble().pow(n).toInt()
        }
        if (i == digitsSum) {
            result += i
        }
    }
    return result
}

// End Euler030

// Start Euler031

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

// End Euler031

// Start Euler032

fun pandigitalProducts(n: Int): Int {
    val products = HashSet<Int>()
    var s = ""
    for (i in 1..n) {
        s += i
    }
    for (a in 1 until 100) {
        for (b in 1 until 10000) {
            val c = a * b
            var chars = (a.toString() + b.toString() + c.toString()).toCharArray()
            chars.sort()
            if (chars.joinToString("") == s) {
                products.add(c)
            }
        }
    }
    var result = 0
    for (product in products) {
        result += product
    }
    return result
}

// End Euler032

// Start Euler033

fun digitCancelingFractions(m: Int): Int {
    var numer = 1
    var denom = 1
    for (d in 10 until m) {
        for (n in 10 until d) {
            val n0 = n % 10
            val n1 = n / 10
            val d0 = d % 10
            val d1 = d / 10
            if ((n1 == d0 && n0 * d == n * d1) || (n0 == d1 && n1 * d == n * d0)) {
                numer *= n
                denom *= d
            }
        }
    }
    var a = numer
    var b = denom
    while (b != 0) {
        val temp = b
        b = a % b
        a = temp
    }
    return denom / a
}

// End Euler033

// Start Euler034

fun digitFactorials(n: Int): Int {
    var result = 0
    for (i in 3 until n) {
        var factSum = 0
        for (digit in i.toString()) {
            var fact = 1
            for (j in 1..digit.toInt() - '0'.toInt()) {
                fact *= j
            }
            factSum += fact
        }
        if (i == factSum) {
            result += i
        }
    }
    return result
}

// End Euler034

// Start Euler035

fun isPrime(n: Int): Boolean {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i in 3..sqrt(n.toDouble()).toInt() step 2) {
        if (n % i == 0) {
            return false
        }
    }
    return true
}

fun circularPrimes(n: Int): Int {
    var count = 0
    for (i in 2 until n) {
        if (isPrime(i)) {
            val rotations = HashSet<Int>()
            val si = i.toString()
            for (j in 0 until si.length) {
                rotations.add((si.substring(j) + si.substring(0, j)).toInt())
            }
            var flag = true
            for (x in rotations) {
                if (!isPrime(x)) {
                    flag = false
                    break
                }
            }
            if (flag) {
                count++
            }
        }
    }
    return count
}

// End Euler035

// Start Euler036

fun isPalindrome(s: String): Boolean {
    for (i in 0 until s.length / 2) {
        if (s[i] != s[s.length - i - 1]) {
            return false
        }
    }
    return true
}

fun doubleBasePalindromes(n: Int): Int {
    var result = 0
    for (i in 1 until n) {
        val strI = i.toString()
        val binI = Integer.toBinaryString(i)
        if (isPalindrome(strI) && isPalindrome(binI)) {
            result += i
        }
    }
    return result
}

// End Euler036

// Start Euler037

fun isPrime(n: Int): Boolean {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i in 3..sqrt(n.toDouble()).toInt() step 2) {
        if (n % i == 0) {
            return false
        }
    }
    return true
}

fun truncatablePrimes(n: Int): Int {
    var result = 0
    for (i in 10 until n) {
        if (isPrime(i)) {
            val si = i.toString()
            var flag = true
            for (j in 1 until si.length) {
                val p1 = si.substring(j).toInt()
                val p2 = si.substring(0, si.length - j).toInt()
                if (!isPrime(p1) || !isPrime(p2)) {
                    flag = false
                    break
                }
            }
            if (flag) {
                result += i
            }
        }
    }
    return result
}

// End Euler037

// Start Euler038

fun pandigitalMultiples(n: Int): Int {
    var result = -1
    for (i in 2..n) {
        var cprod = ""
        for (j in 1 until 10) {
            cprod += (i * j).toString()
            if (cprod.length == 9) {
                val chars = cprod.toCharArray()
                chars.sort()
                if (String(chars) == "123456789") {
                    result = max(result, cprod.toInt())
                    break
                }
            } else if (cprod.length > 9) {
                break
            }
        }
    }
    return result
}

// End Euler038

// Start Euler039

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

// End Euler039

// Start Euler040

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

// End Euler040

// Start Euler041

fun isPrime(n: Int): Boolean {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i in 3..sqrt(n.toDouble()).toInt() step 2) {
        if (n % i == 0) {
            return false
        }
    }
    return true
}

fun pandigitalPrime(n: Int): Int {
    for (i in n - 1 downTo 1) {
        if (isPrime(i)) {
            val si = i.toString()
            val length = si.length
            var flag = true
            for (j in 1..length) {
                if (!si.contains(j.toString())) {
                    flag = false
                    break
                }
            }
            if (flag) {
                return i
            }
        }
    }
    return -1
}

// End Euler041

// Start Euler042

fun codedTriangleNumbers(words: List<String>): Int {
    var result = 0
    for (word in words) {
        var value = 0
        for (c in word) {
            value += c.toInt() - 64
        }
        val n = sqrt((value * 2).toDouble()).toInt()
        if (n * (n + 1) == value * 2) {
            result++
        }
    }
    return result
}

// End Euler042

// Start Euler043

fun genPermutations(s: String): List<String> {
    if (s.length <= 1) {
        return listOf(s)
    }
    val result = mutableListOf<String>()
    for (perm in genPermutations(s.substring(1))) {
        for (i in s.indices) {
            result.add(perm.substring(0, i) + s[0] + perm.substring(i))
        }
    }
    return result
}

fun subStringDivisibility(n: Int): Int {
    var result = 0
    val primes = listOf(2, 3, 5, 7, 11, 13, 17)
    var s = ""
    for (i in 0..n) {
        s += i
    }
    for (i in genPermutations(s)) {
        var flag = true
        for (j in 1 until n - 1) {
            if (i.substring(j, j + 3).toInt() % primes[j - 1] != 0) {
                flag = false
                break
            }
        }
        if (flag) {
            result += i.toInt()
        }
    }
    return result
}

// End Euler043

// Start Euler044

fun pentagonNumbers(n: Int): Int {
    val pentagon = HashSet<Int>()
    for (i in 1 until n) {
        pentagon.add(i * (3 * i - 1) / 2)
    }
    var result = -1
    for (j in pentagon) {
        for (k in pentagon) {
            if (pentagon.contains(j + k) && pentagon.contains(k - j)) {
                if (result == -1 || k - j < result) {
                    result = k - j
                }
            }
        }
    }
    return result
}

// End Euler044

// Start Euler045

fun triangularPentagonalAndHexagonal(n: Int): Int {
    val ps = HashSet<Int>()
    var i = 1
    var c = (0.5 * i * (3 * i - 1)).toInt()
    while (c < n) {
        i++
        ps.add(c)
        c = (0.5 * i * (3 * i - 1)).toInt()
    }
    i = 1
    c = i * (2 * i - 1)
    var result = -1
    while (c < n) {
        i++
        if (ps.contains(c)) {
            result = c
        }
        c = i * (2 * i - 1)
    }
    return result
}

// End Euler045

// Start Euler046

fun isPrime(n: Int): Boolean {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i in 3..sqrt(n.toDouble()).toInt() step 2) {
        if (n % i == 0) {
            return false
        }
    }
    return true
}

fun goldbachsOtherConjecture(n: Int): Int {
    var result = -1
    for (i in 9999 downTo n + 1 step 2) {
        val upper = sqrt(i / 2.0).toInt()
        var flag = false
        for (j in 0..upper) {
            if (isPrime(i - 2 * j * j)) {
                flag = true
                break
            }
        }
        if (!flag) {
            result = i
        }
    }
    return result
}

// End Euler046

// Start Euler047

fun primeFactors(n: Int): Int {
    var num = n
    val factors = mutableListOf<Int>()
    var i = 2
    while (i * i <= num) {
        if (num % i != 0) {
            i++
        } else {
            num /= i
            factors.add(i)
        }
    }
    if (num > 1) {
        factors.add(num)
    }
    return factors.toSet().size
}

fun distinctPrimesFactors(n: Int): Int {
    for (i in n until 1000000) {
        if (primeFactors(i) == 4 && primeFactors(i + 1) == 4 && primeFactors(i + 2) == 4 && primeFactors(i + 3) == 4) {
            return i
        }
    }
    return -1
}

// End Euler047

// Start Euler048

fun selfPowers(n: Int): String {
    val digits = IntArray(10) { 0 }
    for (i in 1..n) {
        val tempDigits = IntArray(10) { 0 }
        tempDigits[0] = 1
        for (j in 0 until i) {
            var carry = 0
            for (k in 0 until 10) {
                tempDigits[k] = tempDigits[k] * i + carry
                carry = tempDigits[k] / 10
                tempDigits[k] %= 10
            }
        }
        for (j in 0 until 10) {
            digits[j] += tempDigits[j]
            if (digits[j] >= 10) {
                digits[j] -= 10
                if (j < 9) {
                    digits[j + 1] += 1
                }
            }
        }
    }
    var result = ""
    for (i in 9 downTo 0) {
        result += digits[i].toString()
    }
    return result
}

// End Euler048

// Start Euler049

fun isPrime(n: Int): Boolean {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i in 3..sqrt(n.toDouble()).toInt() step 2) {
        if (n % i == 0) {
            return false
        }
    }
    return true
}

fun genPermutations(s: String): List<String> {
    if (s.length <= 1) {
        return listOf(s)
    }
    val result = mutableListOf<String>()
    for (perm in genPermutations(s.substring(1))) {
        for (i in s.indices) {
            result.add(perm.substring(0, i) + s[0] + perm.substring(i))
        }
    }
    return result
}

fun primePermutations(n: Int): String {
    for (i in n downTo 999) {
        if (isPrime(i)) {
            val permutations = genPermutations(i.toString())
            val candidates = mutableSetOf<Int>()
            for (j in permutations) {
                val candidate = j.toInt()
                if (candidate > i && isPrime(candidate)) {
                    candidates.add(candidate)
                }
            }
            for (m in candidates) {
                if (candidates.contains(m + (m - i))) {
                    return i.toString() + m.toString() + (m + (m - i)).toString()
                }
            }
        }
    }
    return ""
}

// End Euler049

// Start Euler050

fun consecutivePrimeSum(limit: Int): Int {
    val sieve = Array(limit) { true }
    val primes = mutableListOf<Int>()
    for (i in 2 until limit) {
        if (sieve[i]) {
            primes.add(i)
            for (j in i * 2 until limit step i) {
                sieve[j] = false
            }
        }
    }
    var maxLength = 0
    var maxPrime = 0
    for (i in primes.indices) {
        for (j in i + maxLength until primes.size) {
            var s = 0
            for (k in i until j) {
                s += primes[k]
            }
            if (s >= limit) {
                break
            }
            if (sieve[s] && j - i > maxLength) {
                maxLength = j - i
                maxPrime = s
            }
        }
    }
    return maxPrime
}

// End Euler050

