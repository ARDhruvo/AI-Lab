:- write('The program has been consulted').

% KB (Graph)
edge(i, a, 35).
edge(i, b, 45).
edge(a, c, 22).
edge(a, d, 32).
edge(b, d, 28).
edge(b, e, 36).
edge(b, f, 27).
edge(c, d, 31).
edge(c, g, 47).
edge(d, g, 30).
edge(e, g, 26).

% Rules and Predicates

length(Src, Dst, Cost):- edge(Src, Dst, Cost),!.
length(Src, Dst, Cost):- edge(Src, Node, CostSrcNode), length(Node, Dst, CostDstNode), Cost is (CostSrcNode+ CostDstNode).
