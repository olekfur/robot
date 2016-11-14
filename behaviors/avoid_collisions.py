from behaviors.behavior import Behavior
from sensobs.ultrasonic import Ultrasonic_sensob
from sensobs.irproximity import IRProximity_sensob
from sensobs.camera_color import Camera_color_sensob


class Avoid_collisions_behavior(Behavior):
    def __init__(self, distance_sensob = Ultrasonic_sensob(), ir_sensob=IRProximity_sensob(), camera_sensob = Camera_color_sensob()):
        super(Avoid_collisions_behavior, self).__init__()
        self.sensobs = [distance_sensob, ir_sensob, camera_sensob]

        self.priority = 1

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        dist = self.sensobs[0].value

        ir = self.sensobs[1].value

        color_percentage = self.sensobs[2][0].get_value()
        if color_percentage['red'] >= 10:
            self.motor_recommendations = [(1,1), 2]
            self.match_degree = 1

        if ir[0]:
            self.motor_recommendations = [(1, -1)]
            self.match_degree = 1
        elif ir[1]:
            self.motor_recommendations = [(-1, 1)]
            self.match_degree = 1
        elif dist > 15:
            self.motor_recommendations = [(0.5, 0.5)]
            self.match_degree = 0.1
        else:
            # turn right
            self.motor_recommendations = [(1, -1)]
            self.match_degree = 1