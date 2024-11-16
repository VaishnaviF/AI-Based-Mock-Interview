import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import sys

def view(rlist):
    height=rlist
    bars = ('Accuracy','Precision\nScore','Recall\nScore','F1\nScore')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color=['brown','green','blue','orange'])
    plt.xticks(y_pos, bars)
    plt.xlabel('Algorithm Metrics')
    plt.ylabel('Accuracy')
    plt.title('CNN Algorithm Performance')
    plt.show()


