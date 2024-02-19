// Start Euler001

func MultiplesOf3And5(n int) int {
    result := 0
    for i := 0; i < n; i++ {
        if i % 3 == 0 || i % 5 == 0 {
            result += i
        }
    }
    return result
}

// End Euler001

// Start Euler002

func EvenFibonacciNumbers(n int) int {
    result := 0
    a := 1
    b := 2
    for a < n {
        if a % 2 == 0 {
            result += a
        }
        tmp := a
        a = b
        b = tmp + b
    }
    return result
}

// End Euler002

// Start Euler003

func LargestPrimeFactor(n int) int {
    result := n
    i := 2
    for i * i <= result {
        if result % i != 0 {
            i += 1
        } else {
            result /= i
        }
    }
    return result
}

// End Euler003

// Start Euler004

func IsPalindrome(s string) bool {
    for i := 0; i < len(s) / 2; i++ {
        if s[i] != s[len(s) - i - 1] {
            return false
        }
    }
    return true
}

func LargestPalindromeProduct(n int) int {
    result := 0
    for i := 100; i < 1000; i++ {
        for j := i; j < 1000; j++ {
            prod := i * j
            if IsPalindrome(strconv.Itoa(prod)) && prod > result && prod < n {
                result = prod
            }
        }
    }
    return result
}

// End Euler004

// Start Euler005

func SmallestMultiple(n int) int {
    result := 1
    for i := 1; i <= n; i++ {
        if result % i != 0 {
            for j := 1; j <= n; j++ {
                if (result * j) % i == 0 {
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

func SumSquareDifference(n int) int {
    sqrSum := 0
    numSum := 0
    for i := 1; i <= n; i++ {
        sqrSum += i * i
        numSum += i
    }
    return numSum * numSum - sqrSum
}

// End Euler006

// Start Euler007

func NthPrime(n int) int {
    primes := []int{2}
    i := 3
    for len(primes) < n {
        for _, p := range primes {
            if i % p == 0 {
                break
            }
            if p * p > i {
                primes = append(primes, i)
                break
            }
        }
        i += 2
    }
    return primes[len(primes) - 1]
}

// End Euler007

// Start Euler008

func LargestProductInASeries(s string, k int) int {
    result := 0
    for i := 0; i < len(s) - k; i++ {
        product := 1
        for j := 0; j < k; j++ {
            product *= int(s[i + j] - '0')
        }
        result = max(result, product)
    }
    return result
}

// End Euler008

// Start Euler009

func SpecialPythagoreanTriplet(n int) int {
    for a := 1; a < n; a++ {
        for b := a; b < n; b++ {
            c := n - a - b
            if a * a + b * b == c * c {
                return a * b * c
            }
        }
    }
    return -1
}

// End Euler009

// Start Euler010

func SummationOfPrimes(n int) int {
    primes := []int{2}
    i := 3
    for i <= n {
        for _, p := range primes {
            if i % p == 0 {
                break
            }
            if p * p > i {
                primes = append(primes, i)
                break
            }
        }
        i += 2
    }
    result := 0
    for _, prime := range primes {
        result += prime
    }
    return result
}

// End Euler010

// Start Euler011

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

// End Euler011

// Start Euler012

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

// End Euler012

// Start Euler013

func LargeSum(numbers []string) string {
    digits := make([]int, 60)
    for i := 0; i < 50; i++ {
        tmp := 0
        for _, num := range numbers {
            tmp += int(num[49 - i] - '0')
        }
        for j := i; j < 60; j++ {
            digits[j] += tmp % 10
            if digits[j] >= 10 {
                digits[j + 1] += digits[j] / 10
                digits[j] %= 10
            }
            tmp /= 10
            if tmp == 0 {
                break
            }
        }
    }
    for i := 59; i >= 0; i-- {
        if digits[i] != 0 {
            result := ""
            for j := i; j > i - 10; j-- {
                result += strconv.Itoa(digits[j])
            }
            return result
        }
    }
    return ""
}

// End Euler013

// Start Euler014

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

// End Euler014

// Start Euler015

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

// End Euler015

// Start Euler016

func PowerDigitSum(n int) int {
    digits := []int{2}
    for i := 1; i < n; i++ {
        carry := 0
        for j := 0; j < len(digits); j++ {
            temp := digits[j]*2 + carry
            digits[j] = temp % 10
            carry = temp / 10
        }
        if carry != 0 {
            digits = append(digits, carry)
        }
    }
    result := 0
    for _, digit := range digits {
        result += digit
    }
    return result
}

// End Euler016

// Start Euler017

func NumberToWords(n int) string {
    ones := []string{"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
    teens := []string{"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"}
    tens := []string{"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"}
    if n == 1000 {
        return "one thousand"
    } else if n >= 100 {
        if n % 100 == 0 {
            return ones[n / 100] + " hundred"
        } else {
            return ones[n / 100] + " hundred and " + NumberToWords(n % 100)
        }
    } else if n >= 20 {
        suf := ""
        if n % 10 != 0 {
            suf = " " + ones[n % 10]
        }
        return tens[n / 10] + suf
    } else if n >= 10 {
        return teens[n - 10]
    } else {
        return ones[n]
    }
}

// End Euler017

// Start Euler018

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

// End Euler018

// Start Euler019

func CountingSundays(y1 int, y2 int) int {
    day := 0
    count := 0
    for year := 1900; year <= y2; year++ {
        for month := 1; month <= 12; month++ {
            if year >= y1 && day % 7 == 6 {
                count++
            }
            if month == 4 || month == 6 || month == 9 || month == 11 {
                day += 30
            } else if month == 2 {
                if year % 4 == 0 && (year % 100 != 0 || year % 400 == 0) {
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

func FactorialDigitSum(n int) int {
    digits := []int{1}
    for i := 1; i <= n; i++ {
        carry := 0
        for j := 0; j < len(digits); j++ {
            digits[j] = digits[j] * i + carry
            carry = digits[j] / 10
            digits[j] %= 10
        }
        for carry != 0 {
            digits = append(digits, carry % 10)
            carry /= 10
        }
    }
    result := 0
    for _, digit := range digits {
        result += digit
    }
    return result
}

// End Euler020

// Start Euler021

func D(n int) int {
    result := 1
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            result += i
            if i != n / i {
                result += n / i
            }
        }
    }
    return result
}

func AmicableNumbers(n int) int {
    result := 0
    for a := 2; a < n; a++ {
        b := D(a)
        if a != b && a == D(b) {
            result += a
        }
    }
    return result
}

// End Euler021

// Start Euler022

func NamesScores(names []string, queries []string) int {
    sNames := slices.Clone(names)
    slices.Sort(sNames)
    result := 0
    for i, name := range sNames {
        x := 0
        for _, c := range name {
            x += int(c) - 64
        }
        for _, query := range queries {
            if query == name {
                result += x * (i + 1)
                break
            }
        }
    }
    return result
}

// End Euler022

// Start Euler023

func IsAbundant(n int) bool {
    if n < 12 {
        return false
    }
    sumDivisors := 1
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            sumDivisors += i
            if i != n / i {
                sumDivisors += n / i
            }
        }
    }
    return sumDivisors > n
}

func NonAbundantSums(n int) int {
    abundants := []int{}
    for i := 12; i < n; i++ {
        if IsAbundant(i) {
            abundants = append(abundants, i)
        }
    }
    abundantSums := map[int]bool{}
    for _, i := range abundants {
        for _, j := range abundants {
            abundantSums[i + j] = true
        }
    }
    result := 0
    for i := 0; i < n; i++ {
        if !abundantSums[i] {
            result += i
        }
    }
    return result
}

// End Euler023

// Start Euler024

func LexicographicPermutations(n int) string {
    result := ""
    digits := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    x := n - 1
    for i := 10; i > 0; i-- {
        fact := 1
        for j := 1; j < i; j++ {
            fact *= j
        }
        idx := x / fact
        result += strconv.Itoa(digits[idx])
        digits = append(digits[:idx], digits[idx+1:]...)
        x -= idx * fact
    }
    return result
}

// End Euler024

// Start Euler025

func NDigitFibonacciNumber(n int) int {
    a := []int{1}
    b := []int{1}
    i := 2
    for len(b) < n {
        carry := 0
        c := make([]int, len(b))
        copy(c, b)
        for j := 0; j < len(b); j++ {
            if j < len(a) {
                b[j] = a[j] + b[j] + carry
            } else {
                b[j] = b[j] + carry
            }
            carry = b[j] / 10
            b[j] = b[j] % 10
        }
        if carry != 0 {
            b = append(b, carry)
        }
        a = make([]int, len(c))
        copy(a, c)
        i = i + 1
    }
    return i
}

// End Euler025

// Start Euler026

func ReciprocalCycles(n int) int {
    result := 0
    maxLength := 0
    for i := 1; i < n; i++ {
        remainders := []int{}
        remainder := 1
        for remainder != 0 && !slices.Contains(remainders, remainder) {
            remainders = append(remainders, remainder)
            remainder = (remainder * 10) % i
        }
        length := 0
        if remainder != 0 {
            length = len(remainders) - slices.Index(remainders, remainder)
        }
        if length > maxLength {
            maxLength = length
            result = i
        }
    }
    return result
}

// End Euler026

// Start Euler027

func IsPrime(n int) bool {
    if n < 2 {
        return false
    }
    if n == 2 {
        return true
    }
    if n % 2 == 0 {
        return false
    }
    for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func QuadraticPrimes(n int) int {
    maxPrimes := 0
    result := 0
    for a := -n + 1; a < n; a += 2 {
        for b := -n + 1; b < n; b += 2 {
            x := 0
            for {
                if x*x+a*x+b < 2 {
                    break
                }
                if !IsPrime(x*x+a*x+b) {
                    break
                }
                x++
            }
            if x > maxPrimes {
                maxPrimes = x
                result = a * b
            }
        }
    }
    return result
}

// End Euler027

// Start Euler028

func NumberSpiralDiagonals(n int) int {
    result := 1
    for i := 3; i <= n; i += 2 {
        result += 4 * i * i - 6 * i + 6
    }
    return result
}

// End Euler028

// Start Euler029

func DistinctPowers(n int) int {
    result := 0
    xs := map[string]bool{}
    for i := 2; i <= n; i++ {
        primes := []int{2, 3, 5, 7}
        powers := []int{0, 0, 0, 0}
        num := i
        for j := 0; j < len(primes); j++ {
            for num % primes[j] == 0 {
                num /= primes[j]
                powers[j] += 1
            }
        }
        if num != 1 {
            result += n - 1
            continue
        }
        for j := 2; j <= n; j++ {
            pstr := fmt.Sprintf("%d-%d-%d-%d", powers[0] * j, powers[1] * j, powers[2] * j, powers[3] * j)
            xs[pstr] = true
        }
    }
    result += len(xs)
    return result
}

// End Euler029

// Start Euler030

func DigitNthPowers(n int) int {
    result := 0
    for i := 2; i < 4 * int(math.Pow(10, float64(n))); i++ {
        digitsSum := 0
        for _, digit := range strconv.Itoa(i) {
            digitInt, _ := strconv.Atoi(string(digit))
            digitsSum += int(math.Pow(float64(digitInt), float64(n)))
        }
        if i == digitsSum {
            result += i
        }
    }
    return result
}

// End Euler030

// Start Euler031

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

// End Euler031

// Start Euler032

func PandigitalProducts(n int) int {
    products := map[int]bool{}
    s := ""
    for i := 1; i <= n; i++ {
        s += strconv.Itoa(i)
    }
    for a := 1; a < 100; a++ {
        for b := 1; b < 10000; b++ {
            c := a * b
            chars := []rune(strconv.Itoa(a) + strconv.Itoa(b) + strconv.Itoa(c))
            slices.Sort(chars)
            if string(chars) == s {
                products[c] = true
            }
        }
    }
    result := 0
    for product := range products {
        result += product
    }
    return result
}

// End Euler032

// Start Euler033

func DigitCancelingFractions(m int) int {
    numer := 1
    denom := 1
    for d := 10; d < m; d++ {
        for n := 10; n < d; n++ {
            n0 := n % 10
            n1 := n / 10
            d0 := d % 10
            d1 := d / 10
            if (n1 == d0 && n0 * d == n * d1) || (n0 == d1 && n1 * d == n * d0) {
                numer *= n
                denom *= d
            }
        }
    }
    a := numer
    b := denom
    for b != 0 {
        temp := b
        b = a % b
        a = temp
    }
    return denom / a
}

// End Euler033

// Start Euler034

func DigitFactorials(n int) int {
    result := 0
    for i := 3; i < n; i++ {
        factSum := 0
        for _, digit := range strconv.Itoa(i) {
            fact := 1
            for j := 1; j <= int(digit - '0'); j++ {
                fact *= j
            }
            factSum += fact
        }
        if i == factSum {
            result += i
        }
    }
    return result
}

// End Euler034

// Start Euler035

func IsPrime(n int) bool {
    if n < 2 {
        return false
    }
    if n == 2 {
        return true
    }
    if n % 2 == 0 {
        return false
    }
    for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func CircularPrimes(n int) int {
    count := 0
    for i := 2; i < n; i++ {
        if IsPrime(i) {
            rotations := map[int]bool{}
            si := strconv.Itoa(i)
            for j := 0; j < len(si); j++ {
                x, _ := strconv.Atoi(si[j:] + si[:j])
                rotations[x] = true
            }
            flag := true
            for x := range rotations {
                if !IsPrime(x) {
                    flag = false
                    break
                }
            }
            if flag {
                count++
            }
        }
    }
    return count
}

// End Euler035

// Start Euler036

func IsPalindrome(s string) bool {
    for i := 0; i < len(s) / 2; i++ {
        if s[i] != s[len(s) - i - 1] {
            return false
        }
    }
    return true
}

func DoubleBasePalindromes(n int) int {
    result := 0
    for i := 1; i < n; i++ {
        strI := strconv.Itoa(i)
        binI := strconv.FormatInt(int64(i), 2)
        if IsPalindrome(strI) && IsPalindrome(binI) {
            result += i
        }
    }
    return result
}

// End Euler036

// Start Euler037

func IsPrime(n int) bool {
    if n < 2 {
        return false
    }
    if n == 2 {
        return true
    }
    if n % 2 == 0 {
        return false
    }
    for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func TruncatablePrimes(n int) int {
    result := 0
    for i := 10; i < n; i++ {
        if IsPrime(i) {
            si := strconv.Itoa(i)
            flag := true
            for j := 1; j < len(si); j++ {
                p1, _ := strconv.Atoi(si[j:])
                p2, _ := strconv.Atoi(si[:len(si) - j])
                if !IsPrime(p1) || !IsPrime(p2) {
                    flag = false
                    break
                }
            }
            if flag {
                result += i
            }
        }
    }
    return result
}

// End Euler037

// Start Euler038

func PandigitalMultiples(n int) int {
    result := -1
    for i := 2; i <= n; i++ {
        cprod := ""
        for j := 1; j < 10; j++ {
            cprod += strconv.Itoa(i * j)
            if len(cprod) == 9 {
                chars := strings.Split(cprod, "")
                sort.Strings(chars)
                if strings.Join(chars, "") == "123456789" {
                    cprodInt, _ := strconv.Atoi(cprod)
                    result = max(result, cprodInt)
                    break
                }
            } else if len(cprod) > 9 {
                break
            }
        }
    }
    return result
}

// End Euler038

// Start Euler039

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

// End Euler039

// Start Euler040

func ChampernowneConstant(b int) int {
    s := ""
    for i := 1; i < int(math.Pow(float64(b), 6)); i++ {
        s += strconv.Itoa(i)
    }
    result := 1
    for i := 0; i < 7; i++ {
        n, _ := strconv.Atoi(string(s[int(math.Pow(float64(b), float64(i))) - 1]))
        result *= n
    }
    return result
}

// End Euler040

// Start Euler041

func IsPrime(n int) bool {
    if n < 2 {
        return false
    }
    if n == 2 {
        return true
    }
    if n % 2 == 0 {
        return false
    }
    for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func PandigitalPrime(n int) int {
    for i := n - 1; i > 0; i-- {
        if IsPrime(i) {
            si := strconv.Itoa(i)
            length := len(si)
            flag := true
            for j := 1; j <= length; j++ {
                if !strings.Contains(si, strconv.Itoa(j)) {
                    flag = false
                    break
                }
            }
            if flag {
                return i
            }
        }
    }
    return -1
}

// End Euler041

// Start Euler042

func CodedTriangleNumbers(words []string) int {
    result := 0
    for _, word := range words {
        value := 0
        for _, c := range word {
            value += int(c) - 64
        }
        n := int(math.Sqrt(float64(value * 2)))
        if n * (n + 1) == value * 2 {
            result++
        }
    }
    return result
}

// End Euler042

// Start Euler043

func GenPermutations(s string) []string {
    if len(s) <= 1 {
        return []string{s}
    }
    result := []string{}
    for _, perm := range GenPermutations(s[1:]) {
        for i := 0; i < len(s); i++ {
            result = append(result, perm[:i] + string(s[0]) + perm[i:])
        }
    }
    return result
}

func SubStringDivisibility(n int) int {
    result := 0
    primes := []int{2, 3, 5, 7, 11, 13, 17}
    s := ""
    for i := 0; i <= n; i++ {
        s += strconv.Itoa(i)
    }
    for _, i := range GenPermutations(s) {
        flag := true
        for j := 1; j < n - 1; j++ {
            if n, _ := strconv.Atoi(i[j:j + 3]); n % primes[j - 1] != 0 {
                flag = false
                break
            }
        }
        if flag {
            s0, _ := strconv.Atoi(i)
            result += s0
        }
    }
    return result
}

// End Euler043

// Start Euler044

func PentagonNumbers(n int) int {
    pentagon := map[int]bool{}
    for i := 1; i < n; i++ {
        pentagon[i * (3 * i - 1) / 2] = true
    }
    result := -1
    for j := range pentagon {
        for k := range pentagon {
            if pentagon[j + k] && pentagon[k - j] {
                if result == -1 || k - j < result {
                    result = k - j
                }
            }
        }
    }
    return result
}

// End Euler044

// Start Euler045

func TriangularPentagonalAndHexagonal(n int) int {
    ps := map[int]bool{}
    i := 1
    c := int(0.5 * float64(i) * (3 * float64(i) - 1))
    for c < n {
        i++
        ps[c] = true
        c = int(0.5 * float64(i) * (3 * float64(i) - 1))
    }
    i = 1
    c = i * (2 * i - 1)
    result := -1
    for c < n {
        i++
        if ps[c] {
            result = c
        }
        c = i * (2 * i - 1)
    }
    return result
}

// End Euler045

// Start Euler046

func IsPrime(n int) bool {
    if n < 2 {
        return false
    }
    if n == 2 {
        return true
    }
    if n % 2 == 0 {
        return false
    }
    for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func GoldbachsOtherConjecture(n int) int {
    result := -1
    for i := 9999; i > n; i -= 2 {
        upper := int(math.Sqrt(float64(i / 2)))
        flag := false
        for j := 0; j <= upper; j++ {
            if IsPrime(i - 2 * j * j) {
                flag = true
                break
            }
        }
        if !flag {
            result = i
        }
    }
    return result
}

// End Euler046

// Start Euler047

func PrimeFactors(n int) int {
    num := n
    factors := []int{}
    i := 2
    for i * i <= num {
        if num % i != 0 {
            i++
        } else {
            num /= i
            factors = append(factors, i)
        }
    }
    if num > 1 {
        factors = append(factors, num)
    }
    s := map[int]bool{}
    for _, v := range factors {
        s[v] = true
    }
    return len(s)
}

func DistinctPrimesFactors(n int) int {
    for i := n; i < 1000000; i++ {
        if PrimeFactors(i) == 4 && PrimeFactors(i + 1) == 4 && PrimeFactors(i + 2) == 4 && PrimeFactors(i + 3) == 4 {
            return i
        }
    }
    return -1
}

// End Euler047

// Start Euler048

func SelfPowers(n int) string {
    digits := [10]int{}
    for i := 1; i <= n; i++ {
        tempDigits := [10]int{}
        tempDigits[0] = 1
        for j := 0; j < i; j++ {
            carry := 0
            for k := 0; k < 10; k++ {
                tempDigits[k] = tempDigits[k] * i + carry
                carry = tempDigits[k] / 10
                tempDigits[k] %= 10
            }
        }
        for j := 0; j < 10; j++ {
            digits[j] += tempDigits[j]
            if digits[j] >= 10 {
                digits[j] -= 10
                if j < 9 {
                    digits[j + 1] += 1
                }
            }
        }
    }
    result := ""
    for i := 9; i >= 0; i-- {
        result += strconv.Itoa(digits[i])
    }
    return result
}

// End Euler048

// Start Euler049

func IsPrime(n int) bool {
    if n < 2 {
        return false
    }
    if n == 2 {
        return true
    }
    if n % 2 == 0 {
        return false
    }
    for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func GenPermutations(s string) []string {
    if len(s) <= 1 {
        return []string{s}
    }
    result := []string{}
    for _, perm := range GenPermutations(s[1:]) {
        for i := 0; i < len(s); i++ {
            result = append(result, perm[:i] + string(s[0]) + perm[i:])
        }
    }
    return result
}

func PrimePermutations(n int) string {
    for i := n; i > 999; i-- {
        if IsPrime(i) {
            permutations := GenPermutations(strconv.Itoa(i))
            candidates := map[int]bool{}
            for _, j := range permutations {
                candidate, _ := strconv.Atoi(j)
                if candidate > i && IsPrime(candidate) {
                    candidates[candidate] = true
                }
            }
            for m := range candidates {
                if candidates[m + (m - i)] {
                    return strconv.Itoa(i) + strconv.Itoa(m) + strconv.Itoa(m + (m - i))
                }
            }
        }
    }
    return ""
}

// End Euler049

// Start Euler050

func ConsecutivePrimeSum(limit int) int {
    sieve := make([]bool, limit)
    for i := range sieve {
        sieve[i] = true
    }
    primes := []int{}
    for i := 2; i < limit; i++ {
        if sieve[i] {
            primes = append(primes, i)
            for j := i * 2; j < limit; j += i {
                sieve[j] = false
            }
        }
    }
    maxLength := 0
    maxPrime := 0
    for i := 0; i < len(primes); i++ {
        for j := i + maxLength; j < len(primes); j++ {
            s := 0
            for k := i; k < j; k++ {
                s += primes[k]
            }
            if s >= limit {
                break
            }
            if sieve[s] && j - i > maxLength {
                maxLength = j - i
                maxPrime = s
            }
        }
    }
    return maxPrime
}

// End Euler050

