// Start Euler001

function multiplesOf3And5($n) {
    $result = 0;
    for ($i = 0; $i < $n; $i++) {
        if ($i % 3 === 0 || $i % 5 === 0) {
            $result += $i;
        }
    }
    return $result;
}

// End Euler001

// Start Euler002

function evenFibonacciNumbers($n) {
    $result = 0;
    $a = 1;
    $b = 2;
    while ($a < $n) {
        if ($a % 2 === 0) {
            $result += $a;
        }
        $tmp = $a;
        $a = $b;
        $b = $tmp + $b;
    }
    return $result;
}

// End Euler002

// Start Euler003

function largestPrimeFactor($n) {
    $result = $n;
    $i = 2;
    while ($i * $i <= $result) {
        if ($result % $i !== 0) {
            $i += 1;
        } else {
            $result /= $i;
        }
    }
    return $result;
}

// End Euler003

// Start Euler004

function isPalindrome($s) {
    for ($i = 0; $i < strlen($s) / 2; $i++) {
        if ($s[$i] !== $s[strlen($s) - $i - 1]) {
            return false;
        }
    }
    return true;
}

function largestPalindromeProduct($n) {
    $result = 0;
    for ($i = 100; $i < 1000; $i++) {
        for ($j = $i; $j < 1000; $j++) {
            $prod = $i * $j;
            if (isPalindrome((string)$prod) && $prod > $result && $prod < $n) {
                $result = $prod;
            }
        }
    }
    return $result;
}

// End Euler004

// Start Euler005

function smallestMultiple($n) {
    $result = 1;
    for ($i = 1; $i <= $n; $i++) {
        if ($result % $i !== 0) {
            for ($j = 1; $j <= $n; $j++) {
                if (($result * $j) % $i === 0) {
                    $result *= $j;
                    break;
                }
            }
        }
    }
    return $result;
}

// End Euler005

// Start Euler006

function sumSquareDifference($n) {
    $sqrSum = 0;
    $numSum = 0;
    for ($i = 1; $i <= $n; $i++) {
        $sqrSum += $i * $i;
        $numSum += $i;
    }
    return $numSum * $numSum - $sqrSum;
}

// End Euler006

// Start Euler007

function nthPrime($n) {
    $primes = [2];
    $i = 3;
    while (count($primes) < $n) {
        foreach ($primes as $p) {
            if ($i % $p === 0) {
                break;
            }
            if ($p * $p > $i) {
                $primes[] = $i;
                break;
            }
        }
        $i += 2;
    }
    return end($primes);
}

// End Euler007

// Start Euler008

function largestProductInASeries($s, $k) {
    $result = 0;
    for ($i = 0; $i < strlen($s) - $k; $i++) {
        $product = 1;
        for ($j = 0; $j < $k; $j++) {
            $product *= intval($s[$i + $j]);
        }
        $result = max($result, $product);
    }
    return $result;
}

// End Euler008

// Start Euler009

function specialPythagoreanTriplet($n) {
    for ($a = 1; $a < $n; $a++) {
        for ($b = $a; $b < $n; $b++) {
            $c = $n - $a - $b;
            if ($a * $a + $b * $b === $c * $c) {
                return $a * $b * $c;
            }
        }
    }
    return -1;
}

// End Euler009

// Start Euler010

function summationOfPrimes($n) {
    $primes = [2];
    $i = 3;
    while ($i <= $n) {
        foreach ($primes as $p) {
            if ($i % $p === 0) {
                break;
            }
            if ($p * $p > $i) {
                $primes[] = $i;
                break;
            }
        }
        $i += 2;
    }
    $result = 0;
    foreach ($primes as $prime) {
        $result += $prime;
    }
    return $result;
}

// End Euler010

// Start Euler011

function largestProductInAGrid($grid) {
    $result = 0;
    for ($i = 0; $i < count($grid) - 3; $i++) {
        for ($j = 0; $j < count($grid[$i]) - 3; $j++) {
            $p1 = 1;
            $p2 = 1;
            $p3 = 1;
            $p4 = 1;
            for ($k = 0; $k < 4; $k++) {
                $p1 *= $grid[$i + $k][$j];
            }
            for ($k = 0; $k < 4; $k++) {
                $p2 *= $grid[$i][$j + $k];
            }
            for ($k = 0; $k < 4; $k++) {
                $p3 *= $grid[$i + $k][$j + $k];
            }
            for ($k = 0; $k < 4; $k++) {
                $p4 *= $grid[$i + $k][$j + 3 - $k];
            }
            $result = max($result, $p1, $p2, $p3, $p4);
        }
    }
    return $result;
}

// End Euler011

// Start Euler012

function highlyDivisibleTriangularNumber($n) {
    for ($i = 1; $i < 100000000; $i++) {
        $result = $i * ($i + 1) / 2;
        $count = 0;
        for ($j = 1; $j <= intval(sqrt($result)); $j++) {
            if ($result % $j === 0) {
                $count += 2;
            }
            if ($j * $j === $result) {
                $count -= 1;
            }
        }
        if ($count > $n) {
            return $result;
        }
    }
    return -1;
}

// End Euler012

// Start Euler013

function largeSum($numbers) {
    $digits = array_fill(0, 60, 0);
    for ($i = 0; $i < 50; $i++) {
        $tmp = 0;
        foreach ($numbers as $num) {
            $tmp += (int)$num[49 - $i];
        }
        for ($j = $i; $j < 60; $j++) {
            $digits[$j] += $tmp % 10;
            if ($digits[$j] >= 10) {
                $digits[$j + 1] += intdiv($digits[$j], 10);
                $digits[$j] %= 10;
            }
            $tmp = intdiv($tmp, 10);
            if ($tmp === 0) {
                break;
            }
        }
    }
    for ($i = 59; $i >= 0; $i--) {
        if ($digits[$i] !== 0) {
            $result = '';
            for ($j = $i; $j > $i - 10; $j--) {
                $result .= $digits[$j];
            }
            return $result;
        }
    }
    return '';
}

// End Euler013

// Start Euler014

function longestCollatzSequence($n) {
    $longest = 0;
    $result = 0;
    for ($i = 1; $i < $n; $i++) {
        $chain = 1;
        $num = $i;
        while ($num !== 1) {
            if ($num % 2 === 0) {
                $num = $num / 2;
            } else {
                $num = 3 * $num + 1;
            }
            $chain++;
        }
        if ($chain > $longest) {
            $longest = $chain;
            $result = $i;
        }
    }
    return $result;
}

// End Euler014

// Start Euler015

function latticePaths($m, $n) {
    $grid = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
    for ($i = 0; $i <= $m; $i++) {
        $grid[$i][0] = 1;
    }
    for ($j = 0; $j <= $n; $j++) {
        $grid[0][$j] = 1;
    }
    for ($i = 1; $i <= $m; $i++) {
        for ($j = 1; $j <= $n; $j++) {
            $grid[$i][$j] = $grid[$i - 1][$j] + $grid[$i][$j - 1];
        }
    }
    return $grid[$m][$n];
}

// End Euler015

// Start Euler016

function powerDigitSum($n) {
    $digits = [2];
    for ($i = 1; $i < $n; $i++) {
        $carry = 0;
        for ($j = 0; $j < count($digits); $j++) {
            $temp = $digits[$j] * 2 + $carry;
            $digits[$j] = $temp % 10;
            $carry = intdiv($temp, 10);
        }
        if ($carry !== 0) {
            array_push($digits, $carry);
        }
    }
    $result = 0;
    foreach ($digits as $digit) {
        $result += $digit;
    }
    return $result;
}

// End Euler016

// Start Euler017

function numberToWords($n) {
    $ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    $teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
    $tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
    if ($n === 1000) {
        return "one thousand";
    } elseif ($n >= 100) {
        if ($n % 100 === 0) {
            return $ones[$n / 100] . " hundred";
        } else {
            return $ones[$n / 100] . " hundred and " . numberToWords($n % 100);
        }
    } elseif ($n >= 20) {
        $suf = "";
        if ($n % 10 !== 0) {
            $suf = " " . $ones[$n % 10];
        }
        return $tens[$n / 10] . $suf;
    } elseif ($n >= 10) {
        return $teens[$n - 10];
    } else {
        return $ones[$n];
    }
}

// End Euler017

// Start Euler018

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

// End Euler018

// Start Euler019

function countingSundays($y1, $y2) {
    $day = 0;
    $count = 0;
    for ($year = 1900; $year <= $y2; $year++) {
        for ($month = 1; $month <= 12; $month++) {
            if ($year >= $y1 && $day % 7 === 6) {
                $count++;
            }
            if ($month === 4 || $month === 6 || $month === 9 || $month === 11) {
                $day += 30;
            } else if ($month === 2) {
                if ($year % 4 === 0 && ($year % 100 !== 0 || $year % 400 === 0)) {
                    $day += 29;
                } else {
                    $day += 28;
                }
            } else {
                $day += 31;
            }
        }
    }
    return $count;
}

// End Euler019

// Start Euler020

function factorialDigitSum($n) {
    $digits = [1];
    for ($i = 1; $i <= $n; $i++) {
        $carry = 0;
        for ($j = 0; $j < count($digits); $j++) {
            $digits[$j] = $digits[$j] * $i + $carry;
            $carry = (int)($digits[$j] / 10);
            $digits[$j] %= 10;
        }
        while ($carry !== 0) {
            $digits[] = $carry % 10;
            $carry = (int)($carry / 10);
        }
    }
    $result = 0;
    foreach ($digits as $digit) {
        $result += $digit;
    }
    return $result;
}

// End Euler020

// Start Euler021

function d($n) {
    $result = 1;
    for ($i = 2; $i <= sqrt($n); $i++) {
        if ($n % $i === 0) {
            $result += $i;
            if ($i !== $n / $i) {
                $result += $n / $i;
            }
        }
    }
    return $result;
}

function amicableNumbers($n) {
    $result = 0;
    for ($a = 2; $a < $n; $a++) {
        $b = d($a);
        if ($a !== $b && $a === d($b)) {
            $result += $a;
        }
    }
    return $result;
}

// End Euler021

// Start Euler022

function namesScores($names, $queries) {
    $sNames = $names;
    sort($sNames);
    $result = 0;
    foreach ($sNames as $i => $name) {
        $x = 0;
        foreach (str_split($name) as $c) {
            $x += ord($c) - 64;
        }
        if (in_array($name, $queries)) {
            $result += $x * ($i + 1);
        }
    }
    return $result;
}

// End Euler022

// Start Euler023

function isAbundant($n) {
    if ($n < 12) {
        return false;
    }
    $sumDivisors = 1;
    for ($i = 2; $i <= sqrt($n); $i++) {
        if ($n % $i === 0) {
            $sumDivisors += $i;
            if ($i !== $n / $i) {
                $sumDivisors += $n / $i;
            }
        }
    }
    return $sumDivisors > $n;
}

function nonAbundantSums($n) {
    $abundants = [];
    for ($i = 12; $i < $n; $i++) {
        if (isAbundant($i)) {
            $abundants[] = $i;
        }
    }
    $abundantSums = [];
    foreach ($abundants as $i) {
        foreach ($abundants as $j) {
            $abundantSums[] = $i + $j;
        }
    }
    $result = 0;
    for ($i = 0; $i < $n; $i++) {
        if (!in_array($i, $abundantSums)) {
            $result += $i;
        }
    }
    return $result;
}

// End Euler023

// Start Euler024

function lexicographicPermutations($n) {
    $result = "";
    $digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    $x = $n - 1;
    for ($i = 10; $i > 0; $i--) {
        $fact = 1;
        for ($j = 1; $j < $i; $j++) {
            $fact *= $j;
        }
        $idx = floor($x / $fact);
        $result .= $digits[$idx];
        array_splice($digits, $idx, 1);
        $x -= $idx * $fact;
    }
    return $result;
}

// End Euler024

// Start Euler025

function nDigitFibonacciNumber($n) {
    $a = [1];
    $b = [1];
    $i = 2;
    while (count($b) < $n) {
        $carry = 0;
        $c = $b;
        for ($j = 0; $j < count($b); $j++) {
            if ($j < count($a)) {
                $b[$j] = $a[$j] + $b[$j] + $carry;
            } else {
                $b[$j] = $b[$j] + $carry;
            }
            $carry = intdiv($b[$j], 10);
            $b[$j] = $b[$j] % 10;
        }
        if ($carry !== 0) {
            array_push($b, $carry);
        }
        $a = $c;
        $i = $i + 1;
    }
    return $i;
}

// End Euler025

// Start Euler026

function reciprocalCycles($n) {
    $result = 0;
    $maxLength = 0;
    for ($i = 1; $i < $n; $i++) {
        $remainders = [];
        $remainder = 1;
        while ($remainder !== 0 && !in_array($remainder, $remainders)) {
            array_push($remainders, $remainder);
            $remainder = ($remainder * 10) % $i;
        }
        $length = 0;
        if ($remainder !== 0) {
            $length = count($remainders) - array_search($remainder, $remainders);
        }
        if ($length > $maxLength) {
            $maxLength = $length;
            $result = $i;
        }
    }
    return $result;
}

// End Euler026

// Start Euler027

function isPrime($n) {
    if ($n < 2) {
        return false;
    }
    if ($n === 2) {
        return true;
    }
    if ($n % 2 === 0) {
        return false;
    }
    for ($i = 3; $i <= intval(sqrt($n)); $i += 2) {
        if ($n % $i === 0) {
            return false;
        }
    }
    return true;
}

function quadraticPrimes($n) {
    $maxPrimes = 0;
    $result = 0;
    for ($a = -$n + 1; $a < $n; $a += 2) {
        for ($b = -$n + 1; $b < $n; $b += 2) {
            $x = 0;
            while (true) {
                if ($x * $x + $a * $x + $b < 2) {
                    break;
                }
                if (!isPrime($x * $x + $a * $x + $b)) {
                    break;
                }
                $x++;
            }
            if ($x > $maxPrimes) {
                $maxPrimes = $x;
                $result = $a * $b;
            }
        }
    }
    return $result;
}

// End Euler027

// Start Euler028

function numberSpiralDiagonals($n) {
    $result = 1;
    for ($i = 3; $i <= $n; $i += 2) {
        $result += 4 * $i * $i - 6 * $i + 6;
    }
    return $result;
}

// End Euler028

// Start Euler029

function distinctPowers($n) {
    $result = 0;
    $xs = [];
    for ($i = 2; $i <= $n; $i++) {
        $primes = [2, 3, 5, 7];
        $powers = [0, 0, 0, 0];
        $num = $i;
        for ($j = 0; $j < count($primes); $j++) {
            while ($num % $primes[$j] === 0) {
                $num /= $primes[$j];
                $powers[$j] += 1;
            }
        }
        if ($num !== 1) {
            $result += $n - 1;
            continue;
        }
        for ($j = 2; $j <= $n; $j++) {
            $pstr = sprintf("%d-%d-%d-%d", $powers[0] * $j, $powers[1] * $j, $powers[2] * $j, $powers[3] * $j);
            $xs[$pstr] = true;
        }
    }
    $result += count($xs);
    return $result;
}

// End Euler029

// Start Euler030

function digitNthPowers($n) {
    $result = 0;
    for ($i = 2; $i < 4 * pow(10, $n); $i++) {
        $digitsSum = 0;
        foreach (str_split(strval($i)) as $digit) {
            $digitsSum += pow($digit, $n);
        }
        if ($i === $digitsSum) {
            $result += $i;
        }
    }
    return $result;
}

// End Euler030

// Start Euler031

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

// End Euler031

// Start Euler032

function pandigitalProducts($n) {
    $products = [];
    $s = "";
    for ($i = 1; $i <= $n; $i++) {
        $s .= $i;
    }
    for ($a = 1; $a < 100; $a++) {
        for ($b = 1; $b < 10000; $b++) {
            $c = $a * $b;
            $chars = str_split(strval($a) . strval($b) . strval($c));
            sort($chars);
            if (implode("", $chars) === $s) {
                $products[$c] = true;
            }
        }
    }
    $result = 0;
    foreach (array_keys($products) as $product) {
        $result += $product;
    }
    return $result;
}

// End Euler032

// Start Euler033

function digitCancelingFractions($m) {
    $numer = 1;
    $denom = 1;
    for ($d = 10; $d < $m; $d++) {
        for ($n = 10; $n < $d; $n++) {
            $n0 = $n % 10;
            $n1 = intdiv($n, 10);
            $d0 = $d % 10;
            $d1 = intdiv($d, 10);
            if (($n1 === $d0 && $n0 * $d === $n * $d1) || ($n0 === $d1 && $n1 * $d === $n * $d0)) {
                $numer *= $n;
                $denom *= $d;
            }
        }
    }
    $a = $numer;
    $b = $denom;
    while ($b !== 0) {
        $temp = $b;
        $b = $a % $b;
        $a = $temp;
    }
    return intdiv($denom, $a);
}

// End Euler033

// Start Euler034

function digitFactorials($n) {
    $result = 0;
    for ($i = 3; $i < $n; $i++) {
        $factSum = 0;
        foreach (str_split(strval($i)) as $digit) {
            $fact = 1;
            for ($j = 1; $j <= intval($digit); $j++) {
                $fact *= $j;
            }
            $factSum += $fact;
        }
        if ($i === $factSum) {
            $result += $i;
        }
    }
    return $result;
}

// End Euler034

// Start Euler035

function isPrime($n) {
    if ($n < 2) {
        return false;
    }
    if ($n === 2) {
        return true;
    }
    if ($n % 2 === 0) {
        return false;
    }
    for ($i = 3; $i <= intval(sqrt($n)); $i += 2) {
        if ($n % $i === 0) {
            return false;
        }
    }
    return true;
}

function circularPrimes($n) {
    $count = 0;
    for ($i = 2; $i < $n; $i++) {
        if (isPrime($i)) {
            $rotations = [];
            $si = strval($i);
            for ($j = 0; $j < strlen($si); $j++) {
                $rotations[] = intval(substr($si, $j) . substr($si, 0, $j));
            }
            $flag = true;
            foreach ($rotations as $x) {
                if (!isPrime($x)) {
                    $flag = false;
                    break;
                }
            }
            if ($flag) {
                $count++;
            }
        }
    }
    return $count;
}

// End Euler035

// Start Euler036

function isPalindrome($s) {
    for ($i = 0; $i < strlen($s) / 2; $i++) {
        if ($s[$i] !== $s[strlen($s) - ($i + 1)]) {
            return false;
        }
    }
    return true;
}

function doubleBasePalindromes($n) {
    $result = 0;
    for ($i = 1; $i < $n; $i++) {
        $strI = strval($i);
        $binI = decbin($i);
        if (isPalindrome($strI) && isPalindrome($binI)) {
            $result += $i;
        }
    }
    return $result;
}

// End Euler036

// Start Euler037

function isPrime($n) {
    if ($n < 2) {
        return false;
    }
    if ($n === 2) {
        return true;
    }
    if ($n % 2 === 0) {
        return false;
    }
    for ($i = 3; $i <= intval(sqrt($n)); $i += 2) {
        if ($n % $i === 0) {
            return false;
        }
    }
    return true;
}

function truncatablePrimes($n) {
    $result = 0;
    for ($i = 10; $i < $n; $i++) {
        if (isPrime($i)) {
            $si = strval($i);
            $flag = true;
            for ($j = 1; $j < strlen($si); $j++) {
                $p1 = intval(substr($si, $j));
                $p2 = intval(substr($si, 0, strlen($si) - $j));
                if (!isPrime($p1) || !isPrime($p2)) {
                    $flag = false;
                    break;
                }
            }
            if ($flag) {
                $result += $i;
            }
        }
    }
    return $result;
}

// End Euler037

// Start Euler038

function pandigitalMultiples($n) {
    $result = -1;
    for ($i = 2; $i <= $n; $i++) {
        $cprod = '';
        for ($j = 1; $j < 10; $j++) {
            $cprod .= $i * $j;
            if (strlen($cprod) === 9) {
                $chars = str_split($cprod);
                sort($chars);
                if (implode($chars) === '123456789') {
                    $result = max($result, (int)$cprod);
                    break;
                }
            } elseif (strlen($cprod) > 9) {
                break;
            }
        }
    }
    return $result;
}

// End Euler038

// Start Euler039

function integerRightTriangles($n) {
    $maxSol = 0;
    $result = 0;
    for ($p = 3; $p <= $n; $p++) {
        $sol = 0;
        for ($a = 1; $a < $p / 2; $a++) {
            for ($b = $a; $b < $p / 2; $b++) {
                $c = $p - $a - $b;
                if ($a * $a + $b * $b === $c * $c) {
                    $sol++;
                }
            }
        }
        if ($sol > $maxSol) {
            $maxSol = $sol;
            $result = $p;
        }
    }
    return $result;
}

// End Euler039

// Start Euler040

function champernowneConstant($b) {
    $s = "";
    for ($i = 1; $i < pow($b, 6); $i++) {
        $s .= strval($i);
    }
    $result = 1;
    for ($i = 0; $i < 7; $i++) {
        $result *= intval($s[pow($b, $i) - 1]);
    }
    return $result;
}

// End Euler040

// Start Euler041

function isPrime($n) {
    if ($n < 2) {
        return false;
    }
    if ($n === 2) {
        return true;
    }
    if ($n % 2 === 0) {
        return false;
    }
    for ($i = 3; $i <= intval(sqrt($n)); $i += 2) {
        if ($n % $i === 0) {
            return false;
        }
    }
    return true;
}

function pandigitalPrime($n) {
    for ($i = $n - 1; $i > 0; $i--) {
        if (isPrime($i)) {
            $si = strval($i);
            $length = strlen($si);
            $flag = true;
            for ($j = 1; $j <= $length; $j++) {
                if (strpos($si, strval($j)) === false) {
                    $flag = false;
                    break;
                }
            }
            if ($flag) {
                return $i;
            }
        }
    }
    return -1;
}

// End Euler041

// Start Euler042

function codedTriangleNumbers($words) {
    $result = 0;
    foreach ($words as $word) {
        $value = 0;
        for ($i = 0; $i < strlen($word); $i++) {
            $value += ord($word[$i]) - 64;
        }
        $n = intval(sqrt($value * 2));
        if ($n * ($n + 1) === $value * 2) {
            $result++;
        }
    }
    return $result;
}

// End Euler042

// Start Euler043

function genPermutations($s) {
    if (strlen($s) <= 1) {
        return [$s];
    }
    $result = [];
    foreach (genPermutations(substr($s, 1)) as $perm) {
        for ($i = 0; $i < strlen($s); $i++) {
            $result[] = substr($perm, 0, $i) . $s[0] . substr($perm, $i);
        }
    }
    return $result;
}

function subStringDivisibility($n) {
    $result = 0;
    $primes = [2, 3, 5, 7, 11, 13, 17];
    $s = "";
    for ($i = 0; $i <= $n; $i++) {
        $s .= $i;
    }
    foreach (genPermutations($s) as $i) {
        $flag = true;
        for ($j = 1; $j < $n - 1; $j++) {
            if (intval(substr($i, $j, 3)) % $primes[$j - 1] !== 0) {
                $flag = false;
                break;
            }
        }
        if ($flag) {
            $result += intval($i);
        }
    }
    return $result;
}

// End Euler043

// Start Euler044

function pentagonNumbers($n) {
    $pentagon = array();
    for ($i = 1; $i < $n; $i++) {
        $pentagon[$i * (3 * $i - 1) / 2] = true;
    }
    $result = -1;
    foreach ($pentagon as $j => $value) {
        foreach ($pentagon as $k => $value) {
            if (isset($pentagon[$j + $k]) && isset($pentagon[$k - $j])) {
                if ($result === -1 || $k - $j < $result) {
                    $result = $k - $j;
                }
            }
        }
    }
    return $result;
}

// End Euler044

// Start Euler045

function triangularPentagonalAndHexagonal($n) {
    $ps = [];
    $i = 1;
    $c = 0.5 * $i * (3 * $i - 1);
    while ($c < $n) {
        $i++;
        $ps[$c] = true;
        $c = 0.5 * $i * (3 * $i - 1);
    }
    $i = 1;
    $c = $i * (2 * $i - 1);
    $result = -1;
    while ($c < $n) {
        $i++;
        if (isset($ps[$c])) {
            $result = $c;
        }
        $c = $i * (2 * $i - 1);
    }
    return $result;
}

// End Euler045

// Start Euler046

function isPrime($n) {
    if ($n < 2) {
        return false;
    }
    if ($n === 2) {
        return true;
    }
    if ($n % 2 === 0) {
        return false;
    }
    for ($i = 3; $i <= intval(sqrt($n)); $i += 2) {
        if ($n % $i === 0) {
            return false;
        }
    }
    return true;
}

function goldbachsOtherConjecture($n) {
    $result = -1;
    for ($i = 9999; $i > $n; $i -= 2) {
        $upper = sqrt($i / 2);
        $flag = false;
        for ($j = 0; $j <= $upper; $j++) {
            if (isPrime($i - 2 * $j * $j)) {
                $flag = true;
                break;
            }
        }
        if (!$flag) {
            $result = $i;
        }
    }
    return $result;
}

// End Euler046

// Start Euler047

function primeFactors($n) {
    $num = $n;
    $factors = [];
    $i = 2;
    while ($i * $i <= $num) {
        if ($num % $i !== 0) {
            $i++;
        } else {
            $num /= $i;
            $factors[] = $i;
        }
    }
    if ($num > 1) {
        $factors[] = $num;
    }
    return count(array_unique($factors));
}

function distinctPrimesFactors($n) {
    for ($i = $n; $i < 1000000; $i++) {
        if (primeFactors($i) === 4 && primeFactors($i + 1) === 4 && primeFactors($i + 2) === 4 && primeFactors($i + 3) === 4) {
            return $i;
        }
    }
    return -1;
}

// End Euler047

// Start Euler048

function selfPowers($n) {
    $digits = array_fill(0, 10, 0);
    for ($i = 1; $i <= $n; $i++) {
        $tempDigits = array_fill(0, 10, 0);
        $tempDigits[0] = 1;
        for ($j = 0; $j < $i; $j++) {
            $carry = 0;
            for ($k = 0; $k < 10; $k++) {
                $tempDigits[$k] = $tempDigits[$k] * $i + $carry;
                $carry = intdiv($tempDigits[$k], 10);
                $tempDigits[$k] %= 10;
            }
        }
        for ($j = 0; $j < 10; $j++) {
            $digits[$j] += $tempDigits[$j];
            if ($digits[$j] >= 10) {
                $digits[$j] -= 10;
                if ($j < 9) {
                    $digits[$j + 1] += 1;
                }
            }
        }
    }
    $result = "";
    for ($i = 9; $i >= 0; $i--) {
        $result .= strval($digits[$i]);
    }
    return $result;
}

// End Euler048

// Start Euler049

function isPrime($n) {
    if ($n < 2) {
        return false;
    }
    if ($n === 2) {
        return true;
    }
    if ($n % 2 === 0) {
        return false;
    }
    for ($i = 3; $i <= intval(sqrt($n)); $i += 2) {
        if ($n % $i === 0) {
            return false;
        }
    }
    return true;
}

function genPermutations($s) {
    if (strlen($s) <= 1) {
        return [$s];
    }
    $result = [];
    foreach (genPermutations(substr($s, 1)) as $perm) {
        for ($i = 0; $i < strlen($s); ++$i) {
            $result[] = substr($perm, 0, $i) . $s[0] . substr($perm, $i);
        }
    }
    return $result;
}

function primePermutations($n) {
    for ($i = $n; $i > 999; --$i) {
        if (isPrime($i)) {
            $permutations = genPermutations(strval($i));
            $candidates = [];
            foreach ($permutations as $j) {
                $candidate = intval($j);
                if ($candidate > $i && isPrime($candidate)) {
                    $candidates[] = $candidate;
                }
            }
            foreach ($candidates as $m) {
                if (in_array($m + ($m - $i), $candidates)) {
                    return strval($i) . strval($m) . strval($m + ($m - $i));
                }
            }
        }
    }
    return "";
}

// End Euler049

// Start Euler050

function consecutivePrimeSum($limit) {
    $sieve = array_fill(0, $limit, true);
    $primes = [];
    for ($i = 2; $i < $limit; $i++) {
        if ($sieve[$i]) {
            $primes[] = $i;
            for ($j = $i * 2; $j < $limit; $j += $i) {
                $sieve[$j] = false;
            }
        }
    }
    $maxLength = 0;
    $maxPrime = 0;
    for ($i = 0; $i < count($primes); $i++) {
        for ($j = $i + $maxLength; $j < count($primes); $j++) {
            $s = 0;
            for ($k = $i; $k < $j; $k++) {
                $s += $primes[$k];
            }
            if ($s >= $limit) {
                break;
            }
            if ($sieve[$s] && $j - $i > $maxLength) {
                $maxLength = $j - $i;
                $maxPrime = $s;
            }
        }
    }
    return $maxPrime;
}

// End Euler050

