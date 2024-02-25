import pandas as pd

df = pd.read_csv("insurance.csv")
print(df['sex'].unique())

sex_map = {
    'female':0,
    'male':1
}
smoker_map = {
    'no':0,
    'yes':1
}
df['smoker']=df['smoker'].map(smoker_map)

regian_encodes =pd.get_dummies(df, columns=['region'], dtype=int)
df = pd.concat([df, regian_encodes],axis=1)
df = df.drop(['region'],axis=1)

print(df.head())

df.to_csv('ready_insurance.csv',index=False)