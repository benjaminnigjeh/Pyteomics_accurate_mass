import pyteomics
import pandas
from pyteomics import mass
mass.std_aa_comp['k'] = mass.Composition(
    {'C': 10, 'H': 16, 'N': 2, 'O': 2})
mass.std_aa_comp['c'] = mass.Composition(
    {'C': 2, 'H': 3, 'N': 1, 'O': 1})
mass.std_aa_comp['m'] = mass.Composition(
    {'O': 1})
DF = pandas.read_csv('test.CSV')

t = len(DF)

for x in range(0, t):
    a = DF.iloc[x][1]
    a = int(float(a))
    m_z = mass.calculate_mass(sequence=DF.iloc[x][0], charge=a)
    print(m_z)

