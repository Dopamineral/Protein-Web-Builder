#XML file in dir containing all proteins from Ecoli.
#Test file "ecoli_test.xml" with 10 cases to test program on.

import xml.etree.ElementTree as ET
import re

tree = ET.parse('uniprot-drosophila.xml')
root = tree.getroot()

#Finding the full name of the proteins


def find_full_name():
    """finds the full name in uniprot xml file and returns them in list 'namelist'"""
    namelist = list()
    for entry in root:
        for child in entry:
            if child.tag == "{http://uniprot.org/uniprot}protein":
                for branch in child:
                    if branch.tag == "{http://uniprot.org/uniprot}recommendedName":
                        for twig in branch:
                            if twig.tag == "{http://uniprot.org/uniprot}fullName":
                                full_name = twig.text
                                namelist.append(full_name)
    return namelist
                                
#list called full_names containing all the full names


def find_gene():
    """finds the primary gene in uniprot xml file and returns them in list 'genelist'"""
    genelist = list()
    for entry in root:
        for child in entry:
            if child.tag == "{http://uniprot.org/uniprot}gene":
                for branch in child:
                    for prim in branch.findall("[@type='primary']"):
                        genelist.append(prim.text)
                    
    return genelist



def find_alt_name():
    """finds alternative names in uniprot xml file and returns them in list 'namelist'"""
    namelist = list()
    for entry in root:
        templist = list()
        for child in entry:
            if child.tag == "{http://uniprot.org/uniprot}protein":
                for branch in child:
                    if branch.tag == "{http://uniprot.org/uniprot}alternativeName":
                        for twig in branch:
                            if twig.tag == "{http://uniprot.org/uniprot}fullName":
                                full_name = twig.text
                                templist.append(full_name)
        namelist.append(templist)
    return namelist




def find_accession():
    """finds accession numbers for protein in uniprot xml file"""
    accessionlist=list()
    for entry in root:
        templist = list()
        for child in entry:
            if child.tag == "{http://uniprot.org/uniprot}accession":
                templist.append(child.text)
        accessionlist.append(templist)
    return accessionlist



        
def find_function():
    """Finds all GO functions and assorts them per index"""
    functionlist = list()
    for entry in root:
        templist = list()
        for child in entry:
            if child.tag =="{http://uniprot.org/uniprot}dbReference":
                for dbref in child.findall("[@type='GO']"):
                    for prop in dbref:
                        for term in prop.findall("[@type='term']"):
                            xlist = term.attrib
                            for function in xlist:
                                if xlist[function] != 'term':
                                    templist.append(xlist[function])                        
        functionlist.append(templist)
    return functionlist

namelist = find_full_name()
#genelist = find_gene() --problem in indexing, need to solve
altnamelist=find_alt_name()
accessionlist = find_accession()
functionlist = find_function()


body = open('drosophila-index.html','a')

#building html file structure with above data

"""
format of HTML:
Ecol_index already has the necessary header elements -> now to just append the bodyand finalhtml tag


<h2>Chaperone protein DnaJ</h2> ------------#1
        
        <div class ="content"> ------------#2
            <div class ="metacontent"> ------------------------#16
                <p class="altname">altnamehere</p> ---------------#17
                <p class="genes">genehere</p> --------------------#18
                <p class="accession"><a href="http://www.uniprot.org/uniprot/accessionhere">accessionhere</a></p> #--------19
            </div> -----------------#20
            
            <h3>Biological Process</h3> ------------#3
            
            <div class = subcontent> ------------#4
                <p class="molecular">chaperone cofactor-dependent protein refolding</p> ------------#5
            </div> ------------#6
            
            <h3>Cellular Component</h3> ------------#7
            
            <div class = subcontent> ------------#8
                <p class="cellular">cytoplasm</p> ------------#9
            </div> ------------#10
            
            <h3>Molecular Function</h3> ------------#11
            
            <div class = subcontent> ------------#12
                <p class="molecular">ATP binding</p> ------------#13
            </div> ------------#14
        </div> ------------#15

</body> ------#21
            

</HTML> #22
        
"""
body.write('\n')

for i in range(len(namelist)):
    print(namelist[i])
    body.write('<h2>'+namelist[i]+'</h2>'+'\n') #1
    body.write('<div class = "content">'+'\n') #2
    body.write('<div class ="metacontent">'+'\n')#16

    for x in range(len(altnamelist[i])):
        altname = (altnamelist[i][x])
        body.write('<p class="altname">'+altname+'</p>'+'\n') #17

 #   body.write('<p class="genes"> GENE: '+genelist[i]+'</p>'+'\n') #18 --problem in indexing

    for x in range(len(accessionlist[i])):
        accession = (accessionlist[i][x])
        body.write('<p class="accession"><a href="http://www.uniprot.org/uniprot/'+accession+'" target="_blank">'+accession+'</a></p>'+'\n') #19
        
    body.write('</div>'+'\n')#20 

    body.write('<h3>Biological Process</h3>'+'\n') #3
    body.write('<div class = "subcontent">'+'\n') #4
    
    for x in range(len(functionlist[i])):
        firstname = (functionlist[i][x])
        if firstname[0] =='P':
            body.write('<p class="biological">'+firstname[2:]+'</p>'+'\n') #5

    body.write('</div>'+'\n') #6
    
    body.write('<h3>Cellular Component</h3>'+'\n') #7
    body.write('<div class = "subcontent">'+'\n') #8
    for x in range(len(functionlist[i])):
        firstname = (functionlist[i][x])
        if firstname[0] =='C':
            body.write('<p class="cellular">'+firstname[2:]+'</p>'+'\n') #9

    body.write('</div>'+'\n') #10
            
    body.write('<h3>Molecular Function</h3>'+'\n') #11
    body.write('<div class = "subcontent">'+'\n') #12
    for x in range(len(functionlist[i])):
        firstname = (functionlist[i][x])
        if firstname[0] =='F':
            body.write('<p class="molecular">'+firstname[2:]+'</p>'+'\n') #13

    body.write('</div>'+'\n') #14
    body.write('</div>'+'\n') #15

body.write('</body>'+'\n') #21
body.write('</html>'+'\n') #22


body.close()

     
                    

        
                    
                        
        
                    
                    
                    
    
