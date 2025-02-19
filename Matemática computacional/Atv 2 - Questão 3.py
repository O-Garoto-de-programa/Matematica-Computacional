# Atv 2 (Questão 3) Expressão simplificada S= ~A + ~B + ~C

import tabulate
#MAPA DE KARNAUGH
truth_table = [
    [('0 |'), 1, 1, 1, 1],
    [('1 |'), 1, 1, 1, 0]

]

headers = ['AB/C','00', '01', '10', '11']

table = tabulate.tabulate(truth_table, headers, tablefmt='grid')

print('MAPA DE KARNAUGH')
print(table)

#-----------------------------------------------------------------------------------------------------------------

import ttg

tabela = ttg.Truths(['A','B','C'] , ["~A or ~B or ~C"])

print("TABELA VERDADE")
print(tabela)

#-----------------------------------------------------------------------------------------------------------------

import schemdraw
import schemdraw.logic as logic
with schemdraw.Drawing() as view:
	view.config(unit=.3)
	
	A =view.add(logic.Dot().at((0, 6)).label('A','left'))
	B =view.add(logic.Dot().at((0, 4)).label('B','left'))
	C =view.add(logic.Dot().at((0, 2)).label('C','left'))
	
	not_a =view.add(logic.Not().at((1, 6)))
	view.add(logic.Wire().at(A.start).to(not_a.in1))
	
	not_b =view.add(logic.Not().at((1, 4)))
	view.add(logic.Wire().at(B.start).to(not_b.in1))
	
	not_c =view.add(logic.Not().at((1, 2)))
	view.add(logic.Wire().at(C.start).to(not_c.in1))
	
	Or_gt =view.add(logic.Or(inputs=3).at((4, 4)).label('S', 'right'))
	view.add(logic.Wire().at(not_a.out).to(Or_gt.in1))
	view.add(logic.Wire().at(not_b.out).to(Or_gt.in2))
	view.add(logic.Wire().at(not_c.out).to(Or_gt.in3))
	
view.draw()
