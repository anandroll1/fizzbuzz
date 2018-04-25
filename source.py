import csv
from collections import Counter


class SourceViews:
    path = "C:\\Users\\Anand\\Downloads\\"
    filename = open(path + "blogdata2.csv")
    readview = csv.reader(filename)
    for line in readview:
        # import pdb;pdb.set_trace()

        # source.append(line[3])

        source=[line[3],line[4],line[8],line[9],line[13],line[14],line[18],line[19],line[23],line[24]]
        # print(source)
        z=(Counter(source))
        # print(z,line[0])

        c=(max(z,key=z.get ))
        value=(z[c])
        if c=="NA":
            del z[c]
            c = (max(z, key=z.get))
            value = (z[c])
            # print(value)

        primary=value
        print(line[0]+" has more "+c+" views and count is ",value)
        del z[c]
        c = (max(z, key=z.get))
        value = (z[c])
        secondary=value
        print(line[0] + " has second more " + c + " views and count is ", value)
        # if primary==secondary:
        #     if res=="DV":


        # z.remove[c]
        # c = (max(z, key=z.get))
        # value = (z[c])
        # print(line[0] + " has more second views " + c + " views and count is ", value)