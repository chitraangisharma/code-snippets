import urllib2
import json
import itertools
import csv

#######
# 1
data = urllib2.urlopen("http://jsonplaceholder.typicode.com/todos")
anchor = data.read()
anchor = json.loads(anchor)
response = {'true_d':0, 'false_d':0}
for anch in anchor:
    if anch['completed'] == True:
        response['true_d'] = response['true_d'] + 1
    if anch['completed'] == False:
        response['false_d'] = response['false_d'] + 1
print response
#######


#######
# 2
res=[]
for key, group in itertools.groupby(anchor, lambda item: item["userId"]):
    grp1, grp2 = itertools.tee(group)
    sum_t=sum([item["completed"]==True for item in grp1])
    sum_f=sum([item["completed"]==False for item in grp2])
    dum_d={}
    dum_d[key]={'true':sum_t, 'false':sum_f}
    res.append(dum_d)
print res
#ANS: [{1: {'false': 9, 'true': 11}}, {2: {'false': 12, 'true': 8}}, {3: {'false': 13, 'true': 7}}, {4: {'false': 14, 'true': 6}}, {5: {'false': 8, 'true': 12}}, {6: {'false': 14, 'true': 6}}, {7: {'false': 11, 'true': 9}}, {8: {'false': 9, 'true': 11}}, {9: {'false': 12, 'true': 8}}, {10: {'false': 8, 'true': 12}}]
#######


#######
# 3
fo = open("data.csv", "w")
writer = csv.writer(fo)
writer.writerow(('user', 'id', 'title', 'completed'))

for anch in anchor:
    writer.writerow([anch['userId'], anch['id'], anch['title'], anch['completed']])
#######


#######
# 4
my_dict = {}
for i in range(1,123):
    my_dict[i] = unichr(i)
print my_dict
#######


#######
# 5
find_sentence = [[72, 101, 108, 108, 111], 0, [102, 114, 111, 109], 1,\
[67, 104, 105, 116, 114, 97, 97, 110, 103, 105, None], 2, [33, 33, 33], [58, 45, 41], 3]
sent=[]
for fin in find_sentence:
    if isinstance( fin, int ):
        if fin in my_dict:
            sent.append(str(my_dict[fin]))
    if isinstance( fin, list ):
        for lev in fin:
            if lev in my_dict:
                sent.append(str(my_dict[lev]))
the_sentence = ''.join(sent)
print the_sentence
#ANS: HellofromChitraangi!!!:-)
#######
