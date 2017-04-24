#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql
import ConectaDB


def main():

    sql = 'select id,datamovto,descricao,valor from movtofinanc where conta=6 \
and datamovto between \'2017-01-01\' and now()'
    dados = exec_select(sql, 4)
    print (type(dados))


#Inserir, modificar, deletar
def exec_comando(sql):
    db = ConectaDB.conn()
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
    except:
        print ('Erro: Não foi possível Executar comando sql %s' % (sql))
        db.rollback()
    db.close


def exec_select(sql, qtdcampos):
    db = ConectaDB.conn()
    cur = db.cursor()
    cur.execute(sql)
    valores = cur.fetchall()
    try:
        for linha in valores:
            contador = 0
            while(contador < qtdcampos):
                print(linha)
                contador += 1
        db.close()
    except:
        print('Erro ao processar comando: \n %s \n Quantidade de elementos \
        informados: %s' % (sql, qtdcampos))

if __name__ == main():
    main()