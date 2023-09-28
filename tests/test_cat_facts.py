from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_provide_fact():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock._get_cat_fact.return_value = response_mock
    response_mock.json.return_value = {"fact":"Mohammed loved cats and reportedly his favorite cat, Muezza, was a tabby. Legend says that tabby cats have an \u201cM\u201d for Mohammed on top of their heads because Mohammad would often rest his hand on the cat\u2019s head."}
    catfacts = CatFacts(requester_mock,response_mock)
    assert catfacts.provide() == "Cat fact: Mohammed loved cats and reportedly his favorite cat, Muezza, was a tabby. Legend says that tabby cats have an \u201cM\u201d for Mohammed on top of their heads because Mohammad would often rest his hand on the cat\u2019s head."