minima = [19, 19, 19, 17, 14, 13, 12, 14, 15, 16, 17, 18]
maxima = [27, 28, 27, 25, 23, 22, 22, 23, 24, 25, 26, 26]
mediana = [(minima + maxima)/2 for (minima, maxima) in zip(minima, maxima)]
# for c in zip(minima, maxima):
#     media = sum(c)/2
#     mediana.append(media) 
# print(mediana)

# mediaTemperaturas = [media for c in maxima and i in minima media = (maxima[c] + minima[i])/2]
