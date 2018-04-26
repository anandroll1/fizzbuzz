import csv
from collections import Counter

mappings = {}

def get_header(header):
    return mappings.get(header)

def main():
    path = "/Users/anand/Downloads"
    file = open(path + "blogdata2.csv")
    reader = csv.reader(file)
    file2 = open("result4", "w")
    res =""

    header_flag = False

    for line in reader:
        if not header_flag:
            for index, col in enumerate(line):
                mappings[col] = index

            header_flag = True
        else:
            record = ""
            for col in range(0, 30):
                record += (line[col] + ", ")

            views = "{}, {}, {}, {}, {}".format(
                line[get_header('views1')],
                line[get_header('views2')],
                line[get_header('views3')],
                line[get_header('views4')],
                line[get_header('views5')]
            )

            # print(views)

            if line[get_header('views1')] == "NA":
                if line[get_header('views2')] == "NA":
                    if line[get_header('views3')] == "NA":
                        line[get_header('views3')] = line[get_header('views4')]
                    line[get_header('views2')] = line[get_header('views3')]
                line[get_header('views1')] = line[get_header('views2')]
                # print(line[get_header('views5')])
            try:
                if float(line[get_header('views1')]) >= float(line[get_header('views3')]) > float(line[get_header('views5')]):
                    # file2.write(line[get_header('name')] + " -- Decreasing in views \n")
                    res = "DV"
                elif float(line[get_header('views1')]) <= float(line[get_header('views3')]) < float(line[get_header('views5')]):
                    # file2.write(line[get_header('name')] + " -- increasing in views\n")
                    res = "IV"
                elif float(line[get_header('views1')]) == float(line[get_header('views3')]) == float(line[get_header('views5')]):
                    # file2.write(line[get_header('name')] + " No change in views\n")
                    res = "NC"
                elif float(line[get_header('views1')]) * .8 <= float(line[get_header('views5')]):
                    # file2.write(line[get_header('name')] + " -- No change in views\n")
                    res = "NC"
                elif float(line[get_header('views1')]) * .8 >= float(line[get_header('views5')]):
                    # file2.write(line[get_header('name')] + " -- over all decreased in views\n")
                    res = "OD"

            except Exception as e:
                print(str(e))
                # print(line[get_header('views1')], line[get_header('views3')], line[get_header('views5')], line[get_header('name')])
            print(res)
            source = [line[get_header('source1')], line[get_header('source2')], line[get_header('source3')], line[get_header('source4')], line[get_header('source5')], line[get_header('source6')], line[get_header('source7')], line[get_header('source8')], line[get_header('source9')], line[get_header('source10')]]
            # print(source)
            z = (Counter(source))
            # print(z,line[get_header('name')])

            c = (max(z, key=z.get))
            value = (z[c])
            if c == "NA":
                del z[c]
                c = (max(z, key=z.get))
                value = (z[c])
                # print(value)

            primary = value
            # print(line[get_header('name')] + " has more " + c + " views and count is ", value)
            del z[c]
            c = (max(z, key=z.get))
            value = (z[c])
            secondary = value

            # print(line[get_header('name')] + " has second more " + c + " views and count is ", value)
            if primary == secondary:
                if res == "DV":
                    file2.write(line[get_header('name')]+" having less performance\n")
                elif res=="IV":
                    file2.write(line[get_header('name')]+" well performed blog \n")
                elif res=="NC":
                    file2.write(line[get_header('name')]+" it is working with nochange in views so check with date\n")
                elif res=="OD":
                    file2.write(line[get_header('name')]+" topic might be is getting outdated\n")
            elif c=="organic":
                if res == "DV":
                    file2.write(line[get_header('name')]+" look for bounce rate and title trend status\n")
                elif res=="IV":
                    file2.write(line[get_header('name')]+" well performed blog because of title and worth to write another blog \n")
                elif res=="NC":
                    file2.write(line[get_header('name')]+" it is working good so check with bounce rate n crt content if needed\n")
                elif res=="OD":
                    file2.write(line[get_header('name')]+" topic might be is getting outdated remove check with date again\n")
            elif c=="direct":
                if res == "DV":
                    file2.write(line[get_header('name')]+" check with previous linked blog and title didn't worked well\n")
                elif res=="IV":
                    file2.write(line[get_header('name')]+" previous link is well performed blog \n")
                elif res=="NC":
                    file2.write(line[get_header('name')]+" it is working with nochange in views so check bounce rate and crt title or content if needed\n")
                elif res=="OD":
                    file2.write(line[get_header('name')]+" check with bounce rate and change linked blog and title\n")
            elif c=="social":
                if res == "DV":
                    file2.write(line[get_header('name')]+" topic trend decreases due to time\n")
                elif res=="IV":
                    file2.write(line[get_header('name')]+" it is trending topic expected as coming era, write such kind with more content bounce rate to be considered for content\n")
                elif res=="NC":
                    file2.write(line[get_header('name')]+" we can write more of such blogs but check bounce rate to crt title or content of this blog\n")
                elif res=="OD":
                    file2.write(line[get_header('name')]+" try reposting in social media and depending on bounce rate change content and title\n")

            if primary == secondary:
                if res == "DV":
                    print(line[get_header('name')]+" having less performance")
                elif res=="IV":
                    print(line[get_header('name')]+" well performed blog")
                elif res=="NC":
                    print(line[get_header('name')]+" it is working with nochange in views so check with date")
                elif res=="OD":
                    print(line[get_header('name')]+" topic might be is getting outdated")
            elif primary=="organic":
                if res == "DV":
                    print(line[get_header('name')]+" look for bounce rate and title trend status")
                elif res=="IV":
                    print(line[get_header('name')]+" well performed blog because of title and worth to write another blog ")
                elif res=="NC":
                    print(line[get_header('name')]+" it is working good so check with bounce rate n crt content if needed")
                elif res=="OD":
                    print(line[get_header('name')]+" topic might be is getting outdated remove check with date again")
            elif primary=="direct":
                if res == "DV":
                    print(line[get_header('name')]+" check with previous linked blog and title didn't worked well")
                elif res=="IV":
                    print(line[get_header('name')]+" previous link is well performed blog ")
                elif res=="NC":
                    print(line[get_header('name')]+" it is working with nochange in views so check bounce rate and crt title or content if needed")
                elif res=="OD":
                    print(line[get_header('name')]+" check with bounce rate and change linked blog and title")
            elif primary=="social":
                if res == "DV":
                    print(line[get_header('name')]+" topic trend decreases due to time")
                elif res=="IV":
                    print(line[get_header('name')]+" it is trending topic expected as coming era, write such kind with more content bounce rate to be considered for content")
                elif res=="NC":
                    print(line[get_header('name')]+" we can write more of such blogs but check bounce rate to crt title or content of this blog")
                elif res=="OD":
                    print(line[get_header('name')]+" try reposting in social media and depending on bounce rate change content and title")

            # z.remove[c]
            c = (max(z, key=z.get))
            value = (z[c])
            print(line[get_header('name')] + " has more second views " + c + " views and count is ", value)

    print(res)
    return res


if __name__ == '__main__':
    main()

