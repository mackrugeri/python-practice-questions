def required_skill_present(required_skills, chopping_string):
    for i in required_skills:
        if i not in chopping_string:
            return False
    return True

def min_matching_team(talents, required_skills):
    if not talents or not required_skills:
        return ""

    for i in required_skills:
        if i not in talents:
            return ""
    
    string_choping = ""
    sub_strings = []
    for i in range(0,len(talents)):
        string_choping = talents[1:]
        skill_present = required_skill_present(required_skills, string_choping)
        if skill_present:
            sub_strings.append(string_choping)
            talents = string_choping
            
               
            
        last_index = len(string_choping)
        last_string_choping = talents[:last_index-1]
        skill_present = required_skill_present(required_skills, last_string_choping)
        if skill_present:
            sub_strings.append(last_string_choping)
            talents = last_string_choping
                
            
        
    return sorted(sub_strings)[0]
    

talents = "PPJRPGP"
required_skills = "JRG"

print(min_matching_team(talents, required_skills))