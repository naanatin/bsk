from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self._frames = []
    
    def add_frame(self, frame: Frame) -> None:
        if len(self._frames) == 10:
            raise BowlingError
        self._frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        return self._frames[i]

    def calculate_score(self) -> int:
        score = 0
        for i, frame in enumerate(self._frames, 0):
            if frame.is_spare():
                if i < len(self._frames)-1:
                    score += self._frames[i+1].get_first_throw()
            if frame.is_strike():
                score += self._frames[i+1].score()
            score += frame.score()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        self._frames[len(self._frames)-1].set_bonus(bonus_throw)

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
