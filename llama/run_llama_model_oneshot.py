'''
https://medium.com/@penkow/how-to-run-llama-2-locally-on-cpu-docker-image-731eae6398d1
'''

from llama_cpp import Llama

# Put the location of to the GGUF model that you've download from HuggingFace here
# model_path = "llama-2-7b-chat.Q2_K.gguf"
# model_path = "llama-2-13b-chat.Q2_K.gguf"

# Create a llama model
# model = Llama(model_path=model_path)

# max_list = [10,100]
# max_list = [1000,10000,100000]
# n_trial = 200
# results = {}

# for n_max in max_list:
#     # Prompt creation
#     system_message = ""
#     user_message = f"Pick a random number from 1-{n_max}."
#     prompt = f"""<s>[INST] <<SYS>>
#     {system_message}
#     <</SYS>>
#     {user_message} [/INST]"""
#     # Model parameters
#     max_tokens = 100

#     responses = []
#     for i in range(n_trial):
#         # Run the model
#         output = model(prompt, max_tokens=max_tokens, echo=True)
#         reply = output['choices'][0]['text'].split('[/INST]')[1]
#         random_n = re.findall(r'\d+', reply)
#         if random_n:
#             responses.append(int(random_n[0]))

#     results[n_max] = responses
#     print(n_max)
#     print(responses)

# model_path = "llama-2-7b-chat.Q2_K.gguf"
model_path = "llama-2-13b-chat.Q2_K.gguf"

# Create a llama model
model = Llama(model_path=model_path)
n_trial = 200

system_message = ""
user_message = f"Give me a list of uniform random numbers in the interval [0, 1]:"
# user_message = f"Pick random number from 1 to 10"
prompt = f"""<s>[INST] <<SYS>>
{system_message}
<</SYS>>
{user_message} [/INST]"""
# Model parameters
max_tokens = 100
result_file = "01_llama13b_temp15_results_oneshot.txt"
temperature=1.5

# responses = []
for i in range(n_trial):
    if i % 10 == 0:
        print(f"{i}th term")
    # Run the model
    output = model(prompt, max_tokens=max_tokens, echo=True, temperature=temperature)
    reply = output['choices'][0]['text'].split('[/INST]')[1]
    print(reply)
    with open(result_file, "a") as f: 
        f.writelines(reply+'\n')
    # random_n = re.findall(r'\d+', reply)
    # if random_n:
    #     responses.append(int(random_n[0]))

# print(responses)

# with open("01_llama_results.json", "a") as f: 
#     json.dump(responses, f)
