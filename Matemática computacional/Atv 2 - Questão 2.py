# Atv 2 (Questão 2) expressão simplificada: ~A + ~B + ~C + ~D

import tabulate
#MAPA DE KARNAUGH
truth_table = [
    [('00'), 1, 1, 1, 1],
    [('01'), 1, 1, 1, 1],
    [('10'), 1, 1, 0, 1],
    [('11'), 1, 1, 1, 0],
    
]

headers = ['AB/CD','00', '01', '10', '11']

table = tabulate.tabulate(truth_table, headers, tablefmt='grid')

print('MAPA DE KARNAUGH')
print(table)

#--------------------------------------------------------------------------------------------
#TABELA VERDADE
import ttg

tabela= ttg.Truths(['A','B','C','D'],["~A or ~B or ~C or ~D"])
print("TABELA VERDADE")
print(tabela)

#-----------------------------------------------------------------------------------------------
#CIRCUITO LÓGICO
import schemdraw
import schemdraw.logic as logic
with schemdraw.Drawing() as view:
	view.config(unit=.10)
	
	A =view.add(logic.Dot().at((0, 6)).label('A','left'))
	B =view.add(logic.Dot().at((0, 4)).label('B','left'))
	C =view.add(logic.Dot().at((0, 2)).label('C','left'))
	D =view.add(logic.Dot().at((0, 0)).label('D','left'))
	
	not_a =view.add(logic.Not().at((1, 6)))
	view.add(logic.Wire().at(A.start).to(not_a.in1))
	
	not_b =view.add(logic.Not().at((1, 4)))
	view.add(logic.Wire().at(B.start).to(not_b.in1))
	
	not_c =view.add(logic.Not().at((1, 2)))
	view.add(logic.Wire().at(C.start).to(not_c.in1))
	
	not_d =view.add(logic.Not().at((1, 0)))
	view.add(logic.Wire().at(D.start).to(not_d.in1))
	
	Or_gt =view.add(logic.Or(inputs=4).at((4, 3)))
	view.add(logic.Wire().at(not_a.out).to(Or_gt.in1))
	view.add(logic.Wire().at(not_b.out).to(Or_gt.in2))
	view.add(logic.Wire().at(not_c.out).to(Or_gt.in3))
	view.add(logic.Wire().at(not_d.out).to(Or_gt.in4))
	
view.draw()
