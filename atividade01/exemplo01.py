with open('arquivo.txt', 'r', encoding='utfe-8') as livro:
    conteudo = livro.read()
    print(conteudo)
    print('------------------')

with open('arquivo.txt', 'r', encoding='utf-8') as livro:
    linhas = livro.readlines()
    print(f'Foram impressas {len(linhas)} linhas.')

