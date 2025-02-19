import schemdraw

import schemdraw.logic as logic

d = schemdraw.Drawing()
d.config(unit=.5)

t1 = d.add(logic.Dot().at((0,3)).label('T1','left'))
t2 = d.add(logic.Dot().at((0,1)).label('T2','left'))
n1 = d.add(logic.Dot().at((0,-1.7)).label('N1','left'))
n2 = d.add(logic.Dot().at((0,-2.3)).label('N2','left'))

not_t1 = d.add(logic.Not().at((1,3)))
d.add(logic.Wire().at(t1.start).to(not_t1.in1))
not_t2 = d.add(logic.Not().at((1,1)))
d.add(logic.Wire().at(t2.start).to(not_t2.in1))

and1 = d.add(logic.And().at((3, 2)))
d.add(logic.Wire().at(not_t1.out).to(and1.in1))
d.add(logic.Wire().at(not_t2.out).to(and1.in2))


and2 = d.add(logic.And().at((3, -2)))
d.add(logic.Wire().at(n1.start).to(and2.in1))
d.add(logic.Wire().at(n2.start).to(and2.in2))

s = d.add(logic.Or().at((6, 0)).label('S','right'))
d.add(logic.Wire().at(and1.out).to(s.in1))
d.add(logic.Wire().at(and2.out).to(s.in2))


d.draw()
