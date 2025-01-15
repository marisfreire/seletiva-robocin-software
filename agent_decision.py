import math
# tenho um agente que se move e um target designado a ele
# tenho a posição do target e tenho a posição do robô
# também tenho a posição dos seus obstáculos
# vou desviar dos obstaculos cujos (X,Y) interceptam o caminho do agente até o target


def intersection(coef_ang, coef_linear, op):
    crossed = False
    # Checar se a reta intercepta alguma parte do círculo do agente
    return crossed

def shortest_path(obstacles, pos_agent_x, pos_agent_y, pos_target_x, pos_target_y):
    partial_points = []

    # Temos dois pontos conhecidos, então podemos usar a equação da reta
    # Estou usando uma reta pois a navegação é com base na distância euclidiana entre os pontos
    # PROBLEMA: preciso levar em consideração o fato de que os obstáculos tem um certo raio, ou seja, podem haver partes suas que sejam interceptadas pela reta e não necessariamente seu centro.
    coef_ang = int((pos_agent_y - pos_target_y)/(pos_agent_x - pos_target_x))
    coef_linear = int(pos_agent_y - (coef_ang * pos_agent_x))


    for op in obstacles:
        if (intersection(coef_ang, coef_linear, op)):
            partial_points.append(op)

    return partial_points