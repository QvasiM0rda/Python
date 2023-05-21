from collections import defaultdict


def best_sender(messages: list, senders: list) -> str:
    messages_and_senders = defaultdict(int)
    for i in range(len(messages)):
        messages_and_senders[senders[i]] += len(messages[i].split())
    return max(messages_and_senders.items(), key=lambda ms: (ms[1], ms[0]))[0]


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))

messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))