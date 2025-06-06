import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
from ace_tools import display_dataframe_to_user

# Dados obtidos do dataset "company_sales_data.csv" (citado na resposta em texto)
csv_data = """Month,FaceCream,FaceWash,ToothPaste,BathingSoap,Shampoo,Moisturizer,TotalUnits,TotalProfit
1,2500,1500,5200,9200,1200,1500,21100,211000
2,2630,1200,5100,6100,2100,1200,18330,183300
3,2140,1340,4550,9550,3550,1340,22470,224700
4,3400,1130,5870,8870,1870,1130,22270,222700
5,3600,1740,4560,7760,1560,1740,20960,209600
6,2760,1555,4890,7490,1890,1555,20140,201400
7,2980,1120,4780,8980,1780,1120,29550,295500
8,3700,1400,5860,9960,2860,1400,36140,361400
9,3540,1780,6100,8100,2100,1780,23400,234000
10,1990,1890,8300,10300,2300,1890,26670,266700
11,2340,2100,7300,13300,2400,2100,41280,412800
12,2900,1760,7400,14400,1800,1760,30020,300200
"""

df = pd.read_csv(io.StringIO(csv_data))

# Exibe a base para inspeção
display_dataframe_to_user("Company Sales Data", df)

# Métricas derivadas
df['ProfitPerUnit'] = df['TotalProfit'] / df['TotalUnits']

# Plot 1: Unidades totais por mês
plt.figure()
plt.plot(df['Month'], df['TotalUnits'], marker='o')
plt.title('Total de Unidades Vendidas por Mês')
plt.xlabel('Mês')
plt.ylabel('Unidades')
plt.grid(True)
plt.show()

# Plot 2: Lucro total por mês
plt.figure()
plt.bar(df['Month'], df['TotalProfit'])
plt.title('Lucro Total por Mês')
plt.xlabel('Mês')
plt.ylabel('Lucro (unidades monetárias)')
plt.grid(axis='y')
plt.show()

# Plot 3: Vendas mensais por categoria de produto
plt.figure()
product_cols = ['FaceCream','FaceWash','ToothPaste','BathingSoap','Shampoo','Moisturizer']
for col in product_cols:
    plt.plot(df['Month'], df[col], label=col)
plt.title('Vendas Mensais por Produto')
plt.xlabel('Mês')
plt.ylabel('Unidades')
plt.legend()
plt.grid(True)
plt.show()

# Plot 4: Relação Unidades x Lucro
plt.figure()
plt.scatter(df['TotalUnits'], df['TotalProfit'])
m, b = np.polyfit(df['TotalUnits'], df['TotalProfit'], 1)
x = np.linspace(df['TotalUnits'].min(), df['TotalUnits'].max(), 100)
plt.plot(x, m*x + b)
plt.title('Correlação: Unidades Totais vs Lucro Total')
plt.xlabel('Unidades Totais')
plt.ylabel('Lucro Total')
plt.grid(True)
plt.show()

# Estatísticas descritivas
summary = df.describe().T
display_dataframe_to_user("Resumo Estatístico", summary)
