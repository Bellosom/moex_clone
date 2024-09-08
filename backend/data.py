import cloudscraper


host='localhost'
db_name='xml_data_db'
user='admin'
password='ADGJMadgjm2000'

folder_path='xml_data_all_dates'
#url со всеми Фьючерсами(Срочный рынок)
first_url = 'https://www.moex.com/ru/derivatives/'

#url для каждего полученого кода товара из открытых позиций
second_url = 'https://www.moex.com/api/contract/OpenOptionService/'

#обход защиты
scraper = cloudscraper.create_scraper() 

#xml_dates


#все фьючерсы
fve = ['MXI', 'IMOEXF', 'MIX', 'NASD', 'RTS', 'SPYF', 'RTSM', 'HANG', 'RGBI', 'NIKK', 'IPO', 'R2000', 'DAX', 'DJ30', 'RVI', 'STOX', 'OGI', 'HOME', 'CNI', 'EM', 'FNI', 'MMI', 'GAZR', 'SBRF', 'GMKN', 'SGZH', 'YDEX', 'MVID', 'MTLR', 'VTBR', 'ALRS', 'SIBN', 'TRNF', 'AFLT', 'WUSH', 'MGNT', 'RNFT', 'VKCO', 'BAIDU', 'TCSI', 'LKOH', 'SMLT', 'LEAS', 'BANE', 'RUAL', 'PHOR', 'SVCB', 'FLOT', 'POSI', 'SBPR', 'NLMK', 'MOEX', 'ALIBABA', 'BSPB', 'SNGR', 'ASTR', 'AFKS', 'POLY', 'NOTK', 'ROSN', 'RTKM', 'MTSI', 'TATN', 'PIKK', 'KMAZ', 'HYDR', 'SNGP', 'SOFL', 'TATP', 'MAGN', 'ISKJ', 'FEES', 'PLZL', 'CHMF', 'FESH', 'IRAO', 'CBOM', 'SPBE', 'CNY', 'CNYRUBF', 'Si', 'Eu', 'USDRUBF', 'ED', 'UCNY', 'EURRUBF', 'TRY', 'HKD', 'UJPY', 'UCHF', 'GBPU', 'INR', 'KZT', 'AED', 'AMD', 'AUDU', 'BYN', 'UCAD', 'ECAD', 'EGBP', 'EJPY', 'UKZT', '1MFR', 'RUON', 'NG', 'BR', 'GOLD', 'GLDRUBF', 'SILV', 'GL', 'PLD', 'PLT', 'WHEAT', 'SUGR', 'SUGAR', 'ALMN', 'Co', 'Nl', 'Zn']