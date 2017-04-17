import numpy as np
import pandas as pd
import math


ataqueCardiaco = pd.read_csv("ataque_cardiaco.csv").as_matrix()

ac10primeiros = ataqueCardiaco[:10]



print(ac10primeiros)
