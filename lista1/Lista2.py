import pulp


# todos os exercicios da lista 1 se encontra aqui
class Lista2:
    @classmethod
    def _init__(cls):
        exercicio1()
        exercicio2()
        exercicio3()
        exercicio4()
        exercicio5()
        exercicio7()
        exercicio8()
        exercicio9()


def exercicio1():
    model = pulp.LpProblem('Exemplo', sense=pulp.LpMaximize)
    x = pulp.LpVariable.dicts(indices=[1, 2], cat=pulp.LpContinuous, lowBound=0, name='exercicio1')
    model.addConstraint(-1 * x[1] + 2 * x[2] <= 4, name='restricao-1')
    model.addConstraint(1 * x[1] + 2 * x[2] <= 6, name='restricao-2')
    model.addConstraint(1 * x[1] + 3 * x[2] <= 9, name='restricao-3')

    model.setObjective(2 * x[1] + 3 * x[2])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultado:={x_sol}')


def exercicio2():
    model = pulp.LpProblem('Exemplo', sense=pulp.LpMaximize)
    x = pulp.LpVariable.dicts(indices=[1, 2], cat=pulp.LpContinuous, lowBound=0, name='exercicio2')
    model.addConstraint(2 * x[1] + 1 * x[2] <= 2, name='restricao-1')
    model.addConstraint(1 * x[1] + 3 * x[2] <= 3, name='restricao-2')
    model.setObjective(0.3 * x[1] + 0.5 * x[2])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultado:={x_sol}')


def exercicio3():
    model = pulp.LpProblem('Exemplo', sense=pulp.LpMaximize)
    x = pulp.LpVariable.dicts(indices=[1, 2], cat=pulp.LpContinuous, lowBound=0, name='exercicio3')
    model.addConstraint(1 * x[1] + 3 * x[2] <= 9, name='restricao-1')
    model.addConstraint(-1 * x[1] + 1 * x[2] >= 4, name='restricao-2')
    model.addConstraint(1 * x[1] + 1 * x[2] <= 6, name='restricao-3')

    model.setObjective(2 * x[1] + 3 * x[2])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultado:={x_sol}')


def exercicio4():
    model = pulp.LpProblem('Exemplo', sense=pulp.LpMinimize)
    x = pulp.LpVariable.dicts(indices=[1, 2], cat=pulp.LpContinuous, lowBound=0, name='exercicio4')
    model.addConstraint(1 * x[1] + 1 * x[2] <= 20, name='restricao-1')
    model.addConstraint(1 * x[1] + 1 * x[2] >= 10, name='restricao-2')
    model.addConstraint(5 * x[1] + 6 * x[2] <= 54, name='restricao-3')

    model.setObjective(10 * x[1] + 12 * x[2])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultado:={x_sol}')


def exercicio5():
    model = pulp.LpProblem('Exemplo', sense=pulp.LpMinimize)
    x = pulp.LpVariable.dicts(indices=[1, 2], cat=pulp.LpContinuous, lowBound=0, name='exercicio5')
    model.addConstraint(-1 * x[1] + 1 * x[2] <= 2, name='restricao-1')
    model.addConstraint(1 * x[1] <= 5, name='restricao-2')
    model.addConstraint(1 * x[2] <= 6, name='restricao-3')
    model.addConstraint(3 * x[1] + 5 * x[2] >= 15, name='restricao-4')
    model.addConstraint(5 * x[1] + 4 * x[2] >= 20, name='restricao-5')

    model.setObjective(7 * x[1] + 9 * x[2])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultado:={x_sol}')


def exercicio7():
    model = pulp.LpProblem('Exemplo', sense=pulp.LpMaximize)
    x = pulp.LpVariable.dicts(indices=[1, 2], cat=pulp.LpContinuous, lowBound=0, name='exercicio6')
    model.addConstraint(2 * x[1] + 4 * x[2] <= 100, name='restricao-1')
    model.addConstraint(3 * x[1] + 2 * x[2] <= 90, name='restricao-2')
    model.addConstraint(5 * x[1] + 3 * x[2] <= 120, name='restricao-3')

    model.setObjective(120 * x[1] + 150 * x[2])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultado:={x_sol}')


def exercicio8():
    model = pulp.LpProblem('Exemplo', sense=pulp.LpMaximize)
    x = pulp.LpVariable.dicts(indices=[1, 2, 3], cat=pulp.LpContinuous, lowBound=0, name='exercicio7')
    model.addConstraint(1 * x[1] + 1 * x[2] + 1 * x[3] <= 100, name='restricao-1')
    model.addConstraint(100 * x[2] + 200 * x[3] <= 14000, name='restricao-2')
    model.addConstraint(100000 * x[1] + 200000 * x[2] <= 12750000, name='restricao-3')

    model.setObjective(300 * x[1] + 400 * x[2] + 500 * x[3])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultado:={x_sol}')


def exercicio9():
    model = pulp.LpProblem('Exemplo', sense=pulp.LpMinimize)
    x = pulp.LpVariable.dicts(indices=[1, 2, 3], cat=pulp.LpContinuous, lowBound=0, name='exercicio7')
    model.addConstraint(1 * x[1] + 0 * x[2] + 0 * x[3] >= 3, name='restricao-1')
    model.addConstraint(3 * x[1] + 4 * x[2] >= 30, name='restricao-2')
    model.addConstraint(3 * x[1] + 10 * x[3] >= 30, name='restricao-3')
    model.addConstraint(1 * x[1] + 1 * x[2] + 1 * x[3] <= 10, name='restricao-4')

    model.setObjective(1000 * x[1] + 1000 * x[2] + 1000 * x[3])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultado:={x_sol}')


Lista2._init__()
