// Start Euler001

int multiplesOf3And5(int n) {
    int result = 0;
    for (int i = 0; i < n; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            result += i;
        }
    }
    return result;
}

// End Euler001

// Start Euler002

int evenFibonacciNumbers(int n) {
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

// End Euler002

// Start Euler003

int largestPrimeFactor(int n) {
    int result = n;
    int i = 2;
    while (i * i <= result) {
        if (result % i) {
            i += 1;
        } else {
            result /= i;
        }
    }
    return result;
}

// End Euler003

// Start Euler004

bool isPalindrome(const string& s) {
    for (int i = 0; i < s.size() / 2; i++) {
        if (s[i] != s[s.size() - (i + 1)]) {
            return false;
        }
    }
    return true;
}

int largestPalindromeProduct(int n) {
    int result = 0;
    for (int i = 100; i < 1000; i++) {
        for (int j = i; j < 1000; j++) {
            int prod = i * j;
            if (isPalindrome(to_string(prod)) && prod > result && prod < n) {
                result = prod;
            }
        }
    }
    return result;
}

// End Euler004

// Start Euler005

int smallestMultiple(int n) {
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

// End Euler005

// Start Euler006

int sumSquareDifference(int n) {
    int sqr_sum = 0;
    int num_sum = 0;
    for (int i = 1; i <= n; i++) {
        sqr_sum += i * i;
        num_sum += i;
    }
    return num_sum * num_sum - sqr_sum;
}

// End Euler006

// Start Euler007

int nthPrime(int n) {
    vector<int> primes = {2};
    int i = 3;
    while (primes.size() < n) {
        for (int p : primes) {
            if (i % p == 0) {
                break;
            }
            if (p * p > i) {
                primes.push_back(i);
                break;
            }
        }
        i += 2;
    }
    return primes.back();
}

// End Euler007

// Start Euler008

int largestProductInASeries(const string& s, int k) {
    int result = 0;
    for (int i = 0; i < s.length() - k; i++) {
        int product = 1;
        for (int j = 0; j < k; j++) {
            product *= s[i + j] - '0';
        }
        result = max(result, product);
    }
    return result;
}

// End Euler008

// Start Euler009

int specialPythagoreanTriplet(int n) {
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

// End Euler009

// Start Euler010

int summationOfPrimes(int n) {
    vector<int> primes = {2};
    int i = 3;
    while (i <= n) {
        for (int p : primes) {
            if (i % p == 0) {
                break;
            }
            if (p * p > i) {
                primes.push_back(i);
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

// End Euler010

// Start Euler011

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

// End Euler011

// Start Euler012

int highlyDivisibleTriangularNumber(int n) {
    for (int i = 1; i < 100000000; i++) {
        int result = i * (i + 1) / 2;
        int count = 0;
        for (int j = 1; j <= (int)sqrt(result); j++) {
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

// End Euler012

// Start Euler013

string largeSum(const vector<string>& numbers) {
    vector<int> digits(60, 0);
    for (int i = 0; i < 50; i++) {
        int tmp = 0;
        for (auto num : numbers) {
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
            string result;
            for (int j = i; j > i - 10; j--) {
                result += to_string(digits[j]);
            }
            return result;
        }
    }
    return "";
}

// End Euler013

// Start Euler014

int longestCollatzSequence(int n) {
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

// End Euler014

// Start Euler015

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

// End Euler015

// Start Euler016

int powerDigitSum(int n) {
    vector<int> digits = {2};
    for (int i = 1; i < n; i++) {
        int carry = 0;
        for (int j = 0; j < digits.size(); j++) {
            int temp = digits[j] * 2 + carry;
            digits[j] = temp % 10;
            carry = temp / 10;
        }
        if (carry) {
            digits.push_back(carry);
        }
    }
    int result = 0;
    for (int digit : digits) {
        result += digit;
    }
    return result;
}

// End Euler016

// Start Euler017

string numberToWords(int n) {
    vector<string> ones = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    vector<string> teens = {"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
    vector<string> tens = {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
    if (n == 1000) {
        return "one thousand";
    } else if (n >= 100) {
        if (n % 100 == 0) {
            return ones[n / 100] + " hundred";
        } else {
            return ones[n / 100] + " hundred and " + numberToWords(n % 100);
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

// End Euler017

// Start Euler018

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

// End Euler018

// Start Euler019

int countingSundays(int y1, int y2) {
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

// End Euler019

// Start Euler020

int factorialDigitSum(int n) {
    vector<int> digits = {1};
    for (int i = 1; i <= n; i++) {
        int carry = 0;
        for (int j = 0; j < digits.size(); j++) {
            digits[j] = digits[j] * i + carry;
            carry = digits[j] / 10;
            digits[j] %= 10;
        }
        while (carry) {
            digits.push_back(carry % 10);
            carry /= 10;
        }
    }
    int result = 0;
    for (int digit : digits) {
        result += digit;
    }
    return result;
}

// End Euler020

// Start Euler021

int d(int n) {
    int result = 1;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            result += i;
            if (i != n / i) {
                result += n / i;
            }
        }
    }
    return result;
}

int amicableNumbers(int n) {
    int result = 0;
    for (int a = 2; a < n; a++) {
        int b = d(a);
        if (a != b && a == d(b)) {
            result += a;
        }
    }
    return result;
}

// End Euler021

// Start Euler022

int namesScores(const vector<string>& names, const vector<string>& queries) {
    vector<string> s_names = names;
    sort(s_names.begin(), s_names.end());
    int result = 0;
    for (int i = 0; i < s_names.size(); i++) {
        int x = 0;
        for (int j = 0; j < s_names[i].size(); j++) {
            x += s_names[i][j] - 64;
        }
        if (find(queries.begin(), queries.end(), s_names[i]) != queries.end()) {
            result += x * (i + 1);
        }
    }
    return result;
}

// End Euler022

// Start Euler023

bool isAbundant(int n) {
    if (n < 12) {
        return false;
    }
    int sumDivisors = 1;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            sumDivisors += i;
            if (i != n / i) {
                sumDivisors += n / i;
            }
        }
    }
    return sumDivisors > n;
}

int nonAbundantSums(int n) {
    vector<int> abundants;
    for (int i = 12; i < n; i++) {
        if (isAbundant(i)) {
            abundants.push_back(i);
        }
    }
    set<int> abundantSums;
    for (int i : abundants) {
        for (int j : abundants) {
            abundantSums.insert(i + j);
        }
    }
    int result = 0;
    for (int i = 0; i < n; i++) {
        if (abundantSums.find(i) == abundantSums.end()) {
            result += i;
        }
    }
    return result;
}

// End Euler023

// Start Euler024

string lexicographicPermutations(int n) {
    string result = "";
    vector<int> digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int x = n - 1;
    for (int i = 10; i > 0; i--) {
        int fact = 1;
        for (int j = 1; j < i; j++) {
            fact *= j;
        }
        int idx = x / fact;
        result += to_string(digits[idx]);
        digits.erase(digits.begin() + idx);
        x -= idx * fact;
    }
    return result;
}

// End Euler024

// Start Euler025

int nDigitFibonacciNumber(int n) {
    vector<int> a = {1};
    vector<int> b = {1};
    int i = 2;
    while (b.size() < n) {
        int carry = 0;
        vector<int> c = b;
        for (int j = 0; j < b.size(); j++) {
            if (j < a.size()) {
                b[j] = a[j] + b[j] + carry;
            } else {
                b[j] = b[j] + carry;
            }
            carry = b[j] / 10;
            b[j] = b[j] % 10;
        }
        if (carry) {
            b.push_back(carry);
        }
        a = c;
        i = i + 1;
    }
    return i;
}

// End Euler025

// Start Euler026

int reciprocalCycles(int n) {
    int result = 0;
    int max_length = 0;
    for (int i = 1; i < n; i++) {
        vector<int> remainders;
        int remainder = 1;
        while (remainder != 0 && find(remainders.begin(), remainders.end(), remainder) == remainders.end()) {
            remainders.push_back(remainder);
            remainder = (remainder * 10) % i;
        }
        int length = 0;
        if (remainder != 0) {
            length = remainders.size() - (find(remainders.begin(), remainders.end(), remainder) - remainders.begin());
        }
        if (length > max_length) {
            max_length = length;
            result = i;
        }
    }
    return result;
}

// End Euler026

// Start Euler027

bool isPrime(int n) {
    if (n < 2) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (int i = 3; i <= int(sqrt(n)); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int quadraticPrimes(int n) {
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

// End Euler027

// Start Euler028

int numberSpiralDiagonals(int n) {
    int result = 1;
    for (int i = 3; i <= n; i += 2) {
        result += 4 * i * i - 6 * i + 6;
    }
    return result;
}

// End Euler028

// Start Euler029

int distinctPowers(int n) {
    int result = 0;
    unordered_set<string> xs;
    for (int i = 2; i <= n; i++) {
        vector<int> primes = {2, 3, 5, 7};
        vector<int> powers = {0, 0, 0, 0};
        int num = i;
        for (int j = 0; j < primes.size(); j++) {
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
            string pstr = format("{}-{}-{}-{}", powers[0] * j, powers[1] * j, powers[2] * j, powers[3] * j);
            xs.insert(pstr);
        }
    }
    result += xs.size();
    return result;
}

// End Euler029

// Start Euler030

int digitNthPowers(int n) {
    int result = 0;
    for (int i = 2; i < 4 * pow(10, n); i++) {
        int digit_sum = 0;
        for (char digit : to_string(i)) {
            digit_sum += pow(digit - '0', n);
        }
        if (i == digit_sum) {
            result += i;
        }
    }
    return result;
}

// End Euler030

// Start Euler031

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

// End Euler031

// Start Euler032

int pandigitalProducts(int n) {
    unordered_set<int> products;
    string s;
    for (int i = 1; i <= n; i++) {
        s += to_string(i);
    }
    for (int a = 1; a < 100; a++) {
        for (int b = 1; b < 10000; b++) {
            int c = a * b;
            string chars = to_string(a) + to_string(b) + to_string(c);
            sort(chars.begin(), chars.end());
            if (chars == s) {
                products.insert(c);
            }
        }
    }
    int result = 0;
    for (int product : products) {
        result += product;
    }
    return result;
}

// End Euler032

// Start Euler033

int digitCancelingFractions(int m) {
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
    while (b) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return denom / a;
}

// End Euler033

// Start Euler034

int digitFactorials(int n) {
    int result = 0;
    for (int i = 3; i < n; i++) {
        int factSum = 0;
        for (char digit : to_string(i)) {
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

// End Euler034

// Start Euler035

bool isPrime(int n) {
    if (n < 2) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (int i = 3; i <= int(sqrt(n)); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int circularPrimes(int n) {
    int count = 0;
    for (int i = 2; i < n; i++) {
        if (isPrime(i)) {
            unordered_set<int> rotations;
            string si = to_string(i);
            for (int j = 0; j < si.size(); j++) {
                rotations.insert(stoi(si.substr(j) + si.substr(0, j)));
            }
            bool flag = true;
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

// End Euler035

// Start Euler036

bool isPalindrome(const string& s) {
    for (int i = 0; i < s.size() / 2; i++) {
        if (s[i] != s[s.size() - (i + 1)]) {
            return false;
        }
    }
    return true;
}

int doubleBasePalindromes(int n) {
    int result = 0;
    for (int i = 1; i < n; i++) {
        string str_i = to_string(i);
        string bin_i = bitset<32>(i).to_string();
        bin_i.erase(0, min(bin_i.find_first_not_of('0'), bin_i.size() - 1));
        if (isPalindrome(str_i) && isPalindrome(bin_i)) {
            result += i;
        }
    }
    return result;
}

// End Euler036

// Start Euler037

bool isPrime(int n) {
    if (n < 2) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (int i = 3; i <= int(sqrt(n)); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int truncatablePrimes(int n) {
    int result = 0;
    for (int i = 10; i < n; i++) {
        if (isPrime(i)) {
            string si = to_string(i);
            bool flag = true;
            for (int j = 1; j < si.size(); j++) {
                int p1 = stoi(si.substr(j));
                int p2 = stoi(si.substr(0, si.size() - j));
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

// End Euler037

// Start Euler038

int pandigitalMultiples(int n) {
    int result = -1;
    for (int i = 2; i <= n; i++) {
        string cprod;
        for (int j = 1; j < 10; j++) {
            cprod += to_string(i * j);
            if (cprod.length() == 9) {
                string chars = cprod;
                sort(chars.begin(), chars.end());
                if (chars == "123456789") {
                    result = max(result, stoi(cprod));
                    break;
                }
            } else if (cprod.length() > 9) {
                break;
            }
        }
    }
    return result;
}

// End Euler038

// Start Euler039

int integerRightTriangles(int n) {
    int max_sol = 0;
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
        if (sol > max_sol) {
            max_sol = sol;
            result = p;
        }
    }
    return result;
}

// End Euler039

// Start Euler040

int champernowneConstant(int b) {
    string s = "";
    for (int i = 1; i < pow(b, 6); i++) {
        s += to_string(i);
    }
    int result = 1;
    for (int i = 0; i < 7; i++) {
        result *= s[pow(b, i) - 1] - '0';
    }
    return result;
}

// End Euler040

// Start Euler041

bool isPrime(int n) {
    if (n < 2) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (int i = 3; i <= int(sqrt(n)); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int pandigitalPrime(int n) {
    for (int i = n - 1; i > 0; i--) {
        if (isPrime(i)) {
            string si = to_string(i);
            int length = si.length();
            bool flag = true;
            for (int j = 1; j <= length; j++) {
                if (si.find(to_string(j)) == string::npos) {
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

// End Euler041

// Start Euler042

int codedTriangleNumbers(const vector<string>& words) {
    int result = 0;
    for (const string& word : words) {
        int value = 0;
        for (char c : word) {
            value += c - 64;
        }
        int n = int(sqrt(value * 2));
        if (n * (n + 1) == value * 2) {
            result++;
        }
    }
    return result;
}

// End Euler042

// Start Euler043

vector<string> genPermutations(const string& s) {
    if (s.size() <= 1) {
        return {s};
    }
    vector<string> result;
    for (const string& perm : genPermutations(s.substr(1))) {
        for (int i = 0; i < s.size(); i++) {
            result.push_back(perm.substr(0, i) + s[0] + perm.substr(i));
        }
    }
    return result;
}

int subStringDivisibility(int n) {
    int result = 0;
    vector<int> primes = {2, 3, 5, 7, 11, 13, 17};
    string s;
    for (int i = 0; i <= n; i++) {
        s += to_string(i);
    }
    for (const string& i : genPermutations(s)) {
        bool flag = true;
        for (int j = 1; j < n - 1; j++) {
            if (stoi(i.substr(j, 3)) % primes[j - 1] != 0) {
                flag = false;
                break;
            }
        }
        if (flag) {
            result += stoi(i);
        }
    }
    return result;
}

// End Euler043

// Start Euler044

int pentagonNumbers(int n) {
    unordered_set<int> pentagon;
    for (int i = 1; i < n; i++) {
        pentagon.insert(i * (3 * i - 1) / 2);
    }
    int result = -1;
    for (int j : pentagon) {
        for (int k : pentagon) {
            if (pentagon.count(j + k) && pentagon.count(k - j)) {
                if (result == -1 || k - j < result) {
                    result = k - j;
                }
            }
        }
    }
    return result;
}

// End Euler044

// Start Euler045

int triangularPentagonalAndHexagonal(int n) {
    unordered_set<int> ps;
    int i = 1;
    int c = 0.5 * i * (3 * i - 1);
    while (c < n) {
        i++;
        ps.insert(c);
        c = 0.5 * i * (3 * i - 1);
    }
    i = 1;
    c = i * (2 * i - 1);
    int result = -1;
    while (c < n) {
        i++;
        if (ps.find(c) != ps.end()) {
            result = c;
        }
        c = i * (2 * i - 1);
    }
    return result;
}

// End Euler045

// Start Euler046

bool isPrime(int n) {
    if (n < 2) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (int i = 3; i <= int(sqrt(n)); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int goldbachsOtherConjecture(int n) {
    int result = -1;
    for (int i = 9999; i > n; i -= 2) {
        int upper = sqrt(i / 2);
        bool flag = false;
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

// End Euler046

// Start Euler047

int primeFactors(int n) {
    int num = n;
    vector<int> factors;
    int i = 2;
    while (i * i <= num) {
        if (num % i) {
            i++;
        } else {
            num /= i;
            factors.push_back(i);
        }
    }
    if (num > 1) {
        factors.push_back(num);
    }
    unordered_set<int> s(factors.begin(), factors.end());
    return s.size();
}

int distinctPrimesFactors(int n) {
    for (int i = n; i < 1000000; i++) {
        if (primeFactors(i) == 4 && primeFactors(i + 1) == 4 && primeFactors(i + 2) == 4 && primeFactors(i + 3) == 4) {
            return i;
        }
    }
    return -1;
}

// End Euler047

// Start Euler048

string selfPowers(int n) {
    int digits[10] = {0};
    for (int i = 1; i <= n; i++) {
        int temp_digits[10] = {0};
        temp_digits[0] = 1;
        for (int j = 0; j < i; j++) {
            int carry = 0;
            for (int k = 0; k < 10; k++) {
                temp_digits[k] = temp_digits[k] * i + carry;
                carry = temp_digits[k] / 10;
                temp_digits[k] %= 10;
            }
        }
        for (int j = 0; j < 10; j++) {
            digits[j] += temp_digits[j];
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
        result += to_string(digits[i]);
    }
    return result;
}

// End Euler048

// Start Euler049

bool isPrime(int n) {
    if (n < 2) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    for (int i = 3; i <= int(sqrt(n)); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

vector<string> genPermutations(const string& s) {
    if (s.size() <= 1) {
        return {s};
    }
    vector<string> result;
    for (const string& perm : genPermutations(s.substr(1))) {
        for (int i = 0; i < s.size(); i++) {
            result.push_back(perm.substr(0, i) + s[0] + perm.substr(i));
        }
    }
    return result;
}

string primePermutations(int n) {
    for (int i = n; i > 999; --i) {
        if (isPrime(i)) {
            vector<string> permutations = genPermutations(to_string(i));
            unordered_set<int> candidates;
            for (string j : permutations) {
                int candidate = stoi(j);
                if (candidate > i && isPrime(candidate)) {
                    candidates.insert(candidate);
                }
            }
            for (int m : candidates) {
                if (candidates.count(m + (m - i))) {
                    return to_string(i) + to_string(m) + to_string(m + (m - i));
                }
            }
        }
    }
    return "";
}

// End Euler049

// Start Euler050

int consecutivePrimeSum(int limit) {
    vector<bool> sieve(limit, true);
    vector<int> primes;
    for (int i = 2; i < limit; i++) {
        if (sieve[i]) {
            primes.push_back(i);
            for (int j = i * 2; j < limit; j += i) {
                sieve[j] = false;
            }
        }
    }
    int max_length = 0;
    int max_prime = 0;
    for (int i = 0; i < primes.size(); i++) {
        for (int j = i + max_length; j < primes.size(); j++) {
            int s = 0;
            for (int k = i; k < j; k++) {
                s += primes[k];
            }
            if (s >= limit) {
                break;
            }
            if (sieve[s] && j - i > max_length) {
                max_length = j - i;
                max_prime = s;
            }
        }
    }
    return max_prime;
}

// End Euler050

