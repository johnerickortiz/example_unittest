from nose2.tools import params
def conteo(listaNotas):
    sum = 0
    for nota in listaNotas:
        if nota>=3.0:
            sum+=1
    return sum

@params([])
def test_conteo(lNotas):
    assert conteo(lNotas)==3

if __name__=="__main__":
    import nose2
    nose2.main()