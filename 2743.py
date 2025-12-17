gpa_dict = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0,
       "+": 0.3, "-": -0.3, "0": 0, " ": 0}
gpa = input() + " "

print(gpa_dict[gpa[0]] + gpa_dict[gpa[1]])