import csv

def abrir_leitura(caminho):
    with open(caminho, 'r') as arquivo:
        abrir = csv.reader(arquivo)
        dados = list(abrir)
        arquivo.close()
        return dados


caminho = 'E:\VS Code Python\Manipulação de Arquivos\salarios.txt'
dados = abrir_leitura(caminho)
tamanho = len(dados)
for c in range(tamanho):
    print('\n')
    for i in range(4):
        print(f'{dados[0][i]}: {dados[c][i]}')




