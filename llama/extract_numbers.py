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

# histogram(numbers, '01_llama7b_results_autoreg.png', "Llama 7B model (Autoregressive)")

# Random number generation from [0,1)
numbers_7b_oneshot = parse_floats('01_llama7b_results_oneshot.txt')
numbers_7b_autoreg = parse_floats('01_llama7b_results_autoreg.txt')
numbers_13b_oneshot = parse_floats('01_llama13b_results_oneshot.txt')
numbers_13b_autoreg = parse_floats('01_llama13b_results_autoreg.txt')

data = {}
data['llama_7b_oneshot'] = numbers_7b_oneshot
data['llama_7b_autoreg'] = numbers_7b_autoreg
data['llama_13b_oneshot'] = numbers_13b_oneshot
data['llama_13b_autoreg'] = numbers_13b_autoreg

with open('llama.json', 'w') as f:
    json.dump(data, f)
