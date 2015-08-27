from stats import mean
from nose.tools import assert_equal

def test_mean():
        assert_equal(mean([2,4]), 3)
#test_mean()

def test_float_mean():
        assert_equal(mean([1.0,2]), 1.5)
#test_float_mean()

def test_neg_mean():
	assert_equal(mean([-1,1]), 0)
#test_neg_mean()

def test_std1():
	obs = std([0.0,2.0])
	exp = 1.0
	assert_equal(obs,exp)

def test_std2():
        obs = std([])
        exp = 0
        assert_equal(obs,exp)

def test_std3():
        obs = std([0.0,4.0])
        exp = 2.0
        assert_equal(obs,exp)

def test_std4():
        obs = std([1.0,3.0])
        exp = 1.0
        assert_equal(obs,exp)

def test_std5():
        obs = std([1.0,1.0,1.0])
        exp = 0.0
        assert_equal(obs,exp)
