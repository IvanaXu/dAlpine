# python 3.10
try:
    import pandas as pd
    print(pd)
except:
    print("ERROR pd")

try:
    import numpy as np
    print(np)
except:
    print("ERROR np")

try:
    from tqdm import tqdm
    print(tqdm)
except:
    print("ERROR tqdm")

try:
    import sklearn
    print(sklearn)
except:
    print("ERROR sklearn")

try:
    import jieba
    print(jieba)
except:
    print("ERROR jieba")

try:
    import gensim
    print(gensim)
except:
    print("ERROR gensim")
print()
