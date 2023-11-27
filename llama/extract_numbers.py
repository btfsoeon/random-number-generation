import re
import matplotlib.pyplot as plt
import numpy as np

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


# Random number generation from [0,1)
histogram(parse_floats('01_llama7b_results_autoreg.txt'), '01_llama7b_results_autoreg.png', "Llama 7B model (Autoregressive)")
