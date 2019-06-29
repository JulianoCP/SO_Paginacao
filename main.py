
tamanhoPaginas = 10
tamanhoRam = 32
tamanhoProcesso = 64
endLogico = list();
endFisico = list();

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
            endFisico = ['1'] + ['0'] + ['0'] + dados[0]
            arquivoFisico.write(str(endFisico))
            arquivoFisico.write('\n')
        elif (x == '0') and (z == '1'):
            endFisico = ['1'] + ['0'] + ['1'] + dados[0]
            arquivoFisico.write(str(endFisico))
            arquivoFisico.write('\n')
        elif (x == '1') and (z == '0'):
            endFisico = ['1'] + ['1'] + ['0'] + dados[0]
            arquivoFisico.write(str(endFisico))
            arquivoFisico.write('\n')
        elif (x == '1') and (z == '1'):
            endFisico = ['1'] + ['1'] + ['1'] + dados[0]
            arquivoFisico.write(str(endFisico))
            arquivoFisico.write('\n')

    arquivoFisico.close
    arquivoLogico.close


def main():
    arqLogicos("endLogicos.txt")


if __name__ == '__main__':
    main()
