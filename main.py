
tamanhoPaginas = 10
tamanhoRam = 32
tamanhoProcesso = 64
endLogico = list();
endFisico = list();
endLogico = ['1','1','0','0','0','0','0','0','0','0','0','1','1','0','1']

def arqLogicos(endLogico):
    arquivoLogico = open(endLogico,'r')
    arquivoFisico = open('endFisicos.txt','w')

    listaEndLogicos = arquivoLogico.readlines()
    listaEndLogicos = [ i.replace('\n', '') for i in listaEndLogicos]
    listaEndLogicos = [ i.split(' ') for i in listaEndLogicos]

    print(listaEndLogicos)

    arquivoFisico.close
    arquivoLogico.close

if (endLogico[0] == '0') and (endLogico[1] == '0'):
    print("Endereco Logico: %s" % endLogico)
    print("Frame: 100")
    endLogico.pop(0)
    endLogico.pop(0)
    endFisico = ['1']+ ['0'] + ['0'] + endLogico
    print("Endereco Fisico: %s" % endFisico)
elif (endLogico[0] == '0') and (endLogico[1] == '1'):
    print("Endereco Logico: %s" % endLogico)
    print("Frame: 101")
    endLogico.pop(0)
    endLogico.pop(0)
    endFisico = ['1']+ ['0'] + ['1'] + endLogico
    print("Endereco Fisico: %s" % endFisico)
elif (endLogico[0] == '1') and (endLogico[1] == '0'):  
    print("Endereco Logico: %s" % endLogico)  
    print("Frame: 110")
    endLogico.pop(0)
    endLogico.pop(0)
    endFisico = ['1']+ ['1'] + ['0'] + endLogico
    print("Endereco Fisico: %s" % endFisico)
elif (endLogico[0] == '1') and (endLogico[1] == '1'):  
    print("Endereco Logico: %s" % endLogico)  
    print("Frame: 111")
    endLogico.pop(0)
    endLogico.pop(0)
    endFisico = ['1']+ ['1'] + ['1'] + endLogico
    print("Endereco Fisico: %s" % endFisico)
    print("\n")
    arqLogicos("endLogicos.txt")