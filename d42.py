# Calculate a^b and then do the mod with c

a = int(input())
b = int(input())
m = int(input())

ans = a**b
mod = ans%m
print(ans)
print(mod)