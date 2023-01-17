import lib

url = "https://files.data.gouv.fr/lcsqa/concentrations-de-polluants-atmospheriques-reglementes/temps-reel/2022/FR_E2_2022-01-01.csv"

limits = {'limite NO': 30 ,'limite NO2': 40, 'limite O3': 120, 'limite NOX as NO2': 30, 'limite PM10': 50, 'limite PM2.5': 25}
#liste_polluants = ["NO","NO2","O3","NOX as NO2","PM10","PM2.5"]

df = lib.get_tab(url)
lib.print_graph_with_limits(df)