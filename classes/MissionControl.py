
class MissionControl:

    @staticmethod
    def analyze_report(r):
        if r.urgency_level >= 4:
            return "Immediate response closely."
        elif r.urgency_level == 3:
            return "High priority. Monitor closely."
        else:
            return "Routine analysis"

