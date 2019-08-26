import numpy as np

if __name__ == '__main__':
    dataset = np.recfromtxt(
        'Metro_Interstate_Traffic_Volume.csv',
        delimiter='\t', dtype=str
    )

    print(dataset)