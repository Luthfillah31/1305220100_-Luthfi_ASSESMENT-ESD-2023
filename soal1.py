input1 = [4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0]
input2 = [5,4,2.5,5,3.6,1.1,3.6,4,4.2,1.5]

def MinMaxMean(li):
    min = 9999
    max = 0
    sum = 0
    for i in li:
        if i < min:
            min = i
        if i > max:
            max = i
        sum += i
    print([min,max,sum/len(li)])

MinMaxMean(input1)
MinMaxMean(input2)

