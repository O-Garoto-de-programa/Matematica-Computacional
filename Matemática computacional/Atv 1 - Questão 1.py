import ttg
# Atv 1(Questão 1)  F = ~XYZ + XZ + X~YZ + X~Z + XY.

			# Expressão Simplificada: F = YZ + X

tabela = ttg.Truths(['X', 'Y', 'Z'],['(Y and Z) or X'])
print(tabela)

import schemdraw
import schemdraw.logic as logic

# F = YZ + X

with schemdraw.Drawing() as view:
	x = view.add(logic.Dot().at((-6, 3.3)).label('X'))
	OrGT = view.add(logic.Or().at((0, 3)))
	view.add(logic.Wire().at(x.start).to(OrGT.in1))
	AndGT = view.add(logic.And().at((-3, 2)).right())
	view.add(logic.Line().at(AndGT.in1).dot().left().label('Y', 'left'))
	view.add(logic.Line().at(AndGT.in2).dot().left().label('Z', 'left'))
	view.add(logic.Wire().at(AndGT.out).to(OrGT.in2))
	view.add(logic.Line().at(OrGT.out).right().label('F', 'right').dot())
    
view.draw()
