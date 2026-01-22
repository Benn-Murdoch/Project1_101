def convert_case(character, target_case):
    if type(character) is str:   
        if len(character) <= 1:   
            character_num = ord(character) 
            if 65 <= character_num <= 90 or 97 <= character_num <= 122:
                if (target_case == "upper" or target_case == "Upper" or target_case =="UPPER") and character_num >=97 :
                    new_num = character_num - 32
                    return chr(new_num)
                elif (target_case =="lower" or target_case =="Lower" or target_case =="LOWER") and character_num <=90: 
                    new_num = character_num + 32
                    return chr(new_num)
                else:
                    return chr(character_num)
            else: 
                return character
    else:
       raise ValueError("Input must be a string")
