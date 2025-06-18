import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000
data = {
    "age": np.random.normal(40, 10, size=n),
    "income": np.random.normal(50000, 15000, size=n),
    "job": np.random.choice(["teacher", "engineer", "doctor", "artist"], size=n),
    "target": np.random.choice([0, 1], size=n),
}

df = pd.DataFrame(data)

# 결측치 넣기
df.loc[np.random.choice(n, 150, replace=False), "age"] = np.nan
df.loc[np.random.choice(n, 200, replace=False), "income"] = np.nan
df.loc[np.random.choice(n, 100, replace=False), "job"] = np.nan

df.to_csv("train.csv", index=False)
#test
