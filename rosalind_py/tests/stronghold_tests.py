from nose.tools import *
from rosalind_py.stronghold import *

EXPECTED_FASTA_DICT = {">Rosalind_0808": "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT",
                       ">Rosalind_5959": "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC",
                       ">Rosalind_6404": "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"}

EXPECTED_GC_DICT = {">Rosalind_5959": 53.57142857142857,
                    ">Rosalind_6404": 53.75,
                    ">Rosalind_0808": 60.91954022988506}

def setup():
	pass

def teardown():
	pass

def test_nucleotide_count():
	dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
	count = nucleotide_count(dna)
	assert_equal(count, (20, 12, 17, 21), "Wrong count on nucleotide_count")

	count_none = nucleotide_count(12321)
	assert_equal(count_none, None, "Should have gotten None on invalid input")


def test_complement_create():
    dna =  "AAAACCCGGT"
    complement = complement_create(dna)
    assert_equal(complement, "ACCGGGTTTT", "Wrong DNA complement created")
    assert_equal(complement_create(None), None,
                "Should have gotten None on invalid input")
    assert_equal(complement_create(""), None,
                "Should have gotten None on invalid input")

def test_dna_transcribe():
    dna = "GATGGAACTTGACTACGTAAATT"
    rna = dna_transcribe(dna)
    expected_rna = "GAUGGAACUUGACUACGUAAAUU"

    assert_equal(rna, expected_rna, "Failed to create correct RNA")
    assert_equal(dna_transcribe(None), None,
                 "Should have gotten None on invalid input")
    assert_equal(dna_transcribe(""), None,
                 "Should have gotten None on invalid input")
    assert_equal(dna_transcribe(1), None,
                 "Should have gotten None on invalid input")


def test_fasta_convert():
    fasta_dict = fasta_convert("data/gc_test.txt")
    gc_dict = gc_percent(fasta_dict)

    assert_equal(fasta_dict[">Rosalind_0808"],
                 EXPECTED_FASTA_DICT[">Rosalind_0808"], "Wrong value on lookup")
    assert_equal(fasta_dict[">Rosalind_5959"],
                 EXPECTED_FASTA_DICT[">Rosalind_5959"], "Wrong value on lookup")
    assert_equal(fasta_dict[">Rosalind_6404"],
                 EXPECTED_FASTA_DICT[">Rosalind_6404"], "Wrong value on lookup")

def test_gc_percent_and_max_gc_percent():
    fasta_dict = fasta_convert("data/gc_test.txt")
    gc_dict = gc_percent(fasta_dict)

    assert_equal(gc_dict[">Rosalind_0808"],
                 EXPECTED_GC_DICT[">Rosalind_0808"], "Wrong value on lookup")
    assert_equal(gc_dict[">Rosalind_5959"],
                 EXPECTED_GC_DICT[">Rosalind_5959"], "Wrong value on lookup")
    assert_equal(gc_dict[">Rosalind_6404"],
                 EXPECTED_GC_DICT[">Rosalind_6404"], "Wrong value on lookup")

    # Testing max GC percent
    assert_equal(max_gc_percent(gc_dict), ">Rosalind_0808 60.91954022988506%",
                 "Wrong value on percentage calculation")

def test_motif_find():
    dna = "GATATATGCATATACTT"
    seq = "ATAT"
    expected = [2, 4, 10]

    assert_equal(motif_find(dna, seq), expected,
                 "Wrong number of motifs counted")

def test_point_mutations():
    seq1 = "GAGCCTACTAACGGGAT"
    seq2 = "CATCGTAATGACGGCCT"
    expected_value = 7
    assert_equals(hamming_distance(seq1, seq2), expected_value,
                  "Wrong value for hamming distance")

def test_rna_translate():
    rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    expected_value = "MAMAPRTEINSTRING"

    assert_equal(rna_translate(rna), expected_value,
                 "Wrong value on transcription")
    assert_equal(rna_translate(""), None,
                 "Wrong value on empty str passed in")
    assert_equal(rna_translate(None), None,
                 "Wrong value on None passed in")

def test_shared_motifs():
    fasta_dict = {
        ">Rosalind_1": "GATTACA", 
        ">Rosalind_2": "TAGACCA", 
        ">Rosalind_3": "ATACA"
    }

    expected_values = ["TA", "AC"]
    result = shared_motifs(fasta_dict)
    assert_equal(result, expected_values, "Wrong values shared motifs")

def test_mendel(): 
    result = int(mendel(2, 2, 2) * 10000)
    expected = int(0.78333 * 10000)
    assert_equal(result, expected, "Wrong value for mendelian genetics")
    
def test_mortal_rabbits(): 
    result = mortal_rabbits(6, 3)
    expected = 4
    assert_equal(result, expected, "Wrong value calculated for mortal rabbits")

def test_expected_offspring(): 
    results = [[18220, 17704, 19925, 16701, 18442, 17543], [1, 0, 0, 1, 0, 1]]
    expected = [155191.5, 3.5]
    for i in range(len(results)): 
        assert_equal(expected_offspring(results[i]), expected[i], 
                     "Wrong value for expected offspring")

def test_compute_protein_mass(): 
    proteins = ["SKADYEK"]
    expected = [821]
    for i in range(len(proteins)): 
        assert_equal(int(compute_protein_mass(proteins[i])), expected[i], 
                     "Wrong mass computed")













