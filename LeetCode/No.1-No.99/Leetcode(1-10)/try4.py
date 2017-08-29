index = 0;
str1 = str(input());
newInput = list();

for i in range( 0 , 2*len(str1)+1):
    if i%2 != 0:
        newInput.append(str1[index]);
        index += 1;
    else:
        newInput.append('$');

T = list();


for i in range(0,len(newInput)):
    T.append(0);

start = 0;
end = 0;

for i in range (0 , len(newInput)):
    while  start>0 and end< (len(newInput)-1) and (newInput[start-1] == newInput[end+1]) :
        start -= 1;
        end += 1;

    print "before" ,i, start,end;
    T[i]= end-start+1;


    if end == (len(T)-1):
        break;

    if i%2 == 0:
        newCenter = end + 1;
    else:
        newCenter = end ;

    print "center", newCenter;

    for j in range (i+1 , end+1):
        print "j:" ,j;
        print T[i - (j-i)], 2* (end - j )+1;

        T[j] = min(T[i - (j-i)] , 2* (end - j )+1);
        #if (j+T[i -(j-1)]/2) == end:
        if(j + T[i - (j - i)]/2 == end) :
            newCenter = j;
            break;


    i = newCenter;
    print "i:" , i;
    end = i + T[i]/2;

    start = i - T[i]/2;

    print "after", i, start,end;


pos = -1;
max = -1;
for i in range(0 , len(T)):
    val = T[i] /2 ;
    if max < val:
        max = val;
        pos = i;
print newInput;
print T;
print max;
print pos;
print newInput[ pos - max : pos + max]

