from collections import defaultdict

homework_done = defaultdict(set)

def check_duplicate(homework_result):
    author_info = ("Ivan", "Tupeh")
    homework_info = (
        author_info,
        "I DONE HOMEWORK",
        "CREATE WEBSITE",
    )
    for i in homework_info:
        if i in homework_done[homework_result]:
            return False
    for i in homework_info:
        homework_done[homework_result].add(i)
    return True

print(check_duplicate('one'))
check_duplicate('one')
print(check_duplicate('one'))