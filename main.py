import time
import sys

qtd = 0
qtdPaginas = 3
tamanhoPaginas = 10
tamanhoRam = 32
tamanhoProcesso = 64
endLogico = list();
endFisico = list();
paginas = list();
paginas = [1,2,5,6,8,1,2,3,10,2,0,4,2,1,5,3,2,0,6,7,5,2,5,9,10,1,11,6,5,9,0,1,2]

def delPage(tabPaginas,num):
    arqTab = open('tabPaginas.txt','r')
    listaEndTab = arqTab.readlines()
    arqTab.close

    arqReplace = open('tabPaginas.txt','w')
    for line in listaEndTab:
        if (line[2] != str(num)) and (line[2]+line[3] != str(num)):
            arqReplace.write(line)
    arqReplace.close

def addPage(num):
    arqFisico = open('endFisicos.txt','r')
    arqTab = open('tabPaginas.txt','a')
    listaEndFisico = arqFisico.readlines()
    listaEndFisico = [ i.replace('\n', '') for i in listaEndFisico]

    for i in listaEndFisico:
        if(i[2] == str(num) or (i[2]+i[3]) == str(num)):
            arqTab.write(i)
            arqTab.write('\n')
            arqFisico.close
            arqTab.close
            return
    
    print("[PAGE INVALID]:[REMOVE PROCESS]")
    sys.exit()
    


def tabPagina(tabela,num):
    arqTab = open(tabela,'r')

    listTab = arqTab.readlines()
    listTab = [ i.replace('\n', '') for i in listTab]

    for i in listTab:
        if(i[2] == str(num)):
            x = len(i)
            s = i[6:x]
            print("[HIT]: [%s" % s)
            return
        elif((i[2]+i[3]) == str(num)):
            x = len(i)
            s = i[7:x]
            print("[HIT]: [%s" % s)
            return

    print("[MISS]:[PAGE-FAULT]")

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
    global qtd
    for i in paginas:
        tabPagina("tabPaginas.txt",i)
        time.sleep(1)
        if qtd == qtdPaginas:
            qtd = 0
            delPage('tabPaginas.txt',10)
        qtd += 1



if __name__ == '__main__':
    main()
