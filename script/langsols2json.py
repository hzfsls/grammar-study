import json

langs = ["python", "cpp", "csharp", "go", "java", "javascript", "kotlin", "php", "ruby", "rust", "scala"]

langs_suffix = {
    "python": "py",
    "cpp": "cpp",
    "csharp": "cs",
    "go": "go",
    "java": "java",
    "javascript": "js",
    "kotlin": "kt",
    "php": "php",
    "ruby": "rb",
    "rust": "rs",
    "scala": "scala"
}

sols = {}

for lang in langs:
    sols[lang] = {}
    with open(f"./lang_sols/euler.{langs_suffix[lang]}", "r", encoding="utf-8") as f:
        content = f.read()
        for i in range(1, 51):
            s_i = "0"*(3-len(str(i))) + str(i)
            name = f"Euler{s_i}"    
            if lang in ["python", "ruby"]:
                s_comment = f"# Start {name}\n"
                e_comment = f"# End {name}\n"
            else:
                s_comment = f"// Start {name}\n"
                e_comment = f"// End {name}\n"
            assert content.count(s_comment) == 1, (f"./lang_sols/euler.{langs_suffix[lang]}", s_comment)
            assert content.count(e_comment) == 1, (f"./lang_sols/euler.{langs_suffix[lang]}", e_comment)
            code = content.split(s_comment)[1].split(e_comment)[0]
            sols[lang][name] = code.strip()

with open("./data/euler_sol_1.json", "w", encoding="utf-8") as f:
    json.dump(sols, f, ensure_ascii=False, indent=4)