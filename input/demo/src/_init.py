#!/usr/bin/env python
#######################################################################################
# This file is provided under the Creative Commons Attribution 3.0 license.
#
# You are free to share, copy, distribute, transmit, or adapt this work
# PROVIDED THAT you attribute the work to the authors listed below.
# For more information, please see the following web page:
# http://creativecommons.org/licenses/by/3.0/
#
# This file is a component of the SflE Scientific workFLow Environment for reproducible 
# research, authored by the Huttenhower lab at the Harvard School of Public Health
# (contact Curtis Huttenhower, chuttenh@hsph.harvard.edu).
#
# If you use this environment, the included scripts, or any related code in your work,
# please let us know, sign up for the SflE user's group (sfle-users@googlegroups.com),
# pass along any issues or feedback, and we'll let you know as soon as a formal citation
# is available.
#######################################################################################

"""
.. testsetup::

	from report import *
"""

import argparse
import csv
import sys

def report( aastrLines, ostm ):
	"""
	Outputs simple statistics for each row of a data table.
	
	:param	aastrLines:	Split lines from which data are read.
	:type	aastrLines:	collection of string collections
	:param	ostm:		Output stream to which report is written.
	:type	ostm:		output stream
	"""

	csvw = csv.writer( ostm, csv.excel_tab )
	fFirst = True
	for astrLine in aastrLines:
		strID, astrData = astrLine[0], astrLine[1:]
		if fFirst:
			fFirst = False
			csvw.writerow( ("row", "type", "#missing", "sum or #values") )
		else:
			try:
				strInfo = "%g" % sum( float(s) for s in filter( None, astrData ) )
				strType = "numeric"
			except ValueError:
				strInfo = len( set(astrData) )
				strType = "categorical"
			csvw.writerow( (strID, strType, len( filter( lambda s: not s.strip( ), astrData ) ), strInfo) )

argp = argparse.ArgumentParser( prog = "report.py",
	description = """A simple demonstration script that reports on each row of a tab-delimited text file.""" )
__doc__ = "::\n\n\t" + argp.format_help( ).replace( "\n", "\n\t" ) + __doc__

def _main( ):
	args = argp.parse_args( )
	adVitals = report( csv.reader( sys.stdin, csv.excel_tab ), sys.stdout )

if __name__ == "__main__":
	_main( )
