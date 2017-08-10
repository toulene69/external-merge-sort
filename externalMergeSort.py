import itertools
from itertools import islice, imap
import heapq
import tempfile

def sortNumericFile():
    file = open("i2.txt","r")
    temp_files = []
    e = []
    while True:
        temp_file = tempfile.TemporaryFile()
        e = list(islice(file,2))
        if not e:
            break
        # e.sort(key=lambda line:int(line.split()[1]))
        e.sort(key=lambda line: int(line.split()[0]))
        temp_file.writelines(e)
        temp_files.append(temp_file)
        temp_file.flush()
        temp_file.seek(0)
    file.close()

    with open('o.txt', 'w') as out:
        out.writelines(imap('{}\n'.format, heapq.merge(*(imap(int, f) for f in temp_files))))
    out.close()


def sortAlphanumericFile():
    f = open("i1.txt", "r")
    temp_files = []
    e = []
    while True:
        temp_file = tempfile.NamedTemporaryFile()
        e = list(islice(f, 4))
        if not e:
            temp_file.close()
            break
        # e.sort(key=lambda line:int(line.split()[1]))
        e.sort(key=lambda line: int(line.split()[1]))
        temp_file.writelines(e)
        temp_files.append(temp_file)
        temp_file.flush()
        temp_file.seek(0)
    f.close()

    aux = []
    z = 0
    while len(temp_files) != 1:
        while z < len(temp_files)-1:
            tem = tempfile.NamedTemporaryFile()
            t1 = temp_files[z]
            t2 = temp_files[z+1]
            t1.seek(0)
            t2.seek(0)
            n = 2
            e1 = None
            e2 = None
            while True:
                if not e1:
                    e1 = list(islice(t1, 2))
                if not e2:
                    e2 = list(islice(t2, 2))
                if not e1 and not e2:
                    break
                elif e1 and not e2:
                    tem.writelines(imap('{}'.format,e1))
                    e1 = None
                    continue
                elif not e1 and e2:
                    tem.writelines(imap('{}'.format,e2))
                    e2 = None
                    continue
                i = 0
                j = 0
                while i<len(e1) and j<len(e2):
                    l1 = e1[i]
                    l2 = e2[j]
                    if int(l1.split()[1]) == int(l2.split()[1]):
                        tem.writelines(imap('{}'.format,[l1,l2]))
                        i+=1
                        j+=1
                    elif int(l1.split()[1]) < int(l2.split()[1]):
                        tem.writelines(imap('{}'.format,[l1]))
                        i+=1
                    else:
                        tem.writelines(imap('{}'.format,[l2]))
                        j+=1
                if i>=len(e1):
                    e1 = None
                else:
                    e1 = e1[i:]
                if j>= len(e2):
                    e2 = None
                else:
                    e2 = e2[j:]
            z+=2
            aux.append(tem)
            t1.close()
            t2.close()
            tem.flush()
            tem.seek(0)
        temp_files = aux
        z = 0
        aux = []
    with open("o.txt",'w') as out:
        out.writelines(imap('{}'.format , temp_files[0]))

sortAlphanumericFile()