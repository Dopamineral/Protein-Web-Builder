# Protein Web Builder

The python file scrapes a full protein data XML file that was downloaded from uniprot. It extracts relevant Gene Ontology data and adds this to a hard coded html structure that will be built into a final webpage.

The built webpage consists of a simple list of all the proteins of a given organims. Basic jQuery was used to make it somewhat interactive. If you click on the name of the protein, it reveals a dropdown bar with 3 different options: Biological function, Molecular function and Subcellular localisation. Which themselves can be clicked, revealing all the relevant GO data for the given parameter.

Styling was done with CSS and is quite exotic and might not be to everyone's taste, but its definitely memorable!
