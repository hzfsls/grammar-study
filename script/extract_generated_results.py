import os

models = ["CodeLlama-13b-hf", "starcoderbase"]
langs = ["cpp", "csharp", "go", "java", "javascript", "kotlin", "php", "python", "ruby", "rust", "scala"]

codes = {}

for model in models:
    codes[model] = {}
    for src_lang in langs:
        for tgt_lang in langs:
            folder = f"./generated_results/MyEulerResult/{model}/{src_lang}2{tgt_lang}"
            if os.path.exists(folder):
                if src_lang not in codes[model]:
                    codes[model][src_lang] = {}
                codes[model][src_lang][tgt_lang] = []
                for i in range(50):
                    fname = f"{folder}/{i}.txt"
                    with open(fname, "r") as f:
                        code = f.read().strip()
                        codes[model][src_lang][tgt_lang].append(code)

import json

with open("./generated_results/generated_euler_result.json", "w") as f:
    json.dump(codes, f, indent=4)