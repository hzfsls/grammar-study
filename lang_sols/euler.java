// Start Euler001

class Global {
    public static int multiplesOf3And5(int n) {
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
    public static int evenFibonacciNumbers(int n) {
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
    public static int largestPrimeFactor(int n) {
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
    public static boolean isPalindrome(String s) {
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }

    public static int largestPalindromeProduct(int n) {
        int result = 0;
        for (int i = 100; i < 1000; i++) {
            for (int j = i; j < 1000; j++) {
                int prod = i * j;
                if (isPalindrome(Integer.toString(prod)) && prod > result && prod < n) {
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
    public static int smallestMultiple(int n) {
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

// End Euler006

// Start Euler007

class Global {
    public static int nthPrime(int n) {
        List<Integer> primes = new ArrayList<>(Arrays.asList(2));
        int i = 3;
        while (primes.size() < n) {
            for (int p : primes) {
                if (i % p == 0) {
                    break;
                }
                if (p * p > i) {
                    primes.add(i);
                    break;
                }
            }
            i += 2;
        }
        return primes.get(primes.size() - 1);
    }
}

// End Euler007

// Start Euler008

class Global {
    public static int largestProductInASeries(String s, int k) {
        int result = 0;
        for (int i = 0; i < s.length() - k; i++) {
            int product = 1;
            for (int j = 0; j < k; j++) {
                product *= s.charAt(i + j) - '0';
            }
            result = Math.max(result, product);
        }
        return result;
    }
}

// End Euler008

// Start Euler009

class Global {
    public static int specialPythagoreanTriplet(int n) {
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
    public static int summationOfPrimes(int n) {
        List<Integer> primes = new ArrayList<Integer>();
        primes.add(2);
        int i = 3;
        while (i <= n) {
            for (int p : primes) {
                if (i % p == 0) {
                    break;
                }
                if (p * p > i) {
                    primes.add(i);
                    break;
                }
            }
            i += 2;
        }
        int result = 0;
        for (int prime : primes) {
            result += prime;
        }
        return result;
    }
}

// End Euler010

// Start Euler011

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

// End Euler011

// Start Euler012

class Global {
    public static int highlyDivisibleTriangularNumber(int n) {
        for (int i = 1; i < 100000000; i++) {
            int result = i * (i + 1) / 2;
            int count = 0;
            for (int j = 1; j <= (int)Math.sqrt(result); j++) {
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
    public static String largeSum(List<String> numbers) {
        int[] digits = new int[60];
        for (int i = 0; i < 50; i++) {
            int tmp = 0;
            for (String num : numbers) {
                tmp += num.charAt(49 - i) - '0';
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
                StringBuilder result = new StringBuilder();
                for (int j = i; j > i - 10; j--) {
                    result.append(digits[j]);
                }
                return result.toString();
            }
        }
        return "";
    }
}

// End Euler013

// Start Euler014

class Global {
    public static int longestCollatzSequence(int n) {
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

// End Euler015

// Start Euler016

class Global {
    public static int powerDigitSum(int n) {
        List<Integer> digits = new ArrayList<>(List.of(2));
        for (int i = 1; i < n; i++) {
            int carry = 0;
            for (int j = 0; j < digits.size(); j++) {
                int temp = digits.get(j) * 2 + carry;
                digits.set(j, temp % 10);
                carry = temp / 10;
            }
            if (carry != 0) {
                digits.add(carry);
            }
        }
        int result = 0;
        for (int digit : digits) {
            result += digit;
        }
        return result;
    }
}

// End Euler016

// Start Euler017

class Global {
    public static String numberToWords(int n) {
        String[] ones = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        String[] teens = {"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
        String[] tens = {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
        if (n == 1000) {
            return "one thousand";
        } else if (n >= 100) {
            if (n % 100 == 0) {
                return ones[n / 100] + " hundred";
            } else {
                return ones[n / 100] + " hundred and " + numberToWords(n % 100);
            }
        } else if (n >= 20) {
            String suf = "";
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

// End Euler018

// Start Euler019

class Global {
    public static int countingSundays(int y1, int y2) {
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
    public static int factorialDigitSum(int n) {
        List<Integer> digits = new ArrayList<Integer>();
        digits.add(1);
        for (int i = 1; i <= n; i++) {
            int carry = 0;
            for (int j = 0; j < digits.size(); j++) {
                digits.set(j, digits.get(j) * i + carry);
                carry = digits.get(j) / 10;
                digits.set(j, digits.get(j) % 10);
            }
            while (carry != 0) {
                digits.add(carry % 10);
                carry /= 10;
            }
        }
        int result = 0;
        for (int digit : digits) {
            result += digit;
        }
        return result;
    }
}

// End Euler020

// Start Euler021

class Global {
    public static int d(int n) {
        int result = 1;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                result += i;
                if (i != n / i) {
                    result += n / i;
                }
            }
        }
        return result;
    }

    public static int amicableNumbers(int n) {
        int result = 0;
        for (int a = 2; a < n; a++) {
            int b = d(a);
            if (a != b && a == d(b)) {
                result += a;
            }
        }
        return result;
    }
}

// End Euler021

// Start Euler022

class Global {
    public static int namesScores(List<String> names, List<String> queries) {
        List<String> sNames = new ArrayList<>(names);
        Collections.sort(sNames);
        int result = 0;
        for (int i = 0; i < sNames.size(); i++) {
            int x = 0;
            for (int j = 0; j < sNames.get(i).length(); j++) {
                x += sNames.get(i).charAt(j) - 64;
            }
            if (queries.contains(sNames.get(i))) {
                result += x * (i + 1);
            }
        }
        return result;
    }
}

// End Euler022

// Start Euler023

class Global {
    public static boolean isAbundant(int n) {
        if (n < 12) {
            return false;
        }
        int sumDivisors = 1;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                sumDivisors += i;
                if (i != n / i) {
                    sumDivisors += n / i;
                }
            }
        }
        return sumDivisors > n;
    }

    public static int nonAbundantSums(int n) {
        List<Integer> abundants = new ArrayList<>();
        for (int i = 12; i < n; i++) {
            if (isAbundant(i)) {
                abundants.add(i);
            }
        }
        Set<Integer> abundantSums = new HashSet<>();
        for (int i : abundants) {
            for (int j : abundants) {
                abundantSums.add(i + j);
            }
        }
        int result = 0;
        for (int i = 0; i < n; i++) {
            if (!abundantSums.contains(i)) {
                result += i;
            }
        }
        return result;
    }
}

// End Euler023

// Start Euler024

class Global {
    public static String lexicographicPermutations(int n) {
        String result = "";
        List<Integer> digits = new ArrayList<>(Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9));
        int x = n - 1;
        for (int i = 10; i > 0; i--) {
            int fact = 1;
            for (int j = 1; j < i; j++) {
                fact *= j;
            }
            int idx = x / fact;
            result += digits.get(idx);
            digits.remove(idx);
            x -= idx * fact;
        }
        return result;
    }
}

// End Euler024

// Start Euler025

class Global {
    public static int nDigitFibonacciNumber(int n) {
        List<Integer> a = new ArrayList<Integer>(Arrays.asList(1));
        List<Integer> b = new ArrayList<Integer>(Arrays.asList(1));
        int i = 2;
        while (b.size() < n) {
            int carry = 0;
            List<Integer> c = new ArrayList<Integer>(b);
            for (int j = 0; j < b.size(); j++) {
                if (j < a.size()) {
                    b.set(j, a.get(j) + b.get(j) + carry);
                } else {
                    b.set(j, b.get(j) + carry);
                }
                carry = b.get(j) / 10;
                b.set(j, b.get(j) % 10);
            }
            if (carry != 0) {
                b.add(carry);
            }
            a = new ArrayList<Integer>(c);
            i = i + 1;
        }
        return i;
    }
}

// End Euler025

// Start Euler026

class Global {
    public static int reciprocalCycles(int n) {
        int result = 0;
        int maxLength = 0;
        for (int i = 1; i < n; i++) {
            List<Integer> remainders = new ArrayList<Integer>();
            int remainder = 1;
            while (remainder != 0 && !remainders.contains(remainder)) {
                remainders.add(remainder);
                remainder = (remainder * 10) % i;
            }
            int length = 0;
            if (remainder != 0) {
                length = remainders.size() - remainders.indexOf(remainder);
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
    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= (int)Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int quadraticPrimes(int n) {
        int maxPrimes = 0;
        int result = 0;
        for (int a = -n + 1; a < n; a += 2) {
            for (int b = -n + 1; b < n; b += 2) {
                int x = 0;
                while (true) {
                    if (x * x + a * x + b < 2) {
                        break;
                    }
                    if (!isPrime(x * x + a * x + b)) {
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
    public static int numberSpiralDiagonals(int n) {
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
    public static int distinctPowers(int n) {
        int result = 0;
        HashSet<String> xs = new HashSet<String>();
        for (int i = 2; i <= n; i++) {
            List<Integer> primes = new ArrayList<Integer>(Arrays.asList(2, 3, 5, 7));
            List<Integer> powers = new ArrayList<Integer>(Arrays.asList(0, 0, 0, 0));
            int num = i;
            for (int j = 0; j < primes.size(); j++) {
                while (num % primes.get(j) == 0) {
                    num /= primes.get(j);
                    powers.set(j, powers.get(j) + 1);
                }
            }
            if (num != 1) {
                result += n - 1;
                continue;
            }
            for (int j = 2; j <= n; j++) {
                String pstr = String.format("%d-%d-%d-%d", powers.get(0) * j, powers.get(1) * j, powers.get(2) * j, powers.get(3) * j);
                xs.add(pstr);
            }
        }
        result += xs.size();
        return result;
    }
}

// End Euler029

// Start Euler030

class Global {
    public static int digitNthPowers(int n) {
        int result = 0;
        for (int i = 2; i < 4 * Math.pow(10, n); i++) {
            int digitsSum = 0;
            for (char digit : String.valueOf(i).toCharArray()) {
                digitsSum += Math.pow(digit - '0', n);
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

// End Euler031

// Start Euler032

class Global {
    public static int pandigitalProducts(int n) {
        Set<Integer> products = new HashSet<>();
        String s = "";
        for (int i = 1; i <= n; i++) {
            s += i;
        }
        for (int a = 1; a < 100; a++) {
            for (int b = 1; b < 10000; b++) {
                int c = a * b;
                char[] chars = (Integer.toString(a) + Integer.toString(b) + Integer.toString(c)).toCharArray();
                Arrays.sort(chars);
                if (new String(chars).equals(s)) {
                    products.add(c);
                }
            }
        }
        int result = 0;
        for (int product : products) {
            result += product;
        }
        return result;
    }
}

// End Euler032

// Start Euler033

class Global {
    public static int digitCancelingFractions(int m) {
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
    public static int digitFactorials(int n) {
        int result = 0;
        for (int i = 3; i < n; i++) {
            int factSum = 0;
            for (char digit : Integer.toString(i).toCharArray()) {
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
    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= (int)Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int circularPrimes(int n) {
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                HashSet<Integer> rotations = new HashSet<Integer>();
                String si = Integer.toString(i);
                for (int j = 0; j < si.length(); j++) {
                    rotations.add(Integer.parseInt(si.substring(j) + si.substring(0, j)));
                }
                boolean flag = true;
                for (int x : rotations) {
                    if (!isPrime(x)) {
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
    public static boolean isPalindrome(String s) {
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }

    public static int doubleBasePalindromes(int n) {
        int result = 0;
        for (int i = 1; i < n; i++) {
            String strI = Integer.toString(i);
            String binI = Integer.toBinaryString(i);
            if (isPalindrome(strI) && isPalindrome(binI)) {
                result += i;
            }
        }
        return result;
    }
}

// End Euler036

// Start Euler037

class Global {
    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= (int)Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int truncatablePrimes(int n) {
        int result = 0;
        for (int i = 10; i < n; i++) {
            if (isPrime(i)) {
                String si = String.valueOf(i);
                boolean flag = true;
                for (int j = 1; j < si.length(); j++) {
                    int p1 = Integer.parseInt(si.substring(j));
                    int p2 = Integer.parseInt(si.substring(0, si.length() - j));
                    if (!isPrime(p1) || !isPrime(p2)) {
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
    public static int pandigitalMultiples(int n) {
        int result = -1;
        for (int i = 2; i <= n; i++) {
            String cprod = "";
            for (int j = 1; j < 10; j++) {
                cprod += Integer.toString(i * j);
                if (cprod.length() == 9) {
                    char[] chars = cprod.toCharArray();
                    Arrays.sort(chars);
                    if (new String(chars).equals("123456789")) {
                        result = Math.max(result, Integer.parseInt(cprod));
                        break;
                    }
                } else if (cprod.length() > 9) {
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

// End Euler039

// Start Euler040

class Global {
    public static int champernowneConstant(int b) {
        String s = "";
        for (int i = 1; i < Math.pow(b, 6); i++) {
            s += Integer.toString(i);
        }
        int result = 1;
        for (int i = 0; i < 7; i++) {
            result *= s.charAt((int)Math.pow(b, i) - 1) - '0';
        }
        return result;
    }
}

// End Euler040

// Start Euler041

class Global {
    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= (int)Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int pandigitalPrime(int n) {
        for (int i = n - 1; i > 0; i--) {
            if (isPrime(i)) {
                String si = Integer.toString(i);
                int length = si.length();
                boolean flag = true;
                for (int j = 1; j <= length; j++) {
                    if (si.indexOf(Integer.toString(j)) == -1) {
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
    public static int codedTriangleNumbers(List<String> words) {
        int result = 0;
        for (String word : words) {
            int value = 0;
            for (char c : word.toCharArray()) {
                value += c - 64;
            }
            int n = (int)Math.sqrt(value * 2);
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
    public static List<String> genPermutations(String s) {
        if (s.length() <= 1) {
            return List.of(s);
        }
        List<String> result = new ArrayList<>();
        for (String perm : genPermutations(s.substring(1))) {
            for (int i = 0; i < s.length(); i++) {
                result.add(perm.substring(0, i) + s.charAt(0) + perm.substring(i));
            }
        }
        return result;
    }

    public static int subStringDivisibility(int n) {
        int result = 0;
        List<Integer> primes = List.of(2, 3, 5, 7, 11, 13, 17);
        String s = "";
        for (int i = 0; i <= n; i++) {
            s += i;
        }
        for (String i : genPermutations(s)) {
            boolean flag = true;
            for (int j = 1; j < n - 1; j++) {
                if (Integer.parseInt(i.substring(j, j + 3)) % primes.get(j - 1) != 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                result += Integer.parseInt(i);
            }
        }
        return result;
    }
}

// End Euler043

// Start Euler044

class Global {
    public static int pentagonNumbers(int n) {
        Set<Integer> pentagon = new HashSet<>();
        for (int i = 1; i < n; i++) {
            pentagon.add(i * (3 * i - 1) / 2);
        }
        int result = -1;
        for (int j : pentagon) {
            for (int k : pentagon) {
                if (pentagon.contains(j + k) && pentagon.contains(k - j)) {
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
    public static int triangularPentagonalAndHexagonal(int n) {
        HashSet<Integer> ps = new HashSet<Integer>();
        int i = 1;
        int c = (int)(0.5 * i * (3 * i - 1));
        while (c < n) {
            i++;
            ps.add(c);
            c = (int)(0.5 * i * (3 * i - 1));
        }
        i = 1;
        c = i * (2 * i - 1);
        int result = -1;
        while (c < n) {
            i++;
            if (ps.contains(c)) {
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
    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= (int)Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int goldbachsOtherConjecture(int n) {
        int result = -1;
        for (int i = 9999; i > n; i -= 2) {
            int upper = (int)Math.sqrt(i / 2);
            boolean flag = false;
            for (int j = 0; j <= upper; j++) {
                if (isPrime(i - 2 * j * j)) {
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
    public static int primeFactors(int n) {
        int num = n;
        List<Integer> factors = new ArrayList<Integer>();
        int i = 2;
        while (i * i <= num) {
            if (num % i != 0) {
                i++;
            } else {
                num /= i;
                factors.add(i);
            }
        }
        if (num > 1) {
            factors.add(num);
        }
        return new HashSet<Integer>(factors).size();
    }

    public static int distinctPrimesFactors(int n) {
        for (int i = n; i < 1000000; i++) {
            if (primeFactors(i) == 4 && primeFactors(i + 1) == 4 && primeFactors(i + 2) == 4 && primeFactors(i + 3) == 4) {
                return i;
            }
        }
        return -1;
    }
}

// End Euler047

// Start Euler048

class Global {
    public static String selfPowers(int n) {
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
        String result = "";
        for (int i = 9; i >= 0; i--) {
            result += Integer.toString(digits[i]);
        }
        return result;
    }
}

// End Euler048

// Start Euler049

class Global {
    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= (int)Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static List<String> genPermutations(String s) {
        if (s.length() <= 1) {
            return List.of(s);
        }
        List<String> result = new ArrayList<>();
        for (String perm : genPermutations(s.substring(1))) {
            for (int i = 0; i < s.length(); i++) {
                result.add(perm.substring(0, i) + s.charAt(0) + perm.substring(i));
            }
        }
        return result;
    }

    public static String primePermutations(int n) {
        for (int i = n; i > 999; --i) {
            if (isPrime(i)) {
                List<String> permutations = genPermutations(String.valueOf(i));
                Set<Integer> candidates = new HashSet<>();
                for (String j : permutations) {
                    int candidate = Integer.parseInt(j);
                    if (candidate > i && isPrime(candidate)) {
                        candidates.add(candidate);
                    }
                }
                for (int m : candidates) {
                    if (candidates.contains(m + (m - i))) {
                        return Integer.toString(i) + Integer.toString(m) + Integer.toString(m + (m - i));
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
    public static int consecutivePrimeSum(int limit) {
        boolean[] sieve = new boolean[limit];
        Arrays.fill(sieve, true);
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i < limit; i++) {
            if (sieve[i]) {
                primes.add(i);
                for (int j = i * 2; j < limit; j += i) {
                    sieve[j] = false;
                }
            }
        }
        int maxLength = 0;
        int maxPrime = 0;
        for (int i = 0; i < primes.size(); i++) {
            for (int j = i + maxLength; j < primes.size(); j++) {
                int s = 0;
                for (int k = i; k < j; k++) {
                    s += primes.get(k);
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

