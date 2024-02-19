# Python

def names_scores(names: list[str], queries: list[str]) -> int:
    s_names = sorted(names)
    result = 0
    for i, name in enumerate(s_names):
        x = 0
        for c in name:
            x += ord(c) - 64
        if name in queries:
            result += x * (i + 1)
    return result

# Start translation now

# C++

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

# C#

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

# Go

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

# Java

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

# JavaScript

const namesScores = (names, queries) => {
    let sNames = [...names].sort();
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

# Kotlin

fun namesScores(names: List<String>, queries: List<String>): Int {
    val sNames = names.sorted().toMutableList()
    var result = 0
    for ((i, name) in sNames.withIndex()) {
        var x = 0
        for (c in name) {
            x += c.toInt() - 64
        }
        if (name in queries) {
            result += x * (i + 1)
        }
    }
    return result
}

# PHP

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

# Ruby

def names_scores(names, queries)
    s_names = names.sort
    result = 0
    s_names.each_with_index do |name, i|
        x = 0
        name.each_char do |c|
            x += c.ord - 64
        end
        if queries.include?(name)
            result += x * (i + 1)
        end
    end
    result
end

# Rust

fn names_scores(names: &Vec<String>, queries: &Vec<String>) -> i32 {
    let mut s_names = names.clone();
    s_names.sort();
    let mut result = 0;
    for (i, name) in s_names.iter().enumerate() {
        let mut x = 0;
        for c in name.chars() {
            x += c as i32 - 64;
        }
        if queries.contains(name) {
            result += x * (i as i32 + 1);
        }
    }
    result
}

# Scala

def namesScores(names: Seq[String], queries: Seq[String]): Int = {
    val sNames = names.sorted.to(ArrayBuffer)
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

