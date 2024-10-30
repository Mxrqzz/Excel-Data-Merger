# Excel Data Merger

Este repositório contém scripts em Python para mesclar e consolidar arquivos Excel (.xls) em um único arquivo. O objetivo é facilitar a análise de dados provenientes de múltiplas planilhas.

## Scripts

### JuntandoDados.py: Carregar e Mesclar Planilhas

Este script carrega todas as planilhas no formato .xls de um diretório específico e as mescla em uma única planilha.

#### Como Usar
1. Altere a variável `archives` para o caminho onde estão os arquivos .xls.
2. Execute o script. O arquivo final será salvo em `planilhas/planilhaFinal.xlsx`.

### JuntandoPlanilhas.py: Mesclar Planilhas Específicas

Este script carrega duas planilhas específicas (Dados LI e Anuências) de múltiplos arquivos e as mescla em uma única planilha.

#### Como Usar
1. Certifique-se de que os arquivos .xls estejam na pasta "Planilhas".
2. Execute o script. O arquivo final será salvo em `planilhas/PlanilhaFinal.xlsx`.

## Dependências

- Python 3.x
- Pandas
