import re
import matplotlib.pyplot as plt
import numpy as np
import json


# def parse_integers(filename):
#     regex = '0\.[0-9]*'
#     numbers = []
#     with open(filename) as f:
#         lines = [line for line in f]
    
#     for line in lines:
#         numbers.extend(re.findall(regex, line))

#     return [float(n) for n in numbers]


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
    

def export_json(filename, parse_type, targets):
    data = {}
    if parse_type == 'float':
        # Random number generation from [0,1)
        for target in targets:
            data[target] = parse_floats(target)

    with open(filename, 'w') as f:
        json.dump(data, f)


# histogram(numbers, '01_llama7b_results_autoreg.png', "Llama 7B model (Autoregressive)")


targets = [
    '01_llama7b_temp12_results_oneshot.txt',
    '01_llama7b_temp15_results_oneshot.txt',
    '01_llama13b_temp12_results_oneshot.txt',
    '01_llama13b_temp15_results_oneshot.txt',
    '01_llama7b_temp12_results_autoreg.txt',
    '01_llama7b_temp15_results_autoreg.txt',
    '01_llama13b_temp12_results_autoreg.txt',
    '01_llama13b_temp15_results_autoreg.txt',
]
export_json('llama_with_temperature.json', 'float', targets)
