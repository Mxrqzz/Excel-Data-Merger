import os
import pandas as pd

archives = 'planilhas'

arquivos = []

for file in os.listdir(archives):
    if file.endswith('.xls'):
        print('Carregando arquivo: {0}...'.format(file))
        arquivos.append(pd.read_excel(os.path.join(archives, file)))
        
print(f"{len(arquivos)} Planilhas Carregadas.")
        
arquivo_final = pd.concat(arquivos, axis=0)
arquivo_final.to_excel('planilhas/planilhaFinal.xlsx', index=False)

print("Planilhas copiadas para nova planilha.")