from urllib import request

myUrl ='https://www.ligastavok.ru/bets/popular/soccer/rossiia-id-350/rossiiskaia-premer-liga-id-5271/enisei-lokomotiv-moskva-id-10139516'
otvet = request.urlopen(myUrl)
mytext1 = otvet.readlines()
filetxt = open('txtfile.txt', 'wb')
for line in mytext1:
    filetxt.write(line)
filetxt.close()