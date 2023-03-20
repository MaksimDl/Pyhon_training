import random

koef_beg = -5
koef_end = 15

def return_degree_code(dig):
    result = ''
    ascii_ = {0: '\u2070',
              1: '\u00B9',
              2: '\u00B2',
              3: '\u00B3',
              4: '\u2074',
              5: '\u2075',
              6: '\u2076',
              7: '\u2077',
              8: '\u2078',
              9: '\u2079'
              }
    while (dig > 0):   #if get more than one symbol in  func
        result = ascii_[int(dig % 10)] + result
        dig = int(dig / 10)
    # return ascii_[dig]
    return result


def return_degree_num(asc):
    ascii_ = {'\u2070': 0,
              '\u00B9': 1,
              '\u00B2': 2,
              '\u00B3': 3,
              '\u2074': 4,
              '\u2075': 5,
              '\u2076': 6,
              '\u2077': 7,
              '\u2078': 8,
              '\u2079': 9
              }
    if asc not in ascii_:
        return -1

    result = 0
    # print("try: ", ascii_.get("\u20f9"))
    for i in asc:
        # print("asc[i]= ", i)
        result = result * 10 + ascii_[i]

    return result


def form_polinom(k) -> str:
    result = ""
    for i in range(k, 1, -1):
        temp_rand = random.randint(koef_beg, koef_end)  # generate koef
        if temp_rand == 1:   # no need to write coefficient if it is 1
            if len(result) != 0:
                result += '+'
            result += "x" + str(return_degree_code(i))
        elif temp_rand != 0:
            if temp_rand >= 0 and len(result) != 0:
                result += "+"
            result += str(temp_rand) + "x" + str(return_degree_code(i))
        # if rand = 0 - we just don't add this element to array

    # below for x degree = 1
    if k > 0:
        temp_rand = random.randint(koef_beg, koef_end)
        if temp_rand > 0:
            if len(result) != 0:  # in case it is beginnning of polinom
                result += "+" + str(temp_rand) + "x"
            else:
                result += str(temp_rand) + "x"
        elif temp_rand < 0:
            result += str(temp_rand) + "x"

    # below for x degree = 0 
    temp_rand = random.randint(koef_beg, koef_end)
    if temp_rand > 0:
        if len(result) != 0:  # in case it is beginnning of polinom
            result += "+" + str(temp_rand)
        else:
            result += str(temp_rand)
    elif temp_rand < 0:
        result += str(temp_rand)

    if len(result) == 0:
        result = '0'
    return result


def old_parsing_polinom(in_string):
    if in_string[0] == "-":
        sign = False
    else:
        sign = True
    kof = 0

    degree = 0
    arr_koef = []
    arr_deg = []
    flag_now_degree = False
    for i in in_string:
        # print(" parsing",i, end = "->")
        if i == '-' or i == '+':
            if flag_now_degree and degree == 0:  # condition for last x degree
                arr_deg.append(1)  # this if occurs onl if x degree is 1
            flag_now_degree = False
            if degree != 0:
                arr_deg.append(degree)
                degree = 0
            if i == "-":
                sign = False
            elif i == "+":
                sign = True
        elif i.isdigit() and return_degree_num(i) == -1:
            # print("________i = ", i)
            kof = kof * 10 + int(i)
        elif i == 'x':
            if not sign:
                if kof:
                    arr_koef.append(-kof)
                else:
                    arr_koef.append(-1)
            else:
                if kof:
                    arr_koef.append(kof)
                else:
                    arr_koef.append(1)
            flag_now_degree = True
            # print("found kof = ", kof)
            kof = 0
        # elif return_degree_num(i) != -1:
        elif flag_now_degree:
            degree = degree * 10 + return_degree_num(i)

            # add last kof with degree of x is zero
    if not sign:
        arr_koef.append(-kof)
    else:
        arr_koef.append(kof)

    print("debug: Array of coefficiens: ", arr_koef)
    print("debug: array of x degree: ", arr_deg)
    return arr_koef, arr_deg


def parsing_polinom(in_string):
    if in_string[0] == "-":
        sign = False
    else:
        sign = True
    kof = 0
    degree = 0
    arr_koef = []
    arr_deg = []

    flag_now_degree = False
    for i in in_string:
        # print(" parsing",i, end = "->")
        if (i == '-' or i == '+') and flag_now_degree:
            if degree == 0:
                degree = 1

            if len(arr_deg) == 0:  # simply append - first x-degree
                arr_deg.append(degree)
                degree = 0
                if not sign:
                    arr_koef.append(-kof)
                else:
                    arr_koef.append(kof)
                degree = 0
                kof = 0
                sign = False
                flag_now_degree = False
            else:
                for k in range(0, arr_deg[len(arr_deg) - 1] - degree - 1):
                    arr_deg.append(arr_deg[len(arr_deg) - 1] - k - 1)
                    arr_koef.append(0)
                arr_deg.append(degree)
                degree = 0
                if not sign:
                    arr_koef.append(-kof)
                else:
                    arr_koef.append(kof)
                kof = 0
                sign = True
                flag_now_degree = False
        if i == "-":
            sign = False
        elif i == "+":
            sign = True
        elif i.isdigit() and return_degree_num(i) == -1:  # number - and not in upper case
            kof = kof * 10 + int(i)
        elif i == 'x':
            if kof == 0:  # if starts with x
                kof = 1
            flag_now_degree = True
        elif flag_now_degree:  # number - and not in upper case
            degree = degree * 10 + return_degree_num(i)

            # add last kof with degree of x is zero
    if kof != 0:
        for _ in range(0, arr_deg[len(arr_deg) - 1] - 1):
            arr_deg.append(0)
            arr_koef.append(0)
        arr_deg.append(0)
        if not sign:
            arr_koef.append(-kof)
        else:
            arr_koef.append(kof)

    #print("debug: Array of coefficiens: ", arr_koef)
    #print("debug: array of x    degree: ", arr_deg)

    return arr_koef, arr_deg


def sum_2_polinoms(cof1, deg1, cof2, deg2):
    result_cof = []
    result_deg = []

    # cof1 --- 13
    # cof2 -- 15

    if len(cof1) < len(cof2):
        for i in range(0, len(cof2) - len(cof1)):
            result_cof.append(cof2[i])
            result_deg.append(deg2[i])
        for i in range(len(cof2) - len(cof1), len(cof2)):
            temp = len(cof2) - len(cof1) - i  # -i element
            temp1 = cof1[len(cof2) - len(cof1) - i]
            temp2 = cof2[i]
            result_cof.append(cof1[i - (len(cof2) - len(cof1))] + cof2[i])
            result_deg.append(deg2[i])
    else:  # else part didn't tested (2->1, 1->2 according to if part - mirror!)
        for i in range(0, len(cof1) - len(cof2)):
            result_cof.append(cof1[i])
            result_deg.append(deg1[i])
        for i in range(len(cof1) - len(cof2), len(cof1)):
            result_cof.append(cof2[i - (len(cof1) - len(cof2))] + cof1[i])
            result_deg.append(deg1[i])

    return result_cof, result_deg


def print_polinom_on_array(cof, deg):
    result = ""

    for i in range(0, len(cof)):
        # if cof == 0 -> don't show the element, because coeff is zero
        if cof[i] != 0:
            if cof[i] > 0 and len(result) > 0:
                result += "+"

            if deg[i] == 1:
                result += str(cof[i]) + 'x'
            elif deg[i] == 0:
                result += str(cof[i])
            else:
                result += str(cof[i]) + 'x' + str(return_degree_code(deg[i]))
    # print("result is:", result)
    return result


polin1 = form_polinom(12)
print(polin1)
polin2 = form_polinom(15)
print(polin2)
#print("---------------------------------")
_cof1, _deg1 = parsing_polinom(polin1)
_cof2, _deg2 = parsing_polinom(polin2)
coeff, degrees = sum_2_polinoms(_cof1, _deg1, _cof2, _deg2)

#print("---------------------------------")
#print(coeff)
#print(degrees)

print("__________")
print("the result is:", print_polinom_on_array(coeff, degrees))

# print(return_degree_num("\u2074"))

# print(return_degree_num("\u20f9")) # Not exist

# parsing_polinom(polin1)
