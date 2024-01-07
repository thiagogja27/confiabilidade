import pandas as pd

def encontrar_diferencas(planilha1, planilha2, colunas_chave):
    # Carregar as planilhas em DataFrames
    df1 = pd.read_excel(planilha1)
    df2 = pd.read_excel(planilha2)

    # Encontrar as linhas que estão apenas em df1 ou df2
    diferenca_df1 = pd.merge(df1, df2, on=colunas_chave, how='outer', indicator=True).query('_merge == "left_only"').drop('_merge', axis=1)
    diferenca_df2 = pd.merge(df2, df1, on=colunas_chave, how='outer', indicator=True).query('_merge == "left_only"').drop('_merge', axis=1)

    # Combinar as diferenças de ambas as direções
    diferenca_final = pd.concat([diferenca_df1, diferenca_df2]).drop_duplicates()

    # Salvar as diferenças em um novo arquivo Excel, se houver diferenças
    if not diferenca_final.empty:
        diferenca_final.to_excel("diferencas_encontradas.xlsx", index=False)
        print("Diferenças salvas em 'diferencas_encontradas.xlsx'.")
    else:
        print("Não foram encontradas diferenças entre as planilhas.")

# Substitua 'Meuarquivo1.xlsx' e 'Meuarquivo2.xlsx' pelos nomes reais de suas planilhas e ['Nome', 'CPF'] pelas colunas de chave
encontrar_diferencas('Meuarquivo1.xlsx', 'Meuarquivo2.xlsx', ['Nome', 'CPF'])