% Diet Suggestion Based on Disease

diet(diabetes, 'Whole grains and vegetables').
diet(hypertension, 'Low salt foods and fruits').
diet(anemia, 'Iron rich foods like spinach').
diet(obesity, 'Balanced meals with vegetables').
diet(fever, 'Fluids and nutritious foods').

% Rule

suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).
