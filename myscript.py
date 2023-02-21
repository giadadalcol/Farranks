import pandas as pd

golf_players = pd.read_csv("Dataset/Golf_players.csv")
print(golf_players.summary())
