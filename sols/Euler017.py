# Python

def number_to_words(n: int) -> str:
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n == 1000:
        return "one thousand"
    elif n >= 100:
        if n % 100 == 0:
            return ones[n // 100] + " hundred"
        else:
            return ones[n // 100] + " hundred and " + number_to_words(n % 100)
    elif n >= 20:
        suf = ""
        if n % 10 != 0:
            suf = " " + ones[n % 10]
        return tens[n // 10] + suf
    elif n >= 10:
        return teens[n - 10]
    else:
        return ones[n]

# Start translation now

# C++

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

# C#

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

# Go

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

# Java

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

# JavaScript

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

# Kotlin

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

# PHP

function numberToWords($n) {
    $ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    $teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
    $tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
    if ($n == 1000) {
        return "one thousand";
    } elseif ($n >= 100) {
        if ($n % 100 == 0) {
            return $ones[$n / 100] . " hundred";
        } else {
            return $ones[$n / 100] . " hundred and " . numberToWords($n % 100);
        }
    } elseif ($n >= 20) {
        $suf = "";
        if ($n % 10 != 0) {
            $suf = " " . $ones[$n % 10];
        }
        return $tens[$n / 10] . $suf;
    } elseif ($n >= 10) {
        return $teens[$n - 10];
    } else {
        return $ones[$n];
    }
}

# Ruby

def number_to_words(n)
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n == 1000
        "one thousand"
    elsif n >= 100
        if n % 100 == 0
            ones[n / 100] + " hundred"
        else
            ones[n / 100] + " hundred and " + number_to_words(n % 100)
        end
    elsif n >= 20
        suf = ""
        if n % 10 != 0
            suf = " " + ones[n % 10]
        end
        tens[n / 10] + suf
    elsif n >= 10
        teens[n - 10]
    else
        ones[n]
    end
end

# Rust

fn number_to_words(n: i32) -> String {
    let ones = vec!["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let teens = vec!["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
    let tens = vec!["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
    if n == 1000 {
        "one thousand".to_string()
    } else if n >= 100 {
        if n % 100 == 0 {
            ones[(n / 100) as usize].to_string() + " hundred"
        } else {
            ones[(n / 100) as usize].to_string() + " hundred and " + &number_to_words(n % 100)
        }
    } else if n >= 20 {
        let mut suf = "".to_string();
        if n % 10 != 0 {
            suf = " ".to_string() + &ones[(n % 10) as usize];
        }
        tens[(n / 10) as usize].to_string() + &suf
    } else if n >= 10 {
        teens[(n - 10) as usize].to_string()
    } else {
        ones[n as usize].to_string()
    }
}

# Scala

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


