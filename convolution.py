import numpy
from pandas import read_csv
import csv
import re



def division(b):
    
    if b[0:2] == 'RT':
        b = b[2:]

    r = []        
    
    while b.find('@') != -1:
        if (b.find(' ', b.find('@'))) != -1:
            r.append(b.find(' ', b.find('@')))
        else:
            r.append(len(b))
        if (b.find(',', b.find('@'))) != -1:
            r.append(b.find(',', b.find('@')))
        else:
            r.append(len(b))
        if (b.find('\n', b.find('@'))) != -1:
            r.append(b.find('\n', b.find('@')))  
        else:
            r.append(len(b))
            
        b=b[:b.find('@')]+b[(min(r)):]
        r = []    
            
    while b.find('http:/') != -1:

        if (b.find(' ', b.find('http:/'))) != -1:
            r.append(b.find(' ', b.find('http:/')))
        else:
            r.append(len(b))
        if (b.find(',', b.find('http:/'))) != -1:
            r.append(b.find(',', b.find('http:/')))
        else:
            r.append(len(b))
        if (b.find('\n', b.find('http:/'))) != -1:
            r.append(b.find('\n', b.find('http:/')))  
        else:
            r.append(len(b))
            
        b=b[:b.find('http:/')]+b[(min(r)):]
        r = [] 
    
    b.replace('&lt;3', '')
    b.replace('#', ' ')
    while b.find(':') != -1:
        if (b.find(' ', b.find(':'))) != -1:
            r.append(b.find(' ', b.find(':')))
        else:
            r.append(len(b))
        
        if (b.find(',', b.find(':'))) != -1:
            r.append(b.find(',', b.find(':')))
        else:
            r.append(len(b))
        
        if (b.find('\n', b.find(':'))) != -1:
            r.append(b.find('\n', b.find(':')))  
        else:
            r.append(len(b))
            
        b=b[:b.find(':')]+b[(min(r)):]
        r = []    
    
    tr = 0
    q = []
    for i in range(len(b)):
        if ((b[i] == ' ')or(b[i] == ',')or(b[i] == '.')or(b[i] == '—')or(b[i] == '?'))and((tr == ' ')or(tr == ',')or(tr == '.')or(tr == '-')or(tr == '—')or(tr == '?')):
            q.append(i)
        tr = b[i]
    
    tr = 0
    for i in range(len(q)):
        b=b[:(q[i]-i)]+b[(q[i]+1-i):]
        tr+=q[i]
    
    x = 0
    for i in range(len(b)):
        if b.find(' ',i)!= -1:
            x = x + 1
            i+=b.find(' ')
    
    i = 0
    x1 = []
    x2 = []
    
    for i in range(len(b)):
        if (b[i]==' ')or(b[i]==',')or(b[i]=='\n')or(b[i]=='.')or(b[i] == '?')or(b[i]=='-')or(b[i]==')'):
            x1.append(i)
    
    x1.insert(0,0)
    x1.append(len(b))
    for i in range(len(x1)-1):
        if i == 0:
            x2.append(b[(x1[i]):(x1[i+1])])
        else:
            x2.append(b[(x1[i]+1):(x1[i+1])])
    ix2 = 0
    
    for i in range(len(x2)):
        if x2[i-ix2] == '':
            x2=x2[:(i-ix2)]+x2[(i+1-ix2):]
            ix2 +=1
    ix2 = 0
    for i in range(len(x2)):
        x2[i-ix2] = re.sub(r'[^\w\s]+|[\d]+', r'',x2[i-ix2]).strip()
        
        if x2[i-ix2] == '':
            x2=x2[:i-ix2]+x2[i+1-ix2:]
            ix2+=1
        x2[i-ix2]= x2[i-ix2].lower()    
        
    return x2 
    
def main():
    

    positive = read_csv('positive.csv', sep=';', skiprows=[0], header=None)    
    negaive = read_csv('negative.csv', sep=';', skiprows=[0], header=None)
    output_file_positive = open("positive2.csv", "wb")
    sum_b = 0
    razn_b = []
    ne_b = []
    vir_b = 0
    dic = []
    
    for i in range(5000):
        
        b = positive[3][i]
        #print(b)
        raz_b = division(b)
        
        #print(b,raz_b)
        
        for i_b in range(len(raz_b)):
        
            if raz_b[i_b] in dic:
                vir_b +=1
                #razn_b.append(sum_b)
                
            else:
                
                
                dic.append(raz_b[i_b])
                
                #print(i, sum_b,raz_b[i_b])
                sum_b+=1
        print(i, vir_b,sum_b)
    
    print(len(dic))

    
                
        

    
    
main()