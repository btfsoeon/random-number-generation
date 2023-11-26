import matplotlib.pyplot as plt
import numpy as np
import json

def plot_frequency(json_data, title):
    i, size = 0, len(json_data)
    fig, axes = plt.subplots(size, 1, constrained_layout=True)
    for jd in json_data:
        counts, bins = np.histogram(json_data[jd])
        axes[i].stairs(counts, bins)
        axes[i].set_title(f"Random number generation from 1-{jd}")
        i += 1
    fig.supylabel("frequency")
    fig.set_figwidth(10)
    fig.set_figheight(12)
    plt.savefig(title)


with open('temp_0.8_results.json') as f:
    data = json.load(f)

plot_frequency(data, 'temp_0.8_chatgpt_results.png')
