import json

langs = ["Python", "C++", "C#", "Go", "Java", "JavaScript", "Kotlin", "PHP", "Ruby", "Rust", "Scala"]

codes = {

}

for lang in langs:
    codes[lang] = []

names = []

for i in range(1, 51):
    s_i = "0"*(3-len(str(i))) + str(i)
    name = "Euler"+s_i
    names.append(name)

for name in names:
    with open(f"sols/{name}.py", "r", encoding="utf-8") as f:
        content = f.read()
        assert content.count("# Start translation now\n") == 1, name
        source = content.split("# Start translation now\n")[0].strip()
        assert source.startswith("# Python\n"), name
        py_code = source.split("# Python\n")[1].strip()
        translations = content.split("# Start translation now\n")[1].strip()
        for lang in langs:
            # assert translations.startswith(f"# {lang}\n"), (name, lang)
            assert content.count(f"# {lang}\n") == 1, (name, lang)
        cpp_code = translations.split("# C++\n")[1].strip().split("# C#\n")[0].strip()
        csharp_code = translations.split("# C#\n")[1].strip().split("# Go\n")[0].strip()
        go_code = translations.split("# Go\n")[1].strip().split("# Java\n")[0].strip()
        java_code = translations.split("# Java\n")[1].strip().split("# JavaScript\n")[0].strip()
        js_code = translations.split("# JavaScript\n")[1].strip().split("# Kotlin\n")[0].strip()
        kotlin_code = translations.split("# Kotlin\n")[1].strip().split("# PHP\n")[0].strip()
        php_code = translations.split("# PHP\n")[1].strip().split("# Ruby\n")[0].strip()
        ruby_code = translations.split("# Ruby\n")[1].strip().split("# Rust\n")[0].strip()
        rust_code = translations.split("# Rust\n")[1].strip().split("# Scala\n")[0].strip()
        scala_code = translations.split("# Scala\n")[1].strip()

        codes["Python"].append(py_code)
        codes["C++"].append(cpp_code)
        codes["C#"].append(csharp_code)
        codes["Go"].append(go_code)
        codes["Java"].append(java_code)
        codes["JavaScript"].append(js_code)
        codes["Kotlin"].append(kotlin_code)
        codes["PHP"].append(php_code)
        codes["Ruby"].append(ruby_code)
        codes["Rust"].append(rust_code)
        codes["Scala"].append(scala_code)

lang_name = {
    "C++": "cpp",
    "C#": "csharp",
    "Go": "go",
    "Java": "java",
    "JavaScript": "javascript",
    "Kotlin": "kotlin",
    "PHP": "php",
    "Python": "python",
    "Ruby": "ruby",
    "Rust": "rust",
    "Scala": "scala",
}

sols = {}

for lang in codes:
    assert len(codes[lang]) == 50, lang
    name = lang_name[lang]
    if name not in sols:
        sols[name] = {}
    for i in range(1, 51):
        s_i = "0"*(3-len(str(i))) + str(i)
        sols[name][f"Euler{s_i}"] = codes[lang][i-1]

with open("./data/euler_sol.json", "w", encoding="utf-8") as f:
    json.dump(sols, f, ensure_ascii=False, indent=4)