def grade_classifier(score):
    if score >= 90:
        return "Distinction"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"

test_scores = [95, 82, 89, 73, 59]
for s in test_scores:
    print(f"Score: {s} -> {grade_classifier(s)}")

print("\nRunning loop for given scores---------------------------\n")
scores = [45, 72, 91, 60, 38, 85]
for s in scores:
    result = grade_classifier(s)
    print(f"Score: {s} -> {result}")