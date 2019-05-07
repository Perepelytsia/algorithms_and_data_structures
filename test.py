import sys, os

pwd = os.getcwd()
for listdir in os.listdir():
	if os.path.isdir(listdir) and listdir[0] != '.':
		sys.path.append(os.path.join(pwd, listdir))

import simple_enumarate_1_1
import sieve_of_eratosthenes_1_2

simple_enumarate_1_1.test()
sieve_of_eratosthenes_1_2.test()
