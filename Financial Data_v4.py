import re
import requests
import lxml.html




#structure:
#name share, url to zonebourse, share price, share increase
all_share = ["Europris", "https://www.zonebourse.com/EUROPRIS-ASA-22512661/",
             "Easyvista", "https://www.zonebourse.com/EASYVISTA-32709/?type_recherche=rapide&mots=easyvista", 
             "Claranova", "https://www.zonebourse.com/CLARANOVA-63216172/",
             "Ashler & Manson", "https://www.zonebourse.com/ASHLER-MANSON-23894782/", 
             "S&T AG", "https://www.zonebourse.com/S-T-AG-5451138/", 
             "IDS", "https://www.zonebourse.com/IDS-5557/",
             "Invibes Advertising", "https://www.zonebourse.com/INVIBES-ADVERTISING-N-V-44658586/",
             "Cheops Technology", "https://www.zonebourse.com/CHEOPS-TECHNOLOGY-253735/",
             "Envea", "https://www.zonebourse.com/ENVEA-32714/",
             "Sogeclair", "https://www.zonebourse.com/SOGECLAIR-S-A-5081/",
             "Microwave", "https://www.zonebourse.com/MICROWAVE-VISION-32703/",
             "Bastide Le Confort Medical", "https://www.zonebourse.com/BASTIDE-LE-CONFORT-MEDICA-5023/",
             "Budget Telecom", "https://www.zonebourse.com/BUDGET-TELECOM-33822/",
             "TxCom", "https://www.zonebourse.com/TXCOM-4987514/",
             "Mecelec Composites", "https://www.zonebourse.com/MECELEC-COMPOSITES-34325454/",
             "Scanship", "https://www.zonebourse.com/SCANSHIP-HOLDING-ASA-16290106/",
             "Freelance.com", "https://www.zonebourse.com/FREELANCE-COM-32706/",
             "Streamwide", "https://www.zonebourse.com/STREAMWIDE-382968/",
             "Gaussin", "https://www.zonebourse.com/GAUSSIN-10093451/",
             "Euroland Corporate", "https://www.zonebourse.com/EUROLAND-CORPORATE-5634/",
             "Made", "https://www.zonebourse.com/MADE-185162/?type_recherche=rapide&mots=made"
             ]

i = 0
results = []
while i < len(all_share):
    #price
    html = requests.get(all_share[i+1])
    html_content = lxml.html.fromstring(html.content)
    extract_price = html_content.xpath('//*[@id="zbjsfv_dr"]')[0]
    price_byte = lxml.html.tostring(extract_price)
    price_string = price_byte.decode("utf-8")
    price = re.findall('\<.*\>(.*)\<.*\>', price_string)
    final_price = float(price[0])
    results.append(all_share[i])
    results.append(final_price)
    
    #increase
    extract_increase = html_content.xpath('//*[@id="zbjsfv_pf"]')[0]
    increase_byte = lxml.html.tostring(extract_increase)
    increase_string = increase_byte.decode("utf-8")
    increase = re.findall('\<.*\>(.*)\<.*\>', increase_string)
    increase_percentage = increase[0].strip('%')
    if increase_percentage == '--.--':
        increase_number = 0.00
    else:
        increase_number = float(increase_percentage)
    results.append(increase_number)
    print(all_share[i], final_price, increase_number)
    i = i + 2
    



