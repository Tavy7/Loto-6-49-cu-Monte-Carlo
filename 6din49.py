import random
import matplotlib.pyplot as plt

# Loto 6/49

def AlegeNumere():
	# Functie care returneaza o lista de 6 numere distincte random
	# in ordine crescatoare, echivalentul unui bilet
	numere = []
	for i in range(6):
		numar = random.randint(1, 49)

		if numar in numere:
			ok = False

			while not ok:
				numar = random.randint(1, 49)
				if numar not in numere:
					ok = True

		numere.append(numar)

	return sorted(numere)

def VerificaBilet(bilet, numereCastigatoare):
	nrNumereCastigatoare = 0
	
	for i in range(6):
		# Listele sunt sortate crescator
		if bilet[i] == numereCastigatoare[i]:
			nrNumereCastigatoare += 1

	return nrNumereCastigatoare

def Joaca(numereJucator):
	# Alegem 6 numere random, ca cele castigatoare
	numereCastigatoare = AlegeNumere()

	# Rezultat reprezinta numarul de numere castigatoare
	rezultat = VerificaBilet(numereJucator, numereCastigatoare)
	return rezultat
	

def MonteCarlo(numExperimente = 10 ** 6):
	nrLocul1, nrLocul2, nrLocul3 = 0, 0, 0 # countere

	for nrExperiment in range(numExperimente):
		numereJucator = AlegeNumere()
		rezultat = Joaca(numereJucator)

		# Daca jucatorul a castigat incrementam counterul
		if rezultat == 4:
			nrLocul3 += 1
			print("Loc 3 Simularea {} Numere Jucator {}".format(nrExperiment, numereJucator))

		if rezultat == 5:
			nrLocul2 += 1
			print("Loc 2 Simularea {} Numere Jucator {}".format(nrExperiment, numereJucator))

		if rezultat == 6:
			nrLocul1 += 1
			print("Loc 1 Simularea {} Numere Jucator {}".format(nrExperiment, numereJucator))

	return (nrLocul1, nrLocul2, nrLocul3)

numarExperimente = 10 ** 6
numarCastiguri = MonteCarlo(numarExperimente)

print("Probabilitati castigare la loto dupa {} experimente".format(numarExperimente))
print("Locul 1", numarCastiguri[0] / numarExperimente)
print("Locul 2", numarCastiguri[1] / numarExperimente)
print("Locul 3", numarCastiguri[2] / numarExperimente)