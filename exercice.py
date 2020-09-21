#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	sum = 0
	TAXE_RATE = 0.15

	for item in data :
		sum += INDEX_QUANTITY * item[INDEX_PRICE]
	
	taxe = TAXE_RATE * sum
	total = sum + taxe

	titles = ["SOUS-TOTAL", "TAXES", "TOTAL"]
	bill_data = [("SOUS-TOTAL", sum) , ("TAXES",taxe) , ("TOTAL",total)]

	facture = name
	for d in bill_data :
		facture += "\n" + f"{d[0]: <10s} {d[1] : >10.2f} $"

	
	
	#facture += "\n" + f"SOUS-TOTAL {sum : >10.2f} $"
	#facture += "\n" + f"TAXES      {taxe : >10.2f} $"
	#facture += "\n" + f"TOTAL      {total : >10.2f} $"

	return facture
	

def format_number(number, num_decimal_digits):
	# Separer les deux parties
	decimal_part = abs(number) % 1.0
	whole_part = int(abs(number))
	
	# Formater la partie decimale
	decimal_str = "." + str(int(round(decimal_part * 10**num_decimal_digits)))

	# marche aussi
	# decimal_str =  f"{decimal_part} :.{num_decimal_digits}f}"[1:]
	
	# Formater la partie entiere
	# 1420069 => "1 420 069"
	# si on y va en modulo ca va donner ==> "1 420 69"
	# de plus le  chiffre le plus haut ==> seulement 1
	whole_part_str = ""
	while whole_part >= 1000:
		three_digits = whole_part % 1000
		digits_str = f" {three_digits :0>3}"
		whole_part_str = digits_str + whole_part_str 
		whole_part //= 1000
	whole_part_str = str(whole_part) + whole_part_str


	return ("-" if number < 0 else "") + whole_part_str + decimal_str

def get_triangle(num_rows):

	# "   *   " ligne 1 de 4
	# "  ***  " ligne 2 de 4
	# " ***** " ligne 3 de 4
	# "*******" ligne 4 de 4
	
	BORDER_CHAR = "+"
	TRIANGLE_CHAR = "A"

	# Calculer la largeur de trangle

	largeur = 1 + 2*(num_rows - 1)

	# Construire ma premiere et derniere ligne

	border = BORDER_CHAR * (largeur + 2)

	# Afficher le triangle
	result = border

	# Pour chaque ligne du triangle
		# "+" + ligne du triange avec espace + "+"
	
	for i in range(num_rows):
		num_triangles_char = i * 2 + 1
		triangle_chars = TRIANGLE_CHAR * num_triangles_char
		triangle_line = f"{triangle_chars : ^{largeur}}"
		result += "\n" + BORDER_CHAR + triangle_line + BORDER_CHAR	

	result += "\n" + border


	return result


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
