import csv
from collections import Counter
def main():



    path = "C:\\Users\\Anand\\Downloads\\"
    file = open(path + "blogdata2.csv")
    reader = csv.reader(file)
    file2 = open("result4", "w")
    res =""

    for line in reader:
        record = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + line[5] + "," + "," + \
                 line[6] + "," + line[7] + "," + line[8] + "," + line[9] + "," + line[10] + "," + line[11] + "," + line[
                     12] + line[13] + "," + line[14] + "," + line[15] + "," + line[16] + "," + line[17] + "," + line[
                     18] + "," + line[19] + "," + line[20] + "," + line[21] + "," + line[22] + "," + line[23] + "," + \
                 line[24] + "," + line[25] + "," + line[26]
        Views = [line[2] + "," + line[7] + "," + line[12] + "," + line[17] + "," + line[22]]
        # print(Views)


        if line[2] == "NA":
            if line[7] == "NA":
                if line[12] == "NA":
                    line[12] = line[17]
                line[7] = line[12]
            line[2] = line[7]
            # print(line[22])
        try:
            if float(line[2]) >= float(line[12]) > float(line[22]):
                # file2.write(line[0] + " -- Decreasing in views \n")
                res = "DV"
            elif float(line[2]) <= float(line[12]) < float(line[22]):
                # file2.write(line[0] + " -- increasing in views\n")
                res = "IV"
            elif float(line[2]) == float(line[12]) == float(line[22]):
                # file2.write(line[0] + " No change in views\n")
                res = "NC"
            elif float(line[2]) * .8 <= float(line[22]):
                # file2.write(line[0] + " -- No change in views\n")
                res = "NC"
            elif float(line[2]) * .8 >= float(line[22]):
                # file2.write(line[0] + " -- over all decreased in views\n")
                res = "OD"

        except Exception as e:
            print(str(e))
            # print(line[2], line[12], line[22], line[0])
        print(res)
        for line in reader:
            # import pdb;pdb.set_trace()
            source = []
            # source.append(line[3])

            source = [line[3], line[4], line[8], line[9], line[13], line[14], line[18], line[19], line[23], line[24]]
            # print(source)
            z = (Counter(source))
            # print(z,line[0])

            c = (max(z, key=z.get))
            value = (z[c])
            if c == "NA":
                del z[c]
                c = (max(z, key=z.get))
                value = (z[c])
                # print(value)

            primary = value
            # print(line[0] + " has more " + c + " views and count is ", value)
            del z[c]
            c = (max(z, key=z.get))
            value = (z[c])
            secondary = value

            # print(line[0] + " has second more " + c + " views and count is ", value)
            if primary == secondary:
                if res == "DV":
                    file2.write(line[0]+" having less performance\n")
                elif res=="IV":
                    file2.write(line[0]+" well performed blog \n")
                elif res=="NC":
                    file2.write(line[0]+" it is working with nochange in views so check with date\n")
                elif res=="OD":
                    file2.write(line[0]+" topic might be is getting outdated\n")
            elif c=="organic":
                if res == "DV":
                    file2.write(line[0]+" look for bounce rate and title trend status\n")
                elif res=="IV":
                    file2.write(line[0]+" well performed blog because of title and worth to write another blog \n")
                elif res=="NC":
                    file2.write(line[0]+" it is working good so check with bounce rate n crt content if needed\n")
                elif res=="OD":
                    file2.write(line[0]+" topic might be is getting outdated remove check with date again\n")
            elif c=="direct":
                if res == "DV":
                    file2.write(line[0]+" check with previous linked blog and title didn't worked well\n")
                elif res=="IV":
                    file2.write(line[0]+" previous link is well performed blog \n")
                elif res=="NC":
                    file2.write(line[0]+" it is working with nochange in views so check bounce rate and crt title or content if needed\n")
                elif res=="OD":
                    file2.write(line[0]+" check with bounce rate and change linked blog and title\n")
            elif c=="social":
                if res == "DV":
                    file2.write(line[0]+" topic trend decreases due to time\n")
                elif res=="IV":
                    file2.write(line[0]+" it is trending topic expected as coming era, write such kind with more content bounce rate to be considered for content\n")
                elif res=="NC":
                    file2.write(line[0]+" we can write more of such blogs but check bounce rate to crt title or content of this blog\n")
                elif res=="OD":
                    file2.write(line[0]+" try reposting in social media and depending on bounce rate change content and title\n")

            # if primary == secondary:
            #     if res == "DV":
            #         print(line[0]+" having less performance")
            #     elif res=="IV":
            #         print(line[0]+" well performed blog")
            #     elif res=="NC":
            #         print(line[0]+" it is working with nochange in views so check with date")
            #     elif res=="OD":
            #         print(line[0]+" topic might be is getting outdated")
            # elif primary=="organic":
            #     if res == "DV":
            #         print(line[0]+" look for bounce rate and title trend status")
            #     elif res=="IV":
            #         print(line[0]+" well performed blog because of title and worth to write another blog ")
            #     elif res=="NC":
            #         print(line[0]+" it is working good so check with bounce rate n crt content if needed")
            #     elif res=="OD":
            #         print(line[0]+" topic might be is getting outdated remove check with date again")
            # elif primary=="direct":
            #     if res == "DV":
            #         print(line[0]+" check with previous linked blog and title didn't worked well")
            #     elif res=="IV":
            #         print(line[0]+" previous link is well performed blog ")
            #     elif res=="NC":
            #         print(line[0]+" it is working with nochange in views so check bounce rate and crt title or content if needed")
            #     elif res=="OD":
            #         print(line[0]+" check with bounce rate and change linked blog and title")
            # elif primary=="social":
            #     if res == "DV":
            #         print(line[0]+" topic trend decreases due to time")
            #     elif res=="IV":
            #         print(line[0]+" it is trending topic expected as coming era, write such kind with more content bounce rate to be considered for content")
            #     elif res=="NC":
            #         print(line[0]+" we can write more of such blogs but check bounce rate to crt title or content of this blog")
            #     elif res=="OD":
            #         print(line[0]+" try reposting in social media and depending on bounce rate change content and title")



            # z.remove[c]
            # c = (max(z, key=z.get))
            # value = (z[c])
            # print(line[0] + " has more second views " + c + " views and count is ", value)

    print(res)
    return res


if __name__ == '__main__':
    main()

