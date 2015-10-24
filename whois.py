import os


def get_whois(top_level_domain):
    command = "whois " + top_level_domain
    process = os.popen(command)
    results = str(process.read())
    return results

#print (get_whois("shapy.in"))