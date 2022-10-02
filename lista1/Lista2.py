import pulp


# todos os exercicios da lista 2 se encontra aqui3 * x[2] <= 10, name='restricao-3')
    model.setObjective(1900 * x[1    model.addConstraint(0 * x[1] + 1 * x[2] <= 30, name='restricao-3')
] + 2100 * x[2])

    model.solve()
    x_sol = {i: x[i].value() for i in {1, 2}}
    print(f'resultado:={x_sol}')


Lista2._init__()
