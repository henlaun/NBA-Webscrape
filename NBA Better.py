import bs4 as bs
import urllib
import csv

url = input("Enter the url: ") 
filename = input("Enter the file name. Don't forget to add .csv at the end: ")

sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, 'lxml')

csv_file = open(filename, 'w')
csv_writer = csv.writer(csv_file, lineterminator = '\n')
csv_writer.writerow(['Team','Home','Away'])

x = []
y = []
for info in soup.find_all('td'):
    x.append(info.text)

for i in range(30):
    tup = (x[8*i+1], x[8*i+5], x[8*i+6])
    csv_writer.writerow([tup[0], tup[1], tup[2]])

csv_file.close() 
