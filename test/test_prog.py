


def test_lg_1():
    from prog.prog import valeur_totale
    assert valeur_totale('I') == 1
    assert valeur_totale('V') == 5
    assert valeur_totale('X') == 10
    assert valeur_totale('L') == 50
    assert valeur_totale('C') == 100
    assert valeur_totale('D') == 500
    assert valeur_totale('M') == 1000

def test_carac_identiques():
    from prog.prog import valeur_totale
    assert valeur_totale("II") == 2
    assert valeur_totale("VV") == 10
    assert valeur_totale("XX") == 20
    assert valeur_totale("LL") == 100
    assert valeur_totale("CC") == 200
    assert valeur_totale("DD") == 1000
    assert valeur_totale("MM") == 2000

def test_carac_soustraction():
    from prog.prog import valeur_totale
    assert valeur_totale("IV") == 4