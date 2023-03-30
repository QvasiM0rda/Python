users = [input() for _ in range(int(input()))]
new_users = [input() for _ in range(int(input()))]
for user in new_users:
    uid = 0
    while True:
        mail = user + ('' if not uid else str(uid)) + "@beegeek.bzz"
        if mail in users:
            uid += 1
        else:
            print(mail)
            users.append(mail)
            break
