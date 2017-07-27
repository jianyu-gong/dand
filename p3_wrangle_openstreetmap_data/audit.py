import xml.etree.cElementTree as ET
from collections import defaultdict
import re

def get_element(osmfile):
	context = ET.iterparse(osmfile, events=('start', 'end'))
	_, root = next(context)
	for event, elem in context:
		if event == 'end':
			yield elem
			root.clear()

osmfile = 'toronto_canada.osm'

# Count tags #
def count_tags(osmfile):
	tags = {}
	for element in get_element(osmfile):
		if element.tag not in tags.keys():
			tags[element.tag] = 1
		else:
			tags[element.tag] += 1
	print tags
	return tags
#count_tags(osmfile)

# Match the last word of street name#
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE) 

# The expected last word of street name#
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Circle", "Crescent", "Way", "Heights", "Gate", "Terrace", "Grove",
            "Gardens", "Walk", "East", "West", "North", "South", "Gateway", "Highway", "Hill", "Line", "Common",
            "Close", "Mews", "Path", "Curve", "Row", "Pathway", "Hollow", "Meadoway", "Wood", "Sideroad", "Champions",
            "Crossing", "Willoway", "Park", "Fernway", "Chase", "Placeway", "Woodway", "Landing", "Manor", "Kingsway",
            "Guardia", "Alliston", "Woodmount", "Appleway", "Puschlinch"]

def audit_street_type(street_types, street_name):
   m = street_type_re.search(street_name)
   if m:
       street_type = m.group()
       if street_type not in expected:
           street_types[street_type].add(street_name)

# Check the addr:street#
def is_street_name(elem): 
	return (elem.attrib['k'] == "addr:street")

# Audit the street name#
def audit(osmfile):
	osm_file = open(osmfile, "r")
	street_types = defaultdict(set)
	for elem in get_element(osm_file):
		if elem.tag == "node" or elem.tag == "way":
			for tag in elem.iter("tag"):
				if is_street_name(tag):
					tag.attrib['v'] = update_street_name(tag.attrib['v'], mapping)
#					print tag.attrib['v']
					audit_street_type(street_types, tag.attrib['v'])
	osm_file.close()
#	print street_types
	return street_types


# Audit postal code #
# Search postal code format A1A 1A1 #
postal_code_re = re.compile(r'[A-Z]\d[A-Z]\s\d[A-Z]\d')


def audit_postal_code(osmfile):
	wrong_postal_code = []
	post_file = open(osmfile, "r")
	for elem in get_element(osmfile):
		if elem.tag == "node" or elem.tag == "way":
			for tag in elem.iter("tag"):
				if tag.attrib['k'] == 'addr:postcode':
					tag.attrib['v'] = update_postal_code(tag.attrib['v'])
					m = postal_code_re.match(tag.attrib['v'])
					if m is None:
						wrong_postal_code.append(tag.attrib['v'])
	print "The incorrect postal codes are:", wrong_postal_code					
	post_file.close()


# Update postal code #
def update_postal_code(postal_code):
	m = postal_code_re.match(postal_code)
	if m is None:
		# Convert lower case to capital letter #
		postal_code = postal_code.upper()
		# Add space in middle #
		if " " not in postal_code:
			postal_code = postal_code[:3] + " " + postal_code[3:]
		else:
			postal_code = None
	else:
		postal_code = postal_code
	return postal_code


# Street name update mapping #
mapping = {"Ct": "City",
           "ST": "Street",
           "street": "Street",
           "STREET": "Street",
           "st": "Street",
           "Ave": "Avenue",
           "Ave.": "Avenue",
           "Dr": "Drive",
           "R": "Road",
           "Rd": "Road",
           "Rd.": "Road",
           "rd": "Road",
           "road": "Road",
           "E.": "East",
           "E": "East",
           "E,": "East",
           "W.": "West",
           "W": "West",
           "W,": "West",
           "": "South",
           "S": "South",
           "N.": "North",
           "N": "North",
           "Blvd": "Boulevard",
           "Crt": "Court",
           "Cir": "Circle"}


def update_street_name(street_name, mapping):
	words = street_name.split(" ")
	for w in range(len(words)):
		if words[w] in mapping.keys():
#			print "Before:", street_name
			words[w] = mapping[words[w]]
#			print "After:", street_name
			street_name = " ".join(words)
	return street_name






