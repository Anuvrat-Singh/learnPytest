if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    final_values = student_marks[query_name]
    print("{0:.2f}".format(sum(final_values)/(len(student_marks))))