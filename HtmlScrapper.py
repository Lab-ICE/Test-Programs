'''
Created on Jan 22, 2015

@author: Thomas
'''
import urllib2
import re
from bs4 import BeautifulSoup
from bs4.element import SoupStrainer
from test.test_ssl import NULLBYTECERT
from types import NoneType

def Beautiful_Soup_Creator(url):

    user_agent="Mozilla/5.0 (compatible; MSIE 5.5; Windows NT 5.0"
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url, None, headers)
    string_html = urllib2.urlopen(req).read()
    test_name_html="test.html"
    with open (test_name_html,"w") as f:
        f.write(string_html)
    
    f.close()
    file=open('test.html','r')
    read_file=file.read()
    read_file_decode=read_file.decode('unicode_escape').encode('ascii','ignore')
    #encode ascii???
    file.close()
    soup=BeautifulSoup(read_file_decode)
    
    return soup    

Linear_Amp_Soup=Beautiful_Soup_Creator('http://www.digikey.com/product-detail/en/CA-2207/CP-2207-ND/701168')
#'http://www.digikey.com/product-detail/en/OPA357AIDBVT/296-13009-1-ND/479728'
text_Linear_Amp_Soup=Linear_Amp_Soup.get_text()
Part_Number="(?<=Digi-Key Part Number)(.*)"
Manufacturer="(?<=Manufacturer)(.*)"
Manufacturer_part_number="(?<=Manufacturer Part Number)(.*)"
Description="(?<=Description)(.*)"
Lead_Status_ROHS_Status="(?<=Lead Free Status / RoHS Status)(.*)"
Category="(?<=Category )(.*)"
Family="(?<=Family)(.*)"
Series="(?<=Series)(.*)"
Packaging="(?<=Packaging)(.*)"
Amplifier_Type="(?<=Amplifier)(.*)"
Number_of_Circuits="(?<=Number of Circuits)(.*)"
Slew_Rate="(?<=Slew Rate)(.*)"
Output_Type="(?<=Output Type)(.*)"
Gain_Bandwidth_Product="(?<=Gain Bandwidth Product)(.*)"
db_Bandwidth="(?<=-3db Bandwidth)(.*)"


dict_Para={"Part_Number":"(?<=Digi-Key Part Number)(.*)", #Dictionary data structure of each parameter 
           "Manufacturer":"(?<=Manufacturer)(.*)",
           "Manufacturer_part_number":"(?<=Manufacturer Part Number)(.*)",
           "Description":"(?<=Description)(.*)",
           "Family":"(?<=Family)(.*)",
           "Series":"(?<=Series)(.*)",
           "Packaging":"(?<=Packaging)(.*)",
           "Amplifier_Type":"(?<=Amplifier)(.*)",
           "Number_Of_Circuts":"(?<=Number of Circuits)(.*)",
           "Slew_Rate":"(?<=Slew Rate)(.*)",
           "Output_Type":"(?<=Output_Type)(.*)",
           "Gain_Bandwidth_Product":"(?<=Gain Bandwidth Product)(.*)",
           "db_Bandwidth":"(?<=-3b Bandwidth)(.*)"}




#Gets the parameter description 
def description_getter(regex): 
    desc=re.search(regex,text_Linear_Amp_Soup)
    if desc:
        return_string=desc.group(0)
    else:
        return_string="-"
    return return_string
part_num_Linear_amp=description_getter(Part_Number)
Manufacturer_Linear_Amp_Soup=description_getter(Manufacturer)
Manufacturer_part_number_soup=description_getter(dict_Para["Manufacturer_part_number"])
test_num_circuit=description_getter(dict_Para["Number_Of_Circuts"])

print part_num_Linear_amp
print Manufacturer_Linear_Amp_Soup
print Manufacturer_part_number_soup
#print test_num_circuit
#print text_Linear_Amp_Soup


    











