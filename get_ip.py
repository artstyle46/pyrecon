import os

def get_ip_address(top_level_domain):
    command = "host " + top_level_domain
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]

#print (get_ip_address("shapy.in"))