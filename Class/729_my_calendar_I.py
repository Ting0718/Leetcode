class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        copy = list(self.calendar)
        copy.append([start, end])
        copy.sort(key=lambda x: x[0])

        for b in range(1, len(copy)):
            b1 = copy[b - 1]
            b2 = copy[b]
            if b2[0] < b1[1]:
                return False

        self.calendar.append([start, end])
        return True
