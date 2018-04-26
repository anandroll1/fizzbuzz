import csv
from collections import Counter

mappings = {}

def get_header(header):
    return mappings.get(header)

def main():
    path = "/Users/anand/Downloads/"
    file = open(path + "blogdata2.csv")
    reader = csv.reader(file)
    file2 = open("resultnew", "w")
    res =""
    bouncereslt=""

    header_flag = False
    def subscribers():
        pass
    return
    def bounceRate():
        if line[get_header('bounce1')]>line[get_header('bounce3')]>line[get_header('bounce5')]:
            bouncereslt="GoodDB"
            return bounce
        elif line[get_header('bounce1')]<line[get_header('bounce3')]<line[get_header('bounce5')]:
            bouncereslt="BadIB"
            return bounce
        elif line[get_header('bounce1')]>line[get_header('bounce5')]:
            bouncereslt="DB"
            return bounce
        elif line[get_header('bounce1')]<line[get_header('bounce5')]:
            bouncereslt="IB"
            return bounce
        elif line[get_header('bounce1')]==line[get_header('bounce5')]:
            bouncereslt="SameB"
            return bounce
    def sourceRate():
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
        primary = value
        del sourcecount[c]
        c = (max(sourcecount, key=sourcecount.get))
        value = (sourcecount[c])
        secondary = value
        # return secondary
        if primary == secondary:
            if bounceRate()=="GoodDB":
                file2.write(line[get_header('name')] + " is working good with "+bounceRate()+"\n")
                return (sourcereslt)
            elif bounceRate() == "BadIB":
                file2.write(line[get_header('name')] + " poor performance with "+bounceRate()+"\n")
                return (sourcereslt)
            elif bounceRate() == "DB":
                file2.write(line[get_header('name')] + " check with change in source and make it more published, since it has "+bounceRate()+"\n")
                return (sourcereslt)
            elif bounceRate() == "IB":
                file2.write(line[get_header('name')] + " check with avg time and title matching content, either cta or out dated content or not related to what they are looking for"+"\n")
                return (sourcereslt)

        elif c == "organic":
            if bounceRate()=="GoodDB":
                file2.write(line[get_header('name')] + " is working good with "+bounceRate()+"in "+c+", write more with titlename\n")
                return sourcereslt
            elif bounceRate() == "BadIB":
                file2.write(line[get_header('name')] + " poor performance with "+bounceRate()+"in "+c+", check avgtime content mismatch or cta\n")
                return sourcereslt
            elif bounceRate() == "DB":
                file2.write(line[get_header('name')] + " it created interest to see more, since it has "+bounceRate()+"in "+c+"\n")
                return sourcereslt
            elif bounceRate() == "IB":
                file2.write(line[get_header('name')] + " check with avg time and title matching content, either cta or out dated content or not related to what they are looking for"+bounceRate()+"in "+c+"\n")
                return sourcereslt
        elif c == "direct":
            if bounceRate()=="GoodDB":
                file2.write(line[get_header('name')] + " change title for to increase organic "+bounceRate()+"in "+c+", write more with such content\n")
                return sourcereslt
            elif bounceRate() == "BadIB":
                file2.write(line[get_header('name')] + " see the previous blogs to where it linked, since it has "+bounceRate()+"in "+c+"\n")
                return sourcereslt
            elif bounceRate() == "DB":
                file2.write(line[get_header('name')] + " content is good so try some title for oraganic views, since it has "+bounceRate()+"in "+c+"\n")
                return sourcereslt
            elif bounceRate() == "IB":
                file2.write(line[get_header('name')] + " check out dated content or not related to what they are looking for "+bounceRate()+"in "+c+"\n")
                return sourcereslt
        elif c == "social":
            if bounceRate() == "GoodDB":
                file2.write(line[get_header(
                    'name')] + " change title for to increase organic " + bounceRate() + "in " + c + ", write more with such content\n")
                return sourcereslt
            elif bounceRate() == "BadIB":
                file2.write(line[get_header(
                    'name')] + " see the previous blogs to where it linked, since it has " + bounceRate() + "in " + c + "\n")
                return sourcereslt
            elif bounceRate() == "DB":
                file2.write(line[get_header(
                    'name')] + " content is good so try some title for oraganic views, since it has " + bounceRate() + "in " + c + "\n")
                return sourcereslt
            elif bounceRate() == "IB":
                file2.write(line[get_header(
                    'name')] + " check out dated content or not related to what they are looking for " + bounceRate() + "in " + c + "\n")
                return sourcereslt

    for line in reader:
        if not header_flag:
            for index, col in enumerate(line):
                mappings[col] = index

            header_flag = True
        else:
            for col in range(0, 30):
                print (sourceRate())
if __name__ == '__main__':
    main()


