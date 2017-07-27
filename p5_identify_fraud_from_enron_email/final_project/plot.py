import matplotlib.pyplot as plt
import numpy as np

k = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
     11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ]

precision_score = [
                   0.222, 0.189, 0.282, 0.252, 0.255, 
                   0.265, 0.305, 0.284, 0.294, 0.289,
                   0.302, 0.292, 0.290, 0.290, 0.281, 
                   0.299, 0.287, 0.291, 0.284, 0.278
                  ]

recall_score = [
                0.147, 0.185, 0.309, 0.262, 0.274,
                0.273, 0.309, 0.286, 0.287, 0.281,
                0.292, 0.279, 0.276, 0.275, 0.262,
                0.281, 0.275, 0.276, 0.265, 0.265
               ]

accuracy = [
            0.818, 0.785, 0.803, 0.798, 0.796,
            0.802, 0.814, 0.809, 0.813, 0.812,
            0.816, 0.814, 0.813, 0.813, 0.813,
            0.816, 0.812, 0.814, 0.813, 0.810
           ]


plt.plot(k, accuracy, label='Accuracy', marker='o') 
plt.plot(k, recall_score, label='Recall', marker='o')
plt.plot(k, precision_score, label='Precision', marker='o'plot   plotttt)
plt.xlabel('Number of k best features')
plt.ylabel('Score')
plt.title('Accuracy, Precision, and Recall versus Number of K-best Features')
plt.axis([0, 21, 0, 1])
plt.xticks(np.arange(0, 21, 1.0))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)
plt.legend(loc='best', shadow=True)
plt.show()
