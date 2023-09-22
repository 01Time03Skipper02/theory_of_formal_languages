a = "fg"


class function:
    def __init__(self, l_k, r_k):
        self.first_ord = l_k
        self.second_ord = r_k


# return array like [["a1f", "a2f"], ["b1f", "b2f"]]
def get_compositions_coefficients(func):
    res = []
    for i in range(len(func)):
        l_k = ["a1" + func[i], "a2" + func[i]]
        r_k = ["b1" + func[i], "b2" + func[i]]
        res.append(function(l_k, r_k))

    return res


def mult_ords(ord1, ord2):
    res_ord = [*ord1]
    if len(ord1) >= 2 and len(ord2) == 2:
        res_ord.insert(0, ord2[0])
        res_ord[1] = res_ord[1] + " * " + ord2[1]
    return res_ord


def sum_ords(ord1, ord2):
    if len(ord1) < len(ord2):
        return ord2
    diff = len(ord1) - len(ord2)
    res_ord = ord1
    res_ord[diff] = res_ord[diff] + " + " + ord2[0]
    res_ord = res_ord[:diff + 1]
    ord2.pop(0)
    for i in range(len(ord2)):
        res_ord.append(ord2[i])
    return res_ord


def get_composition(func1, func2):
    l_k = mult_ords(func1.first_ord, func2.first_ord)
    r_k = sum_ords(mult_ords(func1.first_ord, func2.second_ord), func1.second_ord)
    return function(l_k, r_k)


def get_great_output_ords(composition):
    res = "("
    for i in range(len(composition.first_ord)):
        if len(composition.first_ord) - i - 1 > 1:
            res += "w^" + str(len(composition.first_ord) - i - 1) + " * "
        elif len(composition.first_ord) - i - 1 == 1:
            res += "w * "
        if len(composition.first_ord[i]) > 3:
            res += "(" + composition.first_ord[i] + ") + "
        else:
            res += composition.first_ord[i] + " + "
    res = res[:-3]
    if res[-1] != ")":
        res += ") * x + ("
    else:
        res += " * x + ("

    for i in range(len(composition.second_ord)):
        if len(composition.second_ord) - i - 1 > 1:
            res += "w^" + str(len(composition.second_ord) - i - 1) + " * "
        elif len(composition.second_ord) - i - 1 == 1:
            res += "w * "
        if len(composition.second_ord[i]) > 3:
            res += "(" + composition.second_ord[i] + ") + "
        else:
            res += composition.second_ord[i] + " + "

    res = res[:-3]
    if res[-1] != ")":
        res += ")"
    return res


res = get_compositions_coefficients(a)
composition = get_composition(res[0], res[1])
for i in range(2, len(res)):
    composition = get_composition(composition, res[i])
t = get_great_output_ords(composition)

#В процессе написания осознал, что зря эту функцию писал  :-(
def get_polish_func(great_string):
    l_s, r_s = great_string.split(" * x + ")
    l_s, r_s = l_s[1:-1], r_s[1:-1]

    def get_polish_ord(ordinal):
        res = ""
        flag = True
        flag_w = True
        for i in range(len(ordinal)):
            if ordinal[i] == "(" and not flag:
                flag = True
                continue
            if ordinal[i] == "(" and ordinal[i + 10] == ")":
                ordinal = ordinal.replace(ordinal[i:i + 11],
                                          "(* " + ordinal[i + 1:i + 4] + " " + ordinal[i + 7:i + 10] + ")")
            elif ordinal[i] == "(" and ordinal[i + 16] == ")":
                ordinal = ordinal.replace(ordinal[i:i + 17], "(+ (* " + ordinal[i + 1:i + 4] + " " + ordinal[
                                                                                                     i + 7:i + 10] + ") " + ordinal[
                                                                                                                            i + 13:i + 16] + ")")
                flag = False

        for i in range(len(ordinal)):
            if ordinal[i] == "w" and not flag_w:
                flag_w = True
                continue
            if ordinal[i] == "w" and ordinal[i + 1] == "^":
                if ordinal[i + 10] == "+":
                    ordinal = ordinal.replace(ordinal[i:i+9], "(* " + ordinal[i: i + 3] + " " + ordinal[i + 6: i + 9] + ")")
                elif ordinal[i + 18] == "+":
                    ordinal = ordinal.replace(ordinal[i:i + 17], "(* " + ordinal[i: i + 3] + " " + ordinal[i + 6: i + 17] + ")")
                elif ordinal[i + 26] == "+":
                    ordinal = ordinal.replace(ordinal[i:i + 25], "(* " + ordinal[i: i + 3] + " " + ordinal[i + 6: i + 25] + ")")
                flag_w = False
            elif ordinal[i] == "w":
                if ordinal[i + 8] == "+":
                    ordinal = ordinal.replace(ordinal[i:i+7], "(* " + ordinal[i: i + 1] + " " + ordinal[i + 4: i + 7] + ") ")
                elif ordinal[i + 16] == "+":
                    ordinal = ordinal.replace(ordinal[i:i + 15], "(* " + ordinal[i: i + 1] + " " + ordinal[i + 4: i + 15] + ") ")
                elif ordinal[i + 24] == "+":
                    ordinal = ordinal.replace(ordinal[i:i + 23], "(* " + ordinal[i: i + 1] + " " + ordinal[i + 4: i + 23] + ") ")
                flag_w = False
        cnt_br = 0
        pluses_indexes = []
        for i in range(len(ordinal)):
            if ordinal[i] == "(":
                cnt_br += 1
            if ordinal[i] == ")":
                cnt_br -= 1
            if ordinal[i] == "+" and cnt_br == 0:
                pluses_indexes.append(i)
        pluses_indexes.reverse()
        for i in range(len(pluses_indexes)):
            res += "(+ "
        res += ordinal[pluses_indexes[1] + 2:pluses_indexes[0] - 1] + ordinal[-3:] + ") "
        for i in range(1, len(pluses_indexes)):
            if i != len(pluses_indexes) - 1:
                res += ordinal[pluses_indexes[i + 1] + 2:pluses_indexes[i] - 1] + ") "
            else: res += ordinal[:pluses_indexes[i] - 1] + ")"

        return res

    polish_l_s = get_polish_ord(l_s)
    polish_r_s = get_polish_ord(r_s)
    polish_l_s = "(* " + polish_l_s + " x)"
    result = "(+ " + polish_l_s + " " + polish_r_s + ")"
    return result

def get_polish_coefficients(coeff_array):
    def get_polish_coefficient(coeff):
        if len(coeff) == 3:
            return coeff
        elif len(coeff) == 9:
            return "(* " + coeff[:3] + " " + coeff[-3:] + ")"
        elif len(coeff) == 15:
            return "(+ (* " + coeff[:3] + " " + coeff[6:9] + ") " + coeff[-3:] + ")"
    for i in range(len(coeff_array)):
        coeff_array[i] = get_polish_coefficient(coeff_array[i])
    return coeff_array


def get_polish_composition(composition):
    return function(get_polish_coefficients(composition.first_ord), get_polish_coefficients(composition.second_ord))

polish_res = get_polish_composition(composition)
print(polish_res.first_ord, polish_res.second_ord)

