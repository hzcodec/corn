import sys
import os
import time
import datetime
import re

TEST_TO_RUN = 'unicorn.robot'


if sys.version_info[0] < 3:
    raise " *** Python 3 must be used ***"

import robot

def main():
	output = '../Logs/unicorn'

	robot.run(TEST_TO_RUN, \
		loglevel='INFO', \
		exitonfailure=True, \
		noncritical="non-critical", \
		log=output+"_log", \
		output=output, \
		report=output+"_report", \
		timestampoutputs=False, \
		exclude="manual_test")
				

if __name__ == '__main__':
        main()
