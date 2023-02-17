from sklearn.datasets import load_digits

# 手書きデータをロードする
digits = load_digits()
print(digits.data.shape)

import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.gray()
plt.matshow(digits.images[0])
plt.show()
#plt.savefig('figure01.jpg')
