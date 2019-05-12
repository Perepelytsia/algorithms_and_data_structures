import sys, os

pwd = os.getcwd()
for listdir in os.listdir():
	if os.path.isdir(listdir) and listdir[0] != '.':
		sys.path.append(os.path.join(pwd, listdir))

import a_1_1
import a_1_2
import a_1_3
import a_1_4
import a_1_6
import a_1_7
import a_1_15

#a_1_1.test()
#a_1_2.test()
#a_1_3.test()
#a_1_4.test()
#a_1_6.test()
#a_1_7.test()
a_1_15.test()