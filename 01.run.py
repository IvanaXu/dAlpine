# python 3.10
n = 0

try:
    import pandas as pd
    print(pd)
except:
    n += 1
    print("ERROR pd")

try:
    import numpy as np
    print(np)
except:
    n += 1
    print("ERROR np")

try:
    from tqdm import tqdm
    print(tqdm)
except:
    n += 1
    print("ERROR tqdm")

try:
    import sklearn
    print(sklearn)
except:
    n += 1
    print("ERROR sklearn")

try:
    import jieba
    print(jieba)
except:
    n += 1
    print("ERROR jieba")

try:
    import gensim
    print(gensim)
except:
    n += 1
    print("ERROR gensim")
print("END", n)
