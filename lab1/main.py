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


res = get_compositions_coefficients(a)
composition = get_composition(res[0], res[1])
for i in range(2, len(res)):
    composition = get_composition(composition, res[i])
print(composition.first_ord, composition.second_ord)

