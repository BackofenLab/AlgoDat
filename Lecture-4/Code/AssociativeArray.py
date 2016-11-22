# creates a new map (called dictionary)
countries = {"DE" : "Deutschland", \
	"EN" : "England"}

# check if element exists
if "EN" in countries:
	print("Found %s!" % countries["EN"])

# map key "DE" to value 0
countries["DE"] = "Germany"

# delete key "DE"
del countries["DE"]
