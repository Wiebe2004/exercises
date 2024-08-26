import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize('string', [
    '()',
    '(())',
    '()(())',
    '(()(()))',
])
def test_matching_parentheses(string):
    assert matching_parentheses(string), f"String: {string} is all matching"

@pytest.mark.parametrize('string', [
    "((())",
    "(()))",
    "())(",
    "(()))(",
    "())(()",
])
def test_NonMatching_parentheses(string):
    assert not matching_parentheses(string), f"String: {string} is not matching"
    #Alternatieve oplossing, kan ook voor true
    # assert matching_parentheses(string) == False, f"String: {string} is not matching"