
from gemc_api_materials import *


def define_materials(configuration):

	# Scintillator
	scintillator = MyMaterial(name="scintillator", description="neutron veto scintillator material", density="1.032",
		ncomponents="2",  components="C 9 H 10")
	print_mat(configuration, scintillator);

	# Gd2O3 - Gadolinium(III) Oxide foil
	gd_foil = MyMaterial(name="gd_foil", description="neutron veto Gd foil material", density="7.07",
		ncomponents="2",  components="Gd 2 O 3")
	print_mat(configuration, gd_foil);

	# mylar used in BDX-Cal
	bdx_mylar = MyMaterial(name="bdx_mylar", description="BDX mylar material", density="1.4",
		ncomponents="3",  components="G4_H 0.041958 G4_C 0.625017 G4_O 0.333025")
	print_mat(configuration, bdx_mylar);
