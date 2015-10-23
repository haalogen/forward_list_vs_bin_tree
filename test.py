"""Tests for func.py"""
import func as fu
from nose.tools import *


def test_node():
    node = fu.Node('hello')
    assert_equal(node.getData(), 'hello')
    assert_equal(node.getNext(), None)
    

def test_FwdList_add():
    fwd_list = fu.FwdList()
    fwd_list.add('hamburger')
    
    assert_is_not_none(fwd_list)
    assert_is_not_none(fwd_list.head)
    assert_equal(fwd_list.head.getData(), 'hamburger')
    
    fwd_list.add('crazy')
    fwd_list.add('mushroom')
    
    assert_equal(fwd_list.head.getData(), 'crazy')
    
    
    






