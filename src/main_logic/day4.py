class Day4(object):

    def part1(self, data):
        counter = 0
        for lines_data in data.splitlines():
            lines_data = lines_data.strip()
            first_range_start, first_range_end, second_range_start, second_range_end = \
                self.__get_first_second_list_of_elements(lines_data)
            if (first_range_start >= second_range_start and first_range_end <= second_range_end) or \
                    (second_range_start >= first_range_start and second_range_end <= first_range_end):
                counter += 1
        return counter

    def part2(self, data):  # Still a brute force time complexity solution
        counter = 0
        for lines_data in data.splitlines():
            lines_data = lines_data.strip()
            first_range_start, first_range_end, second_range_start, second_range_end = \
                self.__get_first_second_list_of_elements(lines_data)
            first_range = list(range(first_range_start, first_range_end + 1))
            second_range = list(range(second_range_start, second_range_end + 1))
            if set(first_range).intersection(second_range):
                counter += 1
        return counter

    def __get_first_second_list_of_elements(self, data):
        first_elf, second_elf = data.split(",")[0], data.split(",")[1]
        first_range_start, first_range_end = map(int, first_elf.split("-"))
        second_range_start, second_range_end = map(int, second_elf.split("-"))
        return first_range_start, first_range_end, second_range_start, second_range_end
