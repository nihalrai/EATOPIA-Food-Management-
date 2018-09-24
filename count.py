import operator
def recommend():
    file=open('Order.txt','r')
    line=file.readlines()
    string = line
    dict = {}
    for item in string:
         if item in dict:
             dict[item] += 1
         else:
              dict[item] = 1
    list1=dict.items()
    print(max(dict.items(), key=operator.itemgetter(1))[0])
    
