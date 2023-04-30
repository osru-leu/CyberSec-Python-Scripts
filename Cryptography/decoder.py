filename=""
filename = "Substitution.txt"    #Uncomment this to specify a file - useful for testing with the same input file
mapper = {}   # Define an empty dictionary object

"""
The following mappings will allow you to modify the decoding process.
After you run a frequency analysis, you will have the most common letter in your
encoded text.  Suppose the letter Q is the most common letter in the encoded text. We
would expect that to be the letter E.  In the mapping below, change the E INSIDE
the mapper to a Q.  In other words, the first line would read:
mapper['Q']='E' and so on.  This key-value mapping defines the substitution, so this is saying map Q -> E.

Ensure that each letter only occurs once inside the brackets - each key-value mapping should occur only once. So the Q (second up from the bottom)
would need to change based on the change above.

"""
mapper['J']='E'    # Expected 12.7% S  ETOAI
mapper['E']='T'    # Expected 9.1% S  
mapper['L']='A'    # Expected 8.2% S
mapper['A']='O'    # Expected 7.5% S
mapper['U']='I'    # Expected 7.0% S <

mapper['X']='N'    # Expected 6.7%  u
mapper['M']='S'    # Expected 6.3% <x
mapper['V']='H'    # Expected 6.1%  v
mapper['D']='R'    # Expected 6.0%  d 
mapper['G']='D'    # Expected 4.3%  c

mapper['C']='L'    # expected 4.0 Expected 1.0%
mapper['Y']='U'    # Expected 2.8%
mapper['R']='C'    # Expected 2.8% could swap with B
mapper['B']='M'    # Expected 2.4%
mapper['I']='W'    # Expected 2.4%

mapper['Z']='F'    # Expected 2.2%
mapper['S']='Y'    # Expected 2.0%
mapper['F']='G'    # Expected 2.0%
mapper['K']='P'    # Expected 1.9%
mapper['H']='B'    # Expected 1.5%

mapper['W']='V'    # Expected 1.0%
mapper['T']='K'    # Expected .8%
mapper['N']='X'    # expected .2 Expected .15%
mapper['Q']='J'    # expected .2 Expected .15%
mapper['P']='Q'    # Expected .1%

mapper['O']='Z'    # Expected .07%

f=""

while (f=="" or f=="error"):  #NOTE: Filename cannot be "error"
    if filename=="":
        filename = input("What is the name of the file to open? ")
    try:
        f=open(filename)
    except:
        f="error"
        
intext = ""      
outtext = ""
for lett in f.read():
    if lett.upper() in mapper.keys():
        lett = lett.upper()
        intext += lett
        outtext += mapper[lett]
        
f.close()
print("Original Text ",intext)
print("Decrypted Text",outtext)