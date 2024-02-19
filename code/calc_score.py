import json

scores = {}

sources = ["python", "go", "goii", "ges","gesii", "ges-pre", "ges-post", "ges-prepkg", "pythona", "pythonb"]

targets = ["cpp", "csharp", "java", "javascript", "kotlin", "php", "ruby", "rust", "scala"] 

# targets = ["java"] 


with open("./result/mytest_gesnew_temp_0.2_4.json") as f:
    results = json.load(f)
    for model in results:
        scores[model] = {}
        for src in results[model]:
            if src not in sources:
                continue
            scores[model][src] = 0
            for tgt in results[model][src]:
                if tgt not in targets:
                    continue
                for i in range(len(results[model][src][tgt])):
                    if results[model][src][tgt][i]:
                        scores[model][src] += 1

print(scores)

# scores = {}

# with open("./result/mytest.json") as f:
#     results = json.load(f)
#     for model in results:
#         for src in results[model]:
#             if src not in scores:
#                 scores[src] = {}
#             for tgt in results[model][src]:
#                 if tgt not in scores[src]:
#                     scores[src][tgt] = 0
#                 for i in range(len(results[model][src][tgt])):
#                     if results[model][src][tgt][i]:
#                         scores[src][tgt] += 1

# print(scores)