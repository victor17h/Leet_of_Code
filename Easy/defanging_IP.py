address = "1.1.1.1"

def defanged_IP(address):
    find_character = address.split(".")
    print(find_character)
    join_character = "[.]".join(find_character)
    return join_character

print(defanged_IP(address))