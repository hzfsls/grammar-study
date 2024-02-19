import json

with open("./data/euler_sig.json", "r") as f:
    euler_sig = json.load(f)

with open("./data/euler_sol.json", "r") as f:
    euler_sol = json.load(f)

with open("./data/example_sig.json", "r") as f:
    example_sig = json.load(f)

langs = ["Python", "C++", "C#", "Go", "Java", "JavaScript", "Kotlin", "PHP", "Ruby", "Rust", "Scala"]

langs_name = {
    "Python": "python",
    "C++": "cpp",
    "C#": "csharp",
    "Go": "go",
    "Java": "java",
    "JavaScript": "javascript",
    "Kotlin": "kotlin",
    "PHP": "php",
    "Ruby": "ruby",
    "Rust": "rust",
    "Scala": "scala",
}

example_sol = {}

example_sol_1 = {}

for lang in langs:
    lang_name = langs_name[lang]
    fname = f"./data/example/example_sol_{lang_name}_i.json"
    with open(fname, "r") as f:
        example_sol[lang_name] = json.load(f)[lang_name]

for lang in langs:
    lang_name = langs_name[lang]
    if lang != "Go":
        fname = f"./data/example/example_sol_{lang_name}_fn.json"
    else:
        fname = f"./data/example/example_sol_{lang_name}_i.json"
    with open(fname, "r") as f:
        example_sol_1[lang_name] = json.load(f)

def gen_translation_signature(src_lang, tgt_lang):
    src_lang_name = langs_name[src_lang]
    tgt_lang_name = langs_name[tgt_lang]
    src_example_sol = example_sol[src_lang_name]
    tgt_example_sig = example_sig[tgt_lang_name]
    tgt_example_sol = example_sol[tgt_lang_name]

    length = len(src_example_sol)
    assert length == len(tgt_example_sig) == len(tgt_example_sol) == 2
    messages = []
    for k, src_sol in src_example_sol.items():
        tgt_sig = tgt_example_sig[k]
        tgt_sol = tgt_example_sol[k]
        user_txt = f"""\
Translate the following {src_lang} code to {tgt_lang}:
```{src_lang_name}
{src_sol}
```
with this signature:
```{tgt_lang_name}
{tgt_sig}
```"""
        assistant_txt = f"""\
Sure, here is the translated {tgt_lang} code:
```{tgt_lang_name}
{tgt_sol}
```"""
        messages.append({"role": "user", "content": user_txt})
        messages.append({"role": "assistant", "content": assistant_txt})
    
    src_codes = euler_sol[src_lang_name]
    tgt_sigs = euler_sig[tgt_lang_name]

    prompts = []

    assert len(src_codes) == len(tgt_sigs)

    for k, src_sol in src_codes.items():
        
        messages1 = messages.copy()

        assert k in tgt_sigs
        tgt_sig = tgt_sigs[k]
        user_txt = f"""\
Translate the following {src_lang} code to {tgt_lang}:
```{src_lang_name}
{src_sol}
```
with this signature:
```{tgt_lang_name}
{tgt_sig}
```"""
        assistant_txt = f"""\
Sure, here is the translated {tgt_lang} code:
```{tgt_lang_name}
"""
        messages1.append({"role": "user", "content": user_txt})
        messages1.append({"role": "assistant", "content": assistant_txt})
        prompts.append({
            "task_id": k,
            "messages": messages1
        })
    
    return prompts

def chat_to_completion(prompts):
    new_prompts = []
    for prompt in prompts:
        messages = prompt["messages"]
        new_prompt = ""
        for message in messages:
            if message["role"] == "user":
                new_prompt += f"User: {message['content']}\n\n"
            elif message["role"] == "assistant":
                new_prompt += f"Assistant: {message['content']}\n\n"
        new_prompts.append(new_prompt.strip()+'\n')
    return new_prompts

all_prompts = {}

for src_lang in langs:
    for tgt_lang in langs:
        if src_lang != tgt_lang:
            prompts = gen_translation_signature(src_lang, tgt_lang)
            new_prompts = chat_to_completion(prompts)

            src_lang_name = langs_name[src_lang]
            tgt_lang_name = langs_name[tgt_lang]

            if src_lang_name not in all_prompts:
                all_prompts[src_lang_name] = {}
            all_prompts[src_lang_name][tgt_lang_name] = new_prompts

with open("./data/translation_prompts.json", "w") as f:
    json.dump(all_prompts, f, indent=2)