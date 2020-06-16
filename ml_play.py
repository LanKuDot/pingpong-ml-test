class MLPlay:
    def __init__(self, side):
        self.ball_served = False
        self.side = side

    def update(self, scene_info):
        """
        Decide the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            return "SERVE_TO_LEFT"
        else:
            return "MOVE_LEFT"

    def reset(self):
        self.ball_served = False
