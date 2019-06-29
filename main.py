import os
import glob


def readLineByLine(filepath):
    lines = []
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print ("Line {}: {}".format(cnt, line.strip()))
            lines.append(line)
            line = fp.readline()
            cnt += 1

    return lines


print ("Tanium Vulnerable File Read Test")
print ("")
home = "/home/brian/file-read-test/"
vuln_path = home + "results/*/*/vulnerable.txt"
print ("Vulnerable Directory: %s" % vuln_path)
print ("")
vuln_file = glob.glob(vuln_path)
vuln_file.sort(key=os.path.getmtime, reverse=True)
print ("Found Files:")
print (vuln_file)
print ("")
print ("Analyzing..")
if len(vuln_file) <= 0:
    print ("No Files Found")
    exit(0)

for line in readLineByLine(vuln_file[0]):
    item = line.split("|")
    if len(item) <= 4:
        print ("No Files Found Matching Requirements")
        exit(0)
    else:
        print (item)
