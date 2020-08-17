if __name__ == '__main__':
    student = []
    for i in range(int(input("Enter Students' count: "))):
        student.append([input(), float(input())])

#    highest = max(student)
#    print(highest)
#     import pdb;
#     pdb.set_trace()
    student.sort(key= lambda k:k[1])
    lowest = student[0][1]
    nextLowest = student[1][1]

    for i in range(len(student)):
        if lowest == nextLowest:
            lowest = student[i][1]
            nextLowest = student[i+1][1]

#    print(h2)
    final = []
    for i in range(len(student)):
        if student[i][1] == nextLowest:
#            print(student[i][0])
            final.append(student[i][0])

    final.sort()

    for name in final:
        print(name)
# --------------------------------------------------------------------------------------------------

    # student.sort(key=lambda x: (x[1],x[0]))
    # names = [i[0] for i in student]
    # marks = [i[1] for i in student]
    # min_val=min(marks)
    # while marks[0]==min_val:
    #     marks.remove(marks[0])
    #     names.remove(names[0])
    # for x in range(0,len(marks)):
    #     if marks[x]==min(marks):
    #         print(names[x])