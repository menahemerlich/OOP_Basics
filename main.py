from classes.Agent import Agent
from classes.Mission import Mission
from classes.Report import Report
from classes.MissionControl import MissionControl

agent1 = Agent("kodkod", 4)
mission1 = Mission("tracking", "Tel Aviv")
mission1.assigned_agent = agent1
report1 = Report("Report", 4, agent1)
analyze1 = MissionControl()


agent1.report()
mission1.brief()
report1.printed()
analyze1.analyze_report(report1)