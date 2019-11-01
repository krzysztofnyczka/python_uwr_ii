import copy
from collections import deque


def read_input():
    with open("zad_input.txt") as file:
        imp = []
        rows = []
        cols = []

        for line in file:
            imp.append(line.split())

        ro = int(imp[0][0])

        for i in range(1, ro + 1):
            rows.append(list(map(int, imp[i])))

        for i in range(ro + 1, len(imp)):
            cols.append(list(map(int, imp[i])))

    return rows, cols


def image_printer(img):
    image = copy.deepcopy(img)
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j]:
                image[i][j] = '#'
            else:
                image[i][j] = '.'
    return image


def porownaj_listy(l1, l2):
    zmienionych_bitow = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            zmienionych_bitow += 1
    return zmienionych_bitow


def column(m, o):
    return [row[o] for row in m]


def multi_validator(li, lv):
    blocks_max_index = len(lv) - 1
    if li[0] == 0:
        block = -1
        one_or_zero = 0
    else:
        block = 0
        one_or_zero = 1

    current_len_of_subsequence = 1

    for i in range(1, len(li)):
        if li[i] != one_or_zero:
            # 1111110
            one_or_zero = 0
            if li[i] == 0:
                if current_len_of_subsequence != lv[block]:
                    return False
                current_len_of_subsequence = 1
            # 0000001
            if li[i] == 1:
                one_or_zero = 1
                if blocks_max_index == block:
                    return False
                block += 1
                current_len_of_subsequence = 1
        elif li[i] == 1:
            current_len_of_subsequence += 1
    if one_or_zero == 1 and lv[len(lv) - 1] != current_len_of_subsequence:
        return False
    if blocks_max_index != block:
        return False
    return True


# generates combinations of all possible rows/columns from given [list of 1 and 0] and [value list]
# for multi([0,1,1,0,1,1], [1, 3]) generates: [[0, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 1]]
def generate_combinations(row, lv):
    spaces = [1 for _ in range(len(lv) + 1)]
    spaces[0] = 0
    spaces[len(lv)] = 0
    sum_of_chars = sum(spaces) + sum(lv)
    spaces_to_generate = len(row) - sum_of_chars

    def adding_one_space(combs, s):  # list of combinations of spacing ex. [(0,1,1,0),(0,0,1,0)]
        res = []
        for j in range(len(combs)):
            copy_spaces = copy.deepcopy(combs[j])
            for i in range(len(combs[j])):
                copy_spaces[i] += 1
                res.append(copy.copy(copy_spaces))
                copy_spaces[i] -= 1

        for r in range(len(res)):
            res[r] = tuple(res[r])
        res = list(set(res))
        for r in range(len(res)):
            res[r] = list(res[r])
        if s == 1:
            return res
        else:
            s -= 1
            return adding_one_space(res, s)

    if spaces_to_generate == 0:
        combinations = [spaces]
    else:
        combinations = adding_one_space([spaces], spaces_to_generate)

    rows_generated = []
    for c in combinations:
        result = [0 for _ in range(len(row))]
        res_iter = 0
        value_iter = 1
        for i in range(len(c)):
            for k in range(c[i]):
                result[res_iter] = 0
                res_iter += 1
            if i < len(c) - 1:
                current_value = lv[value_iter - 1]
                value_iter += 1
                for val in range(current_value):
                    result[res_iter] = 1
                    res_iter += 1
        rows_generated.append(result)
    return rows_generated

# MAIN ######################################


def logic_image_solver(width, height, data_w, data_h):
    image = [[0 for _ in range(width)] for _ in range(height)]

    # find all possible combinations for all rows/columns and do it once before running a loop
    row_combinations = [generate_combinations(image[i], data_h[i]) for i in range(len(image))]
    col_combinations = [generate_combinations(column(image, i), data_w[i]) for i in range(len(image[0]))]
    checked = [[0 for _ in range(width)] for _ in range(height)]
    not_valid = deque()

    def find_solution(y, x, combs):
        row_point = combs[0][x]

        if all(row[x] == row_point for row in combs):
            checked[y][x] = row_point
            col_combinations[x] = [col for col in col_combinations[x] if col[y] == checked[y][x]]

        else:
            column_point = col_combinations[x][0][y]

            if all(column[y] == column_point for column in col_combinations[x]):
                checked[y][x] = column_point
                row_combinations[y] = [row for row in row_combinations[y] if row[x] == checked[y][x]]
            else:
                not_valid.append((y, x))

    for y in range(height):
        current_rows = row_combinations[y]
        for x in range(width):
            find_solution(y, x, current_rows)

    while len(not_valid) > 0:
        y, x = not_valid.popleft()
        current_rows = row_combinations[y]
        find_solution(y, x, current_rows)

    # image_printer(checked)
    return checked


r = read_input()
res = image_printer(logic_image_solver(len(r[1]), len(r[0]), r[1], r[0]))
for c in res:
    print(*c)
