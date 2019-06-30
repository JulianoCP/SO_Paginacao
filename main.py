import time

qtd = 0
tamanhoPaginas = 10
tamanhoRam = 32
tamanhoProcesso = 64
endLogico = list();
endFisico = list();
paginas = list();
paginas = [11,2,10,11,10,2,3,10,2,0,4,2,1,5,3,2,0,6,7,5,2,5,9,10,1,11]

def delPage(tabPaginas,num): ## vai ser uma funcao para deletar uma linha
    arqTab = open('tabPaginas.txt','r')
    listaEndTab = arqTab.readlines()
    listaEndTab = [ i.replace('\n', '') for i in listaEndTab]

    # for i in listaEndTab:
    #     print(i[2]+i[3])
    #     if (i[2] == str(num) or (i[2]+i[3]) == str(num)): // Funcao para deletar nao funciona kkk 
    #         print("achou")

    arqTab.close

def addPage(num):
    arqFisico = open('endFisicos.txt','r')
    arqTab = open('tabPaginas.txt','a')
    listaEndFisico = arqFisico.readlines()
    listaEndFisico = [ i.replace('\n', '') for i in listaEndFisico]

    for i in listaEndFisico:
        if(i[2] == str(num) or (i[2]+i[3]) == str(num)):
            arqTab.write(i)
            arqTab.write('\n')
            break

    arqFisico.close
    arqTab.close


def tabPagina(tabela,num):
    arqTab = open(tabela,'r')

    listTab = arqTab.readlines()
    listTab = [ i.replace('\n', '') for i in listTab]

    for i in listTab:
        if(i[2] == str(num) or (i[2]+i[3]) == str(num)):
            x = len(i)
            s = i[6:x]
            print("[HIT]: [%s" % s)
            return

    print("[MISS]: [PAGE-FAULT]")

    arqTab.close
    addPage(num)

def arqLogicos(endLogico):
    arquivoLogico = open(endLogico,'r')
    arquivoFisico = open('endFisicos.txt','w')

    listaEndLogicos = arquivoLogico.readlines()
    listaEndLogicos = [ i.replace('\n', '') for i in listaEndLogicos]
    listaEndLogicos = [ i.split(' ') for i in listaEndLogicos]

    dados = []
    dados = [ i.split(',') for i in listaEndLogicos[0]]

    for i in range(len(listaEndLogicos)):
        dados = [ y.split(',') for y in listaEndLogicos[i]]

        x = dados[0].pop(0)
        z = dados[0].pop(0)

        if (x == '0') and (z == '0'):
            endFisico = ['%d' %i] + ['1'] + ['0'] + ['0'] + dados[0]
            arquivoFisico.write(str(endFisico))
            arquivoFisico.write('\n')
        elif (x == '0') and (z == '1'):
            endFisico = ['%d' %i] + ['1'] + ['0'] + ['1'] + dados[0]
            arquivoFisico.write(str(endFisico))
            arquivoFisico.write('\n')
        elif (x == '1') and (z == '0'):
            endFisico = ['%d' %i] + ['1'] + ['1'] + ['0'] + dados[0]
            arquivoFisico.write(str(endFisico))
            arquivoFisico.write('\n')
        elif (x == '1') and (z == '1'):
            endFisico = ['%d' %i] + ['1'] + ['1'] + ['1'] + dados[0]
            arquivoFisico.write(str(endFisico))
            arquivoFisico.write('\n')

    arquivoFisico.close
    arquivoLogico.close
   


def main():
    arqLogicos("endLogicos.txt")
    for i in paginas:
        tabPagina("tabPaginas.txt",i)
        time.sleep(1)



if __name__ == '__main__':
    main()
