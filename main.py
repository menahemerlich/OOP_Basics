from classes.Agent import Agent
from classes.Mission import Mission
from classes.Report import Report
from classes.MissionControl import MissionControl
from classes.IntelTools import IntelTools

agent1 = Agent("kodkod", 4)
mission1 = Mission("tracking", "Tel Aviv")
mission1.assigned_agent = agent1
report1 = Report("Report", 4, agent1)
analyze1 = MissionControl()
message = analyze1.analyze_report(report1)


agent1.report()
print()
mission1.brief()
print()
report1.printed()
print()
analyze1.analyze_report(report1)
IntelTools.log_transmission(agent1.code_name, message)