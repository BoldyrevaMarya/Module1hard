grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {"Johny","Bilbo","Steve","Khendrik","Aaron"}
a=sum(grades[0])/len(grades[0])
print(a)
b=sum(grades[1])/len(grades[1])
print(b)
c=sum(grades[2])/len(grades[2])
print(c)
d=sum(grades[3])/len(grades[3])
print(d)
e=sum(grades[4])/len(grades[4])
print(e)
dictionary={"Aaron":a,"Bilbo":b,"Johny":c,"Khendrik":d,"Steve":e}
print(dictionary)
average_rating = (sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),
                  sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4]))
print(average_rating)
average_rating = dict(zip(dictionary,average_rating))
print(average_rating)