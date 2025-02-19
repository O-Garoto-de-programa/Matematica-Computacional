# Atv 2 (Questão 4) EXPRESSÃO SIMPLIFICADA: ABCD + ~(ABCD) + ~E

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

import ttg


tabela = ttg.Truths(['A','B','C','D','E'],['(A and B and C and D) or ~(A and B and C and D) or ~E'])
print("TABELA VERDADE")
print(tabela)

import schemdraw
import schemdraw.logic as logic
with schemdraw.Drawing() as view:
	view.config(unit=.5)
	
	A =view.add(logic.Dot().at((0, 7)).label('A','left'))
	B =view.add(logic.Dot().at((0, 6)).label('B','left'))
	C =view.add(logic.Dot().at((0, 5)).label('C','left'))
	D =view.add(logic.Dot().at((0, 4)).label('D','left'))
	
	And1 =view.add(logic.And(inputs=4).right().at((3, 5.5)))
	view.add(logic.Wire().at(A.start).to(And1.in1))
	view.add(logic.Wire().at(B.start).to(And1.in2))
	view.add(logic.Wire().at(C.start).to(And1.in3))
	view.add(logic.Wire().at(D.start).to(And1.in4))
	#------------------------------------------------------------------------------------------
	A2 =view.add(logic.Dot().at((0, 3)).label('A','left'))
	B2 =view.add(logic.Dot().at((0, 2)).label('B','left'))
	C2 =view.add(logic.Dot().at((0, 1)).label('C','left'))
	D2 =view.add(logic.Dot().at((0, 0)).label('D','left'))
	
	Nand =view.add(logic.Nand(inputs=4).right().at((3, 1.5)))
	view.add(logic.Wire().at(A2.start).to(Nand.in1))
	view.add(logic.Wire().at(B2.start).to(Nand.in2))
	view.add(logic.Wire().at(C2.start).to(Nand.in3))
	view.add(logic.Wire().at(D2.start).to(Nand.in4))
	#-----------------------------------------------------------------------------------------------
	E = view.add(logic.Dot().at((0, -2)).label('E','left'))
	not_e =view.add(logic.Not().at((3.4, -2)))
	view.add(logic.Wire().at(E.start).to(not_e.in1))
	#-----------------------------------------------------------------------------------------------
	Or = view.add(logic.Or(inputs=3).right().at((6, 1.5)).label('Tautologia','right'))
	view.add(logic.Wire().at(And1.out).to(Or.in1))
	view.add(logic.Wire().at(Nand.out).to(Or.in2))
	view.add(logic.Wire().at(not_e.out).to(Or.in3))
	
view.draw()
