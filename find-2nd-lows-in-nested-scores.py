# Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format

# The first line contains an integer,N , the number of students.
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

# TEST CASE 1:
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# [[Harry, 37.21]]

# TEST CASE 2:
# 5
# Harry
# 42
# Berry
# 37
# Tina
# 37
# Akriti
# 37
# Harsh
# 39

# TEST CASE 3:
# 7
# Harry
# 39
# Berry
# 37.21
# Tina
# 37.21
# Akriti
# 39
# Harsh
# 42
# Juba
# 39
# Shovo
# 45


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if len(students) == 0:
            students.append([name, score])
        else:
            for s in range(len(students)):
                if score <= students[s][1]:
                    students.insert(s, [name, score])
                    break
            else:
                students.append([name, score])

    low = students[0][1]
    for a in range(len(students)):
        if students[0][1] == low:
            del students[0]

    answer = []
    for x in range(len(students)):
        if students[x][1] == students[0][1]:
            answer.append(students[x][0])
        else:
            break
    answer.sort()
    print(*answer, sep='\n')
