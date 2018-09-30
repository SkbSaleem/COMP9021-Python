if 3==3:
    print("first if")
    n = 2
    m = 3
if 2 == 0:
    print("second if")
    print(n)
#elif 5 ==5:
#    print("first elif")
#    print(m)
if 5>2:
    print("something")
#elif 3==3:
#    print("second elif")
else:
    print("else")
    print (m,n)
print("will be prented always")

"""
Conclusion:
    >only one else statemnt can be used in the end.
    >if statemnet will always be executed.
    >elif statment will only execute if the leading if statemt is false.
    >the moment elif statement True, rest of all elif and else statement will not be executed.
    >BUT the if statement after true elif statement will be executed anyway.
    >if statement can be used after elif.
"""
