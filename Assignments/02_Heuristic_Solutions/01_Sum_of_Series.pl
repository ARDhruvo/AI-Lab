:- write('The program has been consulted').

term(N, T):- T is (100 + ((N-1) * 5)).

seriesSum(1, 100):-!.
seriesSum(N, Value):-term(N,T), N1 is N-1, seriesSum(N1, Value1),  Value is (Value1 + T).

