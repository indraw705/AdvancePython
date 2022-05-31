def first_non_repeating_letter(s: str) -> str:
    char_order = []
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
            char_order.append(c)
    for c in char_order:
        if counts[c] == 1:
            return c
    return ' '

# =======================================
def maskify(cc: str) -> str:
  str2 = ""
  cc = str(cc)
  newstr = []
  if len(cc) == 0:
    print("")
  elif len(cc) < 4:
    return(cc)
  else:
    for i in range(0,len(cc)):
      if i < (len(cc)-4):
        newstr.append("#")
      else:
        newstr.append(cc[i])
  for ele in newstr:
    str2 += ele
  return str2

# ========================
def max_pizza(cut: int) -> int:
    if cut < 0:
        return -1
    return int(1 + cut * (cut + 1) / 2)