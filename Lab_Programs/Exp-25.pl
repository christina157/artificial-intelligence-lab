% Fruit and Colour Database

fruit(apple, red).
fruit(banana, yellow).
fruit(grapes, green).
fruit(orange, orange).
fruit(mango, yellow).
fruit(cherry, red).

% Rule

fruit_color(Fruit, Color) :-
    fruit(Fruit, Color).
