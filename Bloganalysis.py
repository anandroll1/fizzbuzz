import csv
from collections import Counter

mappings = {}
line = ""
file2 = open("result5", "w")
sourcereslt=""


def get_header(header):
    return mappings.get(header)

def main():
    path = "/Users/anand/Downloads/"
    file = open(path + "blogdata2.csv")
    reader = csv.reader(file)
    res =""
    bounce=""

    header_flag = False

    for line in reader:
        
        if not header_flag:
            for index, col in enumerate(line):
                mappings[col] = index

            header_flag = True
        else:
            record = ""
            for col in range(0, 26):
                record += (line[col] + ", ")
            print (sourceRate(line))
                # print(sourcereslt)

def subscribers():
    pass

def bounceRate(line):
    if line[get_header('bounce1')]>line[get_header('bounce3')]>line[get_header('bounce5')]:
        bounce="GoodDB"
        return bounce
    elif line[get_header('bounce1')]<line[get_header('bounce3')]<line[get_header('bounce5')]:
        bounce="BadIB"
        return bounce
    elif line[get_header('bounce1')]>line[get_header('bounce5')]:
        bounce="DB"
        return bounce
    elif line[get_header('bounce1')]<line[get_header('bounce5')]:
        bounce="IB"
        return bounce
    elif line[get_header('bounce1')]==line[get_header('bounce5')]:
        bounce="SameB"
        return bounce

def sourceRate(line):
    source = [line[get_header('source1')], line[get_header('source2')], line[get_header('source3')],
              line[get_header('source4')], line[get_header('source5')], line[get_header('source6')],
              line[get_header('source7')], line[get_header('source8')], line[get_header('source9')],
              line[get_header('source10')]]
    if line[get_header('views1')] == "NA":
        if line[get_header('views2')] == "NA":
            if line[get_header('views3')] == "NA":
                line[get_header('views3')] = line[get_header('views4')]
            line[get_header('views2')] = line[get_header('views3')]
        line[get_header('views1')] = line[get_header('views2')]

    sourcecount = (Counter(source))
    c = (max(sourcecount, key=sourcecount.get))
    value = (sourcecount[c])
    if c == "NA":
        del sourcecount[c]
        c = (max(sourcecount, key=sourcecount.get))
        value = (sourcecount[c])
    primary = c
    del sourcecount[c]
    c = (max(sourcecount, key=sourcecount.get))
    value = (sourcecount[c])
    secondary = c
    # return secondary
    if primary == secondary:
        if bounceRate(line)=="GoodDB":
            file2.write(line[get_header('name')] + " is working good with "+bounceRate(line)+"\n")
            return sourcereslt
        elif bounceRate(line) == "BadIB":
            file2.write(line[get_header('name')] + " poor performance with "+bounceRate(line)+"\n")
            return sourcereslt
        elif bounceRate(line) == "DB":
            file2.write(line[get_header('name')] + " check with change in source and make it more published, since it has "+bounceRate(line)+"\n")
            return sourcereslt
        elif bounceRate(line) == "IB":
            file2.write(line[get_header('name')] + " check with avg time and title matching content, "
                                                   "either cta or out dated content or not related to what they are looking for "+"\n")
            return sourcereslt

    elif primary == "organic":
        if bounceRate(line)=="GoodDB":
            file2.write(line[get_header('name')] + " is working good with "+bounceRate(line)+" in "+c+", write more with titlename\n")
            return sourcereslt
        elif bounceRate(line) == "BadIB":
            file2.write(line[get_header('name')] + " poor performance with "+bounceRate(line)+" in "+c+", check avgtime content mismatch or cta\n")
            return sourcereslt
        elif bounceRate(line) == "DB":
            file2.write(line[get_header('name')] + " it created interest to see more, since it has "+bounceRate(line)+" in "+c+"\n")
            return sourcereslt
        elif bounceRate(line) == "IB":
            file2.write(line[get_header('name')] + " check with avg time and title matching content, either cta or out dated content or not related to what they are looking for "+bounceRate(line)+" in "+c+"\n")
            return sourcereslt
    elif primary == "direct":
        if bounceRate(line)=="GoodDB":
            file2.write(line[get_header('name')] + " change title for to increase organic "+bounceRate(line)+" in "+c+", write more with such content\n")
            return sourcereslt
        elif bounceRate(line) == "BadIB":
            file2.write(line[get_header('name')] + " see the previous blogs to where it linked, since it has "+bounceRate(line)+" in "+c+"\n")
            return sourcereslt
        elif bounceRate(line) == "DB":
            file2.write(line[get_header('name')] + " content is good so try some title for oraganic views, since it has "+bounceRate(line)+" in "+c+"\n")
            return sourcereslt
        elif bounceRate(line) == "IB":
            file2.write(line[get_header('name')] + " check out dated content or not related to what they are looking for "+bounceRate(line)+" in "+c+"\n")
            return sourcereslt
    elif primary == "social":
        if bounceRate(line) == "GoodDB":
            file2.write(line[get_header(
                'name')] + " change title for to increase organic " + bounceRate(line) + " in " + c + ", write more with such content\n")
            return sourcereslt
        elif bounceRate(line) == "BadIB":
            file2.write(line[get_header(
                'name')] + " see the previous blogs to where it linked, since it has " + bounceRate(line) + " in " + c + "\n")
            return sourcereslt
        elif bounceRate(line) == "DB":
            file2.write(line[get_header(
                'name')] + " content is good so try some title for oraganic views, since it has " + bounceRate(line) + " in " + c + "\n")
            return sourcereslt
        elif bounceRate(line) == "IB":
            file2.write(line[get_header(
                'name')] + " check out dated content or not related to what they are looking for " + bounceRate(line) + " in " + c + "\n")
            return sourcereslt

if __name__ == '__main__':

    main()


