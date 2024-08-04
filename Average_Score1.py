grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
rating=[sum(grades[0])/len(grades[0]),
        sum(grades[1])/len(grades[1]),
        sum(grades[2])/len(grades[2]),
        sum(grades[3])/len(grades[3]),
        sum(grades[4])/len(grades[4])]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Students=sorted(students)
Average_score={Students[0]:rating[0],
               Students[1]:rating[1],
               Students[2]:rating[2],
               Students[3]:rating[3],
               Students[4]:rating[4]}
print(Average_score)


