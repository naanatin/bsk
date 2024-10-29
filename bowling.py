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
        frames = self._frames
        for i, frame in enumerate(frames, 0):
            if frame.is_spare():
                score += frames[i+1].get_first_throw()
            score += frame.get_first_throw() + frame.get_second_throw()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
