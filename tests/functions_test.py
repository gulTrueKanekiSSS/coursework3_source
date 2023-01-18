import pytest

import functions.functions
from functions.functions import *

def test_load_posts():
    assert type(load_posts()) == list, 'формат не является json'
    assert type(load_posts()[0]) == dict, 'ты харош'

def test_load_comments():
    assert type(load_comments(1)) == list, 'формат не является json'

def test_get_post_by_pk():
    for i in range(len(load_posts())):
        assert type(get_post_by_pk(i)) == list
