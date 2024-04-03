

from lib.string_builder import *

def test_string_builder_adds_banana():
    stringbuilder = StringBuilder()
    stringbuilder.add('banana')
    result = stringbuilder.output()

    assert result == 'banana'

def test_string_builder_size_works_banana():
    stringbuilder = StringBuilder()
    stringbuilder.add('banana')
    result = stringbuilder.size()
    assert result == 6

def test_string_builder_adds_multiple_strings():
    stringbuilder = StringBuilder()
    stringbuilder.add('banana')
    stringbuilder.add('apple')
    result = stringbuilder.output()

    assert result == 'bananaapple'

    
