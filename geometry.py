from gemc_api_geometry import *
from math import cos, sin, radians


def makeBDX_DRIFT(configuration, parameters):
	global NUM_BARS, dx, dy, dz, gd_foil_thickness
	# Assign paramters to local variables
	inches = 2.54		# This is in the gemc api math module
	NUM_BARS = int(parameters["neutron_veto_number_of_bars"])
	dx    =   parameters["bar_width"]/2.0          # width at top,cm
	dy    =   parameters["bar_length"]/2.0         # length, cm
	dz    =   parameters["bar_height"]/2.0         # height, cm
	gd_foil_thickness    =   parameters["gd_thick"]/2.0   # half-thicness of Gd2O3 foil, cm
#	NUM_BARS = 5
#	dx    =   3.0          # width, cm
#	dy    =   10.0         # length, cm
#	dz    =   10.0         # heigth, cm

	build_mother(configuration)
	build_drift(configuration)
	build_neutron_veto_front_gd(configuration)
	build_neutron_veto_front(configuration)
	build_neutron_veto_back_gd(configuration)
	build_neutron_veto_back(configuration)
#	build_neutron_veto_top(configuration)
#	build_neutron_veto_bottom(configuration)

def build_mother(configuration):
	detector = MyDetector()
	detector.name = "bdxdrift_main_volume"
	detector.mother = "root"
	detector.description = "BDX DRIFT Mother Volume"
	detector.pos = "0*cm 0.0*cm 0*cm"
	detector.rotation = "0*deg 0*deg 0*deg"
	detector.color = "000000"
	detector.type = "Box"

	detector.dimensions = "150.0*cm 150.0*cm 150.0*cm"
	detector.material = "G4_AIR"
	detector.mfield = "no"
	detector.visible = 1
	detector.style = 0
	detector.sensitivity = "no"
	detector.hit_type = "no"
	detector.identifiers = "no"

	print_det(configuration, detector)

def build_drift(configuration):
	detector = MyDetector()
	detector.name = "drift"
	detector.mother = "bdxdrift_main_volume"
	detector.description = "BDX-DRIFT drift volume"
	detector.pos = "0*cm 0.0*cm 0*cm"
	detector.rotation = "0*deg 0*deg 0*deg"
	detector.color = "000000"
	detector.type = "Box"

	detector.dimensions = "%5.1f*cm %5.1f*cm %5.1f*cm" % (dz, dz, dz)
#	detector.dimensions = "50.0*cm 50.0*cm 50.0*cm"
	detector.material = "G4_AIR"
	detector.mfield = "no"
	detector.visible = 1
	detector.style = 0
	detector.sensitivity = "no"
	detector.hit_type = "no"
	detector.identifiers = "no"

	print_det(configuration, detector)

def build_neutron_veto_back_gd(configuration):
	pos_offset = dy
	for n in range(0, NUM_BARS):
		detector = MyDetector();

		# first fill the volume with Gd
		detector.name = "gd_foil_back_%02d" % n
		detector.mother = "bdxdrift_main_volume"
		detector.description = "BDX-DRIFT Neutron Veto Gd Foil back %d" % n

		# positioning
		dx_Gd = dx + gd_foil_thickness
		x      = pos_offset + n*dx_Gd
		y      = 0.0
		z      = 0.0
		detector.pos = "%s*cm %s*cm %s*cm" % (x, y, z)
		detector.rotation = "0*deg 0*deg 0*deg"
		detector.color = "ff0000"
		detector.type = "Box"
		detector.dimensions = "%5.1f*cm %5.1f*cm %5.1f*cm" % (dx_Gd, dy, dz)
		detector.material = "gd_foil"
#		detector.material = "G4_AIR"
		detector.mfield = "no"
		detector.visible = 1
		detector.style = 0
		detector.sensitivity = "no"
		detector.hit_type = "no"
		detector.identifiers = "no"

		print_det(configuration, detector)

def build_neutron_veto_back(configuration):
	pos_offset = dy
	for n in range(0, NUM_BARS):
		detector = MyDetector();

		# imbed the scintillators inside the Gd foil
		detector.name = "back_%02d" % n
		detector.mother = "gd_foil_back_%02d" % n
		detector.description = "BDX-DRIFT Neutron Veto back %d" % n

		# positioning
		x      = 0.0
		y      = 0.0
		z      = 0.0
		detector.pos = "%s*cm %s*cm %s*cm" % (x, y, z)
		detector.rotation = "0*deg 0*deg 0*deg"
		detector.color = "66bbff"
		detector.type = "Box"
		detector.dimensions = "%5.1f*cm %5.1f*cm %5.1f*cm" % (dx, dy, dz)
		detector.material = "scintillator"
		detector.mfield = "no"
		detector.visible = 1
		detector.style = 1
		detector.sensitivity = "flux"
		detector.hit_type = "flux"
		detector.identifiers = "face manual 2 paddle manual %d" % n

		print_det(configuration, detector)

def build_neutron_veto_front_gd(configuration):
	pos_offset = dy
	for n in range(0, NUM_BARS):
		detector = MyDetector();

		# first fill the volume with Gd
		detector.name = "gd_foil_front_%02d" % n
		detector.mother = "bdxdrift_main_volume"
		detector.description = "BDX-DRIFT Neutron Veto Gd Foil front %d" % n

		# positioning
		dx_Gd = dx + gd_foil_thickness
		x      = -pos_offset + n*dx_Gd
		y      = 0.0
		z      = 0.0
		detector.pos = "%s*cm %s*cm %s*cm" % (x, y, z)
		detector.rotation = "0*deg 0*deg 0*deg"
		detector.color = "ff0000"
		detector.type = "Box"
		detector.dimensions = "%5.1f*cm %5.1f*cm %5.1f*cm" % (dx_Gd, dy, dz)
		detector.material = "gd_foil"
#		detector.material = "G4_AIR"
		detector.mfield = "no"
		detector.visible = 1
		detector.style = 0
		detector.sensitivity = "no"
		detector.hit_type = "no"
		detector.identifiers = "no"

		print_det(configuration, detector)

def build_neutron_veto_front(configuration):
	pos_offset = dy
	for n in range(0, NUM_BARS):
		detector = MyDetector();

		# imbed the scintillators inside the Gd foil
		detector.name = "front_%02d" % n
		detector.mother = "gd_foil_front_%02d" % n
		detector.description = "BDX-DRIFT Neutron Veto front %d" % n

		# positioning
		x      = 0.0
		y      = 0.0
		z      = 0.0
		detector.pos = "%s*cm %s*cm %s*cm" % (x, y, z)
		detector.rotation = "0*deg 0*deg 0*deg"
		detector.color = "66bbff"
		detector.type = "Box"
		detector.dimensions = "%5.1f*cm %5.1f*cm %5.1f*cm" % (dx, dy, dz)
		detector.material = "scintillator"
		detector.mfield = "no"
		detector.visible = 1
		detector.style = 1
		detector.sensitivity = "flux"
		detector.hit_type = "flux"
		detector.identifiers = "face manual 1 paddle manual %d" % n

		print_det(configuration, detector)

def build_neutron_veto_top(configuration):
	pos_offset = dy
	for n in range(0, NUM_BARS):
		detector = MyDetector();

		detector.name = "top_%02d" % n
		detector.mother = "bdxdrift_main_volume"
		detector.description = "BDX-DRIFT Neutron Veto top %d" % n

		# positioning
		x      = 0.0
		y      = pos_offset + n*dx
		z      = 0.0
		detector.pos = "%s*cm %s*cm %s*cm" % (x, y, z)
		detector.rotation = "0*deg 0*deg 0*deg"
		detector.color = "66bbff"
		detector.type = "Box"
		detector.dimensions = "%5.1f*cm %5.1f*cm %5.1f*cm" % (dy, dx, dz)
		detector.material = "scintillator"
		detector.mfield = "no"
		detector.visible = 1
		detector.style = 0
		detector.sensitivity = "flux"
		detector.hit_type = "flux"
		detector.identifiers = "face manual 3 paddle manual %d" % n

		print_det(configuration, detector)

def build_neutron_veto_bottom(configuration):
	pos_offset = dy
	for n in range(0, NUM_BARS):
		detector = MyDetector();

		detector.name = "bottom_%02d" % n
		detector.mother = "bdxdrift_main_volume"
		detector.description = "BDX-DRIFT Neutron Veto top %d" % n

		# positioning
		x      = 0.0
		y      = -pos_offset + n*dx
		z      = 0.0
		detector.pos = "%s*cm %s*cm %s*cm" % (x, y, z)
		detector.rotation = "0*deg 0*deg 0*deg"
		detector.color = "66bbff"
		detector.type = "Box"
		detector.dimensions = "%5.1f*cm %5.1f*cm %5.1f*cm" % (dy, dx, dz)
		detector.material = "scintillator"
		detector.mfield = "no"
		detector.visible = 1
		detector.style = 0
		detector.sensitivity = "flux"
		detector.hit_type = "flux"
		detector.identifiers = "face manual 4 paddle manual %d" % n

		print_det(configuration, detector)
