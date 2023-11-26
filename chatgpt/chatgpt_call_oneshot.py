from openai import OpenAI
import json
import re

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

n_trial = 200

messages = [ {"role": "user", "content": "Give me a list of uniform random numbers in the interval [0, 1]:"} ]
responses = []
for i in range(n_trial):
    if i % 50 == 0:
        print(f"{i}th term")
    chat_completion = client.chat.completions.create(
        messages=messages,
        # temperature=2,
        model="gpt-3.5-turbo",
    )
    reply = chat_completion.choices[0].message.content
    print(reply)
    with open("01_chatgpt35_results.txt", "a") as f: 
        f.writelines(reply+'\n')
