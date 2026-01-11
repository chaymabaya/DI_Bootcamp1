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
#Section 1
import pandas as pd
try:
    df = pd.read_csv('air_traffic_data.csv')
    print("Dataset loaded successfully!")
    print(f"Shape: {df.shape}")
except FileNotFoundError:
    print("Creating sample air traffic data...")
    np.random.seed(42)
    n_samples = 200
    dom_flights = np.random.normal(15000, 3000, n_samples)
    int_flights = np.random.normal(8000, 2000, n_samples)
    dom_pax = dom_flights * np.random.normal(12, 2, n_samples) + np.random.normal(0, 10000, n_samples)
    int_pax = int_flights * np.random.normal(15, 3, n_samples) + np.random.normal(0, 15000, n_samples)
    dom_rpm = dom_pax * np.random.normal(800, 100, n_samples)
    dom_flights = np.abs(dom_flights)
    int_flights = np.abs(int_flights)
    dom_pax = np.abs(dom_pax)
    int_pax = np.abs(int_pax)
    dom_rpm = np.abs(dom_rpm)
    df = pd.DataFrame({
        'Dom_Flt': dom_flights.astype(int),
        'Int_Flt': int_flights.astype(int),
        'Flt': (dom_flights + int_flights).astype(int),
        'Dom_Pax': dom_pax.astype(int),
        'Int_Pax': int_pax.astype(int),
        'Pax': (dom_pax + int_pax).astype(int),
        'Dom_RPM': dom_rpm.astype(int)
    })
    print("Sample data created successfully!")
    print(f"Shape: {df.shape}")
#Section 2
df.head()
df.info()
df.describe()
df.isnull().sum()
corr_matrix = df.corr()
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Matrice de corrélation")
plt.show()

#Section 3
from scipy import stats
t_stat, p_value_ttest = stats.ttest_ind(df['Dom_Pax'], df['Int_Pax'])
df['Total_Flights'] = df['Dom_Flt'] + df['Int_Flt']
df['Total_Pax'] = df['Dom_Pax'] + df['Int_Pax']
corr_coef, p_value_corr = stats.pearsonr(df['Total_Pax'], df['Total_Flights'])
#test1
alpha = 0.05

if p_value_ttest < alpha:
    print("Décision : Rejet de H₀")
    print("Conclusion : Différence significative entre les passagers nationaux et internationaux")
else:
    print("Décision : On ne rejette pas H₀")
    print("Conclusion : Pas de différence significative")

#Test 2
if p_value_corr < alpha:
    print("Décision : Rejet de H₀")
    print("Conclusion : Corrélation significative")
else:
    print("Décision : On ne rejette pas H₀")
    print("Conclusion : Corrélation non significative")
#Section 4
X = df[['Total_Flights']]
y = df['Total_Pax']
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
intercept = model.intercept_
coef = model.coef_[0]
y_pred = model.predict(X_test)
R2 = r2_score(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)
MAE = mean_absolute_error(y_test, y_pred)

plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred)
plt.xlabel("Total Flights")
plt.ylabel("Total Passengers")
plt.title("Régression linéaire : Total Flights vs Total Passengers")
plt.show()

residuals = y_test - y_pred
plt.scatter(y_pred, residuals)
plt.axhline(0)
plt.xlabel("Valeurs prédites")
plt.ylabel("Résidus")
plt.title("Graphique des résidus")
plt.show()

#Section 5
X = df[['Dom_Pax', 'Int_Pax', 'Dom_Flt', 'Int_Flt', 'Dom_RPM']]
y = df['Pax']
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)  
X_test_scaled = scaler.transform(X_test) 
model_multi = LinearRegression()
model_multi.fit(X_train_scaled, y_train)
y_pred_multi =model_multi.predict(X_test_scaled)
R2_multi = r2_score(y_test, y_pred_multi)
MSE_multi = mean_squared_error(y_test, y_pred_multi)
RMSE_multi = np.sqrt(MSE_multi)
MAE_multi = mean_absolute_error(y_test, y_pred_multi)
coefficients = pd.DataFrame({
    'Variable': X.columns,
    'Coefficient': model_multi.coef_
})

#Section 6

performance_simple = {
    'R2': R2,
    'RMSE': RMSE,
    'MAE': MAE
}


performance_multiple = {
    'R2': R2_multi,
    'RMSE': RMSE_multi,
    'MAE': MAE_multi
}
comparison_df = pd.DataFrame([performance_simple, performance_multiple],index=['Simple', 'Multiple'])
best_model = 'Multiple' if (R2_multi > R2 and RMSE_multi < RMSE and MAE_multi < MAE) else 'Simple'
print("Le modèle le plus performant :", best_model)
improvement_rmse = (RMSE - RMSE_multi) / RMSE * 100
improvement_mae = (MAE - MAE_multi) / MAE * 10
improvement_r2 = (R2_multi - R2) / R2 * 100
comparison_df.plot(kind='bar', figsize=(8,5), title='Comparaison des modèles')


#Section 7 
# resume : 
# L’analyse démontre une relation significative entre le nombre de vols et le nombre de passagers.                            
#  Les modèles de régression permettent de prédire la demande et améliorer la planification.
#Les résultats statistiques sont cohérents avec les décisions opérationnelles réelles, offrant un outil pratique pour la stratégie aérienne.

#Section 8  Questions de réflexion
#Q 1 Que révèlent les résultats des tests d'hypothèses sur les schémas de trafic aérien
   # Test 1 (passagers nationaux vs internationaux) :
   # Résultat : p-value < 0.05 → différence significative
   # Interprétation : le trafic national et international ne suit pas le même schéma → certaines périodes ou lignes sont plus occupées à l’international ou à l’intérieur du pays.
   # Test 2 (corrélation Total_Pax vs Total_Flights) :
   # Corrélation positive et significative → plus de vols entraînent plus de passager

# Q2 Pourquoi un modèle de régression a-t-il été plus performant que l'autre
   # Régression simple : un seul prédicteur (Total_Flights) → bonne approximation mais limité
   # Régression multiple : plusieurs variables (Dom_Pax, Int_Pax, Dom_Flt, Int_Flt, Dom_RPM) → capte plus de facteurs influents
   # Résultat :
   # R² plus élevé
   # RMSE et MAE plus faible

#Q3 Comment les compagnies aériennes peuvent-elles utiliser les informations de corrélation de manière opérationnelle ?
   #Identifier les variables qui influencent le plus le nombre de passagers (ex : Dom_RPM, Dom_Pax)
   # Planification des vols : augmenter la fréquence sur les lignes avec forte corrélation
   # Gestion des ressources : allocation de personnel et avions selon la demande prévue
   #Prévision saisonnière : ajuster le calendrier des vols en fonction des périodes de forte affluence
#Q4️ Que nous apprennent les graphiques de résidus sur les hypothèses du modèle ?
   #es résidus aléatoires et dispersés indiquent :
   # Relation linéaire adéquate
   # Variance constante (homoscédasticité)
   # Pas de motifs → modèle correct
#Q5️ Quelles sont les applications pratiques de ces modèles statistiques ?
   # Décision stratégique : quelles lignes augmenter ou diminuer
   # Planification des ressources : personnel, avions, carburant
   # Analyse de rentabilité : comprendre quelles lignes rapportent le plus
   # Support à la planification saisonnière et événements spéciaux (vacances, festivals)


 
