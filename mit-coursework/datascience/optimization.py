
def optimal_score(toConsider, avail, score):
    print(toConsider, avail, score)
    if avail <= 20 or not toConsider:
        return (score, toConsider)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = optimal_score(toConsider[1:], avail, score)
        withoutVal, withoutToTake = optimal_score(toConsider[1:], avail-10, score-nextItem)

        if withVal >= withoutVal:
            return (withVal, withToTake + [nextItem])
        else:
            return (withoutVal, withoutToTake)

def lookup_update(toConsider, avail, score, memo, func):
    key = (len(toConsider), avail, score)
    if key in memo:
        return memo[key]
    else:
        memo[key] = func(toConsider, avail, score, memo)
        return memo[key]

def optimal_score_dynamicprograming(toConsider, avail, score, memo):
    print(toConsider, avail, score)
    if avail <= 20 or not toConsider:
        return (score, toConsider)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = lookup_update(toConsider[1:], avail, score, memo, optimal_score_dynamicprograming)
        withoutVal, withoutToTake = lookup_update(toConsider[1:], avail-10, score-nextItem, memo, optimal_score_dynamicprograming)

        if withVal >= withoutVal:
            return (withVal, withToTake + [nextItem])
        else:
            return (withoutVal, withoutToTake)


# Score	=	((60	–	(a+b+c+d+e))*F	+	a*ps1	+	b*ps2	+	c*ps3	+	d*ps4	+	e*ps5
#       = 60*F + (-F + ps1)*a + (-F + ps2)*b + (-F + ps3)*c + (-F + ps4)*d + (-F + ps5)*e

def formulize_items(params):
    weight = 10
    items = []
    for i, p in enumerate(params):
        if not i:
            F = p
        else:
            items.append((-F+p)*weight)
    return items

params = [30, 10, 60, 25, 20, 50]
items = formulize_items(params)

score = params[0] * 60 
for x in items:
    score += x

print('base score: {}'.format(score))
max_score = optimal_score(items, len(items) * 10, score)
print(max_score)

print('\ndynamic programing')
max_score = optimal_score_dynamicprograming(items, len(items) * 10, score, {})
print(max_score)

