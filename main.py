import json
import requests
import time

def submit(address, zipcode):
    url = f'https://portal.gonetspeed.com/service/addresscheck?streetaddress={address}.&zipCode={zipcode}&servicetype=Residential'

    r = requests.get(
        url
    ) 

    print(f'{number} {street} {zipcode} \t {r.status_code}')


t0 = time.time()
addr_count = 0
with open('us_ct_statewide-addresses-state.geojson', 'r') as f:
    for line in f.readlines():
        address = json.loads(line)

        number = address['properties']['number']
        street = address['properties']['street']
        unit = address['properties']['unit']
        city = address['properties']['city']
        state = 'CT'
        zipcode = address['properties']['postcode']
        
        if zipcode == '06518' or city == 'Hamden':
            print(f'{number} {street} {zipcode}', end='\r')
            submit(f'{number} {street}', zipcode)
            addr_count += 1

print(f'Complete! Submitted {addr_count} addresses in {time.time - t0} sec')
