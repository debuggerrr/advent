class ElfCalories(object):
    def max_calories(self, data):
        max_num = 0
        sum_val = 0
        for line in data.split("\n"):
            line = line.strip()
            if line and line.isdigit():
                sum_val += int(line)
            else:
                sum_val = 0
            max_num = max(max_num, sum_val)
        return max_num

    def top_three_sum_of_calories(self, data):
        sums_list = []
        sum_val = 0
        new_sum = 0
        for line in data.split("\n"):
            line = line.strip()
            if line and line.isdigit():
                sum_val += int(line)
            else:
                sums_list.append(sum_val)
                sum_val = 0
        sorted_list = sorted(sums_list, reverse=True)
        for i in range(0, 3):
            new_sum += sorted_list[i]
        return new_sum
