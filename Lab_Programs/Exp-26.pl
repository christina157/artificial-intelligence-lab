% Best First Search Algorithm

edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).

heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 3).
heuristic(d, 5).
heuristic(e, 2).
heuristic(f, 1).
heuristic(g, 0).

best_first(Start, Goal, Path) :-
    heuristic(Start, H),
    best_search([H-[Start]], Goal, [], RevPath),
    reverse(RevPath, Path).

best_search([_-[Goal|Path]|_], Goal, _, [Goal|Path]).

best_search([_-[Node|Path]|Rest], Goal, Visited, Result) :-
    findall(H-[Next,Node|Path],
        (edge(Node, Next),
         \+ member(Next, Visited),
         heuristic(Next, H)),
        NewNodes),
    append(Rest, NewNodes, Open),
    keysort(Open, Sorted),
    best_search(Sorted, Goal, [Node|Visited], Result).
