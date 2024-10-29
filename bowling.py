from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.frames = []
    
    def add_frame(self, frame: Frame) -> None:
        if len(self.frames) == 10:
            raise BowlingError
        self.frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        return self.frames[i]

    def calculate_score(self) -> int:
        score = 0
        for i, frame in enumerate(self.frames, 0):
            if frame.is_spare():
                if i < len(self.frames)-1:
                    score += self.frames[i + 1].get_first_throw()
            if frame.is_strike():
                score += self.frames[i + 1].score()
            score += frame.score()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        self.frames[len(self.frames) - 1].set_bonus(bonus_throw)

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
