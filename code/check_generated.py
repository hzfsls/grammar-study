from polyeval.parsing import parse
from polyeval.eval import ProjectTemplate, EvalStatus, gen_codes, gen_codes_for_single_file, create_project

from tqdm import tqdm
import sys
import os
import argparse
import json

from pebble import ProcessPool

from typing import List

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# langs = ["cpp", "csharp", "dart", "go", "java", "javascript", "kotlin", "php", "python", "ruby", "rust", "scala", "swift", "typescript"]

langs = [
    "cpp",
    "csharp",
    # "dart",
    "go",
    "java",
    "javascript",
    "kotlin",
    "php",
    "python",
    "ruby",
    "rust",
    "scala",
    # "swift",
    # "typescript",
]



suffix = {
    "cpp": "cpp",
    "csharp": "cs",
    "dart": "dart",
    "go": "go",
    "java": "java",
    "javascript": "js",
    "kotlin": "kt",
    "php": "php",
    "python": "py",
    "ruby": "rb",
    "rust": "rs",
    "scala": "scala",
    "swift": "swift",
    "typescript": "ts"
}

cur_langs = langs

parser = argparse.ArgumentParser()
parser.add_argument("--problem", type=str, default=os.path.join(ROOT, "./data/euler.ped"))
parser.add_argument("--input", type=str, default=None)
parser.add_argument("--output", type=str, default="./output_data/result.json")

args = parser.parse_args()
input_file = args.input
output_file = args.output



print(f"Loading problem description and solution...")
with open(args.problem, "r") as f:
    desc_str = f.read()
    problems = parse(desc_str)
with open(os.path.join(ROOT, input_file), "r") as f:
    solutions = json.load(f)

print(f"Loading project templates...")
single_file_templates = {}
for lang in cur_langs:
    single_file_templates[lang] = ProjectTemplate(os.path.join(ROOT, "./project-templates/single-file", lang))


def evaluate(name, lang, problem, solution, single_file_template):
    single_file_codes = gen_codes_for_single_file(lang=lang, problem=problem, target_code=solution)
    single_file_proj = create_project(single_file_template, f"{name}-sf", single_file_codes,
                                      root=os.path.join(ROOT, ".polyeval/"), overwrite=True)
    ret_stat, msg = single_file_proj.evaluate(compile_timeout=20, run_timeout=20, keep_when_fail=True)
    if ret_stat == EvalStatus.Pass:
        return True, ret_stat.name
    return False, ret_stat.name


results = {}

for model_name in solutions:
    for src_lang in solutions[model_name]:
        for tgt_lang in solutions[model_name][src_lang]:
            assert len(solutions[model_name][src_lang][tgt_lang]) == 50
            for i in range(50):
                solution = solutions[model_name][src_lang][tgt_lang][i]
                problem = list(problems.values())[i]
                name = f"{model_name}-{src_lang}-{tgt_lang}-{i}"
                ret, stat_name = evaluate(name, tgt_lang, problem, solution, single_file_templates[tgt_lang])
                if not ret:
                    print(f"{name} Failed: {stat_name}")
                if model_name not in results:
                    results[model_name] = {}
                if src_lang not in results[model_name]:
                    results[model_name][src_lang] = {}
                if tgt_lang not in results[model_name][src_lang]:
                    results[model_name][src_lang][tgt_lang] = [None for _ in range(50)]
                results[model_name][src_lang][tgt_lang][i] = stat_name

with open(output_file, "w") as f:
    json.dump(results, f, indent=4)