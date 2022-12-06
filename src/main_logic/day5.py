import re


class Day5(object):
    def part1(self, data):
        first = ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P']
        second = ['M', 'Q', 'H']
        third = ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L']
        fourth = ['Z', 'T', 'F', 'Q', 'M', 'W', 'G']
        fifth = ['M', 'T', 'H', 'P']
        sixth = ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T']
        seventh = ['M', 'N', 'B', 'F', 'V', 'R']
        eight = ['P', 'L', 'H', 'M', 'R', 'G', 'S']
        nine = ['P', 'B', 'D', 'C', 'N']
        stack_numbers = {1: first, 2: second, 3: third, 4: fourth, 5: fifth, 6: sixth, 7: seventh, 8: eight, 9: nine}
        for i in data.splitlines():
            i = i.strip()
            temp = re.findall(r'\d+', i)
            res = list(map(int, temp))
            n = res[0]
            move_from = stack_numbers[res[1]]
            move_to = stack_numbers[res[2]]
            for i in range(n):
                a = move_from.pop()
                stack_numbers[res[1]] = move_from
                move_to.append(a)
                stack_numbers[res[2]] = move_to
        seq = first.pop() + second.pop() + third.pop() + fourth.pop() + fifth.pop() + sixth.pop() + seventh.pop() + eight.pop() + nine.pop()
        return seq
