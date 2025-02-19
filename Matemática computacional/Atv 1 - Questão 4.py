import ttg

tabela = ttg.Truths(['P', 'D', 'S', 'T'],['(D and S and T) or (P and S) or (P and T) or (P and D)'])
print("TABELA VERDADE")
print(tabela)

#----------------------------------------------------------------------------------
import schemdraw
import schemdraw.logic as logic
with schemdraw.Drawing() as view:
	view.config(unit=.4)
	
	D1 =view.add(logic.Dot().at((0, 8)).label('D','left'))
	S1 =view.add(logic.Dot().at((0, 7)).label('S','left'))
	T1 =view.add(logic.Dot().at((0, 6)).label('T','left'))
	and1 =view.add(logic.And(inputs=3).at((2,7)))
	view.add(logic.Wire().at(D1.start).to(and1.in1))
	view.add(logic.Wire().at(S1.start).to(and1.in2))
	view.add(logic.Wire().at(T1.start).to(and1.in3))
	
	P1 =view.add(logic.Dot().at((0, 4)).label('P','left'))
	S2 =view.add(logic.Dot().at((0, 3)).label('S','left'))
	and2 =view.add(logic.And().at((2, 3.5)))
	view.add(logic.Wire().at(P1.start).to(and2.in1))
	view.add(logic.Wire().at(S2.start).to(and2.in2))
	
	P2 =view.add(logic.Dot().at((0, 1)).label('P','left'))
	T2 =view.add(logic.Dot().at((0, 0)).label('T','left'))
	and3 =view.add(logic.And().at((2, 0.5)))
	view.add(logic.Wire().at(P2.start).to(and3.in1))
	view.add(logic.Wire().at(T2.start).to(and3.in2))
	
	P3 =view.add(logic.Dot().at((0, -2)).label('P','left'))
	D2 =view.add(logic.Dot().at((0, -3)).label('D','left'))
	and4 =view.add(logic.And().at((2, -2.5)))
	view.add(logic.Wire().at(P3.start).to(and4.in1))
	view.add(logic.Wire().at(D2.start).to(and4.in2))
	
	Or=view.add(logic.Or(inputs=4).at((5, 2)))
	view.add(logic.Wire().at(and1.out).to(Or.in1))
	view.add(logic.Wire().at(and2.out).to(Or.in2))
	view.add(logic.Wire().at(and3.out).to(Or.in3))
	view.add(logic.Wire().at(and4.out).to(Or.in4))
	
view.draw()
