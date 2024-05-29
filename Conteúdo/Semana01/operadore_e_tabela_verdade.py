# Operadores e Tabela Verdade AND e OR


''' Conjunção [ ^ ] é equivalente a AND(E)

+-------------------------+----------------+-----------------+
| P                       | Q              | P ^ Q           |
+-------------------------+----------------+-----------------+
| True                    | True           | True            |
| True                    | False          | False           |
| False                   | True           | False           |
| False                   | False          | False           |
+-------------------------+----------------+-----------------+
'''

''' Disjunção [ v ] é equivalente a OR(OU)

+-------------------------+----------------+-----------------+
| P                       | Q              | P v Q           |
+-------------------------+----------------+-----------------+
| True                    | True           | True            |
| True                    | False          | True            |
| False                   | True           | True            |
| False                   | False          | False           |
+-------------------------+----------------+-----------------+
'''

''' Negação [ ~ ] é equivalente a NOT(NÃO)

+-------------------------+-----------------+
| P                       | ~P              |
+-------------------------+-----------------+
| True                    | False           |
| False                   | True            |
+-------------------------+-----------------+
'''

''' Implicação [ -> ] é equivalente a [ Condicional => ]

+-------------------------+----------------+-----------------+
| P                       | Q              | P -> Q          |
+-------------------------+----------------+-----------------+
| True                    | True           | True            |
| True                    | False          | False           |
| False                   | True           | True            |
| False                   | False          | True            |
+-------------------------+----------------+-----------------+
'''

''' Bicondicional [ <=> ] (se e somente se)

+-------------------------+----------------+-----------------+
| P                       | Q              | P <=> Q         |
+-------------------------+----------------+-----------------+
| True                    | True           | True            |
| True                    | False          | False           |
| False                   | True           | False           |
| False                   | False          | True            |
+-------------------------+----------------+-----------------+
'''

''' Disjunção [ Exclusiva v ] é equivalente a XOR

+-------------------------+----------------+-----------------+
| P                       | Q              | P v Q           |
+-------------------------+----------------+-----------------+
| True                    | True           | False           |
| True                    | False          | True            |
| False                   | True           | True            |
| False                   | False          | False           |
+-------------------------+----------------+-----------------+
'''

# Tautologia: é uma proposição que é sempre verdadeira, independente dos valores lógicos das proposições que a compõem.
# Contradição: é uma proposição que é sempre falsa, independente dos valores lógicos das proposições que a compõem.
''' Leis de De Morgan

Lei de De Morgan: ~(A ^ B) <=> (~A v ~B)

+-------------------------+----------------+-----------------+-----------------+------------------------+
| A                       | B              | ~(A ^ B)        | (~A v ~B)       | ~(A ^ B) <=> (~A v ~B) |
+-------------------------+----------------+-----------------+-----------------+------------------------+
| True                    | True           | False           | False           | True                   |
| True                    | False          | True            | False           | True                   |
| False                   | True           | True            | False           | True                   |
| False                   | False          | True            | True            | True                   |
+-------------------------+----------------+-----------------+-----------------+------------------------+
'''
