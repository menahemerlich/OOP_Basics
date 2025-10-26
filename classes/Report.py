class Report:
    def __init__(self, summary: str, urgency_level: int, submitted_by):
        self.summary = summary
        self.urgency_level = urgency_level
        self.submitted_by = submitted_by

    def printed(self):
        print(f"summary: {self.summary}\n"
              f"urgency_level: {self.urgency_level}\n"
              f"submitted_by: {self.submitted_by.code_name}")
