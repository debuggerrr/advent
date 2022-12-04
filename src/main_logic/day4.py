class Day4(object):

    def part1(self, data):
        counter = 0
        for lines_data in data.splitlines():
            lines_data = lines_data.strip()
            first_range, second_range = self.__get_first_second_list_of_elements(lines_data)
            check_first_side_if_returns_true = all(item in first_range for item in second_range)
            check_second_side_if_returns_true = all(item in second_range for item in first_range)
            if check_first_side_if_returns_true or check_second_side_if_returns_true:
                counter += 1
        return counter

    def part2(self, data):
        counter = 0
        for lines_data in data.splitlines():
            lines_data = lines_data.strip()
            first_range, second_range = self.__get_first_second_list_of_elements(lines_data)
            check_first_side_if_returns_true = any(item in first_range for item in second_range)
            check_second_side_if_returns_true = any(item in second_range for item in first_range)
            if check_first_side_if_returns_true or check_second_side_if_returns_true:
                counter += 1
        return counter

    def __get_first_second_list_of_elements(self, data):
        first_elf, second_elf = data.split(",")[0], data.split(",")[1]
        first_range_start, first_range_end = map(int, first_elf.split("-"))
        second_range_start, second_range_end = map(int, second_elf.split("-"))
        first_range = list(range(first_range_start, first_range_end + 1))
        second_range = list(range(second_range_start, second_range_end + 1))
        return first_range, second_range
