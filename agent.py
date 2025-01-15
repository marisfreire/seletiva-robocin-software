from utils.ssl.Navigation import Navigation
from utils.ssl.base_agent import BaseAgent

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
        target_velocity, target_angle_velocity = Navigation.goToPoint(self.robot, self.targets[0])
        self.set_vel(target_velocity)
        self.set_angle_vel(target_angle_velocity)

        return

    def post_decision(self):
        pass
