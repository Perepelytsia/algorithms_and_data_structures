import sys, os

pwd = os.getcwd()
for listdir in os.listdir():
	if os.path.isdir(listdir) and listdir[0] != '.':
		sys.path.append(os.path.join(pwd, listdir))

import sieve_of_eratosthenes_1_1

print(sieve_of_eratosthenes_1_1.__doc__)