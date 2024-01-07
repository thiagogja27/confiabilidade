import pandas as pd

def procv_python(planilha1, planilha2, colunas_chave, colunas_interesse):
    # Carregar as planilhas em DataFrames
    df1 = pd.read_excel(planilha1)
    df2 = pd.read_excel(planilha2)

    # Realizar a operação semelhante ao PROCV
    resultado = pd.merge(df1, df2, on=colunas_chave, how='outer', indicator=True)
    diferenca_df = resultado[resultado['_merge'] == 'left_only'][colunas_interesse]

    # Salvar as diferenças em um novo arquivo Excel
    diferenca_df.to_excel("diferencas_encontradas.xlsx", index=False)
    print("Diferenças salvas em 'diferencas_encontradas.xlsx'.")

# Substitua 'planilha1.xlsx', 'planilha2.xlsx' e ['Nome', 'Data'] pelos valores reais das suas planilhas e colunas de chave
procv_python('Meuarquivo2.xlsx', 'Meuarquivo1.xlsx', ['Nome','CPF'],['Nome','CPF'])