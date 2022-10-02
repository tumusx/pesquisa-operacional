# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import null as null
import pulp

model = pulp.LpProblem('Exemplo', sense=pulp.LpMaximize)
x = pulp.LpVariable.dicts(indices=[1, 2], cat=pulp.LpContinuous, lowBound=0, name='x')
model.addConstraint(2*x[1] + 4*x[2] == 100, name='restricao-1')
model.setObjective(3 * x[1] + 5 * x[2])

model.solve()
x_sol = {i: x[i].value() for i in {1, 2}}
print(f'resultado:={x_sol}')
