import re
import matplotlib.pyplot as plt
import numpy as np
import json

def parse_floats(filename):
    regex = '0\.[0-9]*'
    numbers = []
    with open(filename) as f:
        lines = [line for line in f]
    
    for line in lines:
        numbers.extend(re.findall(regex, line))

    return [float(n) for n in numbers]


def histogram(numbers, imagefile, title):
    counts, bins = np.histogram(numbers)
    plt.stairs(counts, bins)
    plt.title(title)
    plt.savefig(imagefile)


# histogram(parse_floats('01_chatgpt35_results_autoreg.txt'), '01_chatgpt35_results_autoreg.png', 'ChatGPT 3.5 turbo model (Autoregressive)')
# Random number generation from [0,1)

numbers_35_oneshot = parse_floats('01_chatgpt35_results_oneshot.txt')
numbers_35_autoreg = parse_floats('01_chatgpt35_results_autoreg.txt')
numbers_4_oneshot = parse_floats('01_chatgpt4_results_oneshot.txt')
numbers_4_autoreg = parse_floats('01_chatgpt4_results_autoreg.txt')

data = {}
data['chatgpt35_oneshot'] = numbers_35_oneshot
data['chatgpt35_autoreg'] = numbers_35_autoreg
data['chatgpt4_oneshot'] = numbers_4_oneshot
data['chatgpt4_autoreg'] = numbers_4_autoreg

with open('chatgpt.json', 'w') as f:
    json.dump(data, f)
