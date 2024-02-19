from polyeval.parsing import parse
from polyeval.eval import (
    ProjectTemplate,
    EvalStatus,
    gen_codes,
    gen_codes_for_single_file,
    create_project,
)

from tqdm import tqdm
import sys
import os
import argparse
import json

from typing import List

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    "typescript": "ts",
}

cur_langs = langs

parser = argparse.ArgumentParser()
parser.add_argument("--problem", type=str, default=os.path.join(ROOT, "./data/euler.ped"))
parser.add_argument("--input", type=str, default=None)
parser.add_argument("--output", type=str, default=None)
parser.add_argument("--lang", type=str, default=None)
parser.add_argument("--idx", type=int, nargs="+", default=None)

args = parser.parse_args()
if args.lang is not None:
    if args.lang not in langs:
        raise Exception(f"Language not supported: {args.lang}")
    cur_langs = [args.lang]

print(f"Loading problem description and solution...")
with open(args.problem, "r") as f:
    desc_str = f.read()
    problems = parse(desc_str)
with open(args.input, "r") as f:
    solutions = json.load(f)

print(f"Loading project templates...")
single_file_templates = {}
for lang in cur_langs:
    print(f"Loading {lang} single file ...")
    single_file_templates[lang] = ProjectTemplate(
        os.path.join(ROOT, "./project-templates/single-file", lang)
    )


def evaluate(lang, problem, solution, single_file_template):
    p_name = problem.name.replace("/", "_")
    single_file_codes = gen_codes_for_single_file(
        lang=lang, problem=problem, target_code=solution
    )
    single_file_proj = create_project(
        single_file_template,
        f"{lang}-{p_name}-sf",
        single_file_codes,
        root=os.path.join(ROOT, ".polyeval/"),
        overwrite=True,
    )
    ret_stat, msg = single_file_proj.evaluate(
        compile_timeout=10, run_timeout=10, keep_when_fail=True
    )
    if ret_stat == EvalStatus.Pass:
        return True, ret_stat.name
    return False, ret_stat.name


res = {}

for model_name in solutions:
    for src_lang in solutions[model_name]:
        for tgt_lang in solutions[model_name][src_lang]:
            assert len(solutions[model_name][src_lang][tgt_lang]) == 50
            for i in range(50):
                solution = solutions[model_name][src_lang][tgt_lang][i]
                problem = list(problems.values())[i]
                name = f"{model_name}-{src_lang}-{tgt_lang}-{i}"

# for lang in cur_langs:
#     res[lang] = {}
#     for idx in tqdm(idxs):
#         problem = list(problems.values())[idx]
#         solution = solutions[lang][problem.name]
#         ret, stat_name = evaluate(lang, problem, solution, single_file_templates[lang])
#         if not ret:
#             print(f"{lang}-{problem.name} failed")
#         res[lang][problem.name] = stat_name


# with open(args.output, "w") as f:
#     json.dump(res, f, indent=4)
