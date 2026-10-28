

# Decision Tree Implementation

def decision_tree(study_hours, attendance):
    if study_hours >= 2:
        if attendance >= 75:
            return "Pass"
        else:
            return "Fail"
    else:
        return "Fail"

# Input
hours = int(input("Enter study hours: "))
attendance = int(input("Enter attendance percentage: "))

# Prediction
result = decision_tree(hours, attendance)

print("Prediction:", result)
