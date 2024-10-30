import os
import pandas as pd

# Definindo a pasta onde estão as planilhas
archives = 'Planilhas'

# Dicionario para armazenar os Dataframes por categoria
df_dict = {'Dados LI': [], 'Anuências': []}

for file in os.listdir(archives):
    if file.endswith('.xls'):
        print('Carregando arquivo: {0}...'.format(file))
        # Carrega as planilhas especificas do arquivo
        dados_df = pd.read_excel(os.path.join(
            archives, file), sheet_name='Dados LI')
        anuencias_df = pd.read_excel(os.path.join(
            archives, file), sheet_name='Anuências')

        df_dict['Dados LI'].append(dados_df)
        df_dict['Anuências'].append(anuencias_df)

# Dicionário para armazenar os DataFrames finais
final_df_dict = {}

# Concatena os DataFrames de cada categoria
for sheet_name, df_list in df_dict.items():
    if df_list:
        final_df_dict[sheet_name] = pd.concat(df_list, ignore_index=True)

# Salva o Arquivo Final
with pd.ExcelWriter('planilhas/PlanilhaFinal.xlsx') as writer:
    for sheet_name, df in final_df_dict.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print('Planilha finalizada')
