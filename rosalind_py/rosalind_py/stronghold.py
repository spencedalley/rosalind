from __future__ import division 

__doc__ = """

    Notes
    -----
    Add notes

    
"""



import itertools
import logging
import operator
import string
import time

BASE_PAIRS = ["A", "C", "G", "T"]

RNA_CODON_TABLE = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
    "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

MONOISOTOPIC_MASS_TABLE = {
    "A": 71.03711, 
    "C": 103.00919, 
    "D": 115.02694, 
    "E": 129.04259, 
    "F": 147.06841, 
    "G": 57.02146, 
    "H": 137.05891, 
    "I": 113.08406, 
    "K": 128.09496, 
    "L": 113.08406, 
    "M": 131.04049, 
    "N": 114.04293, 
    "P": 97.05276, 
    "Q": 128.05858, 
    "R": 156.10111, 
    "S": 87.03203, 
    "T": 101.04768, 
    "V": 99.06841, 
    "W": 186.07931, 
    "Y": 163.06333 
}



################################################################################
# Count nucleotides
def nucleotide_count(dna):
    """Returns a count of base pairs in a given dna sequence"""
    if dna == "" or dna is None or type(dna) is not str:
        return None

    dna = dna.upper()
    a = dna.count("A")
    c = dna.count("C")
    g = dna.count("G")
    t = dna.count("T")

    return (a, c, g, t)

################################################################################
# DNA complement
def complement_create(dna):
    """Returns the complement of a dna sequence"""
    if dna == "" or dna is None or type(dna) is not str:
        return None

    dna = dna.upper()
    complement = []

    for i in range(len(dna)):
        if dna[i] == "A": complement.insert(0, "T")
        elif dna[i] == "C": complement.insert(0, "G")
        elif dna[i] == "G": complement.insert(0, "C")
        elif dna[i] == "T": complement.insert(0, "A")

    return "".join(complement)

################################################################################
# DNA transcription
def dna_transcribe(dna):
    """Transcribes dna to rna"""
    if dna == "" or dna is None or type(dna) is not str:
        return None

    return dna.upper().replace("T", "U")

################################################################################
# Computing GC content in DNA sequence
def gc_percent(fasta_dict):
    """Computes the gc content in a given dna sequence

    Parameters
    -----------
    dna: dictionary
         A dictionary of the form {fasta_tag[string]: dna_sequence[string]}

    Returns
    -------
    result: dictionary
            A dictionary of the form {(string)fasta_tag: (float)gc_percent}
    """
    if fasta_dict is None or fasta_dict == {} or type(fasta_dict) is not dict:
        return None

    result = {}

    for tag, seq in fasta_dict.items():
        g_count = fasta_dict[tag].upper().count("G")
        c_count = fasta_dict[tag].upper().count("C")
        result[tag] = (((g_count + c_count) / len(fasta_dict[tag])) * 100)

    return result

def max_gc_percent(fasta_gc_dict):
    "Returns the max GC count from a series of GC percentages as a string"
    current_max = 0
    result = ""

    for tag, gc_percent in fasta_gc_dict.items():
        if gc_percent > current_max:
            current_max = gc_percent
            result = "%s %s%%" % (tag, gc_percent)

    return result

################################################################################
# Motifs
def motif_find(dna, seq):
    """Returns list of indices where seq is found in dna"""
    i, positions = 0, []

    while True:
        i = dna.find(seq, i+1)
        if i != -1: positions.append(i+1)
        else: break

    return positions

################################################################################
# Point mutations

def hamming_distance(s, t):
    """Returns number of positions where s differs from t"""

    if len(s) != len(t):
        raise ValueError("The strings must be equal length")

    if s is None or t is None or s is "" or t is "":
        return None

    return len(list(filter(lambda pair: pair[0] != pair[1],
                           zip(list(s), list(t)))))


################################################################################
# Fibonnaci
def fib(n, k):
    """Computes fibonnaci numbers"""
    if n < 2: return n
    else: return fib(n-1, k) + (fib(n-2, k) * k)

################################################################################
# RNA translation
def rna_translate(rna):
    """Translates an rna sequence to a protein"""

    if type(rna) is not str or len(rna) == 0:
        return None

    protein = ""

    for i in range(0, len(rna), 3):
        amino_acid = RNA_CODON_TABLE.get(rna[i:i+3], None)
        if amino_acid is None:
            # TODO: ValueError or just ignore
            raise ValueError("Got \"None\" on protein transcription")
        elif amino_acid == "STOP" or (i + 3 - 1) > len(rna):
            return protein
        else:
            protein += amino_acid

    return protein


################################################################################
# FASTA Utils

def fasta_convert(fasta_file):
    """Converts a fasta file to a dictionary of form
       {(string)fasta_tag: (string)dna_seq}
      """
    try:
        contents = open(fasta_file).read().replace("\r", "").split("\n")
    except IOError:
        raise IOError("Unable to open file")

    fasta_tag = ""
    result = {}

    for i in range(len(contents)):
        if contents[i].startswith(">"):
            fasta_tag = contents[i]
            result[fasta_tag] = ""
        else:
            result[fasta_tag] += contents[i]

    return result


################################################################################
# Consensus building

def matrix_build(d):
    result = []

    for key, val in d.items():
        result.append(list(val))

    return result

def get_matrix_columns(matrix, offset):
    """Returns column of multidimensional matrix"""
    return [row[offset] for row in matrix]


def profile_build(fasta_dict):
    """Returns dictionary of the form"""
    profile = {}
    profile["A"], profile["C"], profile["G"], profile["T"] = [], [], [], []
    dna_matrix = matrix_build(fasta_dict)

    for i in range(len(dna_matrix[0])):
        col = get_matrix_columns(dna_matrix, i)
        profile["A"].append(col.count("A"))
        profile["C"].append(col.count("C"))
        profile["G"].append(col.count("G"))
        profile["T"].append(col.count("T"))

    return [profile["A"], profile["C"], profile["G"], profile["T"]]

def profile_print(profile_matrix):
    for i in range(len(profile_matrix)):
        profile = "{0}: {1}".format(BASE_PAIRS[i], " ".join([str(val) for val in profile_matrix[i]]))
        print(profile)

def consensus_build(fasta_file, print_profile=False):
    fasta_dict = fasta_convert(fasta_file)
    profile_matrix = profile_build(fasta_dict)
    consensus = ""

    for i in range(len(profile_matrix[0])):
        col = get_matrix_columns(profile_matrix, i)
        max_val_index = col.index(max(col))
        consensus += BASE_PAIRS[max_val_index]

    if print_profile is True:
        profile_print(profile_matrix)

    return consensus

################################################################################
# Overlap Graphs

# I think that the problem is a prefix is one string

def seq_overlap_all(fasta_dict):
    """Takes in 2 SuffixTree's and compares their suffix_array to see if there is a match"""

    fasta_tags = list(fasta_dict.keys())
    fasta_suffix_arrays = {}
    overlaps = []

    for tag, seq in fasta_dict.items():
        fasta_suffix_arrays[tag] = SuffixArray(seq)

    for i in range(len(fasta_tags)):
        for j in range(len(fasta_tags)):
            f1 = fasta_suffix_arrays[fasta_tags[i]].suffix_only
            f2 = fasta_suffix_arrays[fasta_tags[j]].prefix_only
            if fasta_tags[i] == fasta_tags[j]:
                continue
            if f1.intersection(f2):
                val = sorted([fasta_tags[i], fasta_tags[j]])
                val.reverse()
                if val not in overlaps:
                    overlaps.append(val)
            else:
                print("False")

    return overlaps

def seq_overlap_offset(fasta_dict, k):
    fasta_tags = list(fasta_dict.keys())
    overlap = []

    for i in range(len(fasta_tags)):
        for j in range(len(fasta_tags)):
            if fasta_tags[i] == fasta_tags[j]:
                continue
            elif fasta_dict[fasta_tags[i]][-k:] == fasta_dict[fasta_tags[j]][:k]:
                overlap.append([fasta_tags[i].replace(">", ""), fasta_tags[j].replace(">", "")])
    return overlap


################################################################################
# Suffix Array
class SuffixArray():

    def __init__(self, s):
        # takes in a suffix tree and
        self.s = s
        self.array = self.create()
        self.prefix_only = self.create_prefix()
        self.suffix_only = self.create_suffix()
        self.length = len(self.array)
        self.indices = None

    def create(self, prefix=False, suffix=False):
        """Returns a set of suffixes"""
        result = set()

        for i in range(1, len(self.s)):
            result.add(self.s[-i:])

        result.add(self.s)
        return result

    def create_prefix(self):
        result = set()
        length = int(len(self.s)/2)

        for i in range(length):
            result.add(self.s[i:length])

        return result

    def create_suffix(self):
        result = set()
        length = int(len(self.s)/2)

        for i in range(length+1, len(self.s)):
            result.add(self.s[i:])

        return result

    def find_suffix(data, length):
        pass

    def substr(s, i):
        pass

# Create all substrings 

def substrings_find_all(s, reverse=False): 
    result = []
    # maybe just return a generator that can yield
    for i in range(len(s)): 
        for j in range(len(s)): 
            if j <= i+1: 
                # ignore single characters
                continue 
            if s[i:j] not in result: 
                result.append(s[i:j])
    return result

def shared_motifs(fasta_dict): 
    fasta_tags = list(fasta_dict.keys())
    primary_seq = fasta_dict[fasta_tags[0]]
    seq_len = len(primary_seq)
    result = []
    match = ""

    for i in range(seq_len): 
        for j in range(seq_len): 
            if j <= i+1: 
                # ignore single characters and index out of bounds
                continue 
            else: 
                match = primary_seq[i:j]
                for k in range(len(fasta_tags)): 
                    if fasta_dict[fasta_tags[k]].find(match) != -1: 
                        continue
                    else: 
                        match = ""
                        break

                if match == "":
                    pass
                else: 
                    if match not in result: 
                        result.append(match)
    return result

# Mendelian genetics
def mendel(k, m, n): 
    return ((k*k - k) + 2*(k*m) + 2*(k*n) + (.75*(m*m - m)) + 2*(.5*m*n))/((k + m + n)*(k + m + n -1))

def mortal_rabbits(n, m): 
    """Return """
    ages = ([1] + ([0] * (m-1)))

    for i in range(n-1): 
        ages = [sum(ages[1:])] + ages[:-1]

    return sum(ages)

# Enumerating genes
def gene_enumerate(n, output_file): 
    """Computes permutations and outputs to file

    Parameters
    -----------
    n (int): A positive integer n <=7
    output_file (str): File that results are to be written to 

    Yields
    ------
    tuple: A tuple of permutations
    """
    i = itertools.permutations(range(1, n+1))
    f = open(output_file, "w")
    chars_to_remove = {ord("("): None, ord(")"): None, ord(","): None}
    count = 0

    while True: 
        try: 
            val = str(next(i)).translate(None, "(),")
            count += 1
            f.write(val+"\n")
        except StopIteration: 
            break

    f.write(str(count))
    f.close()

def permutations(l):
    """Returns list of permutations

    Parameters
    -----------
    l (list): A list of elements

    Returns
    -------
    result(2d list): A list of all permutations of elements from l
    """
    result =  [ (m[:i] + [l[0]] + m[i:]) for m in permutations(l[1:]) for i in xrange(len(m)+1) ] if len(l)>1 else [l]
    return result

def buildPhenotypeMatrix(pheno1, pheno2): 
    result = []
    for i in range(len(s1)): 
        s = []

def expected_offspring(l): 
    """Returns number of expected offspring to have dominant phenotype

    Parameters
    -----------
    l (int list): A list of number of couples with the following genotypes
        1) AA-AA
        2) AA-Aa
        3) AA-aa
        4) Aa-Aa
        5) Aa-aa
        6) aa-aa

    Returns
    -------
    result (float): percent chance that the offspring of parents will have 'A' in 
                    their phenotype
    """
    if len(l) == 0: return 0
    return (l[0]*2) + (l[1]*2) + (l[2]*2) + (l[3]*3/4*2) + (l[4]*1/2*2) + (l[0]*0)

def compute_protein_mass(protein):
    """Returns mass of protein

    Parameters
    -----------
    protein (str): A list of number of couples with the following genotypes

    Returns
    -------
    result (float): mass of protein
    """
    if protein is None: return 0
    result = 0 

    for symbol in protein: 
        mass = MONOISOTOPIC_MASS_TABLE.get(symbol, None)
        if mass is not None: result += mass 

    return result

    
if __name__ == "__main__": 
    pass

