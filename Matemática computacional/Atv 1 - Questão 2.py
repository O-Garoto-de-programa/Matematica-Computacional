import ttg
# Atv 1(Questão 2)  F = ~AB + A~B.


tabela = ttg.Truths(['A', 'B'],['~(~A and B)','A or ~B','~(~(~A and B) or (A or ~B))'])
print(tabela)

#--------------------------------------------------------------------------------------------

import schemdraw
import schemdraw.logic as logic
with schemdraw.Drawing() as view:
	view.config(unit=.10)
	
	not_gate1 = view.add(logic.Not().right().at((-1.2,4.26)))
	view.add(logic.Line().at(not_gate1.in1).left().label('A','left'))
	
	
	and_gate1 = view.add(logic.Nand().right().at((0,4)))
	view.add(logic.Wire().at(not_gate1.out).to(and_gate1.in1))
	view.add(logic.Line().at(and_gate1.in2).left().dot().label('B','left'))
	
	not_gate2 = view.add(logic.Not().right().at((-1.2,0.45)))
	view.add(logic.Line().at(not_gate2.in1).left().label('B','left'))
	
	or_gate1 = view.add(logic.Or().right().at((0,0.7)))
	view.add(logic.Line().at(or_gate1.in1).left().dot().label('A','left'))
	view.add(logic.Wire().at(not_gate2.out).to(or_gate1.in2))
	
	nor_gate1 = view.add(logic.Nor().right().at((3,2.35)))
	view.add(logic.Wire().at(and_gate1.out).to(nor_gate1.in1))
	view.add(logic.Wire().at(or_gate1.out).to(nor_gate1.in2))
	view.add(logic.Line().at(nor_gate1.out).dot().label('F', 'right'))
	
view.draw()
