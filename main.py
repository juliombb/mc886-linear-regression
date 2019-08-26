import numpy as np

if __name__ == '__main__':
    dataset = np.recfromtxt(
        'Metro_Interstate_Traffic_Volume.csv',
        delimiter='\t', dtype=str
    )
    print(dataset)
    dataset2 = []
    for d in dataset:
        print(d.split(','))
        dataset2.append(d.split(',')[5])

    print(set(dataset2))