#!/usr/bin/python
#//Ijin Gabungin Ya Mastah, Supaya Toolnya Bisa Mudah Kami Pakai.//

import os 
import random 
import sys
import time

os.system("clear")
print "\n\n\n"
print "\033[93m|-----------------------|"
print "\033[0m|Penyusun: Dede Jomblo  |"
print "|Kumpulan: BruteForce Fb|"
print "\033[93m|-----------------------|"
print "\033[92m#########################"
print ""
print "\033[91m()===||==================>>"
print "\033[0m [1] Brute Force _1_"
print " [2] Brute Force _2_"
print " [3] Brute Force _3_"
print "\033[91m()===||==================>>\033[92m"
jomblo=raw_input("        Pilih No: ")
if jomblo == '01' or jomblo == '1':
	try:
		import fbbrute
	except(ImportError):
		print " Cek Lagi Module Dan File Nya"
		sys.exit()
if jomblo == '02' or jomblo == '2':
	try:
		import fbbrute2
	except(ImportError):
		print " Cek Lagi Module Dan File Nya"
		sys.exit()
if jomblo == '03' or jomblo == '3':
	try:
		import MBF
	except(ImportError):
		print " Cek Lagi Module Dan File Nya"
		sys.exit()
else:
	print "\n[~] Pilih No Nya Yang Benar Donk Sayank [~]\n"
	time.sleep(1)
	sys.exit()