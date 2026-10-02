# membeship operator use to check that one string is present in another string or not
# --> 'in'  'not in'

res = "iot" in "in iot batch"
res1 = "iot" not in "in iot batch"
res3 = "i" in "in iot batch"        # we can check single letter and specific symbol also
print(res)
print(res1)
print(res3)