word = ["همان جا", "علاقه مند", "راستی", "می آورد", "زیبا", "کثیف", "*"]
Poem = ["من همان جا می روم", "راستی * به او علاقه مند شدم", "او خودش می آورد"]

wanted = []

for wnt in word:
    wnt = wnt.encode('utf-8')
    wanted.append(wnt)

poem_en = []

for wnt in Poem:
    wnt = wnt.encode('utf-8')
    poem_en.append(wnt)

count = 0
for i in wanted:
    for j in poem_en:
        if i in j:
            count += 1

print(count)