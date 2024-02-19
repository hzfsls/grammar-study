// Start Euler001

class Global {
    public static int MultiplesOf3And5(int n) {
        int result = 0;
        for (int i = 0; i < n; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                result += i;
            }
        }
        return result;
    }
}

// End Euler001

// Start Euler002

class Global {
    public static int EvenFibonacciNumbers(int n) {
        int result = 0;
        int a = 1;
        int b = 2;
        while (a < n) {
            if (a % 2 == 0) {
                result += a;
            }
            int tmp = a;
            a = b;
            b = tmp + b;
        }
        return result;
    }
}

// End Euler002

// Start Euler003

class Global {
    public static int LargestPrimeFactor(int n) {
        int result = n;
        int i = 2;
        while (i * i <= result) {
            if (result % i != 0) {
                i += 1;
            } else {
                result /= i;
            }
        }
        return result;
    }
}

// End Euler003

// Start Euler004

class Global {
    public static bool IsPalindrome(string s) {
        for (int i = 0; i < s.Length / 2; i++) {
            if (s[i] != s[s.Length - i - 1]) {
                return false;
            }
        }
        return true;
    }

    public static int LargestPalindromeProduct(int n) {
        int result = 0;
        for (int i = 100; i < 1000; i++) {
            for (int j = i; j < 1000; j++) {
                int prod = i * j;
                if (IsPalindrome(prod.ToString()) && prod > result && prod < n) {
                    result = prod;
                }
            }
        }
        return result;
    }
}

// End Euler004

// Start Euler005

class Global {
    public static int SmallestMultiple(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            if (result % i != 0) {
                for (int j = 1; j <= n; j++) {
                    if ((result * j) % i == 0) {
                        result *= j;
                        break;
                    }
                }
            }
        }
        return result;
    }
}

// End Euler005

// Start Euler006

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

// End Euler006

// Start Euler007

class Global {
    public static int NthPrime(int n) {
        List<int> primes = new List<int> {2};
        int i = 3;
        while (primes.Count < n) {
            foreach (int p in primes) {
                if (i % p == 0) {
                    break;
                }
                if (p * p > i) {
                    primes.Add(i);
                    break;
                }
            }
            i += 2;
        }
        return primes.Last();
    }
}

// End Euler007

// Start Euler008

class Global {
    public static int LargestProductInASeries(string s, int k) {
        int result = 0;
        for (int i = 0; i < s.Length - k; i++) {
            int product = 1;
            for (int j = 0; j < k; j++) {
                product *= s[i + j] - '0';
            }
            result = Math.Max(result, product);
        }
        return result;
    }
}

// End Euler008

// Start Euler009

class Global {
    public static int SpecialPythagoreanTriplet(int n) {
        for (int a = 1; a < n; a++) {
            for (int b = a; b < n; b++) {
                int c = n - a - b;
                if (a * a + b * b == c * c) {
                    return a * b * c;
                }
            }
        }
        return -1;
    }
}

// End Euler009

// Start Euler010

class Global {
    public static int SummationOfPrimes(int n) {
        List<int> primes = new List<int> {2};
        int i = 3;
        while (i <= n) {
            foreach (int p in primes) {
                if (i % p == 0) {
                    break;
                }
                if (p * p > i) {
                    primes.Add(i);
                    break;
                }
            }
            i += 2;
        }
        int result = 0;
        foreach (int prime in primes) {
            result += prime;
        }
        return result;
    }
}

// End Euler010

// Start Euler011

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

// End Euler011

// Start Euler012

class Global {
    public static int HighlyDivisibleTriangularNumber(int n) {
        for (int i = 1; i < 100000000; i++) {
            int result = i * (i + 1) / 2;
            int count = 0;
            for (int j = 1; j <= (int)Math.Sqrt(result); j++) {
                if (result % j == 0) {
                    count += 2;
                }
                if (j * j == result) {
                    count -= 1;
                }
            }
            if (count > n) {
                return result;
            }
        }
        return -1;
    }    
}

// End Euler012

// Start Euler013

class Global {
    public static string LargeSum(IList<string> numbers) {
        int[] digits = new int[60];
        for (int i = 0; i < 50; i++) {
            int tmp = 0;
            foreach (var num in numbers) {
                tmp += num[49 - i] - '0';
            }
            for (int j = i; j < 60; j++) {
                digits[j] += tmp % 10;
                if (digits[j] >= 10) {
                    digits[j + 1] += digits[j] / 10;
                    digits[j] %= 10;
                }
                tmp /= 10;
                if (tmp == 0) {
                    break;
                }
            }
        }
        for (int i = 59; i >= 0; i--) {
            if (digits[i] != 0) {
                string result = "";
                for (int j = i; j > i - 10; j--) {
                    result += digits[j].ToString();
                }
                return result;
            }
        }
        return "";
    }
}

// End Euler013

// Start Euler014

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

// End Euler014

// Start Euler015

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

// End Euler015

// Start Euler016

class Global {
    public static int PowerDigitSum(int n) {
        List<int> digits = new List<int> {2};
        for (int i = 1; i < n; i++) {
            int carry = 0;
            for (int j = 0; j < digits.Count; j++) {
                int temp = digits[j] * 2 + carry;
                digits[j] = temp % 10;
                carry = temp / 10;
            }
            if (carry != 0) {
                digits.Add(carry);
            }
        }
        int result = 0;
        foreach (int digit in digits) {
            result += digit;
        }
        return result;
    }
}

// End Euler016

// Start Euler017

class Global {
    public static string NumberToWords(int n) {
        string[] ones = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        string[] teens = {"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
        string[] tens = {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
        if (n == 1000) {
            return "one thousand";
        } else if (n >= 100) {
            if (n % 100 == 0) {
                return ones[n / 100] + " hundred";
            } else {
                return ones[n / 100] + " hundred and " + NumberToWords(n % 100);
            }
        } else if (n >= 20) {
            string suf = "";
            if (n % 10 != 0) {
                suf = " " + ones[n % 10];
            }
            return tens[n / 10] + suf;
        } else if (n >= 10) {
            return teens[n - 10];
        } else {
            return ones[n];
        }
    }
}

// End Euler017

// Start Euler018

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

// End Euler018

// Start Euler019

class Global {
    public static int CountingSundays(int y1, int y2) {
        int day = 0;
        int count = 0;
        for (int year = 1900; year <= y2; year++) {
            for (int month = 1; month <= 12; month++) {
                if (year >= y1 && day % 7 == 6) {
                    count++;
                }
                if (month == 4 || month == 6 || month == 9 || month == 11) {
                    day += 30;
                } else if (month == 2) {
                    if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
                        day += 29;
                    } else {
                        day += 28;
                    }
                } else {
                    day += 31;
                }
            }
        }
        return count;
    }
}

// End Euler019

// Start Euler020

class Global {
    public static int FactorialDigitSum(int n) {
        List<int> digits = new List<int> {1};
        for (int i = 1; i <= n; i++) {
            int carry = 0;
            for (int j = 0; j < digits.Count; j++) {
                digits[j] = digits[j] * i + carry;
                carry = digits[j] / 10;
                digits[j] %= 10;
            }
            while (carry != 0) {
                digits.Add(carry % 10);
                carry /= 10;
            }
        }
        int result = 0;
        foreach (int digit in digits) {
            result += digit;
        }
        return result;
    }
}

// End Euler020

// Start Euler021

class Global {
    public static int D(int n) {
        int result = 1;
        for (int i = 2; i <= Math.Sqrt(n); i++) {
            if (n % i == 0) {
                result += i;
                if (i != n / i) {
                    result += n / i;
                }
            }
        }
        return result;
    }

    public static int AmicableNumbers(int n) {
        int result = 0;
        for (int a = 2; a < n; a++) {
            int b = D(a);
            if (a != b && a == D(b)) {
                result += a;
            }
        }
        return result;
    }
}

// End Euler021

// Start Euler022

class Global {
    public static int NamesScores(IList<string> names, IList<string> queries) {
        var sNames = names.OrderBy(x => x).ToList();
        var result = 0;
        for (var i = 0; i < sNames.Count; i++) {
            var x = 0;
            foreach (var c in sNames[i]) {
                x += c - 64;
            }
            if (queries.Contains(sNames[i])) {
                result += x * (i + 1);
            }
        }
        return result;
    }
}

// End Euler022

// Start Euler023

class Global {
    public static bool IsAbundant(int n) {
        if (n < 12) {
            return false;
        }
        int sumDivisors = 1;
        for (int i = 2; i <= Math.Sqrt(n); i++) {
            if (n % i == 0) {
                sumDivisors += i;
                if (i != n / i) {
                    sumDivisors += n / i;
                }
            }
        }
        return sumDivisors > n;
    }

    public static int NonAbundantSums(int n) {
        List<int> abundants = new List<int>();
        for (int i = 12; i < n; i++) {
            if (IsAbundant(i)) {
                abundants.Add(i);
            }
        }
        HashSet<int> abundantSums = new HashSet<int>();
        foreach (int i in abundants) {
            foreach (int j in abundants) {
                abundantSums.Add(i + j);
            }
        }
        int result = 0;
        for (int i = 0; i < n; i++) {
            if (!abundantSums.Contains(i)) {
                result += i;
            }
        }
        return result;
    }
}

// End Euler023

// Start Euler024

class Global {
    public static string LexicographicPermutations(int n) {
        string result = "";
        List<int> digits = new List<int> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int x = n - 1;
        for (int i = 10; i > 0; i--) {
            int fact = 1;
            for (int j = 1; j < i; j++) {
                fact *= j;
            }
            int idx = x / fact;
            result += digits[idx].ToString();
            digits.RemoveAt(idx);
            x -= idx * fact;
        }
        return result;
    }
}

// End Euler024

// Start Euler025

class Global {
    public static int NDigitFibonacciNumber(int n) {
        List<int> a = new List<int> {1};
        List<int> b = new List<int> {1};
        int i = 2;
        while (b.Count < n) {
            int carry = 0;
            List<int> c = new List<int>(b);
            for (int j = 0; j < b.Count; j++) {
                if (j < a.Count) {
                    b[j] = a[j] + b[j] + carry;
                } else {
                    b[j] = b[j] + carry;
                }
                carry = b[j] / 10;
                b[j] = b[j] % 10;
            }
            if (carry != 0) {
                b.Add(carry);
            }
            a = new List<int>(c);
            i = i + 1;
        }
        return i;
    }
}

// End Euler025

// Start Euler026

class Global {
    public static int ReciprocalCycles(int n) {
        int result = 0;
        int maxLength = 0;
        for (int i = 1; i < n; i++) {
            List<int> remainders = new List<int>();
            int remainder = 1;
            while (remainder != 0 && !remainders.Contains(remainder)) {
                remainders.Add(remainder);
                remainder = (remainder * 10) % i;
            }
            int length = 0;
            if (remainder != 0) {
                length = remainders.Count - remainders.IndexOf(remainder);
            }
            if (length > maxLength) {
                maxLength = length;
                result = i;
            }
        }
        return result;
    }
}

// End Euler026

// Start Euler027

class Global {
    public static bool IsPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= (int)Math.Sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int QuadraticPrimes(int n) {
        int maxPrimes = 0;
        int result = 0;
        for (int a = -n + 1; a < n; a += 2) {
            for (int b = -n + 1; b < n; b += 2) {
                int x = 0;
                while (true) {
                    if (x * x + a * x + b < 2) {
                        break;
                    }
                    if (!IsPrime(x * x + a * x + b)) {
                        break;
                    }
                    x++;
                }
                if (x > maxPrimes) {
                    maxPrimes = x;
                    result = a * b;
                }
            }
        }
        return result;
    }
}

// End Euler027

// Start Euler028

class Global {
    public static int NumberSpiralDiagonals(int n) {
        int result = 1;
        for (int i = 3; i <= n; i += 2) {
            result += 4 * i * i - 6 * i + 6;
        }
        return result;
    }
}

// End Euler028

// Start Euler029

class Global {
    public static int DistinctPowers(int n) {
        int result = 0;
        HashSet<string> xs = new HashSet<string>();
        for (int i = 2; i <= n; i++) {
            List<int> primes = new List<int> {2, 3, 5, 7};
            List<int> powers = new List<int> {0, 0, 0, 0};
            int num = i;
            for (int j = 0; j < primes.Count; j++) {
                while (num % primes[j] == 0) {
                    num /= primes[j];
                    powers[j] += 1;
                }
            }
            if (num != 1) {
                result += n - 1;
                continue;
            }
            for (int j = 2; j <= n; j++) {
                string pstr = string.Format("{0}-{1}-{2}-{3}", powers[0] * j, powers[1] * j, powers[2] * j, powers[3] * j);
                xs.Add(pstr);
            }
        }
        result += xs.Count;
        return result;
    }
}

// End Euler029

// Start Euler030

class Global {
    public static int DigitNthPowers(int n) {
        int result = 0;
        for (int i = 2; i < 4 * Math.Pow(10, n); i++) {
            int digitsSum = 0;
            foreach (char digit in i.ToString()) {
                digitsSum += (int)Math.Pow(digit - '0', n);
            }
            if (i == digitsSum) {
                result += i;
            }
        }
        return result;
    }
}

// End Euler030

// Start Euler031

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

// End Euler031

// Start Euler032

class Global {
    public static int PandigitalProducts(int n) {
        HashSet<int> products = new HashSet<int>();
        string s = "";
        for (int i = 1; i <= n; i++) {
            s += i.ToString();
        }
        for (int a = 1; a < 100; a++) {
            for (int b = 1; b < 10000; b++) {
                int c = a * b;
                char[] chars = (a.ToString() + b.ToString() + c.ToString()).ToCharArray();
                Array.Sort(chars);
                if (new string(chars) == s) {
                    products.Add(c);
                }
            }
        }
        int result = 0;
        foreach (int product in products) {
            result += product;
        }
        return result;
    }
}

// End Euler032

// Start Euler033

class Global {
    public static int DigitCancelingFractions(int m) {
        int numer = 1;
        int denom = 1;
        for (int d = 10; d < m; d++) {
            for (int n = 10; n < d; n++) {
                int n0 = n % 10;
                int n1 = n / 10;
                int d0 = d % 10;
                int d1 = d / 10;
                if ((n1 == d0 && n0 * d == n * d1) || (n0 == d1 && n1 * d == n * d0)) {
                    numer *= n;
                    denom *= d;
                }
            }
        }
        int a = numer;
        int b = denom;
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return denom / a;
    }
}

// End Euler033

// Start Euler034

class Global {
    public static int DigitFactorials(int n) {
        int result = 0;
        for (int i = 3; i < n; i++) {
            int factSum = 0;
            foreach (char digit in i.ToString()) {
                int fact = 1;
                for (int j = 1; j <= digit - '0'; j++) {
                    fact *= j;
                }
                factSum += fact;
            }
            if (i == factSum) {
                result += i;
            }
        }
        return result;
    }
}

// End Euler034

// Start Euler035

class Global {
    public static bool IsPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= (int)Math.Sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int CircularPrimes(int n) {
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (IsPrime(i)) {
                HashSet<int> rotations = new HashSet<int>();
                string si = i.ToString();
                for (int j = 0; j < si.Length; j++) {
                    rotations.Add(int.Parse(si.Substring(j) + si.Substring(0, j)));
                }
                bool flag = true;
                foreach (int x in rotations) {
                    if (!IsPrime(x)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    count++;
                }
            }
        }
        return count;
    }
}

// End Euler035

// Start Euler036

class Global {
    public static bool IsPalindrome(string s) {
        for (int i = 0; i < s.Length / 2; i++) {
            if (s[i] != s[s.Length - i - 1]) {
                return false;
            }
        }
        return true;
    }

    public static int DoubleBasePalindromes(int n) {
        int result = 0;
        for (int i = 1; i < n; i++) {
            string strI = i.ToString();
            string binI = Convert.ToString(i, 2);
            if (IsPalindrome(strI) && IsPalindrome(binI)) {
                result += i;
            }
        }
        return result;
    }
}

// End Euler036

// Start Euler037

class Global {
    public static bool IsPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= (int)Math.Sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int TruncatablePrimes(int n) {
        int result = 0;
        for (int i = 10; i < n; i++) {
            if (IsPrime(i)) {
                string si = i.ToString();
                bool flag = true;
                for (int j = 1; j < si.Length; j++) {
                    int p1 = int.Parse(si.Substring(j));
                    int p2 = int.Parse(si.Substring(0, si.Length - j));
                    if (!IsPrime(p1) || !IsPrime(p2)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    result += i;
                }
            }
        }
        return result;
    }
}

// End Euler037

// Start Euler038

class Global {
    public static int PandigitalMultiples(int n) {
        int result = -1;
        for (int i = 2; i <= n; i++) {
            string cprod = "";
            for (int j = 1; j < 10; j++) {
                cprod += (i * j).ToString();
                if (cprod.Length == 9) {
                    char[] chars = cprod.ToCharArray();
                    Array.Sort(chars);
                    if (new string(chars) == "123456789") {
                        result = Math.Max(result, int.Parse(cprod));
                        break;
                    }
                } else if (cprod.Length > 9) {
                    break;
                }
            }
        }
        return result;
    }
}

// End Euler038

// Start Euler039

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

// End Euler039

// Start Euler040

class Global {
    public static int ChampernowneConstant(int b) {
        string s = "";
        for (int i = 1; i < Math.Pow(b, 6); i++) {
            s += i.ToString();
        }
        int result = 1;
        for (int i = 0; i < 7; i++) {
            result *= s[(int)Math.Pow(b, i) - 1] - '0';
        }
        return result;
    }
}

// End Euler040

// Start Euler041

class Global {
    public static bool IsPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= (int)Math.Sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int PandigitalPrime(int n) {
        for (int i = n - 1; i > 0; i--) {
            if (IsPrime(i)) {
                string si = i.ToString();
                int length = si.Length;
                bool flag = true;
                for (int j = 1; j <= length; j++) {
                    if (!si.Contains(j.ToString())) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    return i;
                }
            }
        }
        return -1;
    }
}

// End Euler041

// Start Euler042

class Global {
    public static int CodedTriangleNumbers(IList<string> words) {
        int result = 0;
        foreach (string word in words) {
            int value = 0;
            foreach (char c in word) {
                value += c - 64;
            }
            int n = (int)Math.Sqrt(value * 2);
            if (n * (n + 1) == value * 2) {
                result++;
            }
        }
        return result;
    }
}

// End Euler042

// Start Euler043

class Global {
    public static IList<string> GenPermutations(string s) {
        if (s.Length <= 1) {
            return new List<string> { s };
        }
        List<string> result = new List<string>();
        foreach (string perm in GenPermutations(s.Substring(1))) {
            for (int i = 0; i < s.Length; i++) {
                result.Add(perm.Substring(0, i) + s[0] + perm.Substring(i));
            }
        }
        return result;
    }

    public static int SubStringDivisibility(int n) {
        int result = 0;
        List<int> primes = new List<int> { 2, 3, 5, 7, 11, 13, 17 };
        string s = "";
        for (int i = 0; i <= n; i++) {
            s += i.ToString();
        }
        foreach (string i in GenPermutations(s)) {
            bool flag = true;
            for (int j = 1; j < n - 1; j++) {
                if (int.Parse(i.Substring(j, 3)) % primes[j - 1] != 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                result += int.Parse(i);
            }
        }
        return result;
    }
}

// End Euler043

// Start Euler044

class Global {
    public static int PentagonNumbers(int n) {
        HashSet<int> pentagon = new HashSet<int>();
        for (int i = 1; i < n; i++) {
            pentagon.Add(i * (3 * i - 1) / 2);
        }
        int result = -1;
        foreach (int j in pentagon) {
            foreach (int k in pentagon) {
                if (pentagon.Contains(j + k) && pentagon.Contains(k - j)) {
                    if (result == -1 || k - j < result) {
                        result = k - j;
                    }
                }
            }
        }
        return result;
    }
}

// End Euler044

// Start Euler045

class Global {
    public static int TriangularPentagonalAndHexagonal(int n) {
        HashSet<int> ps = new HashSet<int>();
        int i = 1;
        int c = (int)(0.5 * i * (3 * i - 1));
        while (c < n) {
            i++;
            ps.Add(c);
            c = (int)(0.5 * i * (3 * i - 1));
        }
        i = 1;
        c = i * (2 * i - 1);
        int result = -1;
        while (c < n) {
            i++;
            if (ps.Contains(c)) {
                result = c;
            }
            c = i * (2 * i - 1);
        }
        return result;
    }
}

// End Euler045

// Start Euler046

class Global {
    public static bool IsPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= (int)Math.Sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int GoldbachsOtherConjecture(int n) {
        int result = -1;
        for (int i = 9999; i > n; i -= 2) {
            int upper = (int)Math.Sqrt(i / 2);
            bool flag = false;
            for (int j = 0; j <= upper; j++) {
                if (IsPrime(i - 2 * j * j)) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                result = i;
            }
        }
        return result;
    }
}

// End Euler046

// Start Euler047

class Global {
    public static int PrimeFactors(int n) {
        int num = n;
        List<int> factors = new List<int>();
        int i = 2;
        while (i * i <= num) {
            if (num % i != 0) {
                i++;
            } else {
                num /= i;
                factors.Add(i);
            }
        }
        if (num > 1) {
            factors.Add(num);
        }
        return factors.Distinct().Count();
    }

    public static int DistinctPrimesFactors(int n) {
        for (int i = n; i < 1000000; i++) {
            if (PrimeFactors(i) == 4 && PrimeFactors(i + 1) == 4 && PrimeFactors(i + 2) == 4 && PrimeFactors(i + 3) == 4) {
                return i;
            }
        }
        return -1;
    }
}

// End Euler047

// Start Euler048

class Global {
    public static string SelfPowers(int n) {
        int[] digits = new int[10];
        for (int i = 1; i <= n; i++) {
            int[] tempDigits = new int[10];
            tempDigits[0] = 1;
            for (int j = 0; j < i; j++) {
                int carry = 0;
                for (int k = 0; k < 10; k++) {
                    tempDigits[k] = tempDigits[k] * i + carry;
                    carry = tempDigits[k] / 10;
                    tempDigits[k] %= 10;
                }
            }
            for (int j = 0; j < 10; j++) {
                digits[j] += tempDigits[j];
                if (digits[j] >= 10) {
                    digits[j] -= 10;
                    if (j < 9) {
                        digits[j + 1] += 1;
                    }
                }
            }
        }
        string result = "";
        for (int i = 9; i >= 0; i--) {
            result += digits[i].ToString();
        }
        return result;
    }
}

// End Euler048

// Start Euler049

class Global {
    public static bool IsPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= (int)Math.Sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static IList<string> GenPermutations(string s) {
        if (s.Length <= 1) {
            return new List<string> { s };
        }
        List<string> result = new List<string>();
        foreach (string perm in GenPermutations(s.Substring(1))) {
            for (int i = 0; i < s.Length; i++) {
                result.Add(perm.Substring(0, i) + s[0] + perm.Substring(i));
            }
        }
        return result;
    }

    public static string PrimePermutations(int n) {
        for (int i = n; i > 999; --i) {
            if (IsPrime(i)) {
                var permutations = GenPermutations(i.ToString());
                var candidates = new HashSet<int>();
                foreach (var j in permutations) {
                    var candidate = int.Parse(j);
                    if (candidate > i && IsPrime(candidate)) {
                        candidates.Add(candidate);
                    }
                }
                foreach (var m in candidates) {
                    if (candidates.Contains(m + (m - i))) {
                        return i.ToString() + m.ToString() + (m + (m - i)).ToString();
                    }
                }
            }
        }
        return "";
    }
}

// End Euler049

// Start Euler050

class Global {
    public static int ConsecutivePrimeSum(int limit) {
        bool[] sieve = new bool[limit];
        Array.Fill(sieve, true);
        List<int> primes = new List<int>();
        for (int i = 2; i < limit; i++) {
            if (sieve[i]) {
                primes.Add(i);
                for (int j = i * 2; j < limit; j += i) {
                    sieve[j] = false;
                }
            }
        }
        int maxLength = 0;
        int maxPrime = 0;
        for (int i = 0; i < primes.Count; i++) {
            for (int j = i + maxLength; j < primes.Count; j++) {
                int s = 0;
                for (int k = i; k < j; k++) {
                    s += primes[k];
                }
                if (s >= limit) {
                    break;
                }
                if (sieve[s] && j - i > maxLength) {
                    maxLength = j - i;
                    maxPrime = s;
                }
            }
        }
        return maxPrime;
    }
}

// End Euler050

