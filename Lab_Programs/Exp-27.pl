% Medical Diagnosis System

symptom(ravi, fever).
symptom(ravi, cough).
symptom(ravi, headache).

symptom(anu, sneezing).
symptom(anu, cough).

% Diagnosis Rules

disease(X, flu) :-
    symptom(X, fever),
    symptom(X, cough).

disease(X, common_cold) :-
    symptom(X, sneezing),
    symptom(X, cough).
