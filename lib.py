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

def print_graph_with_limits(df, limits):
    lim = pd.DataFrame(limits)
    plot = df.plot()
    limits.plot(style='--', ax=plot)
    mpl.show(plot)