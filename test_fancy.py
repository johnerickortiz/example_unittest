from nose2.tools import params

@params("Sir Bedere","Miss Islington","Duck")
def test_is_knigth(value):
    assert value.startswith('Sir')

if __name__ == '__main__':
    import nose2
    nose2.main()