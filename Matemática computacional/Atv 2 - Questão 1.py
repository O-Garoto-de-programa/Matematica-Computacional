# Atv 2 (Questão 1) Expressão Simplificada: F = (AB) + (~A.B.~C.~(D.E)) + (A.~B.~C.~D.E)

import tabulate
#MAPA DE KARNAUGH
truth_table = [
    [('000'), 0, 1, 0, 1],
    [('001'), 0, 1, 1, 1],
    [('010'), 0, 1, 0, 1],
    [('011'), 0, 0, 0, 1],
    [('100'), 0, 0, 0, 1],
    [('101'), 0, 0, 0, 1],
    [('110'), 0, 0, 0, 1],
    [('111'), 0, 0, 0, 1]
]

headers = ['AB/CDE','00', '01', '10', '11']

table = tabulate.tabulate(truth_table, headers, tablefmt='grid')

print('MAPA DE KARNAUGH')
print(table)

#--------------------------------------------------------------------------------------------------------------------------------------
#TABELA VERDADE
import ttg

tabela = ttg.Truths(['A', 'B', 'C', 'D', 'E'],['(A and B) or (~A and B and ~C and ~(D and E)) or (A and ~B and ~C and ~D and E)'])
print("TABELA VERDADE")
print(tabela)

#------------------------------------------------------------------------------------------------------------------------------------
#CIRCUITO LÓGICO
import schemdraw
import schemdraw.logic as logic
with schemdraw.Drawing() as view:
	view.config(unit=.10)
	
	a1 = view.add(logic.Dot().at((0, 8)).label('A','left'))
	b1 = view.add(logic.Dot().at((0, 7)).label('B','left'))
	And1 = view.add(logic.And().at((4, 7.5)).right())
	view.add(logic.Wire().at(a1.start).to(And1.in1))
	view.add(logic.Wire().at(b1.start).to(And1.in2))
#------------------------------------------------------------------------------------------------------------------------------------
	a2 = view.add(logic.Dot().at((0, 5.5)).label('A','left'))
	b2 = view.add(logic.Dot().at((0, 4.5)).label('B','left'))
	c1 = view.add(logic.Dot().at((0, 3)).label('C','left'))
	d1 = view.add(logic.Dot().at((0, 1.8)).label('D','left'))
	e1 = view.add(logic.Dot().at((0, 1.2)).label('E','left'))
	
	not_a2=view.add(logic.Not().right().at((1,5.5)))
	view.add(logic.Wire().at(a2.start).to(not_a2.in1))
	not_c1=view.add(logic.Not().right().at((1.5,3)))
	view.add(logic.Wire().at(c1.start).to(not_c1.in1))
	nand_gt=view.add(logic.Nand().at((0.7, 1.5)).right())
	view.add(logic.Wire().at(d1.start).to(nand_gt.in1))
	view.add(logic.Wire().at(e1.start).to(nand_gt.in2))
	
	And2 = view.add(logic.And(inputs=4).at((4, 3)).right())
	view.add(logic.Wire().at(not_a2.out).to(And2.in1))
	view.add(logic.Wire().at(b2.start).to(And2.in2))
	view.add(logic.Wire().at(not_c1.out).to(And2.in3))
	view.add(logic.Wire().at(nand_gt.out).to(And2.in4))
#-------------------------------------------------------------------------------------------------------------------------------------
	a3 = view.add(logic.Dot().at((0, -0.2)).label('A','left'))
	b3 = view.add(logic.Dot().at((0, -1.5)).label('B','left'))
	c2 = view.add(logic.Dot().at((0, -2.8)).label('C','left'))
	d2 = view.add(logic.Dot().at((0, -4.1)).label('D','left'))
	e2 = view.add(logic.Dot().at((0, -5.4)).label('E','left'))
	
	not_b3=view.add(logic.Not().right().at((1,-1.5)))
	view.add(logic.Wire().at(b3.start).to(not_b3.in1))
	not_c2=view.add(logic.Not().right().at((1,-2.8)))
	view.add(logic.Wire().at(c2.start).to(not_c2.in1))
	not_d2=view.add(logic.Not().right().at((1,-4.1)))
	view.add(logic.Wire().at(d2.start).to(not_d2.in1))
	
	And3 = view.add(logic.And(inputs=5).at((4, -2.8)).right())
	view.add(logic.Wire().at(a3.start).to(And3.in1))
	view.add(logic.Wire().at(not_b3.out).to(And3.in2))
	view.add(logic.Wire().at(not_c2.out).to(And3.in3))
	view.add(logic.Wire().at(not_d2.out).to(And3.in4))
	view.add(logic.Wire().at(e2.start).to(And3.in5))
#-------------------------------------------------------------------------------------------------------------------------------------
	Or_gt=view.add(logic.Or(inputs=3).at((8.5, 3)).right().label('F','right'))
	view.add(logic.Wire().at(And1.out).to(Or_gt.in1))
	view.add(logic.Wire().at(And2.out).to(Or_gt.in2))
	view.add(logic.Wire().at(And3.out).to(Or_gt.in3))
	
view.draw()
