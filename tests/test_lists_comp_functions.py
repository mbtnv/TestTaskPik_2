from metro_verificate.main import get_lists_difference, get_lists_intersection

first_list = ['q', 'w', 'w']
second_list = ['w', 'w', 'e']


def test_lists_difference():
    assert get_lists_difference(first_list, second_list) == ['q']


def test_lists_intersection():
    assert get_lists_intersection(first_list, second_list) == ['w', 'w']
