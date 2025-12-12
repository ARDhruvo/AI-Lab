parent('Hasib', 'Rakib').
parent('Rakib','Sohel').
parent('Rakib','Rebeka').
parent('Rashid','Hasib').
parent('Rebeka','Ayesha').
parent('Sohel','Fatima').
male('Hasib').
male('Rakib').
male('Sohel').
male('Rashid').

grandparent(X,Z):-parent(X,Y),parent(Y,Z).
brother(X,Z):-parent(Y,X),parent(Y,Z),male(X),not(X=Z).
sister(X,Z):-parent(Y,X),parent(Y,Z),not(male(X)),not(X=Z).
uncle(X,Z):-parent(Y,Z),brother(X,Y).
aunt(X,Z):-parent(Y,Z),sister(X,Y).


findGp:-write('Grandchild: '),read(X),write('Grandparents: '),
    grandparent(Gp,X),write(Gp),tab(5),fail.
findGp.

findBrother:-write('Sibling: '),read(X),write('Brothers: '),
    brother(Bro,X),write(Bro),tab(5),fail.
findBrother.

findSister:-write('Sibling: '),read(X),write('Sisters: '),
    sister(Sis,X),write(Sis),tab(5),fail.
findSister.


findUncle:-write('Niece/Nephew: '),read(X),write('Uncles: '),
    uncle(Unc,X),write(Unc),tab(5),fail.
findUncle.

findAunt:-write('Niece/Nephew: '),read(X),write('Aunt: '),
    aunt(Ant,X),write(Ant),tab(5),fail.
findAunt.