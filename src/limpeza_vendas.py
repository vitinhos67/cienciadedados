import pandas as pd
import numpy as np

# Carrega o dataset
df = pd.read_csv('./assets/vendas_modificado.csv')

# 1. Ajuste de formatação e remoção de espaços extras
df.columns = df.columns.str.strip()  # Remove espaços dos nomes das colunas
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # Remove espaços dos valores textuais

# 2. Padronização de produtos
df['produto'] = df['produto'].str.title().str.replace(r'[^\w\s]', '', regex=True)

# 3. Tratamento de dados faltantes com valores padrão
df.fillna({
    'valor': 0.0,
    'quantidade': 0,
    'total': 0.0,
    'frete': 0.0,
    'cep': '00000-000',
}, inplace=True)

# 4. Validação e formatação de CEPs
df['cep'] = df['cep'].astype(str).str.replace(r'[^\d]', '', regex=True)
df['cep'] = df['cep'].apply(lambda x: f"{x[:5]}-{x[5:]}" if len(x) == 8 else '00000-000')

# 5. Conversão de tipos para colunas numéricas
colunas_numericas = ['valor', 'quantidade', 'total', 'frete']
for col in colunas_numericas:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# 6. Remoção de registros duplicados
df.drop_duplicates(inplace=True)

# 7. Validação da coluna 'total' (com margem de erro)
df['total_calculado'] = df['valor'] * df['quantidade'] + df['frete']
df = df[np.isclose(df['total'], df['total_calculado'], atol=0.01)]

# 8. Salva o DataFrame limpo
df.to_csv('./assets/limpos/dados_megasuper_vendas_limpos.csv', index=False)

# Relatório Resumido
relatorio = """
RELATÓRIO DE LIMPEZA DE DADOS

1. Ajustes de Formatação:
   - Espaços removidos de colunas e valores.
   - Produtos padronizados (Title Case, sem caracteres especiais).

2. Tratamento de Dados Faltantes:
   - Preenchimento com valores padrão (ex.: CEP '00000-000', valor 0).

3. Validações:
   - CEPs formatados corretamente (XXXXX-XXX).
   - Colunas numéricas convertidas com segurança.

4. Remoção de Inconsistências:
   - Duplicatas eliminadas.
   - Coluna 'total' validada com: total = valor * quantidade + frete.

O DataFrame limpo foi salvo em 'dados_megasuper_vendas_limpos.csv'.
"""

print(relatorio)
