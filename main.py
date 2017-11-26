import os
def main():
    continua = True
    pesos = []
    vertice = []

    while continua:
        os.system('clear')
        print "[*] 1 - Adicionar vertice"
        print "[*] 2 - Adicionar arestas com os pesos"
        print "[*] 3 - Rodar algoritmo de Kruskal"
        print "[*] 4 - Sair\n\n"
        op = raw_input('Qual a opcao desejada: ')


        if op == '1':
            print 'Adicionando vertice. Digite 0 para sair\n\n'

            ok = True
            while ok:
                v = raw_input('Vertice: ')
                if v == '0':
                    break
                vertice.append(v)


        if op == '2':
            print vertice
            print 'Adicionando aresta com os pesos. Digite 0 para sair\n\n'
            print 'Exemplo:\nAresta: A-B\nPeso: 5\n\n'


            ok = True
            while ok:
                a = raw_input('Aresta: ')
                p = raw_input('Peso: ')
                print "\n"

                if a == '0' or p == '0':
                    break

                dados = {'a': a, 'p': p}
                pesos.append(dados)


        if op == '3':
            print 'Rodando o algoritmo de Kruskal\n\n'
            pesos = sorted(pesos, key=lambda x: x['p'])
            for peso in pesos:
                print peso['a'] + ': ' + str(peso['p'])


            return 0

        if op == '4':
            print 'Saindo...\n\n'
            return 0



    return 0

if __name__ == '__main__':
    main()