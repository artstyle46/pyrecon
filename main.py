from general import *
from domain import *
from get_ip import *
from nmap_scan import *
from robots import *
from whois import *


ROOT_DIR = 'Url_details'

create_dir(ROOT_DIR)

def get_info(name, url):
    domain_name = get_domain_name(url)
    ip_addr = get_ip_address(domain_name)
    nmap = get_nmap("-F", ip_addr)
    robots_txt = get_robots_txt(url)
    who_is = get_whois(domain_name)
    save_info(name,url,domain_name,ip_addr,nmap,robots_txt,who_is)

def save_info(name,url,domain_name,ip_addr,nmap,robots_txt,who_is):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + "/top_level_domain.txt", domain_name)
    write_file(project_dir + "/ip_address.txt", ip_addr)
    write_file(project_dir + "/nmap.txt", nmap)
    write_file(project_dir + "/robots_txt.txt", robots_txt)
    write_file(project_dir + "/whois.txt", who_is)


name = raw_input("enter name of folder:")
url = raw_input("enter the url:")

get_info(name, url)