// Start Euler001

const multiplesOf3And5 = (n) => {
    let result = 0;
    for (let i = 0; i < n; i++) {
        if (i % 3 === 0 || i % 5 === 0) {
            result += i;
        }
    }
    return result;
}

// End Euler001

// Start Euler002

const evenFibonacciNumbers = (n) => {
    let result = 0;
    let a = 1;
    let b = 2;
    while (a < n) {
        if (a % 2 === 0) {
            result += a;
        }
        const tmp = a;
        a = b;
        b = tmp + b;
    }
    return result;
}

// End Euler002

// Start Euler003

const largestPrimeFactor = (n) => {
    let result = n;
    let i = 2;
    while (i * i <= result) {
        if (result % i !== 0) {
            i += 1;
        } else {
            result /= i;
        }
    }
    return result;
}

// End Euler003

// Start Euler004

const isPalindrome = (s) => {
    for (let i = 0; i < s.length / 2; i++) {
        if (s[i] !== s[s.length - i - 1]) {
            return false;
        }
    }
    return true;
}

const largestPalindromeProduct = (n) => {
    let result = 0;
    for (let i = 100; i < 1000; i++) {
        for (let j = i; j < 1000; j++) {
            let prod = i * j;
            if (isPalindrome(prod.toString()) && prod > result && prod < n) {
                result = prod;
            }
        }
    }
    return result;
}

// End Euler004

// Start Euler005

const smallestMultiple = (n) => {
    let result = 1;
    for (let i = 1; i <= n; i++) {
        if (result % i !== 0) {
            for (let j = 1; j <= n; j++) {
                if ((result * j) % i === 0) {
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

const sumSquareDifference = (n) => {
    let sqrSum = 0;
    let numSum = 0;
    for (let i = 1; i <= n; i++) {
        sqrSum += i * i;
        numSum += i;
    }
    return numSum * numSum - sqrSum;
}

// End Euler006

// Start Euler007

const nthPrime = (n) => {
    const primes = [2];
    let i = 3;
    while (primes.length < n) {
        for (let p of primes) {
            if (i % p === 0) {
                break;
            }
            if (p * p > i) {
                primes.push(i);
                break;
            }
        }
        i += 2;
    }
    return primes[primes.length - 1];
}

// End Euler007

// Start Euler008

const largestProductInASeries = (s, k) => {
    let result = 0;
    for (let i = 0; i < s.length - k; i++) {
        let product = 1;
        for (let j = 0; j < k; j++) {
            product *= parseInt(s[i + j]);
        }
        result = Math.max(result, product);
    }
    return result;
}

// End Euler008

// Start Euler009

const specialPythagoreanTriplet = (n) => {
    for (let a = 1; a < n; a++) {
        for (let b = a; b < n; b++) {
            let c = n - a - b;
            if (a * a + b * b === c * c) {
                return a * b * c;
            }
        }
    }
    return -1;
}

// End Euler009

// Start Euler010

const summationOfPrimes = (n) => {
    const primes = [2];
    let i = 3;
    while (i <= n) {
        for (let p of primes) {
            if (i % p === 0) {
                break;
            }
            if (p * p > i) {
                primes.push(i);
                break;
            }
        }
        i += 2;
    }
    let result = 0;
    for (let prime of primes) {
        result += prime;
    }
    return result;
}

// End Euler010

// Start Euler011

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

// End Euler011

// Start Euler012

const highlyDivisibleTriangularNumber = (n) => {
    for (let i = 1; i < 100000000; i++) {
        let result = i * (i + 1) / 2;
        let count = 0;
        for (let j = 1; j <= Math.trunc(Math.sqrt(result)); j++) {
            if (result % j === 0) {
                count += 2;
            }
            if (j * j === result) {
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

const largeSum = (numbers) => {
    const digits = Array(60).fill(0);
    for (let i = 0; i < 50; i++) {
        let tmp = 0;
        for (let num of numbers) {
            tmp += parseInt(num[49 - i]);
        }
        for (let j = i; j < 60; j++) {
            digits[j] += tmp % 10;
            if (digits[j] >= 10) {
                digits[j + 1] += Math.floor(digits[j] / 10);
                digits[j] %= 10;
            }
            tmp = Math.floor(tmp / 10);
            if (tmp === 0) {
                break;
            }
        }
    }
    for (let i = 59; i >= 0; i--) {
        if (digits[i] !== 0) {
            let result = '';
            for (let j = i; j > i - 10; j--) {
                result += digits[j];
            }
            return result;
        }
    }
    return '';
}

// End Euler013

// Start Euler014

const longestCollatzSequence = (n) => {
    let longest = 0;
    let result = 0;
    for (let i = 1; i < n; i++) {
        let chain = 1;
        let num = i;
        while (num !== 1) {
            if (num % 2 === 0) {
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

const latticePaths = (m, n) => {
    const grid = new Array(m + 1).fill(0).map(() => new Array(n + 1).fill(0));
    for (let i = 0; i <= m; i++) {
        grid[i][0] = 1;
    }
    for (let j = 0; j <= n; j++) {
        grid[0][j] = 1;
    }
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1];
        }
    }
    return grid[m][n];
}

// End Euler015

// Start Euler016

const powerDigitSum = (n) => {
    let digits = [2];
    for (let i = 1; i < n; i++) {
        let carry = 0;
        for (let j = 0; j < digits.length; j++) {
            let temp = digits[j] * 2 + carry;
            digits[j] = temp % 10;
            carry = Math.floor(temp / 10);
        }
        if (carry !== 0) {
            digits.push(carry);
        }
    }
    let result = 0;
    for (let digit of digits) {
        result += digit;
    }
    return result;
}

// End Euler016

// Start Euler017

const numberToWords = (n) => {
    const ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    const teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
    const tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
    if (n === 1000) {
        return "one thousand";
    } else if (n >= 100) {
        if (n % 100 === 0) {
            return ones[Math.floor(n / 100)] + " hundred";
        } else {
            return ones[Math.floor(n / 100)] + " hundred and " + numberToWords(n % 100);
        }
    } else if (n >= 20) {
        let suf = "";
        if (n % 10 !== 0) {
            suf = " " + ones[n % 10];
        }
        return tens[Math.floor(n / 10)] + suf;
    } else if (n >= 10) {
        return teens[n - 10];
    } else {
        return ones[n];
    }       
}

// End Euler017

// Start Euler018

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

// End Euler018

// Start Euler019

const countingSundays = (y1, y2) => {
    let day = 0;
    let count = 0;
    for (let year = 1900; year <= y2; year++) {
        for (let month = 1; month <= 12; month++) {
            if (year >= y1 && day % 7 === 6) {
                count++;
            }
            if (month === 4 || month === 6 || month === 9 || month === 11) {
                day += 30;
            } else if (month === 2) {
                if (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)) {
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

const factorialDigitSum = (n) => {
    let digits = [1];
    for (let i = 1; i <= n; i++) {
        let carry = 0;
        for (let j = 0; j < digits.length; j++) {
            digits[j] = digits[j] * i + carry;
            carry = Math.floor(digits[j] / 10);
            digits[j] %= 10;
        }
        while (carry !== 0) {
            digits.push(carry % 10);
            carry = Math.floor(carry / 10);
        }
    }
    let result = 0;
    for (let digit of digits) {
        result += digit;
    }
    return result;
}

// End Euler020

// Start Euler021

const d = (n) => {
    let result = 1;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            result += i;
            if (i !== n / i) {
                result += n / i;
            }
        }
    }
    return result;
}

const amicableNumbers = (n) => {
    let result = 0;
    for (let a = 2; a < n; a++) {
        let b = d(a);
        if (a !== b && a === d(b)) {
            result += a;
        }
    }
    return result;
}

// End Euler021

// Start Euler022

const namesScores = (names, queries) => {
    let sNames = names.slice().sort();
    let result = 0;
    for (let i = 0; i < sNames.length; i++) {
        let x = 0;
        for (let j = 0; j < sNames[i].length; j++) {
            x += sNames[i].charCodeAt(j) - 64;
        }
        if (queries.includes(sNames[i])) {
            result += x * (i + 1);
        }
    }
    return result;
}

// End Euler022

// Start Euler023

const isAbundant = (n) => {
    if (n < 12) {
        return false;
    }
    let sumDivisors = 1;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            sumDivisors += i;
            if (i !== n / i) {
                sumDivisors += n / i;
            }
        }
    }
    return sumDivisors > n;
}

const nonAbundantSums = (n) => {
    const abundants = [];
    for (let i = 12; i < n; i++) {
        if (isAbundant(i)) {
            abundants.push(i);
        }
    }
    const abundantSums = new Set();
    for (let i of abundants) {
        for (let j of abundants) {
            abundantSums.add(i + j);
        }
    }
    let result = 0;
    for (let i = 0; i < n; i++) {
        if (!abundantSums.has(i)) {
            result += i;
        }
    }
    return result;
}

// End Euler023

// Start Euler024

const lexicographicPermutations = (n) => {
    let result = "";
    let digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let x = n - 1;
    for (let i = 10; i > 0; i--) {
        let fact = 1;
        for (let j = 1; j < i; j++) {
            fact *= j;
        }
        let idx = Math.floor(x / fact);
        result += digits[idx];
        digits.splice(idx, 1);
        x -= idx * fact;
    }
    return result;
}

// End Euler024

// Start Euler025

const nDigitFibonacciNumber = (n) => {
    let a = [1];
    let b = [1];
    let i = 2;
    while (b.length < n) {
        let carry = 0;
        let c = b.slice();
        for (let j = 0; j < b.length; j++) {
            if (j < a.length) {
                b[j] = a[j] + b[j] + carry;
            } else {
                b[j] = b[j] + carry;
            }
            carry = Math.floor(b[j] / 10);
            b[j] = b[j] % 10;
        }
        if (carry) {
            b.push(carry);
        }
        a = c;
        i = i + 1;
    }
    return i;
}

// End Euler025

// Start Euler026

const reciprocalCycles = (n) => {
    let result = 0;
    let maxLength = 0;
    for (let i = 1; i < n; i++) {
        let remainders = [];
        let remainder = 1;
        while (remainder !== 0 && !remainders.includes(remainder)) {
            remainders.push(remainder);
            remainder = (remainder * 10) % i;
        }
        let length = 0;
        if (remainder !== 0) {
            length = remainders.length - remainders.indexOf(remainder);
        }
        if (length > maxLength) {
            maxLength = length;
            result = i;
        }
    }
    return result;
}

// End Euler026

// Start Euler027

const isPrime = (n) => {
    if (n < 2) {
        return false;
    }
    if (n === 2) {
        return true;
    }
    if (n % 2 === 0) {
        return false;
    }
    for (let i = 3; i <= Math.trunc(Math.sqrt(n)); i += 2) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

const quadraticPrimes = (n) => {
    let maxPrimes = 0;
    let result = 0;
    for (let a = -n + 1; a < n; a += 2) {
        for (let b = -n + 1; b < n; b += 2) {
            let x = 0;
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

const numberSpiralDiagonals = (n) => {
    let result = 1;
    for (let i = 3; i <= n; i += 2) {
        result += 4 * i * i - 6 * i + 6;
    }
    return result;
}

// End Euler028

// Start Euler029

const distinctPowers = (n) => {
    let result = 0;
    let xs = new Set();
    for (let i = 2; i <= n; i++) {
        let primes = [2, 3, 5, 7];
        let powers = [0, 0, 0, 0];
        let num = i;
        for (let j = 0; j < primes.length; j++) {
            while (num % primes[j] === 0) {
                num /= primes[j];
                powers[j] += 1;
            }
        }
        if (num !== 1) {
            result += n - 1;
            continue;
        }
        for (let j = 2; j <= n; j++) {
            let pstr = `${powers[0] * j}-${powers[1] * j}-${powers[2] * j}-${powers[3] * j}`;
            xs.add(pstr);
        }
    }
    result += xs.size;
    return result;
}

// End Euler029

// Start Euler030

const digitNthPowers = (n) => {
    let result = 0;
    for (let i = 2; i < 4 * 10 ** n; i++) {
        let digitsSum = 0;
        for (const digit of i.toString()) {
            digitsSum += parseInt(digit) ** n;
        }
        if (i === digitsSum) {
            result += i;
        }
    }
    return result;
}

// End Euler030

// Start Euler031

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

// End Euler031

// Start Euler032

const pandigitalProducts = (n) => {
    const products = new Set();
    let s = "";
    for (let i = 1; i <= n; i++) {
        s += i;
    }
    for (let a = 1; a < 100; a++) {
        for (let b = 1; b < 10000; b++) {
            const c = a * b;
            let chars = (a.toString() + b.toString() + c.toString()).split("");
            chars.sort();
            if (chars.join("") === s) {
                products.add(c);
            }
        }
    }
    let result = 0;
    for (let product of products) {
        result += product;
    }
    return result;
}

// End Euler032

// Start Euler033

const digitCancelingFractions = (m) => {
    let numer = 1;
    let denom = 1;
    for (let d = 10; d < m; d++) {
        for (let n = 10; n < d; n++) {
            let n0 = n % 10;
            let n1 = Math.floor(n / 10);
            let d0 = d % 10;
            let d1 = Math.floor(d / 10);
            if ((n1 === d0 && n0 * d === n * d1) || (n0 === d1 && n1 * d === n * d0)) {
                numer *= n;
                denom *= d;
            }
        }
    }
    let a = numer;
    let b = denom;
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return denom / a;
}

// End Euler033

// Start Euler034

const digitFactorials = (n) => {
    let result = 0;
    for (let i = 3; i < n; i++) {
        let factSum = 0;
        for (let digit of i.toString()) {
            let fact = 1;
            for (let j = 1; j <= parseInt(digit); j++) {
                fact *= j;
            }
            factSum += fact;
        }
        if (i === factSum) {
            result += i;
        }
    }
    return result;
}

// End Euler034

// Start Euler035

const isPrime = (n) => {
    if (n < 2) {
        return false;
    }
    if (n === 2) {
        return true;
    }
    if (n % 2 === 0) {
        return false;
    }
    for (let i = 3; i <= Math.trunc(Math.sqrt(n)); i += 2) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

const circularPrimes = (n) => {
    let count = 0;
    for (let i = 2; i < n; i++) {
        if (isPrime(i)) {
            const rotations = new Set();
            const si = i.toString();
            for (let j = 0; j < si.length; j++) {
                rotations.add(parseInt(si.substring(j) + si.substring(0, j)));
            }
            let flag = true;
            for (let x of rotations) {
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

const isPalindrome = (s) => {
    for (let i = 0; i < s.length / 2; i++) {
        if (s[i] !== s[s.length - i - 1]) {
            return false;
        }
    }
    return true;
}

const doubleBasePalindromes = (n) => {
    let result = 0;
    for (let i = 1; i < n; i++) {
        const strI = i.toString();
        const binI = i.toString(2);
        if (isPalindrome(strI) && isPalindrome(binI)) {
            result += i;
        }
    }
    return result;
}

// End Euler036

// Start Euler037

const isPrime = (n) => {
    if (n < 2) {
        return false;
    }
    if (n === 2) {
        return true;
    }
    if (n % 2 === 0) {
        return false;
    }
    for (let i = 3; i <= Math.trunc(Math.sqrt(n)); i += 2) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

const truncatablePrimes = (n) => {
    let result = 0;
    for (let i = 10; i < n; i++) {
        if (isPrime(i)) {
            const si = i.toString();
            let flag = true;
            for (let j = 1; j < si.length; j++) {
                const p1 = parseInt(si.substring(j));
                const p2 = parseInt(si.substring(0, si.length - j));
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

const pandigitalMultiples = (n) => {
    let result = -1;
    for (let i = 2; i <= n; i++) {
        let cprod = '';
        for (let j = 1; j < 10; j++) {
            cprod += (i * j).toString();
            if (cprod.length === 9) {
                let chars = cprod.split('');
                chars.sort();
                if (chars.join('') === '123456789') {
                    result = Math.max(result, parseInt(cprod));
                    break;
                }
            } else if (cprod.length > 9) {
                break;
            }
        }
    }
    return result;
}

// End Euler038

// Start Euler039

const integerRightTriangles = (n) => {
    let maxSol = 0;
    let result = 0;
    for (let p = 3; p <= n; p++) {
        let sol = 0;
        for (let a = 1; a < p / 2; a++) {
            for (let b = a; b < p / 2; b++) {
                let c = p - a - b;
                if (a * a + b * b === c * c) {
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

// End Euler039

// Start Euler040

const champernowneConstant = (b) => {
    let s = "";
    for (let i = 1; i < Math.pow(b, 6); i++) {
        s += i.toString();
    }
    let result = 1;
    for (let i = 0; i < 7; i++) {
        result *= parseInt(s[Math.pow(b, i) - 1]);
    }
    return result;
}

// End Euler040

// Start Euler041

const isPrime = (n) => {
    if (n < 2) {
        return false;
    }
    if (n === 2) {
        return true;
    }
    if (n % 2 === 0) {
        return false;
    }
    for (let i = 3; i <= Math.trunc(Math.sqrt(n)); i += 2) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

const pandigitalPrime = (n) => {
    for (let i = n - 1; i > 0; i--) {
        if (isPrime(i)) {
            let si = i.toString();
            let length = si.length;
            let flag = true;
            for (let j = 1; j <= length; j++) {
                if (!si.includes(j.toString())) {
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

const codedTriangleNumbers = (words) => {
    let result = 0;
    for (let word of words) {
        let value = 0;
        for (let c of word) {
            value += c.charCodeAt(0) - 64;
        }
        let n = parseInt(Math.sqrt(value * 2));
        if (n * (n + 1) === value * 2) {
            result++;
        }
    }
    return result;
}

// End Euler042

// Start Euler043

const genPermutations = (s) => {
    if (s.length <= 1) {
        return [s];
    }
    const result = [];
    for (const perm of genPermutations(s.slice(1))) {
        for (let i = 0; i < s.length; ++i) {
            result.push(perm.slice(0, i) + s[0] + perm.slice(i));
        }
    }
    return result;
}

const subStringDivisibility = (n) => {
    let result = 0;
    const primes = [2, 3, 5, 7, 11, 13, 17];
    let s = "";
    for (let i = 0; i <= n; i++) {
        s += i;
    }
    for (const i of genPermutations(s)) {
        let flag = true;
        for (let j = 1; j < n - 1; j++) {
            if (parseInt(i.substring(j, j + 3)) % primes[j - 1] !== 0) {
                flag = false;
                break;
            }
        }
        if (flag) {
            result += parseInt(i);
        }
    }
    return result;
}

// End Euler043

// Start Euler044

const pentagonNumbers = (n) => {
    const pentagon = new Set();
    for (let i = 1; i < n; i++) {
        pentagon.add(i * (3 * i - 1) / 2);
    }
    let result = -1;
    for (let j of pentagon) {
        for (let k of pentagon) {
            if (pentagon.has(j + k) && pentagon.has(k - j)) {
                if (result === -1 || k - j < result) {
                    result = k - j;
                }
            }
        }
    }
    return result;
}

// End Euler044

// Start Euler045

const triangularPentagonalAndHexagonal = (n) => {
    const ps = new Set();
    let i = 1;
    let c = 0.5 * i * (3 * i - 1);
    while (c < n) {
        i++;
        ps.add(c);
        c = 0.5 * i * (3 * i - 1);
    }
    i = 1;
    c = i * (2 * i - 1);
    let result = -1;
    while (c < n) {
        i++;
        if (ps.has(c)) {
            result = c;
        }
        c = i * (2 * i - 1);
    }
    return result;
}

// End Euler045

// Start Euler046

const isPrime = (n) => {
    if (n < 2) {
        return false;
    }
    if (n === 2) {
        return true;
    }
    if (n % 2 === 0) {
        return false;
    }
    for (let i = 3; i <= Math.trunc(Math.sqrt(n)); i += 2) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

const goldbachsOtherConjecture = (n) => {
    let result = -1;
    for (let i = 9999; i > n; i -= 2) {
        let upper = parseInt(Math.sqrt(i / 2));
        let flag = false;
        for (let j = 0; j <= upper; j++) {
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

const primeFactors = (n) => {
    let num = n;
    const factors = [];
    let i = 2;
    while (i * i <= num) {
        if (num % i !== 0) {
            i++;
        } else {
            num /= i;
            factors.push(i);
        }
    }
    if (num > 1) {
        factors.push(num);
    }
    return new Set(factors).size;
}

const distinctPrimesFactors = (n) => {
    for (let i = n; i < 1000000; i++) {
        if (primeFactors(i) === 4 && primeFactors(i + 1) === 4 && primeFactors(i + 2) === 4 && primeFactors(i + 3) === 4) {
            return i;
        }
    }
    return -1;
}

// End Euler047

// Start Euler048

const selfPowers = (n) => {
    const digits = new Array(10).fill(0);
    for (let i = 1; i <= n; i++) {
        const tempDigits = new Array(10).fill(0);
        tempDigits[0] = 1;
        for (let j = 0; j < i; j++) {
            let carry = 0;
            for (let k = 0; k < 10; k++) {
                tempDigits[k] = tempDigits[k] * i + carry;
                carry = Math.floor(tempDigits[k] / 10);
                tempDigits[k] %= 10;
            }
        }
        for (let j = 0; j < 10; j++) {
            digits[j] += tempDigits[j];
            if (digits[j] >= 10) {
                digits[j] -= 10;
                if (j < 9) {
                    digits[j + 1] += 1;
                }
            }
        }
    }
    let result = "";
    for (let i = 9; i >= 0; i--) {
        result += digits[i].toString();
    }
    return result;
}

// End Euler048

// Start Euler049

const isPrime = (n) => {
    if (n < 2) {
        return false;
    }
    if (n === 2) {
        return true;
    }
    if (n % 2 === 0) {
        return false;
    }
    for (let i = 3; i <= Math.trunc(Math.sqrt(n)); i += 2) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

const genPermutations = (s) => {
    if (s.length <= 1) {
        return [s];
    }
    const result = [];
    for (const perm of genPermutations(s.substring(1))) {
        for (let i = 0; i < s.length; ++i) {
            result.push(perm.substring(0, i) + s[0] + perm.substring(i));
        }
    }
    return result;
}

const primePermutations = (n) => {
    for (let i = n; i > 999; --i) {
        if (isPrime(i)) {
            const permutations = genPermutations(i.toString());
            const candidates = new Set();
            for (const j of permutations) {
                const candidate = parseInt(j);
                if (candidate > i && isPrime(candidate)) {
                    candidates.add(candidate);
                }
            }
            for (const m of candidates) {
                if (candidates.has(m + (m - i))) {
                    return i.toString() + m.toString() + (m + (m - i)).toString();
                }
            }
        }
    }
    return "";
}

// End Euler049

// Start Euler050

const consecutivePrimeSum = (limit) => {
    const sieve = Array(limit).fill(true);
    const primes = [];
    for (let i = 2; i < limit; i++) {
        if (sieve[i]) {
            primes.push(i);
            for (let j = i * 2; j < limit; j += i) {
                sieve[j] = false;
            }
        }
    }
    let maxLength = 0;
    let maxPrime = 0;
    for (let i = 0; i < primes.length; i++) {
        for (let j = i + maxLength; j < primes.length; j++) {
            let s = 0;
            for (let k = i; k < j; k++) {
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

// End Euler050

