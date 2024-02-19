// Start Euler001

def multiplesOf3And5(n: Int): Int = {
    var result = 0
    for (i <- 0 until n) {
        if (i % 3 == 0 || i % 5 == 0) {
            result += i
        }
    }
    result
}

// End Euler001

// Start Euler002

def evenFibonacciNumbers(n: Int): Int = {
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
    result
}

// End Euler002

// Start Euler003

def largestPrimeFactor(n: Int): Int = {
    var result = n
    var i = 2
    while (i * i <= result) {
        if (result % i != 0) {
            i += 1
        } else {
            result /= i
        }
    }
    result
}

// End Euler003

// Start Euler004

def isPalindrome(s: String): Boolean = {
    for (i <- 0 until s.length / 2) {
        if (s(i) != s(s.length - i - 1)) {
            return false
        }
    }
    true
}

def largestPalindromeProduct(n: Int): Int = {
    var result = 0
    for (i <- 100 until 1000) {
        for (j <- i until 1000) {
            val prod = i * j
            if (isPalindrome(prod.toString) && prod > result && prod < n) {
                result = prod
            }
        }
    }
    result
}

// End Euler004

// Start Euler005

def smallestMultiple(n: Int): Int = {
    var result = 1
    for (i <- 1 to n) {
        if (result % i != 0) {
            breakable {
                for (j <- 1 to n) {
                    if ((result * j) % i == 0) {
                        result *= j
                        break
                    }
                }
            }
        }
    }
    result
}

// End Euler005

// Start Euler006

def sumSquareDifference(n: Int): Int = {
    var sqrSum = 0
    var numSum = 0
    for (i <- 1 to n) {
        sqrSum += i * i
        numSum += i
    }
    numSum * numSum - sqrSum
}

// End Euler006

// Start Euler007

def nthPrime(n: Int): Int = {
    var primes = mutable.Buffer(2)
    var i = 3
    while (primes.length < n) {
        breakable {
            for (p <- primes) {
                if (i % p == 0) {
                    break
                }
                if (p * p > i) {
                    primes += i
                    break
                }
            }
        }
        i += 2
    }
    primes.last
}

// End Euler007

// Start Euler008

def largestProductInASeries(s: String, k: Int): Int = {
    var result = 0
    for (i <- 0 until s.length - k) {
        var product = 1
        for (j <- 0 until k) {
            product *= s(i + j).asDigit
        }
        result = result.max(product)
    }
    result
}

// End Euler008

// Start Euler009

def specialPythagoreanTriplet(n: Int): Int = {
    for (a <- 1 until n) {
        for (b <- a until n) {
            val c = n - a - b
            if (a * a + b * b == c * c) {
                return a * b * c
            }
        }
    }
    -1
}

// End Euler009

// Start Euler010

def summationOfPrimes(n: Int): Int = {
    var primes = mutable.Buffer(2)
    var i = 3
    while (i <= n) {
        var isPrime = true
        breakable {
            for (p <- primes) {
                if (i % p == 0) {
                    isPrime = false
                    break
                }
                if (p * p > i) {
                    break
                }
            }
        }
        if (isPrime) {
            primes += i
        }
        i += 2
    }
    var result = 0
    for (prime <- primes) {
        result += prime
    }
    result
}

// End Euler010

// Start Euler011

def largestProductInAGrid(grid: collection.Seq[collection.Seq[Int]]): Int = {
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

// End Euler011

// Start Euler012

def highlyDivisibleTriangularNumber(n: Int): Int = {
    for (i <- 1 until 100000000) {
        val result = i * (i + 1) / 2
        var count = 0
        for (j <- 1 to math.sqrt(result).toInt) {
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

// End Euler012

// Start Euler013

def largeSum(numbers: collection.Seq[String]): String = {
    val digits = Array.fill(60)(0)
    for (i <- 0 until 50) {
        var tmp = 0
        for (num <- numbers) {
            tmp += num(49 - i).asDigit
        }
        breakable {
            for (j <- i until 60) {
                digits(j) += tmp % 10
                if (digits(j) >= 10) {
                    digits(j + 1) += digits(j) / 10
                    digits(j) %= 10
                }
                tmp /= 10
                if (tmp == 0) {
                    break
                }
            }
        }
    }
    for (i <- 59 to 0 by -1) {
        if (digits(i) != 0) {
            val result = new StringBuilder
            for (j <- i to i - 9 by -1) {
                result.append(digits(j))
            }
            return result.toString
        }
    }
    ""
}

// End Euler013

// Start Euler014

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

// End Euler014

// Start Euler015

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

// End Euler015

// Start Euler016

def powerDigitSum(n: Int): Int = {
    var digits = mutable.Buffer(2)
    for (i <- 1 until n) {
        var carry = 0
        for (j <- digits.indices) {
            val temp = digits(j) * 2 + carry
            digits(j) = temp % 10
            carry = temp / 10
        }
        if (carry != 0) {
            digits += carry
        }
    }
    var result = 0
    for (digit <- digits) {
        result += digit
    }
    result
}

// End Euler016

// Start Euler017

def numberToWords(n: Int): String = {
    val ones = Array("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    val teens = Array("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
    val tens = Array("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
    if (n == 1000) {
        "one thousand"
    } else if (n >= 100) {
        if (n % 100 == 0) {
            ones(n / 100) + " hundred"
        } else {
            ones(n / 100) + " hundred and " + numberToWords(n % 100)
        }
    } else if (n >= 20) {
        val suf = if (n % 10 != 0) " " + ones(n % 10) else ""
        tens(n / 10) + suf
    } else if (n >= 10) {
        teens(n - 10)
    } else {
        ones(n)
    }
}

// End Euler017

// Start Euler018

def maximumPathSumI(triangle: collection.Seq[collection.Seq[Int]]): Int = {
    var curr = triangle.last.to(mutable.Buffer)
    for (i <- triangle.length - 2 to 0 by -1) {
        val next = triangle(i).to(mutable.Buffer)
        for (j <- 0 until next.length) {
            next(j) += curr(j).max(curr(j + 1))
        }
        curr = next
    }
    curr.head
}

// End Euler018

// Start Euler019

def countingSundays(y1: Int, y2: Int): Int = {
    var day = 0
    var count = 0
    for (year <- 1900 to y2) {
        for (month <- 1 to 12) {
            if (year >= y1 && day % 7 == 6) {
                count += 1
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
    count
}

// End Euler019

// Start Euler020

def factorialDigitSum(n: Int): Int = {
    var digits = mutable.Buffer(1)
    for (i <- 1 to n) {
        var carry = 0
        for (j <- digits.indices) {
            digits(j) = digits(j) * i + carry
            carry = digits(j) / 10
            digits(j) = digits(j) % 10
        }
        while (carry != 0) {
            digits += carry % 10
            carry /= 10
        }
    }
    var result = 0
    for (digit <- digits) {
        result += digit
    }
    result
}

// End Euler020

// Start Euler021

def d(n: Int): Int = {
    var result = 1
    for (i <- 2 to math.sqrt(n).toInt) {
        if (n % i == 0) {
            result += i
            if (i != n / i) {
                result += n / i
            }
        }
    }
    result
}

def amicableNumbers(n: Int): Int = {
    var result = 0
    for (a <- 2 until n) {
        val b = d(a)
        if (a != b && a == d(b)) {
            result += a
        }
    }
    result
}

// End Euler021

// Start Euler022

def namesScores(names: collection.Seq[String], queries: collection.Seq[String]): Int = {
    val sNames = names.sorted.to(mutable.Buffer)
    var result = 0
    for ((name, i) <- sNames.zipWithIndex) {
        var x = 0
        for (c <- name) {
            x += c.toInt - 64
        }
        if (queries.contains(name)) {
            result += x * (i + 1)
        }
    }
    result
}

// End Euler022

// Start Euler023

def isAbundant(n: Int): Boolean = {
    if (n < 12) {
        return false
    }
    var sumDivisors = 1
    for (i <- 2 to math.sqrt(n).toInt) {
        if (n % i == 0) {
            sumDivisors += i
            if (i != n / i) {
                sumDivisors += n / i
            }
        }
    }
    sumDivisors > n
}

def nonAbundantSums(n: Int): Int = {
    val abundants = mutable.Buffer[Int]()
    for (i <- 12 until n) {
        if (isAbundant(i)) {
            abundants += i
        }
    }
    val abundantSums = mutable.Buffer[Int]()
    for (i <- abundants) {
        for (j <- abundants) {
            abundantSums += i + j
        }
    }
    var result = 0
    for (i <- 0 until n) {
        if (!abundantSums.contains(i)) {
            result += i
        }
    }
    result
}

// End Euler023

// Start Euler024

def lexicographicPermutations(n: Int): String = {
    var result = ""
    var digits = List(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    var x = n - 1
    for (i <- 10 to 1 by -1) {
        var fact = 1
        for (j <- 1 until i) {
            fact *= j
        }
        var idx = x / fact
        result += digits(idx)
        digits = digits.patch(idx, Nil, 1)
        x -= idx * fact
    }
    result
}

// End Euler024

// Start Euler025

def nDigitFibonacciNumber(n: Int): Int = {
    val a = mutable.Buffer(1)
    val b = mutable.Buffer(1)
    var i = 2
    while (b.length < n) {
        var carry = 0
        val c = b.clone
        for (j <- b.indices) {
            if (j < a.length) {
                b(j) = a(j) + b(j) + carry
            } else {
                b(j) = b(j) + carry
            }
            carry = b(j) / 10
            b(j) = b(j) % 10
        }
        if (carry != 0) {
            b += carry
        }
        a.clear
        a ++= c
        i = i + 1
    }
    i
}

// End Euler025

// Start Euler026

def reciprocalCycles(n: Int): Int = {
    var result = 0
    var maxLength = 0
    for (i <- 1 until n) {
        val remainders = mutable.Buffer[Int]()
        var remainder = 1
        while (remainder != 0 && !remainders.contains(remainder)) {
            remainders += remainder
            remainder = (remainder * 10) % i
        }
        var length = 0
        if (remainder != 0) {
            length = remainders.length - remainders.indexOf(remainder)
        }
        if (length > maxLength) {
            maxLength = length
            result = i
        }
    }
    result
}

// End Euler026

// Start Euler027

def isPrime(n: Int): Boolean = {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i <- 3 to math.sqrt(n).toInt by 2) {
        if (n % i == 0) {
            return false
        }
    }
    true
}

def quadraticPrimes(n: Int): Int = {
    var maxPrimes = 0
    var result = 0
    for (a <- -n + 1 until n by 2) {
        for (b <- -n + 1 until n by 2) {
            var x = 0
            breakable {
                while (x * x + a * x + b >= 2) {
                    if (!isPrime(x * x + a * x + b)) {
                        break
                    }
                    x += 1
                }
            }
            if (x > maxPrimes) {
                maxPrimes = x
                result = a * b
            }
        }
    }
    result
}

// End Euler027

// Start Euler028

def numberSpiralDiagonals(n: Int): Int = {
    var result = 1
    for (i <- 3 to n by 2) {
        result += 4 * i * i - 6 * i + 6
    }
    result
}

// End Euler028

// Start Euler029

def distinctPowers(n: Int): Int = {
    var result = 0
    val xs = mutable.Set[String]()
    for (i <- 2 to n) {
        val primes = List(2, 3, 5, 7)
        val powers = mutable.Buffer(0, 0, 0, 0)
        var num = i
        for (j <- primes.indices) {
            while (num % primes(j) == 0) {
                num /= primes(j)
                powers(j) += 1
            }
        }
        if (num != 1) {
            result += n - 1
        } else {
            for (j <- 2 to n) {
                val pstr = s"${powers(0) * j}-${powers(1) * j}-${powers(2) * j}-${powers(3) * j}"
                xs.add(pstr)
            }
        }
    }
    result += xs.size
    result
}

// End Euler029

// Start Euler030

def digitNthPowers(n: Int): Int = {
    var result = 0
    for (i <- 2 until 4 * math.pow(10, n).toInt) {
        var digitsSum = 0
        for (digit <- i.toString) {
            digitsSum += math.pow(digit.asDigit, n).toInt
        }
        if (i == digitsSum) {
            result += i
        }
    }
    result
}

// End Euler030

// Start Euler031

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

// End Euler031

// Start Euler032

def pandigitalProducts(n: Int): Int = {
    val products =  mutable.Set[Int]()
    var s = ""
    for (i <- 1 to n) {
        s += i
    }
    for (a <- 1 until 100) {
        for (b <- 1 until 10000) {
            val c = a * b
            var chars = (a.toString + b.toString + c.toString).toCharArray
            chars = chars.sorted
            if (chars.mkString == s) {
                products.add(c)
            }
        }
    }
    var result = 0
    for (product <- products) {
        result += product
    }
    result
}

// End Euler032

// Start Euler033

def digitCancelingFractions(m: Int): Int = {
    var numer = 1
    var denom = 1
    for (d <- 10 until m) {
        for (n <- 10 until d) {
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
    denom / a
}

// End Euler033

// Start Euler034

def digitFactorials(n: Int): Int = {
    var result = 0
    for (i <- 3 until n) {
        var factSum = 0
        for (digit <- i.toString) {
            var fact = 1
            for (j <- 1 to digit.asDigit) {
                fact *= j
            }
            factSum += fact
        }
        if (i == factSum) {
            result += i
        }
    }
    result
}

// End Euler034

// Start Euler035

def isPrime(n: Int): Boolean = {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i <- 3 to math.sqrt(n).toInt by 2) {
        if (n % i == 0) {
            return false
        }
    }
    true
}

def circularPrimes(n: Int): Int = {
    var count = 0
    for (i <- 2 until n) {
        if (isPrime(i)) {
            val rotations =  mutable.Set[Int]()
            val si = i.toString
            for (j <- 0 until si.length) {
                rotations.add((si.substring(j) + si.substring(0, j)).toInt)
            }
            var flag = true
            breakable {
                for (x <- rotations) {
                    if (!isPrime(x)) {
                        flag = false
                        break
                    }
                }
            }
            if (flag) {
                count += 1
            }
        }
    }
    count
}

// End Euler035

// Start Euler036

def isPalindrome(s: String): Boolean = {
    for (i <- 0 until s.length / 2) {
        if (s(i) != s(s.length - i - 1)) {
            return false
        }
    }
    true
}

def doubleBasePalindromes(n: Int): Int = {
    var result = 0
    for (i <- 1 until n) {
        val strI = i.toString
        val binI = i.toBinaryString
        if (isPalindrome(strI) && isPalindrome(binI)) {
            result += i
        }
    }
    result
}

// End Euler036

// Start Euler037

def isPrime(n: Int): Boolean = {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i <- 3 to math.sqrt(n).toInt by 2) {
        if (n % i == 0) {
            return false
        }
    }
    true
}

def truncatablePrimes(n: Int): Int = {
    var result = 0
    for (i <- 10 until n) {
        if (isPrime(i)) {
            val si = i.toString
            var flag = true
            breakable {
                for (j <- 1 until si.length) {
                    val p1 = si.substring(j).toInt
                    val p2 = si.substring(0, si.length - j).toInt
                    if (!isPrime(p1) || !isPrime(p2)) {
                        flag = false
                        break
                    }
                }
            }
            if (flag) {
                result += i
            }
        }
    }
    result
}

// End Euler037

// Start Euler038

def pandigitalMultiples(n: Int): Int = {
    var result = -1
    for (i <- 2 to n) {
        var cprod = ""
        breakable {
            for (j <- 1 until 10) {
                cprod += (i * j).toString
                if (cprod.length == 9) {
                    val chars = cprod.split("").sorted
                    if (chars.mkString == "123456789") {
                        result = result.max(cprod.toInt)
                        break
                    }
                } else if (cprod.length > 9) {
                    break
                }
            }
        }
    }
    result
}

// End Euler038

// Start Euler039

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

// End Euler039

// Start Euler040

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

// End Euler040

// Start Euler041

def isPrime(n: Int): Boolean = {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i <- 3 to math.sqrt(n).toInt by 2) {
        if (n % i == 0) {
            return false
        }
    }
    true
}

def pandigitalPrime(n: Int): Int = {
    for (i <- n - 1 to 1 by -1) {
        if (isPrime(i)) {
            val si = i.toString
            val length = si.length
            var flag = true
            breakable {
                for (j <- 1 to length) {
                    if (!si.contains(j.toString)) {
                        flag = false
                        break
                    }
                }
                if (flag) {
                    return i
                }
            }
        }
    }
    -1
}

// End Euler041

// Start Euler042

def codedTriangleNumbers(words: collection.Seq[String]): Int = {
    var result = 0
    for (word <- words) {
        var value = 0
        for (c <- word) {
            value += c.toInt - 64
        }
        val n = math.sqrt(value * 2).toInt
        if (n * (n + 1) == value * 2) {
            result += 1
        }
    }
    result
}

// End Euler042

// Start Euler043

def genPermutations(s: String): collection.Seq[String] = {
    if (s.length <= 1) {
        return Seq(s)
    }
    val result = mutable.Buffer[String]()
    for (perm <- genPermutations(s.substring(1))) {
        for (i <- s.indices) {
            result += perm.substring(0, i) + s(0) + perm.substring(i)
        }
    }
    result
}

def subStringDivisibility(n: Int): Int = {
    var result = 0
    val primes = Seq(2, 3, 5, 7, 11, 13, 17)
    var s = ""
    for (i <- 0 to n) {
        s += i
    }
    for (i <- genPermutations(s)) {
        var flag = true
            breakable {
            for (j <- 1 until n - 1) {
                if (i.substring(j, j + 3).toInt % primes(j - 1) != 0) {
                    flag = false
                    break
                }
            }
            if (flag) {
                result += i.toInt
            }
        }
    }
    result
}

// End Euler043

// Start Euler044

def pentagonNumbers(n: Int): Int = {
    val pentagon = mutable.Set[Int]()
    for (i <- 1 until n) {
        pentagon.add(i * (3 * i - 1) / 2)
    }
    var result = -1
    for (j <- pentagon) {
        for (k <- pentagon) {
            if (pentagon.contains(j + k) && pentagon.contains(k - j)) {
                if (result == -1 || k - j < result) {
                    result = k - j
                }
            }
        }
    }
    result
}

// End Euler044

// Start Euler045

def triangularPentagonalAndHexagonal(n: Int): Int = {
    val ps =  mutable.Set[Int]()
    var i = 1
    var c = (0.5 * i * (3 * i - 1)).toInt
    while (c < n) {
        i += 1
        ps.add(c)
        c = (0.5 * i * (3 * i - 1)).toInt
    }
    i = 1
    c = i * (2 * i - 1)
    var result = -1
    while (c < n) {
        i += 1
        if (ps.contains(c)) {
            result = c
        }
        c = i * (2 * i - 1)
    }
    result
}

// End Euler045

// Start Euler046

def isPrime(n: Int): Boolean = {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i <- 3 to math.sqrt(n).toInt by 2) {
        if (n % i == 0) {
            return false
        }
    }
    true
}

def goldbachsOtherConjecture(n: Int): Int = {
    var result = -1
    for (i <- 9999 until n by -2) {
        val upper = math.sqrt(i / 2).toInt
        var flag = false
        breakable {
            for (j <- 0 to upper) {
                if (isPrime(i - 2 * j * j)) {
                    flag = true
                    break
                }
            }
        }
        if (!flag) {
            result = i
        }
    }
    result
}

// End Euler046

// Start Euler047

def primeFactors(n: Int): Int = {
    var num = n
    val factors = mutable.Buffer[Int]()
    var i = 2
    while (i * i <= num) {
        if (num % i != 0) {
            i += 1
        } else {
            num /= i
            factors += i
        }
    }
    if (num > 1) {
        factors += num
    }
    factors.toSet.size
}

def distinctPrimesFactors(n: Int): Int = {
    for (i <- n until 1000000) {
        if (primeFactors(i) == 4 && primeFactors(i + 1) == 4 && primeFactors(i + 2) == 4 && primeFactors(i + 3) == 4) {
            return i
        }
    }
    -1
}

// End Euler047

// Start Euler048

def selfPowers(n: Int): String = {
    val digits = Array.fill(10)(0)
    for (i <- 1 to n) {
        val tempDigits = Array.fill(10)(0)
        tempDigits(0) = 1
        for (j <- 0 until i) {
            var carry = 0
            for (k <- 0 until 10) {
                tempDigits(k) = tempDigits(k) * i + carry
                carry = tempDigits(k) / 10
                tempDigits(k) %= 10
            }
        }
        for (j <- 0 until 10) {
            digits(j) += tempDigits(j)
            if (digits(j) >= 10) {
                digits(j) -= 10
                if (j < 9) {
                    digits(j + 1) += 1
                }
            }
        }
    }
    var result = ""
    for (i <- 9 to 0 by -1) {
        result += digits(i).toString
    }
    result
}

// End Euler048

// Start Euler049

def isPrime(n: Int): Boolean = {
    if (n < 2) {
        return false
    }
    if (n == 2) {
        return true
    }
    if (n % 2 == 0) {
        return false
    }
    for (i <- 3 to math.sqrt(n).toInt by 2) {
        if (n % i == 0) {
            return false
        }
    }
    true
}

def genPermutations(s: String): collection.Seq[String] = {
    if (s.length <= 1) {
        return Seq(s)
    }
    val result = mutable.Buffer[String]()
    for (perm <- genPermutations(s.substring(1))) {
        for (i <- s.indices) {
            result += perm.substring(0, i) + s(0) + perm.substring(i)
        }
    }
    result
}

def primePermutations(n: Int): String = {
    for (i <- n to 999 by -1) {
        if (isPrime(i)) {
            val permutations = genPermutations(i.toString)
            val candidates =  mutable.Set[Int]()
            for (j <- permutations) {
                val candidate = j.toInt
                if (candidate > i && isPrime(candidate)) {
                    candidates += candidate
                }
            }
            for (m <- candidates) {
                if (candidates.contains(m + (m - i))) {
                    return i.toString + m.toString + (m + (m - i)).toString
                }
            }
        }
    }
    ""
}

// End Euler049

// Start Euler050

def consecutivePrimeSum(limit: Int): Int = {
    val sieve = Array.fill(limit)(true)
    val primes = mutable.Buffer[Int]()
    for (i <- 2 until limit) {
        if (sieve(i)) {
            primes += i
            for (j <- i * 2 until limit by i) {
                sieve(j) = false
            }
        }
    }
    var maxLength = 0
    var maxPrime = 0
    for (i <- primes.indices) {
        breakable {
            for (j <- i + maxLength until primes.length) {
                var s = 0
                for (k <- i until j) {
                    s += primes(k)
                }
                if (s >= limit) {
                    break
                }
                if (sieve(s) && j - i > maxLength) {
                    maxLength = j - i
                    maxPrime = s
                }
            }
        }
    }
    maxPrime
}

// End Euler050

