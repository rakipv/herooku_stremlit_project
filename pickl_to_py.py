import pickle as pkl
import pandas as pd

with open("R:/react_voice/chritograph_recommendation/data/movie_dict.pkl", "rb") as f:
    object1 = pkl.load(f)

df = pd.DataFrame(object1)
df.to_csv(r'file.csv')