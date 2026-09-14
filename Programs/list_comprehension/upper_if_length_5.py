words = ["python","java","programming","hello","gaming","computer","project","chair","table"]

result = [val.upper() for val in words if len(val)>5]
print(result) 