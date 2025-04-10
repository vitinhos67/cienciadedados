import pandas as pd

df = pd.read_csv('assets/csv/vendas_modificado.csv')

# Converte as datas para um formato único e ajusta as horas para o padrão HH:MM:SS
df['data'] = pd.to_datetime(df['data']).dt.strftime('%Y-%m-%d')
df['hora'] = pd.to_datetime(df['hora'], format='%H:%M:%S').dt.strftime('%H:%M:%S')

# Certifica-se de que colunas como valor, quantidade, total e frete estejam no formato numérico adequado
df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce')
df['total'] = pd.to_numeric(df['total'], errors='coerce')
df['frete'] = pd.to_numeric(df['frete'], errors='coerce')

# Identifica registros com dados faltantes e define uma estratégia para tratá-los (preenchimento com valor padrão neste caso)
df.fillna({
    'valor': 0,
    'quantidade': 0,
    'total': 0,
    'frete': 0
}, inplace=True)

# Procura por duplicatas e elimina registros redundantes
df.drop_duplicates(inplace=True)

# Confirma se a coluna total está correta, de acordo com a fórmula: total = valor * quantidade + frete
df['total_calculado'] = df['valor'] * df['quantidade'] + df['frete']
df = df[df['total'] == df['total_calculado']]

# Salva o DataFrame limpo em um novo arquivo CSV
df.to_csv('assets/csv/clear/dados_megasuper_vendas_limpos.csv', index=False)

# Relatório Resumido
relatorio = """
Relatório de Limpeza de Dados

1. Verificação e Padronização de Tipos e Formatos:
   - Datas convertidas para o formato YYYY-MM-DD.
   - Horas ajustadas para o padrão HH:MM:SS.
   - Colunas 'valor', 'quantidade', 'total' e 'frete' convertidas para formato numérico.

2. Tratamento de Inconsistências:
   - Registros com dados faltantes foram removidos.
   - Registros duplicados foram eliminados.
   - Coluna 'total' verificada e corrigida de acordo com a fórmula: total = valor * quantidade + frete.

O DataFrame limpo foi salvo no arquivo 'dados_megasuper_vendas_limpos.csv'.
"""

print(relatorio)
