import pandas as pd
import matplotlib.pyplot as mpl

# Créer et renvoie un tableau à partir d'un CSV récupérer à l'adresse "url"
def get_tab(url):
    df = pd.read_csv(url, sep=";")
    df = df[['Date de début','Polluant','valeur brute']][df["nom site"]=="VITRY-SUR-SEINE"][df["Polluant"] != "SO2"]         
    df = pd.pivot_table(df, values='valeur brute',columns='Polluant',index='Date de début')
    return(df)

def print_graph(df):
    df.plot()
    mpl.show()
    
def print_specific(df, col):
    df[col].plot()
    mpl.show()
    
def print_each_column(df):
    axes = mpl.subplot(nrows=3, ncols=2)
    df["NO"].plot(ax=axes[0,0])
    df["NO2"].plot(ax=axes[0,1])
    df["O3"].plot(ax=axes[1,0])
    df["NOX as NO2"].plot(ax=axes[1,1])
    df["PM10"].plot(ax=axes[2,0])
    df["PM2.5"].plot(ax=axes[2,1])
    mpl.show(axes)
    
    