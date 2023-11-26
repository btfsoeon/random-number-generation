import re
import matplotlib.pyplot as plt
import numpy as np

def parse_floats(filename):
    regex = '0\.[0-9]*'
    numbers = []
    with open(filename) as f:
        lines = [line for line in f]
    
    for line in lines:
        result = re.findall(regex, line)
        print(result)
        numbers.extend(result)

    return numbers


def histogram(numbers, imagefile):
    counts, bins = np.histogram(numbers)
    plt.stairs(counts, bins)
    plt.title("Random number generation from [0,1)")
    plt.savefig(imagefile)


histogram(parse_floats('01_llama7b_results_autoreg.txt'), '01_llama7b_results_autoreg.png')
