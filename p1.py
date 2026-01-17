def convert_case(character, target_case):
    character_num = ord(character) 
    
    if 65 <= character_num <= 90 or 97 <= character_num <= 122:
        if target_case == ("upper" or "Upper" or "UPPER") and character_num >=97 :
            new_num = character_num + 32
            return chr(new_num)
        elif target_case == ("lower" or "Lower" or "LOWER") and character_num <=90: 
            new_num = character_num - 32
            return chr(new_num)
        else:
            return chr(character_num)

    else: 
        return character

print(convert_case("a", "upper"))