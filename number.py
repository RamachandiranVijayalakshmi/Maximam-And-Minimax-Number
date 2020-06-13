def num(a):
    print('The Orginal List Is:',a)
    b=len(a)
    print('Length Of Original List Is:',b)
    c=set(a)
    d=len(c)
    print("Atrer Remove Duplicate Number In The List:",c)
    print('Length Of Atrer Remove Duplicate Number List Is:',d)
    print('Length of Duplicate Number In The List:',(b-d))
    print('Minimam Number In The List:',min(c))
    print('Maximam Number In The List:',max(c))
number=[11,55,11,10,66,87,99,65,55,87]
num(number)
