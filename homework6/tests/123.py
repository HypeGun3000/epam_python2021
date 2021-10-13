from collections import defaultdict

dictww = defaultdict(set)


author_info = ("Ivan", "Tupeh")
homework_info = (
            author_info,
            "I DONE HOMEWORK",
            "CREATE WEBSITE",
        )

dictww['one'].add(homework_info)
abc = set(homework_info)
for i in dictww.values():
    print(i)