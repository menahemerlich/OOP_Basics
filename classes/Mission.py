class Mission:
    def __init__(self, mission_name: str, target_location: str):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = None

    def assigned_agent(self, assigned_agent):
        self.assigned_agent = assigned_agent

    def brief(self):
        print(f"Mission: {self.mission_name}\n"
              f"Target: {self.target_location}\n"
              f"Agent {self.assigned_agent.code_name}")




