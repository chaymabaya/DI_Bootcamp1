import pandas as pd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
data = pd.read_csv('air_traffic_data.csv')
data.head()
data.columns  
data.info()
data.describe()
data.isnull().sum()
data["Activity Period"] = pd.to_datetime(data["Activity Period"], format="%Y%m")
data['Year'] = data['Activity Period'].dt.year
data['Month_Num'] = data['Activity Period'].dt.month
data['Month_Name'] = data['Activity Period'].dt.strftime('%B')
df = data.drop(columns=['Month'])
months_order = ["January","February","March","April","May","June",
                "July","August","September","October","November","December"]
df['Month_Name'] = pd.Categorical(df['Month_Name'], categories=months_order, ordered=True)
df = df.sort_values('Month_Name')
df.describe()
df['Activity Period'].min()
df['Activity Period'].max()
df.isnull().sum()
df = df.dropna()
numeric_cols = df.select_dtypes(include='number')

corr = numeric_cols.corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')  
plt.title('Correlation Matrix')
plt.show()

from scipy import stats
cols = [
    "GEO Summary",
    "Passenger Count",
    "Adjusted Passenger Count"
]
df_test = df[cols].copy()
df_test.dropna(inplace=True)
df_test.head()
domestic = df_test[df_test["GEO Summary"] == "Domestic"]["Passenger Count"]
international = df_test[df_test["GEO Summary"] == "International"]["Passenger Count"]

domestic.shape
international.shape
t_stat, p_value = stats.ttest_ind(
    domestic,
    international,
    equal_var=False  
)

print("Statistique t:", t_stat)
print("p-value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("Rejet de H0 : différence significative entre Domestic et International")
else:
    print("Non-rejet de H0 : pas de différence significative")
df_corr = df.copy()
df_corr["Total_Flights"] = 1  
monthly_data = df_corr.groupby(
    ["Year", "Month_Num"]
).agg(
    total_passengers=("Adjusted Passenger Count", "sum"),
    total_flights=("Total_Flights", "sum")
).reset_index()

monthly_data.head()
r, p_value = stats.pearsonr(
    monthly_data["total_passengers"],
    monthly_data["total_flights"]
)

print("Coefficient de corrélation:", r)
print("p-value:", p_value)

if p_value < 0.05:
    print("Corrélation statistiquement significative")
else:
    print("Corrélation non significative")

#section 4 
df_reg = df.copy()
df_reg["total_flights"] = 1

monthly_data = df_reg.groupby(
    ["Year", "Month_Num"]
).agg(
    total_passengers=("Adjusted Passenger Count", "sum"),
    total_flights=("total_flights", "sum")
).reset_index()

monthly_data.head()

X = monthly_data[["total_flights"]]  
y = monthly_data["total_passengers"]  
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
lr = LinearRegression()
lr.fit(X_train, y_train)
lr.coef_
lr.intercept_
lr.score(X_test, y_test)
y_pred = lr.predict(X_test)
y = f"{lr.intercept_:.2f} + {lr.coef_[0]:.2f} × x"
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
plt.figure()
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred)
plt.xlabel("Nombre total de vols")
plt.ylabel("Nombre total de passagers")
plt.title("Régression linéaire : Vols vs Passagers")
plt.show()
  
