import pandas as pd
from xgboost import XGBClassifier
import pickle

# load dataset
data = pd.read_csv("dataset/aqua_sentinel_clean.csv")

# rename columns for easier handling
data = data.rename(columns={
"ITS-90 water temperature [degrees C]":"temperature",
"Water body pH [pH units]":"ph",
"Water body chlorophyll-a [mg/m^3]":"chlorophyll",
"Water body dissolved oxygen concentration [umol/l]":"oxygen"
})

# remove rows without required values
data = data.dropna(subset=["temperature","ph","chlorophyll","oxygen"])

# create algae bloom label
data["algal_bloom"] = (data["chlorophyll"] > 15).astype(int)

# features
X = data[["temperature","ph","oxygen"]]

# target
y = data["algal_bloom"]

# train model
model = XGBClassifier()
model.fit(X,y)

# save model
pickle.dump(model,open("ml/model.pkl","wb"))

print("Model trained successfully")