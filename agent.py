from utils.ssl.Navigation import Navigation
from utils.ssl.base_agent import BaseAgent
from agent_decision import shortest_path

class ExampleAgent(BaseAgent):
    def __init__(self, id=0, yellow=False):
        super().__init__(id, yellow)

    def decision(self):
        if len(self.targets) == 0:
            return

        # preciso ter noção de quem são meus oponentes e meus teammates para poder evitá-los quando eu navegar até o ponto
        # tenho acesso a eles por self.opponents ae self.teammates
        # cada um desses opponents ou teammates são robôs, ou seja, possuem posições X e Y
        # assim posso construir um caminho ideal até o target que seja mais curto e tenha menos robôs.
        # como Navigation.goToPoint() é um método estático, não posso alterá-lo
        # sendo assim eu penso que eu tenho que fazer o robô navegar até pontos "parciais" do caminho até o target real, mas já conhecendo o caminho ideal inteiro 
        # os pontos parciais vão ser definidos de tal forma: se houver obstáculos no caminho, o ponto parcial será um pouco antes de cada obstáculo, após isso ele deve DESVIAR do obstáculo e continuar até o target/próximo ponto parcial.
        # de um modo, isso já nos dá o caminho ideal pois sabemos que a menor distância entre dois pontos é uma reta, que é o que goToPoint() tenta fazer. Nos resta agora fazer com que o agente desvie dos obstáculos do seu caminho. (PARA O MODO EASY)
        obstacles = {**self.opponents, **self.teammates}
        partial_points = shortest_path(obstacles, self.robot.x, self.robot.y, self.targets[0].x, self.targets[0].y)
        partial_points.append(self.targets[0])
        
        # PROBLEMA: Não ainda consigo fazer com que o agente vá até um ponto e DEPOIS vá até outro
        
        target_velocity, target_angle_velocity = Navigation.goToPoint(self.robot, partial_points[0])
        partial_points = partial_points[1:]
        self.set_vel(target_velocity)
        self.set_angle_vel(target_angle_velocity)
            
        
        return

        

    def post_decision(self):
        # o processo de pós decision vai ser relevante quando possuirmos mais de um target e, portanto, mais de um agente a segui-lo.
        # após o agente chegar ao seu target, ele deverá decidir se fica parado ou se há outro target disponível para ele
        pass
