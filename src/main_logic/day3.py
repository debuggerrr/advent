from string import ascii_lowercase
from string import ascii_uppercase

class day3(object):
    def part1(self, data):
        priorities = self.__get_priorities()
        sum = 0
        for actual_data in data.splitlines():
            line = actual_data.strip()
            firstpart, secondpart = line[:len(line) // 2], line[len(line) // 2:]
            (ch,) = list(set(firstpart) & set(secondpart))
            sum += priorities[ch]
        return sum
    def part2(self, data):
        priorities = self.__get_priorities()
        lines = data.split('\n')
        lines = lines.strip()
        sum = 0
        for i in range(0, len(lines), 3):
            (ch,) = list(set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2]))
            sum += priorities[ch]
        return sum

    def __get_priorities(self):
        priorities = {}
        for i, j in zip(ascii_lowercase, range(1, 27)):
            priorities[i] = j
        for i, j in zip(ascii_uppercase, range(27, 53)):
            priorities[i] = j
        return priorities