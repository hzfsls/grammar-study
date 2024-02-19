# Python

def pandigital_multiples(n: int) -> int:
    result = -1
    for i in range(2, n + 1):
        cprod = ''
        for j in range(1, 10):
            cprod += str(i * j)
            if len(cprod) == 9:
                if ''.join(sorted(cprod)) == '123456789':
                    result = max(result, int(cprod))
                    break
            elif len(cprod) > 9:
                break
    return result

# Start translation now

# C++

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
                
# C#

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

# Go

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

# Java

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

# JavaScript

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

# Kotlin

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

# PHP

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

# Ruby

def pandigital_multiples(n)
    result = -1
    for i in 2..n
        cprod = ''
        for j in 1...10
            cprod += (i * j).to_s
            if cprod.length == 9
                chars = cprod.split('').sort.join
                if chars == '123456789'
                    result = [result, cprod.to_i].max
                    break
                end
            elsif cprod.length > 9
                break
            end
        end
    end
    result
end

# Rust

fn pandigital_multiples(n: i32) -> i32 {
    let mut result = -1;
    for i in 2..=n {
        let mut cprod = String::new();
        for j in 1..10 {
            cprod += &(i * j).to_string();
            if cprod.len() == 9 {
                let mut chars: Vec<char> = cprod.chars().collect();
                chars.sort();
                if chars.iter().collect::<String>() == "123456789" {
                    result = result.max(cprod.parse::<i32>().unwrap());
                    break;
                }
            } else if cprod.len() > 9 {
                break;
            }
        }
    }
    result
}

# Scala

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

