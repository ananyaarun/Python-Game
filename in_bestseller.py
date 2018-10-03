#!/usr/bin/python3
import csv
import urllib.request as urllib2

nam = []
ur = []
aut = []
pri = []
rat = []
sta = []
total = 0

for lv in range(1, 6, 1):

    var = 0
    chk = 0
    flag = 0

    wiki = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_" + \
        str(lv) + "?ie=UTF8&pg=" + str(lv)
    page = urllib2.urlopen(wiki)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page, "lxml")
    books = soup.find_all("div", {"class": "zg_itemWrapper"})

    for book in books:
        var = 0
        chk = 0
        flag = 0
        total = total + 1
        name = book.find_all("img")
        if name != []:
            for i in name:
                tempnam = i.get("alt")
                nam.append(tempnam.strip())
        else:
            nam.append("Not available")

        auth = book.find_all("div", {"class": "a-row a-size-small"})
        if auth != []:
            for m in auth:
                if var == 0:
                    if m.text == 'Paperback':
                        aut.append("Not available")
                        var = 1
                    else:
                        aut.append(m.text)
                        var = 1
        else:

            aut.append("Not available")

        price = book.find_all("span", {"class": "p13n-sc-price"})
        if price != []:
            for j in price:
                pri.append(j.text)
        else:
            pri.append("Not available")

        rating = book.find_all("a", {"class": "a-size-small a-link-normal"})
        if rating != []:
            for k in rating:
                rat.append(k.text)
        else:
            rat.append("Not available")

        url = book.find_all("a", {"class": "a-link-normal"})
        if url != []:
            for n in url:
                if flag == 0:
                    ur.append("https://www.amazon.in" + n.get("href"))
                    flag = 1
        else:
            if flag == 0:
                ur.append("Not available")
                flag = 1

        stars = book.find_all("span", {"class": "a-icon-alt"})
        if stars != []:
            for l in stars:
                if "out of" in l.text and chk == 0:
                    sta.append(l.text)
                    chk = 1
                else:
                    if chk == 0:
                        sta.append("Not available")
                        chk = 1
        else:
            sta.append("Not available")
            chk = 1

myFile = open('output/in_book.csv', 'w')
o = 0
myFile.write("Name" + ";" + "URL" + ";" + "Author" + ";" +
             "Price" + ";" + "Number of Ratings" + ";" + "Average Rating")
myFile.write("\n")
while o < total:
    myFile.write(str(nam[o]) + ";" + str(ur[o]) + ";" + str(aut[o]) +
                 ";" + str(pri[o]) + ";" + str(rat[o]) + ";" + str(sta[o]))
    myFile.write("\n")
    o = o + 1

print("Bestsellers from amazon.in scrapped !!")
