var1=1
print(type(var1))
var1='1'
print('changement de type :',type(var1))
prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
more_than_seven = 0 
for prenom in prenoms:
    if len(prenom) > 7:
        more_than_seven += 1
        print("Prenom supérieur à 7 : " + prenom)
    else:
        print("Prenom inférieur ou égal à 7 : " + prenom)
print("Nombre de prénoms supérieurs à 7 : " + str(more_than_seven))
import unittest

"""
Count names with more than seven letters
"""
def names(prenoms):
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print("Prenom supérieur à 7 : " + prenom)
        else:
            print("Prenom inférieur ou égal à 7 : " + prenom)
    return more_than_seven

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = names(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()
#à optimiser pour la prochaine fois :
    """
Count names with more than seven letters
"""
def names(prenoms: list):
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print("Prenom supérieur à 7 : " + prenom)
        else:
            print("Prenom inférieur ou égal à 7 : " + prenom)
    return more_than_seven

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
print("Nombre de prénoms supérieurs à 7 : " + str(names(prenoms=prenoms)))