#exercice1
import pandas as pd 
df = pd.read_csv("dataset_heart.csv")
df.columns
X= df.drop("heart disease" , axis= "columns")
y = df["heart disease"]
df.columns = df.columns.str.strip()
from sklearn import pipeline
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
df.info()
df.describe()

df.isna().sum()
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x=y)
#exercice 2  logistic regerssion sans grid search cv
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
from sklearn.linear_model import LogisticRegression
lgr = LogisticRegression()
lgr.fit(X_train_scaled , y_train)
lgr.score(X_test_scaled , y_test)
prd = lgr.predict(X_test_scaled)
from sklearn.metrics import accuracy_score , confusion_matrix
import seaborn as sns
accuracy = accuracy_score(y_test, prd)
cm = confusion_matrix(y_test, prd)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')

#exercice 3 logistic regerssion avec grid search cv
from sklearn.pipeline import Pipeline

pipeline =Pipeline([
    ("scaler", StandardScaler()),
    ("logreg", LogisticRegression())
])
param_grid = {
    "logreg__C": [0.01, 0.1, 1, 10, 100],
    "logreg__penalty": ["l1", "l2"],
    "logreg__solver": ["liblinear"]
}
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)
grid.fit(X_train, y_train)
grid.best_params_   
grid.best_score_
grid.score(X_test, y_test)
prd_grid = grid.predict(X_test)

accuracy_grid = accuracy_score(y_test, prd_grid)
cm_grid = confusion_matrix(y_test, prd_grid)    
plt.figure(figsize=(6,4))
sns.heatmap(cm_grid, annot=True, fmt='d', cmap='Blues')
#exercice 4 SVM sans grid search cv
from sklearn.svm import SVC
svm = SVC()
svm.fit(X_train_scaled , y_train)
svm.score(X_test_scaled , y_test)
prd_svm = svm.predict(X_test_scaled)
accuracy_svm = accuracy_score(y_test, prd_svm)
cm_svm = confusion_matrix(y_test, prd_svm)
plt.figure(figsize=(6,4))   
sns.heatmap(cm_svm, annot=True, fmt='d', cmap='Blues')
#exercice 5 SVM avec grid search cv
pipeline_svm =Pipeline([
    ("scaler", StandardScaler()),
    ("svm", SVC())
])
param_grid_svm = {
    "svm__C": [0.1, 1, 10, 100],
    "svm__kernel": ["linear", "rbf", "poly"],
    "svm__gamma": ["scale", "auto"]
}
grid_svm = GridSearchCV(
    pipeline_svm,
    param_grid_svm,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)
grid_svm.fit(X_train, y_train)
grid_svm.best_params_   
grid_svm.best_score_
grid_svm.score(X_test, y_test)
prd_grid_svm = grid_svm.predict(X_test)
accuracy_grid_svm = accuracy_score(y_test, prd_grid_svm)
cm_grid_svm = confusion_matrix(y_test, prd_grid_svm)
plt.figure(figsize=(6,4))
sns.heatmap(cm_grid_svm, annot=True, fmt='d', cmap='Blues')
#exercice 6 XGBoost sans recherche par grille
from xgboost import XGBClassifier
y_train.unique()
y_train = y_train.map({1: 0, 2: 1})
y_test  = y_test.map({1: 0, 2: 1})
xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
xgb.fit(X_train, y_train)
xgb.score(X_test, y_test)
prd_xgb = xgb.predict(X_test)
accuracy_xgb = accuracy_score(y_test, prd_xgb)
cm_xgb = confusion_matrix(y_test, prd_xgb)
plt.figure(figsize=(6,4))
sns.heatmap(cm_xgb, annot=True, fmt='d', cmap='Blues')
#exercice 7 XGBoost avec recherche par grille
pipeline_xgb =Pipeline([
    ("xgb", XGBClassifier(use_label_encoder=False, eval_metric='logloss'))
])
param_grid_xgb = {
    "xgb__n_estimators": [50, 100, 200],
    "xgb__max_depth": [3, 5, 7],
    "xgb__learning_rate": [0.01, 0.1, 0.2]
}
grid_xgb = GridSearchCV(
    pipeline_xgb,
    param_grid_xgb, 
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)
grid_xgb.fit(X_train, y_train)
grid_xgb.best_params_
grid_xgb.best_score_
grid_xgb.score(X_test, y_test)
prd_grid_xgb = grid_xgb.predict(X_test)
accuracy_grid_xgb = accuracy_score(y_test, prd_grid_xgb)
cm_grid_xgb = confusion_matrix(y_test, prd_grid_xgb)
plt.figure(figsize=(6,4))
sns.heatmap(cm_grid_xgb, annot=True, fmt='d', cmap='Blues')
