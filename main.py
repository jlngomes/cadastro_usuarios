import pandas as pd
import os

class cadastroUsuarios:
    def __init__(self, nome: str,
                 email: str,
                 telefone: str) -> None:
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def RuleCell(self) -> dict:
        '''
        Função responsável por criar um dicionário que contém itens da lista criada na coluna 'NAME SHEET' (Key) e
        onde deve ser preenchida com o valor da coluna 'CELL'
        '''
        path_rule = f'{os.getcwd()}/database/Rule.xslx'
        dfRule = pd.read_excel(path_rule,sheet_name='Rule.xlsx')
        array_cell = dfRule['NAME SHEET'].dropna().to_list()
        varAux = {}
        for cell_name in array_cell:
            varAux[cell_name] = dfRule.loc[dfRule['NAME SHEET'] == cell_name, 'CELL'].to_list()[0]
        return varAux






teste = cadastroUsuarios('jean','jean.luca162021@outlook.com','(11) 94170-3408')

teste.RuleCell()