import csv
from collections import Counter

mappings = {}

def get_header(header):
    return mappings.get(header)

def main():
    path = "C:\\Users\\Anand\\Downloads\\"
    file = open(path + "blogdata2.csv")
    reader = csv.reader(file)
    file2 = open("result4", "w")
    res =""

    header_flag = False
    def subscribers():
        pass
    return
    def bounceRate():
        if line[get_header('bounce1')]>line[get_header('bounce3')]>line[get_header('bounce5')]:
            bounce="GoodDB"
            return (bounce)
        elif line[get_header('bounce1')]<line[get_header('bounce3')]<line[get_header('bounce5')]:
            bounce="BadIB"
            return (bounce)
        elif line[get_header('bounce1')]>line[get_header('bounce5')]:
            bounce="DB"
            return (bounce)
        elif line[get_header('bounce1')]<line[get_header('bounce5')]:
            bounce="IB"
            return (bounce)
        elif line[get_header('bounce1')]==line[get_header('bounce5')]:
            bounce="SameB"
            return (bounce)
    def sourceRate():
        source = [line[get_header('source1')], line[get_header('source2')], line[get_header('source3')],
                  line[get_header('source4')], line[get_header('source5')], line[get_header('source6')],
                  line[get_header('source7')], line[get_header('source8')], line[get_header('source9')],
                  line[get_header('source10')]]
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
        if primary == secondary:
            if res == "DV":
                file2.write(line[get_header('name')] + " having less performance\n")
            elif res == "IV":
                file2.write(line[get_header('name')] + " well performed blog \n")
            elif res == "NC":
                file2.write(line[get_header('name')] + " it is working with nochange in views so check with date\n")
            elif res == "OD":
                file2.write(line[get_header('name')] + " topic might be is getting outdated\n")
        elif c == "organic":
            if res == "DV":
                file2.write(line[get_header('name')] + " look for bounce rate and title trend status\n")
            elif res == "IV":
                file2.write(line[get_header(
                    'name')] + " well performed blog because of title and worth to write another blog \n")
            elif res == "NC":
                file2.write(line[get_header(
                    'name')] + " it is working good so check with bounce rate n crt content if needed\n")
            elif res == "OD":
                file2.write(
                    line[get_header('name')] + " topic might be is getting outdated remove check with date again\n")
        elif c == "direct":
            if res == "DV":
                file2.write(
                    line[get_header('name')] + " check with previous linked blog and title didn't worked well\n")
            elif res == "IV":
                file2.write(line[get_header('name')] + " previous link is well performed blog \n")
            elif res == "NC":
                file2.write(line[get_header(
                    'name')] + " it is working with nochange in views so check bounce rate and crt title or content if needed\n")
            elif res == "OD":
                file2.write(line[get_header('name')] + " check with bounce rate and change linked blog and title\n")
        elif c == "social":
            if res == "DV":
                file2.write(line[get_header('name')] + " topic trend decreases due to time\n")
            elif res == "IV":
                file2.write(line[get_header(
                    'name')] + " it is trending topic expected as coming era, write such kind with more content bounce rate to be considered for content\n")
            elif res == "NC":
                file2.write(line[get_header(
                    'name')] + " we can write more of such blogs but check bounce rate to crt title or content of this blog\n")
            elif res == "OD":
                file2.write(line[get_header(
                    'name')] + " try reposting in social media and depending on bounce rate change content and title\n")
        if primary == secondary:
            if res == "DV":
                print(line[get_header('name')] + " having less performance")
            elif res == "IV":
                print(line[get_header('name')] + " well performed blog")
            elif res == "NC":
                print(line[get_header('name')] + " it is working with nochange in views so check with date")
            elif res == "OD":
                print(line[get_header('name')] + " topic might be is getting outdated")
        elif primary == "organic":
            if res == "DV":
                print(line[get_header('name')] + " look for bounce rate and title trend status")
            elif res == "IV":
                print(
                    line[get_header('name')] + " well performed blog because of title and worth to write another blog ")
            elif res == "NC":
                print(
                    line[get_header('name')] + " it is working good so check with bounce rate n crt content if needed")
            elif res == "OD":
                print(line[get_header('name')] + " topic might be is getting outdated remove check with date again")
        elif primary == "direct":
            if res == "DV":
                print(line[get_header('name')] + " check with previous linked blog and title didn't worked well")
            elif res == "IV":
                print(line[get_header('name')] + " previous link is well performed blog ")
            elif res == "NC":
                print(line[get_header(
                    'name')] + " it is working with nochange in views so check bounce rate and crt title or content if needed")
            elif res == "OD":
                print(line[get_header('name')] + " check with bounce rate and change linked blog and title")
        elif primary == "social":
            if res == "DV":
                print(line[get_header('name')] + " topic trend decreases due to time")
            elif res == "IV":
                print(line[get_header(
                    'name')] + " it is trending topic expected as coming era, write such kind with more content bounce rate to be considered for content")
            elif res == "NC":
                print(line[get_header(
                    'name')] + " we can write more of such blogs but check bounce rate to crt title or content of this blog")
            elif res == "OD":
                print(line[get_header(
                    'name')] + " try reposting in social media and depending on bounce rate change content and title")

    for line in reader:
        if not header_flag:
            for index, col in enumerate(line):
                mappings[col] = index

            header_flag = True
        else:
            for col in range(0, 30):
                if


