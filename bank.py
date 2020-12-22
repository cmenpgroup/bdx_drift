from gemc_api_bank import *

# Variable Type is two chars.
# The first char:
#  R for raw integrated variables
#  D for dgt integrated variables
#  S for raw step by step variables
#  M for digitized multi-hit variables
#  V for voltage(time) variables
#
# The second char:
# i for integers
# d for doubles

bankId   = 600;
bankname = "nveto";

def define_bank(configuration):

	# uploading the hit definition
	insert_bank_variable(configuration, bankname, "bankid", bankId, "Di", bankname+" bank ID")
	insert_bank_variable(configuration, bankname, "face",       1, "Di", "stack number")
	insert_bank_variable(configuration, bankname, "paddle",       2, "Di", "paddle number")
	insert_bank_variable(configuration, bankname, "adc1",         3, "Di", "ADC 1")
	insert_bank_variable(configuration, bankname, "adc2",         4, "Di", "ADC 2")
	insert_bank_variable(configuration, bankname, "tdc1",         5, "Di", "TDC 1")
	insert_bank_variable(configuration, bankname, "tdc2",         6, "Di", "TDC 2")
	insert_bank_variable(configuration, bankname, "hitn",        99, "Di", "hit number")
