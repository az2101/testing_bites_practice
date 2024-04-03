

from lib.gratitudes import *

def test_gratitudes_for_family():
    gratitudes = Gratitudes()
    gratitudes.add('family')
    result = gratitudes.format()
    assert result == 'Be grateful for: family'

def test_gratitudes_for_2_strings():
    gratitudes = Gratitudes()
    gratitudes.add('family')
    gratitudes.add('health')
    result = gratitudes.format()
    assert result == 'Be grateful for: family, health'



