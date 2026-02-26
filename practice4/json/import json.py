import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in data.get('imdata', []):
    attributes = item.get('l1PhysIf', {}).get('attributes', {})
    dn = attributes.get('dn', '')
    descr = attributes.get('descr', '')
    speed = attributes.get('speed', '')
    mtu = attributes.get('mtu', '')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))