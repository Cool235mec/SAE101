from pandas import * 

s = '../FR_E2_2023-01-10.csv'

#liste_polluants = ["NO","NO2","O3","NOX as NO2","PM10","PM2.5"]

df = read_csv(s, sep=";")
df = df[['Date de début','Polluant','valeur brute']][df["nom site"]=="VITRY-SUR-SEINE"]
print(df)

#temp_df = df[df["Polluant"]=="NO"]
#dict_by_hour = {h: [] for h in temp_df["Date de début"]}

#for Pol in liste_polluants:
#    df_by_gas = df_by_city[df_by_city["Polluant"]=="Pol"]
#    for date in dict_by_hour.keys():
#        print(date)
#        print(str(df_by_gas["Date de début"]))
#        if date == df_by_gas["Date de début"]:
#            dict_by_hour[date].append(df["valeur brute"])
            
df = pivot_table(df, values='valeur brute',columns='Polluant',index='Date de début')
print(df)