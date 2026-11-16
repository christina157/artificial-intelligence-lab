% Monkey Banana Problem

% Initial State
initial(state(door, onfloor, window, hasnot)).

% Goal State
goal(state(_, _, _, has)).

% Move Actions

move(state(P, onfloor, B, H),
     walk(P, P2),
     state(P2, onfloor, B, H)).

move(state(P, onfloor, P, H),
     push(P, P2),
     state(P2, onfloor, P2, H)).

move(state(P, onfloor, P, H),
     climb,
     state(P, onbox, P, H)).

move(state(middle, onbox, middle, hasnot),
     grasp,
     state(middle, onbox, middle, has)).

% Solve the Problem

solve(State, Plan) :-
    solve(State, [], Plan).

solve(State, _, []) :-
    goal(State).

solve(State, Visited, [Action|Plan]) :-
    move(State, Action, NewState),
    \+ member(NewState, Visited),
    solve(NewState, [State|Visited], Plan).

% Query
