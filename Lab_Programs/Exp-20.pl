% Towers of Hanoi

hanoi(1, Source, Destination, _) :-
    write('Move disk from '),
    write(Source),
    write(' to '),
    write(Destination),
    nl.

hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Auxiliary, Destination),
    hanoi(1, Source, Destination, Auxiliary),
    hanoi(M, Auxiliary, Destination, Source).
