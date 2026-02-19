import pandas as pd

df = pd.read_csv("can_data.csv")

# CONVERTING UNIX NUMBERS INTO HUMAN REDABLE DATA (TIMESTAMPS)
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

# REMOVING PRESSURE TYPE AND TEMP TYPE
df = df.drop(["Pressure Type", "Temp Type"], axis=1)

# FIND THE MEAN OF ALL COLUMNS
df = df.fillna(df.mean())
