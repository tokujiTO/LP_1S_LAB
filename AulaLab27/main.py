from biblio import *

# Nomes dos furacões
nomes = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II',
         'CubaBrownsville', 'Tampico', 'Labor Day', 'New England',
         'Carol', 'Janet', 'Carla', 'Hattie',
         'Beulah', 'Camille', 'Edith', 'Anita',
         'David', 'Allen', 'Gilbert', 'Hugo',
         'Andrew', 'Mitch', 'Isabel', 'Ivan',
         'Emily', 'Katrina', 'Rita', 'Wilma',
         'Dean', 'Felix', 'Matthew', 'Irma',
         'Maria', 'Michael']

# Mês de ocorrência
meses = ['October', 'September', 'September', 'November', 'August',
         'September', 'September', 'September', 'September', 'September',
         'September', 'October', 'September', 'August', 'September',
         'September', 'August', 'August', 'September', 'September',
         'August', 'October', 'September', 'September', 'July',
         'August', 'September', 'October', 'August', 'September',
         'October', 'September', 'September', 'October']

# Ano de ocorrência
anos = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961,
        1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998,
        2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# Velocidade máxima dos ventos (mph)
max_velocidades = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175,
                   160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180,
                   165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# Áreas afetadas pelos furacões
areas_afetadas = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'],
                  ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'],
                  ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'],
                  ['Mexico'], ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'],
                  ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'],
                  ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'],
                  ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# Danos registrados (USD($))
danos = ['Damages not recorded', '100M', 'Damages not recorded', '40M',
         '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M',
         '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded',
         '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B',
         '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M',
         '15.1B', '64.8B', '91.6B', '25.1B']

# Mortes registradas
mortes = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319,
          688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325, 51, 124,
          17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

print(converte_moeda(danos=danos))

print("-="*20)

dic_nomes = gera_dic_nomes(nomes, meses, anos, max_velocidades,
                   areas_afetadas, danos, mortes)
print('Entrada de chave "Cuba I":')
print(dic_nomes['Cuba I'])
print('Entrada de chave "Camille":')
print(dic_nomes['Camille'])
print('Dicionário completo:')
print(dic_nomes)

print("-="*20)

dic_anos = gera_dic_anos(nomes, meses, anos, max_velocidades,
                         areas_afetadas, danos, mortes)
print('Entrada de chave "1932":')
print(dic_anos[1932])
print('Entrada de chave "2018":')
print(dic_anos[2018])
print('Dicionário completo:')
print(dic_anos)

print("-="*20)

print(contagem_areas(areas_afetadas))