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
    df['Total_Negros'] = df['Quantidade_Preto'] + df['Quantidade_Pardo']
    df['Total_Empregados'] = (df['Quantidade_Amarelo'] + df['Quantidade_Branco'] + 
                               df['Quantidade_Preto'] + df['Quantidade_Pardo'] + 
                               df['Quantidade_Indigena'] + df['Quantidade_Outros'])
    df['Percentual_Negros'] = (df['Total_Negros'] / df['Total_Empregados']) * 100
    return df

lider_2024 = processar_dados(lider_2024)
lider_2025 = processar_dados(lider_2025)

print("ESTATÍSTICAS 2024")
print(f"Média: {lider_2024['Percentual_Negros'].mean():.2f}%")
print(f"Mediana: {lider_2024['Percentual_Negros'].median():.2f}%")
print(f"Desvio Padrão: {lider_2024['Percentual_Negros'].std():.2f}")
print(f"Q1: {lider_2024['Percentual_Negros'].quantile(0.25):.2f}%")
print(f"Q3: {lider_2024['Percentual_Negros'].quantile(0.75):.2f}%\n")

print("ESTATÍSTICAS 2025")
print(f"Média: {lider_2025['Percentual_Negros'].mean():.2f}%")
print(f"Mediana: {lider_2025['Percentual_Negros'].median():.2f}%")
print(f"Desvio Padrão: {lider_2025['Percentual_Negros'].std():.2f}")
print(f"Q1: {lider_2025['Percentual_Negros'].quantile(0.25):.2f}%")
print(f"Q3: {lider_2025['Percentual_Negros'].quantile(0.75):.2f}%")

