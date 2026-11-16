% Forward Chaining

:- dynamic known/1.

% Initial Facts

known(rain).
known(cloudy).

% Rules

rule(wet_ground) :-
    known(rain).

rule(carry_umbrella) :-
    known(rain).

rule(weather_change) :-
    known(cloudy),
    known(rain).

% Forward Chaining

forward :-
    rule(X),
    \+ known(X),
    !,
    assertz(known(X)),
    forward.

forward.
