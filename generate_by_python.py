import random
import matplotlib.pyplot as plt
import numpy as np

def generate_random_numbers():
    result = []
    n_trial = 2000
    for n in range(n_trial):
        result.append(random.random())
    return result

def histogram(numbers, imagefile, title):
    counts, bins = np.histogram(numbers)
    plt.stairs(counts, bins)
    plt.title(title)
    plt.savefig(imagefile)
    
histogram(generate_random_numbers(), '01_python_results_n2000.png', 'n=2000')
