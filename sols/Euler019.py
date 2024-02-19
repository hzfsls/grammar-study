# Python

def counting_sundays(y1: int, y2: int) -> int:
    day = 0
    count = 0
    for year in range(1900, y2 + 1):
        for month in range(1, 13):
            if year >= y1 and day % 7 == 6:
                count += 1
            if month in [4, 6, 9, 11]:
                day += 30
            elif month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    day += 29
                else:
                    day += 28
            else:
                day += 31
    return count

# Start translation now

# C++

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

# C#

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

# Go

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

# Java

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

# JavaScript

const countingSundays = (y1, y2) => {
    let day = 0;
    let count = 0;
    for (let year = 1900; year <= y2; year++) {
        for (let month = 1; month <= 12; month++) {
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

# Kotlin

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

# PHP

function countingSundays($y1, $y2) {
    $day = 0;
    $count = 0;
    for ($year = 1900; $year <= $y2; $year++) {
        for ($month = 1; $month <= 12; $month++) {
            if ($year >= $y1 && $day % 7 == 6) {
                $count++;
            }
            if ($month == 4 || $month == 6 || $month == 9 || $month == 11) {
                $day += 30;
            } else if ($month == 2) {
                if ($year % 4 == 0 && ($year % 100 != 0 || $year % 400 == 0)) {
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

# Ruby

def counting_sundays(y1, y2)
    day = 0
    count = 0
    (1900..y2).each do |year|
        (1..12).each do |month|
            if year >= y1 && day % 7 == 6
                count += 1
            end
            if [4, 6, 9, 11].include?(month)
                day += 30
            elsif month == 2
                if year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
                    day += 29
                else
                    day += 28
                end
            else
                day += 31
            end
        end
    end
    count
end

# Rust

fn counting_sundays(y1: i32, y2: i32) -> i32 {
    let mut day = 0;
    let mut count = 0;
    for year in 1900..=y2 {
        for month in 1..=12 {
            if year >= y1 && day % 7 == 6 {
                count += 1;
            }
            if month == 4 || month == 6 || month == 9 || month == 11 {
                day += 30;
            } else if month == 2 {
                if year % 4 == 0 && (year % 100 != 0 || year % 400 == 0) {
                    day += 29;
                } else {
                    day += 28;
                }
            } else {
                day += 31;
            }
        }
    }
    count
}

# Scala

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
