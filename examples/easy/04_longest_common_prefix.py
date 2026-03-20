strs = ["flower", "fkow"]

first_element = strs[0]
flag = False
i = 1
if first_element == "":
    pass  # return first_element

for i in range(1, len(first_element)):
    for j in range(1, len(strs)):
        if strs[j].startswith(first_element[0:i]):
            j += 1

        else:

            if j != len(strs) or len(strs[j]) <= i - 1:
                i -= 1

            flag = True
            break

    if flag:
        break

    i += 1

print(first_element[0:i])

a = "a"
for i in range(1, len(a)):
    print(a[i])