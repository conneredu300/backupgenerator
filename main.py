import sys
from tools import *

def main():
    # tools = Tools(sys.argv[1])
    tools = Tools("ta.txt")
    tools.lerArquivo()
    for dados in tools.arrDados:
        tools.backup(dados)

    print "Finalizado com sucesso"


if __name__ == "__main__":
    main()