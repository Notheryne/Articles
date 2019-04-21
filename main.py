import gazeta as gz
import interia
import og
import se
import wyborcza as wb

gazeta_urls = {
# url : category name
"http://wiadomosci.gazeta.pl/wiadomosci/0,114884.html?str=" : "Polityka",
"http://wiadomosci.gazeta.pl/wiadomosci/0,114885.html?str=" : "Nauka",
"http://wiadomosci.gazeta.pl/wiadomosci/0,156046.html?str=" : "Edukacja",
}

interia_biznes_urls = {
# url : category name
"https://biznes.interia.pl/wiadomosci," : "Biznes - wiadomości",
"https://biznes.interia.pl/nieruchomosci," : "Biznes - nieruchomości",
"https://biznes.interia.pl/budownictwo," : "Biznes - budownictwo",
"https://biznes.interia.pl/firma," : "Biznes - firma",
"https://biznes.interia.pl/media," : "Biznes - media",
}

interia_urls = {
#url : category name
"https://fakty.interia.pl/nauka,nPack," : "Nauka",
"https://sport.interia.pl/pilka-nozna,nPack," : "Sport",
"https://sport.interia.pl/sporty-walki,nPack," : "Sport",
"https://motoryzacja.interia.pl/wiadomosci,nPack," : "Motoryzacja",
"https://nt.interia.pl/komputery,nPack," : "Technologia",
"https://nt.interia.pl/technauka,nPack," : "Nauka",
"https://muzyka.interia.pl/artykuly,nPack," : "Kultura",
}

og_urls = {
#url : category name
"http://obserwatorgospodarczy.pl/gospodarka?start=" : "Gospodarka",
"http://obserwatorgospodarczy.pl/transport-i-infrastruktura?start=" : "Transport i infrastruktura",
"http://obserwatorgospodarczy.pl/finanse?start=" : "Finanse",
}

se_urls = {
#url : category name
"https://www.se.pl/rozrywka/plotki/?page=" : "Plotki",
"https://www.se.pl/wiadomosci/polityka/?page=" : "Polityka",
"https://superbiz.se.pl/wiadomosci/?page=" : "Wiadomości",
"https://superbiz.se.pl/firma/?page=" : "Biznes - firma",
"https://superbiz.se.pl/prawo/?page=" : "Biznes - prawo",
"https://superbiz.se.pl/technologie/?page=" : "Technologie",
"https://sport.se.pl/pilka-nozna/?page=" : "Sport",
"https://sport.se.pl/pozostale/?page=" : "Sport",
"https://www.se.pl/auto/nowosci/?page=" : "Motoryzacja",
}

wyborcza_urls = {
#url : category name
"http://wyborcza.pl/TylkoZdrowie/0,0.html?str=" : "Zdrowie",
"http://wyborcza.pl/0,154903.html?str=" : "Sport",
"http://wyborcza.pl/0,75410.html?str=2" : "Kultura",
"http://wyborcza.pl/0,156282.html?str=" : "Technologia",
"http://wyborcza.pl/0,75400.html?str=" : "Nauka",
"http://wyborcza.pl/0,155287.html?str=" : "Gospodarka",
}

#for url, category in gazeta_urls.items():
#    gz.scrape_gazeta(url, category)

#for url, category in interia_biznes_urls.items():
#    interia.scrape_interia_biznes(url, category)

#for url, category in interia_urls.items():
#    interia.scrape_interia(url, category)

#for url, category in og_urls.items():
#    og.scrape_og(url, category)

#for url, category in se_urls.items():
#    se.scrape_se(url, category)

for url, category in wyborcza_urls.items():
    wb.scrape_wyborcza(url, category)
