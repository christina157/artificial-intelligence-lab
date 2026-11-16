% Backward Chaining

% Initial Facts

fact(rain).
fact(cloudy).

% Rules

rule(wet_ground, [rain]).
rule(carry_umbrella, [rain]).
rule(weather_change, [cloudy, rain]).

% Backward Chaining

prove(X) :-
    fact(X).

prove(X) :-
    rule(X, Conditions),
    check(Conditions).

% Check Conditions

check([]).

check([H|T]) :-
    prove(H),
    check(T).


