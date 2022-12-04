import re


class Day4(object):

    def part1(self, data):
        pattern = r"(\d+)\-(\d+)"
        counter = 0
        for lines_data in data.splitlines():
            first_range = ""
            second_range = ""
            lines_data = lines_data.strip()
            first_elf, second_elf = lines_data.split(",")[0], lines_data.split(",")[1]
            first_match, second_match = re.findall(pattern, first_elf), re.findall(pattern, second_elf)
            for tuple in first_match:
                low = int(tuple[0])
                high = int(tuple[1])
                first_range = list(range(low, high + 1))
            for tuple in second_match:
                low = int(tuple[0])
                high = int(tuple[1])
                second_range = list(range(low, high + 1))
            check_first_side = all(item in first_range for item in second_range)
            check_second_side = all(item in second_range for item in first_range)
            if check_first_side or check_second_side:
                counter += 1
        return counter


    def part2(self, data):
        pattern = r"(\d+)\-(\d+)"
        counter = 0
        for lines_data in data.splitlines():
            first_range = ""
            second_range = ""
            lines_data = lines_data.strip()
            first_elf, second_elf = lines_data.split(",")[0], lines_data.split(",")[1]
            first_match, second_match = re.findall(pattern, first_elf), re.findall(pattern, second_elf)
            for tuple in first_match:
                low = int(tuple[0])
                high = int(tuple[1])
                first_range = list(range(low, high + 1))
            for tuple in second_match:
                low = int(tuple[0])
                high = int(tuple[1])
                second_range = list(range(low, high + 1))
            check_first_side = any(item in first_range for item in second_range)
            check_second_side = any(item in second_range for item in first_range)
            if check_first_side or check_second_side:
                counter += 1
        return counter
