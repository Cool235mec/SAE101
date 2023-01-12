from pandas import * 

s = '../FR_E2_2023-01-10.csv'

df = read_csv(s, sep=";")
print(df)
df_by_city = df[df["nom site"]=="VITRY-SUR-SEINE"]
for Pol in liste_polluants:
    df_by_gas = df_by_city[df_by_city["Polluant"]==""]