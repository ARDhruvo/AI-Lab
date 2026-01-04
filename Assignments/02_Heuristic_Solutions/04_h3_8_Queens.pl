:- write('The program has been consulted').
:- dynamic(hval/1).

% Height Check

nthel(N,[_|T],El):- N1 is N-1, nthel(N1,T,El).
nthel(1,[H|_],H):-!.

incr_hval:-hval(V), V1 is V+1, retract(hval(_)), assert(hval(V1)).

do_incr(X,Y):- X=Y, incr_hval.
do_incr(_,_).

chk_incr(8,_,_):-!.
chk_incr(I,L,X):- I1 is I+1, nthel(I1,L,Y), do_incr(X,Y), chk_incr(I1,L,X).

hl(8,_):-!.
hl(I,L):- nthel(I,L,X), chk_incr(I,L,X), I1 is I+1, hl(I1,L).

% Diagonal Up

doup_incr(X,Y,K1):- X1 is X+K1, Y=X1, incr_hval.
doup_incr(_,_,_).

chkup_incr(8,_,_,_):-!.
chkup_incr(I,L,X,K):- I1 is I+1, nthel(I1,L,Y), K1 is K+1, doup_incr(X,Y,K1), chkup_incr(I1,L,X,K1).

di_up(8,_):-!.
di_up(I,L):- nthel(I,L,X), chkup_incr(I,L,X,0), I1 is I+1, di_up(I1,L).


% Diagonal Down

dodn_incr(X,Y,K1):- X1 is X-K1, Y=X1, incr_hval.
dodn_incr(_,_,_).

chkdn_incr(8,_,_,_):-!.
chkdn_incr(I,L,X,K):- I1 is I+1, nthel(I1,L,Y), K1 is K+1, dodn_incr(X,Y,K1), chkdn_incr(I1,L,X,K1).

di_dn(8,_):-!.
di_dn(I,L):- nthel(I,L,X), chkdn_incr(I,L,X,0), I1 is I+1, di_dn(I1,L).

% Evaluation State

evalState(L,V):- assert(hval(0)),hl(1,L), di_up(1,L), di_dn(1,L), hval(V), retractall(hval(_)).












