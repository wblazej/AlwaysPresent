from dataclasses import dataclass

@dataclass
class Questionnaire:
    question: str
    answers: list
    answers_count: list
    channel_id: str
    result_msg_id: str

    def __init__(self, question: str, answers: list, answers_count: list, channel_id: str, result_msg_id: str):
        self.question = question
        self.answers = answers
        self.answers_count = answers_count
        self.channel_id = channel_id
        self.result_msg_id = result_msg_id