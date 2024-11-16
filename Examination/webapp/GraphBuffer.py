
import numpy as np
import matplotlib.pyplot as plt
import sys
import random
from io import BytesIO
import base64


def generate_bar_graph(values, yl='Metrics', tit="Perfomance Graph",categories=('Accuracy','Precision\nScore','Recall\nScore','F1\nScore')):
    categories = categories
    values = values

    colors = ['#{:06x}'.format(random.randint(0, 0xFFFFFF)) for _ in range(len(categories))]
    plt.bar(categories, values, color=colors)
    plt.xlabel('')
    plt.ylabel(yl)
    plt.title(tit)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Convert the plot to base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return image_base64
