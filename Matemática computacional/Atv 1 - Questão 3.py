import ttg
# Atv1(Questão 3)  F = ~((A ⊕ ~B) + ~(B.C))


tabela = ttg.Truths(['A', 'B', 'C'],['~((A xor ~B) or ~(B and C))'])
print(tabela)

#---------------------------------------------------------------------------

import schemdraw
import schemdraw.logic as logic
with schemdraw.Drawing() as view:
	view.config(unit=.10)
	
	not_B = view.add(logic.Not().right().at((-1,1.25)))
	view.add(logic.Line().at(not_B.in1).left().dot().label('B','left'))
	
	xor_gate = view.add(logic.Xor().right().at((0,1.5)))
	view.add(logic.Line().at(xor_gate.in1).left().dot().label('A','left'))
	view.add(logic.Wire().at(not_B.out).to(xor_gate.in2))
	
	nand_gate = view.add(logic.Nand().right().at((0,-1.5)))
	view.add(logic.Line().at(nand_gate.in1).left().dot().label('B','left'))
	view.add(logic.Line().at(nand_gate.in2).left().dot().label('C','left'))
	
	nor_gate = view.add(logic.Nor().right().at((3,0)).label('F','right'))
	view.add(logic.Wire().at(xor_gate.out).to(nor_gate.in1))
	view.add(logic.Wire().at(nand_gate.out).to(nor_gate.in2))
	
view.draw()
