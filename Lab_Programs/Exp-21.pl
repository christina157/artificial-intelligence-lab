% Bird Database

bird(parrot).
bird(eagle).
bird(pigeon).
bird(penguin).
bird(ostrich).

% Birds that can fly

flying(parrot).
flying(eagle).
flying(pigeon).

% Rules

can_fly(X) :-
    bird(X),
    flying(X).

cannot_fly(X) :-
    bird(X),
    \+ flying(X).
