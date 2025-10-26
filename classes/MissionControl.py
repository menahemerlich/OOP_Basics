
class MissionControl:

    @staticmethod
    def analyze_report(r):
        if r.urgency_level >= 4:
            print("Immediate response closely.")
        elif r.urgency_level == 3:
            print("High priority. Monitor closely.")
        else:
            print("Routine analysis")

