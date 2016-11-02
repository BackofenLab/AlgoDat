# creates a new map (called dictionary)
countires = {"DE" : "Deutschland", \
	"EN" : "England"}

# check if element exists
if "EN" in countires:
	print("Found %s!" % countires["EN"])

# map key "DE" to value 0
countires["DE"] = "Germany"

# delete key "DE"
del countires["DE"]
