# backupgenerator

# SCRIPT PYTHON QUE FAZ A LEITURA DE UM ARQUIVO E GERA O BACKUP
# VERSÃO ATUAL SÓ FUNCIONA COM LINUX

[NOMEQUALQUER]              -- DISPENSAVEL
database=BASEDEDADOS        -- ESSENCIAL
database=BASEDEDADOS
user=USUARIO                -- ESSENCIAL
port=PORTA                  -- DISPENSAVEL
password=SENHA              -- ESSENCIAL
host=HOST                   -- ESSENCIAL
ignoreTables=TAB1,TAB2,TAB3 -- TABELAS QUE SERÃO IGNORADAS
name=QUALQUERNOME           -- DISPENSAVEL, UM NOME EXTRA PARA O SCRIPT
#backupFolder=/path/to/dir   -- CASO NENHUM CAMINHO PASSADO, O DIRETÓRIO ./backups/ É CRIADO NO LOCAL DE EXECUÇÃO DO SCRIPT
backupFolder=/backup/bostanenhuma/
                            -- INSTANCIAS DEVEM SER SEPARADAS COM 2 QUEBRAS DE LINHA
#[NOMEQUALQUER2]            -- O CARACTERE "#" É UTILIZADO COMO COMENTÁRIO DE LINHA
#database=db_sisfadivale    -- LINHA IGNORADA
#user=fadivale_ofc          -- LINHA IGNORADA
#port=3306                  -- LINHA IGNORADA
#password=SENHA             -- LINHA IGNORADA
#host=HOST                  -- LINHA IGNORADA
[END]                       -- TAG USADA PARA INDICAR O FIM DO ARQUIVO