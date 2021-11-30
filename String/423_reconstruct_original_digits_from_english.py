from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        out = {}

        # zero -> z
        # one -> n - 7 - 9
        # two -> w
        # three -> h - 8
        # four -> u
        # five -> f - 4
        # six -> x
        # seven -> v - 5
        # eight -> g
        # nine -> i - 5 - 6 - 8

        out["0"] = count["z"]
        out["2"] = count["w"]
        out["4"] = count["u"]
        out["6"] = count["x"]
        out["8"] = count["g"]

        out["3"] = count["h"] - out["8"]
        out["5"] = count["f"] - out["4"]
        out["7"] = count["v"] - out["5"]
        out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
        out["1"] = count["n"] - out["7"] - 2 * out["9"]

        output = [key * out[key] for key in sorted(out.keys())]
        return "".join(output)
