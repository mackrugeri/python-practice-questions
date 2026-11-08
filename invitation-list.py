def Solution(lina_list,carlos_list):
    if len(lina_list) != len(carlos_list):
        return False
    for lina_invited_person in lina_list:
        if lina_invited_person not in carlos_list:
            return False
    return True

print(Solution(["Ali", "Ahmed", "Ahsan",],["Sara", "Ali", "Ahmed"]))