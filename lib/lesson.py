class Lesson:
    _id: str
    teacher: str
    channel: str
    guild: str
    started: int
    msg_id: str
    time: any
    practice: bool

    def create(self, teacher: str, channel: str, guild: str, msg_id: str, time: any = None, practice: bool = Flse):
        pass