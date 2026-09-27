import numpy as np
import pandas as pd

data = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)
