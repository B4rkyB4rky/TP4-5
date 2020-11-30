from prog.prog import *

def test_lg_1():
    assert valeur_totale('') == 0
    assert valeur_totale('I') == 1
    assert valeur_totale('V') == 5
    assert valeur_totale('X') == 10
    assert valeur_totale('L') == 50
    assert valeur_totale('C') == 100
    assert valeur_totale('D') == 500
    assert valeur_totale('M') == 1000

def test_carac_identiques():
    assert valeur_totale("II") == 2
    assert valeur_totale("VV") == 10
    assert valeur_totale("XX") == 20
    assert valeur_totale("LL") == 100
    assert valeur_totale("CC") == 200
    assert valeur_totale("DD") == 1000
    assert valeur_totale("MM") == 2000

def test_carac_soustraction():
    assert valeur_totale("IV") == 4
    assert valeur_totale("IX") == 9
    assert valeur_totale("MIV") == 1004
    assert valeur_totale("CDLXXXVII") == 487


def test_calculatrice_soustraction():
    assert calculatrice('-', "CDLXXXVII", "MIV") == -517
    assert calculatrice('-', "MIV", "CDLXXXVII") == 517

def test_calculatrice_addition():
    assert calculatrice('+', "CDLXXXVII", "MIV") == 1491
    assert calculatrice('+', "MIV", "XIV") == 1018

def test_calculatrice_mutiplication():
    assert calculatrice('*', "", "I") == 0
    assert calculatrice('*', "V", "XIV") == 70

def test_calculatrice_division():
    assert calculatrice('/', "XIV", "XIV") == 1
    assert calculatrice('/', "", "I") == 0
    assert calculatrice('/', "V", "") == "erreur"
    assert calculatrice('/', "V", "II") == 2.5
    assert calculatrice('/', "II", "V") == 0.4
    assert calculatrice('/', "MIV", "XIV") == 71.71428571428571

