import sys
from tools import *

def main():
    tools = Tools(sys.argv[1])
    tools.lerArquivo()
    tools.prepareData()
    for dados in tools.arrDados:
        tools.backup(dados)

    print "Finalizado com sucesso"


if __name__ == "__main__":
    main()