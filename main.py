import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

df_2024 = pd.read_csv('fre_cia_aberta_empregado_posicao_declaracao_raca_2024.csv', 
                      sep=';', 
                      encoding='latin-1')

df_2025 = pd.read_csv('fre_cia_aberta_empregado_posicao_declaracao_raca_2025.csv', 
                      sep=';', 
                      encoding='latin-1')


lider_2024 = df_2024[df_2024['Posicao'] == 'Liderança'].copy()
lider_2025 = df_2025[df_2025['Posicao'] == 'Liderança'].copy()


def processar_dados(df):
    df['Total_Empregados'] = (df['Quantidade_Amarelo'] + df['Quantidade_Branco'] + 
                               df['Quantidade_Preto'] + df['Quantidade_Pardo'] + 
                               df['Quantidade_Indigena'] + df['Quantidade_Outros'])
    df['Percentual_Negros'] = (df['Quantidade_Preto'] / df['Total_Empregados']) * 100
    return df

lider_2024 = processar_dados(lider_2024)
lider_2025 = processar_dados(lider_2025)

print("Pessoas pretas em cargo de liderança nas empresas da B3 (de capital aberto) em 2024:")
print(f"Média: {lider_2024['Percentual_Negros'].mean():.2f}%")
print(f"Mediana: {lider_2024['Percentual_Negros'].median():.2f}%")
print(f"Desvio Padrão: {lider_2024['Percentual_Negros'].std():.2f}")
print(f"Q1: {lider_2024['Percentual_Negros'].quantile(0.25):.2f}%")
print(f"Q3: {lider_2024['Percentual_Negros'].quantile(0.75):.2f}%\n")

print("Pessoas pretas em cargo de liderança nas empresas da B3 (de capital aberto) em 2025:")
print(f"Média: {lider_2025['Percentual_Negros'].mean():.2f}%")
print(f"Mediana: {lider_2025['Percentual_Negros'].median():.2f}%")
print(f"Desvio Padrão: {lider_2025['Percentual_Negros'].std():.2f}")
print(f"Q1: {lider_2025['Percentual_Negros'].quantile(0.25):.2f}%")
print(f"Q3: {lider_2025['Percentual_Negros'].quantile(0.75):.2f}%")

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# GRÁFICO DE PIZZA
print("Gerando gráfico de pizza:")

total_amarelo = lider_2025['Quantidade_Amarelo'].sum()
total_branco = lider_2025['Quantidade_Branco'].sum()
total_preto = lider_2025['Quantidade_Preto'].sum()
total_pardo = lider_2025['Quantidade_Pardo'].sum()
total_indigena = lider_2025['Quantidade_Indigena'].sum()
total_outros = lider_2025['Quantidade_Outros'].sum()

racas = ['Amarelo', 'Branco', 'Preto', 'Pardo', 'Indígena', 'Outros']
valores = [total_amarelo, total_branco, total_preto, total_pardo, total_indigena, total_outros]
cores = ['#FFD700', '#E8E8E8', '#8B4513', '#D2691E', '#FF6347', '#A9A9A9']

fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(valores, 
                                    labels=racas, 
                                    autopct='%1.1f%%',
                                    colors=cores,
                                    startangle=90,
                                    textprops={'fontsize': 11, 'weight': 'bold'})


for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

plt.title('Distribuição Racial em Cargos de Liderança (2025)\nEmpresas de Capital Aberto B3', 
          fontsize=14, weight='bold', pad=20)
plt.tight_layout()
plt.savefig('grafico_pizza_lideranca_raca.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Gráfico de pizza salvo: grafico_pizza_lideranca_raca.png")


# GRÁFICO DE BARRAS
print("Gerando gráfico de barras:")

lider_data = lider_2025[['Quantidade_Amarelo', 'Quantidade_Branco', 'Quantidade_Preto', 
                         'Quantidade_Pardo', 'Quantidade_Indigena', 'Quantidade_Outros']].sum()
total_lider = lider_data.sum()

nao_lider_2025 = df_2025[df_2025['Posicao'] != 'Liderança'].copy()
nao_lider_data = nao_lider_2025[['Quantidade_Amarelo', 'Quantidade_Branco', 'Quantidade_Preto', 
                                  'Quantidade_Pardo', 'Quantidade_Indigena', 'Quantidade_Outros']].sum()
total_nao_lider = nao_lider_data.sum()

racas_labels = ['Amarelo', 'Branco', 'Preto', 'Pardo', 'Indígena', 'Outros']
perc_lider = (lider_data / total_lider * 100).values
perc_nao_lider = (nao_lider_data / total_nao_lider * 100).values

# Criar gráfico
x = np.arange(len(racas_labels))
width = 0.35

fig, ax = plt.subplots(figsize=(14, 8))
bars1 = ax.bar(x - width/2, perc_lider, width, label='Liderança', color='#2E86AB', alpha=0.8)
bars2 = ax.bar(x + width/2, perc_nao_lider, width, label='Não Liderança', color='#F08080', alpha=0.8)


for bar in bars1:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}%', ha='center', va='bottom', fontsize=9, weight='bold')

for bar in bars2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}%', ha='center', va='bottom', fontsize=9, weight='bold')


ax.set_xlabel('Raça/Cor', fontsize=12, weight='bold')
ax.set_ylabel('Percentual (%)', fontsize=12, weight='bold')
ax.set_title('Comparação de Diversidade Racial:\nCargos de Liderança vs Não Liderança (2025)', 
             fontsize=14, weight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(racas_labels, fontsize=11)
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('grafico_barras_lideranca_comparacao.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Gráfico de barras salvo: grafico_barras_lideranca_comparacao.png\n")