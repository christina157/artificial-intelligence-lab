% Family Tree

male(ramesh).
male(arun).
male(kumar).

female(lakshmi).
female(priya).
female(riya).

parent(ramesh, arun).
parent(lakshmi, arun).

parent(ramesh, priya).
parent(lakshmi, priya).

parent(arun, riya).

% Rules

father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

brother(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    male(X),
    X \= Y.

sister(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    female(X),
    X \= Y.
