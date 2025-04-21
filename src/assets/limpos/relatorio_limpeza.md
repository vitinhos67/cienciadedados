
# RELATÓRIO DE LIMPEZA DE DADOS

## 1. AJUSTES DE FORMATAÇÃO:
- Espaços extras removidos de colunas e valores.
- Produtos padronizados para "Title Case" e caracteres especiais removidos.

## 2. TRATAMENTO DE DADOS FALTANTES:
- Valores ausentes preenchidos com padrões adequados (ex.: CEP '00000-000').

## 3. VALIDAÇÃO E CORREÇÃO:
- CEPs formatados corretamente.
- Colunas numéricas validadas e convertidas.

## 4. REMOÇÃO DE INCONSISTÊNCIAS:
- Registros duplicados eliminados.
- Coluna 'total' validada com base na fórmula: total = valor * quantidade + frete.

O DataFrame limpo foi salvo no arquivo `dados_megasuper_vendas_limpos.csv`.
