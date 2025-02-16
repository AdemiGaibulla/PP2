import json

with open("PP2/TSIS4/json/sample-data.json") as file:
    data = json.load(file)

print("Interface status")
print("=" * 85)
print("{:<50} {:<20} {:<7} {:<5}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "-" * 6, "-" * 6)

for items in data["imdata"]:
    item = items["l1PhysIf"]["attributes"]
    print("{:<50} {:<20} {:<7} {:<5}".format(item["dn"], item["descr"], item["speed"],item["mtu"]))