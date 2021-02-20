from dataclasses import dataclass

@dataclass
class Questionnaire:
    answers_count: list
    channel_id: str
    result_msg_id: str

    def __init__(self, answers_count: list, channel_id: str, result_msg_id: str):
        self.answers_count = answers_count
        self.channel_id = channel_id
        self.result_msg_id = result_msg_id