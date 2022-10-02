import pulp


# todos os exercicios dexercicio1():
    model = pulp.LpProblem('Exemplo', sense=pulp.LpMaximize)
    x = pulp.LpVariable.dicts(indices=[1, 2], cat=pulp.LpContinuous, lowBound=0, name='exercicio1')
    model.addConstraint(10 * x[1] + 12 * x[2] <= 60, name='restricao-1')
    model.addConstraint(2 * x[1] + 1 * x[2] <= 6, name='restricao-2')
    model.setObjective(5 * x[1] + 2 * x[2])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultdef exercicio2():
    model = pulp.LpProblem('Exemplo', sense=pulp.LpMaximize)
    x = pulp.LpVariable.dicts(indices=[1, 2], cat=pulp.LpContinuous, lowBound=0, name='exercicio2')
    model.addConstraint(2 * x[1] + 3 * x[2] <= 120, name='restricao-1')
    model.addConstraint(1 * x[1] + 0 * x[2] <= 40, name='restricao-2')
    model.addConstraint(0 * x[1] + 1 * x[2] <= 30, name='restricao-3')
    model.setObjective(100 * x[1] + 150 * x[2])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultado:={x_sol}')


def exercicio3():
    model = pulp.LpProblem('Exemplo', sense=pulp.LpMaximize)
    x = pulp.LpVariable.dicts(indices=[1, 2], cat=pulp.LpContinuous, lowBound=0, name='exercicio3')
    model.addConstraint(1 * x[1] + 1 * x[2] <= 600, name='restricao-1')
    model.addConstraint(1 * x[1] + 0 * x[2] >= 100, name='restricao-2')
    model.addConstraint(0 * x[1] + 1 * x[2] <=
    model.setObjective(4 * x[1] + 3 * x[2])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultado:={x_sol}')


def exercicio6():
    model = pulp.LpProblem('Exemplo', sense=pulp.LpMaximize)
    x = pulp.LpVariable.dicts(indices=[1, 2], cat=pulp.LpContinuous, lowBound=0, name='exercicio6')
    model.addConstraint(2 * x[1] + 4 * x[2] <= 100, name='restricao-1')
    model.addConstraint(3 * x[1] + 2 * x[2] <= 90, name='restricao-2')
    model.addConstraint(5 * x[1] + 3 * x[2] <= 120, name='restricao-3')

    model.setObjectiv
    x = pulp.LpVariable.dicts(indices=[1, 2, 3], cat=pulp.LpContinuous, lowBound=0, name='exercicio7')
    model.addConstraint(1 * x[1] + 0 * x[2] + 0 * x[3] >= 3, name='restricao-1')
    model.addConstraint(3 * x[1] + 4 * x[2] >= 30, name='restricao-2')
    model.addConstraint(3 * x[1] + 10 * x[3] >= 30, name='restricao-3')
    model.addConstraint(1 * x[1] + 1 * x[2] + 1 * x[3] <= 10, name='restricao-4')

    model.setObjective(1000 * x[1] + 1000 * x[2] + 1000 * x[3])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultado:={x_sol}')


Lista1._init_