from openai import OpenAI
import json
import re
import random

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
    organization="org-etrIrRiqCGY9JJ8m6uwX3kcU",
)

# max_list = [10,100]
# max_list = [1000,10000,100000]
# n_trial = 200
# results = {}

# for n_max in max_list:
#     messages = [ {"role": "user", "content": f"Pick a random number from 1-{n_max}."} ]
#     responses = []
#     for i in range(n_trial):
#         if i % 50 == 0:
#             print(f"{i}th term")
#         chat_completion = client.chat.completions.create(
#             messages=messages,
#             temperature=2,
#             model="gpt-3.5-turbo",
#         )
#         reply = chat_completion.choices[0].message.content
#         random_n = re.findall(r'\d+', reply)
#         if random_n:
#             responses.append(int(random_n[0]))
    
#     results[n_max] = responses
#     print(n_max)
#     print(responses)

# print(results)

# with open("temp_2.0_results.json", "w") as f: 
#     json.dump(results, f)

result_file = "1_10_chatgpt35_range_results_oneshot.txt"
model = "gpt-3.5-turbo"
n_trial = 200

responses = []
for i in range(n_trial):
    if i % 10 == 0:
        print(f"{i}th term")
    
    prompt = 'The following is a list of uniform random numbers in the interval [1, 10]:\n'
    random.seed(i)
    synthetic_prompt_samples = [random.randint(6, 10) for _ in range(3)]
    for i, sample in enumerate(synthetic_prompt_samples):
        prompt += '{}. {}\n'.format(i + 1, sample)
    prompt += '{}.'.format(len(synthetic_prompt_samples) + 1)
    messages = [ {"role": "user", "content": prompt} ]
        
    chat_completion = client.chat.completions.create(
        messages=messages,
        # temperature=1.5,
        model=model,
    )
    reply = chat_completion.choices[0].message.content
    print(reply)
    # parse only the first number
    number = re.findall(r"\d+", reply)[0]
    
    with open(result_file, "a") as f: 
        f.writelines(number+'\n')
