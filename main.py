import pandas as pd

df = pd.read_csv("dataset/aqua_sentinel_clean.csv")

# Drop first 3 columns safely
df = df.iloc[:, 3:]

df = df.drop(columns=[
    "yyyy-mm-ddThh:mm:ss.sss",
    "Longitude [degrees_east]",
    "Latitude [degrees_north]"
], errors="ignore")

df.replace(9, pd.NA, inplace=True)

df = df.dropna(subset=["Water body chlorophyll-a [mg/m^3]"])

# print(df.head())

# print(df.describe())
# print(df.isna().sum())

df = df[
    (df["ITS-90 water temperature [degrees C]"] < 50) &
    (df["Water body salinity [per mille]"] < 50) &
    (df["Water body dissolved oxygen concentration [umol/l]"] < 500)
]

df["Water body chlorophyll-a [mg/m^3]"].describe()