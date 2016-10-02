from nose.tools import *
from rosalind_py.leet import * 

def setup(): 
    pass

def teardown(): 
    pass 

def test_regexMatcher(): 
    assert_equal(regexMatch("aaab", "a*b"), True)
    assert_equal(regexMatch("bccbb", "bc*cb."), True)
    assert_equal(regexMatch("aaab", "a*ab"), True)
    assert_equal(regexMatch("aaaab", "a*aaaaaaaab"), True)
    assert_equal(regexMatch("aaaajkfdslfjsdlk432432", ".*"), True)
    assert_equal(regexMatch("ba", "a*ba"), True)
    assert_equal(regexMatch("babab", "cava"), False)
    assert_equal(regexMatch("", "a*"), True)
    assert_equal(regexMatch("aab", "c*a*b*"), True)
    assert_equal(regexMatch("hithere", ""), False)
    assert_equal(regexMatch("aa", "aa"), True)
    assert_equal(regexMatch("aaa", "aaaa"), False)
    assert_equal(regexMatch("abbbbb", ".*c"), False)
    assert_equal(regexMatch("aaa", "ab*a*c*a"), True)
    assert_equal(regexMatch("bbbba", ".*a*a"), True)
    assert_equals(regexMatch("", ".*b"), False)
    assert_equals(regexMatch("ab", ".*.."), True)
    # assert_equals(regexMatch("ab", ".*..c*"), True)

def test_atoi(): 
    assert_equal(atoi("-123"), -123)
    assert_equal(atoi("-+-123"), 0)
    assert_equal(atoi("+-asd123"), 0)
    assert_equals(atoi("   -12    "), -12)
    assert_equals(atoi("-123a123"), -123)
    assert_equals(atoi("123an"), 123)
    assert_equals(atoi("0"), 0)
    assert_equals(atoi("-"), 0)
    assert_equals(atoi("+"), 0)
    assert_equals(atoi(" "), 0)
    assert_equal(atoi(""), 0)

def test_longest_common_prefix(): 
    str_list = ["hello", "helloo", "hello", "hello"]
    assert_equals(longestCommonPrefix(str_list), "hello")
    str_list = ["hello", "hello", "hello", "hello"]
    assert_equals(longestCommonPrefix(str_list), "hello")
    str_list = ["aa", "a", "a", "a"]
    assert_equals(longestCommonPrefix(str_list), "a")
    str_list = ["a", "b"]
    assert_equals(longestCommonPrefix(str_list), "")
    str_list = []
    assert_equals(longestCommonPrefix(str_list), "")

def test_getLongestStringFromList(): 
    str_list = ["me", "you", "hello", "there", "I", "am"]
    assert_equals(getLongestStringFromList(str_list), "hello")
    str_list = ["me", "you", "hiflafjldas", "there", "I", "am"]
    assert_equals(getLongestStringFromList(str_list), "hiflafjldas")
    str_list = ["me", "you", "hello", "there", "I", "hihihi"]
    assert_equals(getLongestStringFromList(str_list), "hihihi")

def test_validParen(): 
    assert_equals(validParen(""), True)
    assert_equals(validParen("()"), True)
    assert_equals(validParen("[)"), False)
    assert_equals(validParen("[[]]"), True)
    assert_equals(validParen("()()()(){}[][]{{[]()}}"), True)
    assert_equals(validParen("]"), False)

def test_integerToEnglishWords(): 
    assert_equals(integerToEnglishWords(1), "One")
    assert_equals(integerToEnglishWords(10), "Ten")
    assert_equals(integerToEnglishWords(12), "Twelve")
    assert_equals(integerToEnglishWords(14), "Fourteen")
    assert_equals(integerToEnglishWords(12), "Twelve")
    assert_equals(integerToEnglishWords(122), "One Hundred Twenty Two")
    assert_equals(integerToEnglishWords(510), "Five Hundred Ten")
    assert_equals(integerToEnglishWords(645), "Six Hundred Forty Five")
    assert_equals(integerToEnglishWords(711), "Seven Hundred Eleven")
    assert_equals(integerToEnglishWords(999), "Nine Hundred Ninety Nine")
    assert_equals(integerToEnglishWords(1000), "One Thousand")
    assert_equals(integerToEnglishWords(10000), "Ten Thousand")
    assert_equals(integerToEnglishWords(11000), "Eleven Thousand")
    assert_equals(integerToEnglishWords(12000), "Twelve Thousand")
    assert_equals(integerToEnglishWords(22000), "Twenty Two Thousand")
    assert_equals(integerToEnglishWords(100000), "One Hundred Thousand")
    assert_equals(integerToEnglishWords(120000), "One Hundred Twenty Thousand")
    assert_equals(integerToEnglishWords(143000), "One Hundred Forty Three Thousand")
    assert_equals(integerToEnglishWords(1143000), "One Million One Hundred Forty Three Thousand")
    assert_equals(integerToEnglishWords(10143000), "Ten Million One Hundred Forty Three Thousand")











