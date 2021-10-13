class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
                 "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        s = ""
        date = date.split()
        s = s + date[2] + "-" + month[date[1]] + "-"
        if int(date[0][:-2]) < 10:
            date[0] = "0" + date[0][:-2]
        else:
            date[0] = date[0][:-2]

        s += date[0]

        return s