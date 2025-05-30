# 6. В предложении каждое слово sin заменить на sin(),  cos заменить на cos(),  tg заменить на tg()
sl = {"sin": "sin()", "cos": "cos()", "tg": "tg()", "ctg": "ctg()"}
a = input()
it = []
for i in a.split():
    if i in sl.keys():
        it.append(sl[i])
    else:
        it.append(i)
print(" ".join(it))

# Abra cadabra abra unana sin cos inter r