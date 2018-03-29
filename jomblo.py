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
print "\033[0m [1] Brute Force 1"
print " [2] Brute Force 2"
print " [3] Brute Force 3"
print "\033[91m()===||==================>>\033[92m"
jomblo=raw_input("        Pilih No: ")
if jomblo == '01' or jomblo == '1':
	try:
		os.system("python2 fbbrute.py")
	except(ImportError):
		print " Cek Lagi Module Dan File Nya"

if jomblo == '02' or jomblo == '2':
	try:
		os.system("python2 fbbrute2.py")
	except(ImportError):
		print " Cek Lagi Module Dan File Nya"

if jomblo == '03' or jomblo == '3':
	try:
		os.system("python2 MBF.py")
	except(ImportError):
		print " Cek Lagi Module Dan File Nya"

else:
	print "\n[~] Pilih No Nya Yang Benar Donk Sayank [~]\n"
	time.sleep(1)
	sys.exit()