first_name = str(input("Hey, what's your first name? : "))
last_name = str(input("And your last name? : "))

def introduce(first_name: str, last_name: str) -> str:
    return f"Well, pleased to meet you, {first_name} {last_name}.\n"

print(introduce(first_name, last_name))