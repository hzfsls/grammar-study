import json

with open("./data/euler_sol.json", "r", encoding="utf-8") as f:
    j = json.load(f)

langs = ["python", "cpp", "csharp", "go", "java", "javascript", "kotlin", "php", "ruby", "rust", "scala"]

lang_suffix = {
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

for lang in langs:
    sols = j[lang]
    filename = f"./lang_sols/euler.{lang_suffix[lang]}"
    with open(filename, "w", encoding="utf-8") as f:
        for name, sol in sols.items():
            if lang in ["python", "ruby"]:
                f.write(f"# Start {name}\n\n")
            else:
                f.write(f"// Start {name}\n\n")
            f.write(sol.strip())
            if lang in ["python", "ruby"]:
                f.write(f"\n\n# End {name}\n\n")
            else:
                f.write(f"\n\n// End {name}\n\n")

