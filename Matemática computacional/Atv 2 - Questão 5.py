# Atv 2 (Questão 5): Q1 + Q4

import tabulate
#MAPA DE KARNAUGH
truth_table = [
    [('000'), 1, 1, 1, 1],
    [('001'), 1, 1, 1, 1],
    [('010'), 1, 1, 1, 1],
    [('011'), 1, 1, 1, 1],
    [('100'), 1, 1, 1, 1],
    [('101'), 1, 1, 1, 1],
    [('110'), 1, 1, 1, 1],
    [('111'), 1, 1, 1, 1]
]

headers = ['AB/CDE','00', '01', '10', '11']

table = tabulate.tabulate(truth_table, headers, tablefmt='grid')

print('MAPA DE KARNAUGH')
print(table)
#------------------------------------------------------------------------------------------------------
#CIRCUITO LÓGICO

import schemdraw
import schemdraw.logic as logic
with schemdraw.Drawing() as view:
	view.config(unit=.5)
	
	Q1 =view.add(logic.Dot().at((0, 2.5)).label('F','left'))
	Q4 =view.add(logic.Dot().at((0, 1.5)).label('Tautologia','left'))
	
	Or = view.add(logic.Or().at((3,2)).label('Tautologia','right'))
	view.add(logic.Wire().at(Q1.start).to(Or.in1))
	view.add(logic.Wire().at(Q4.start).to(Or.in2))
view.draw()
