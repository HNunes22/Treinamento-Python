

from sys import getsizeof
# Methodo que mostra quanto de memoria está usando em bytes



values = [x * 10 for x in range(150)]
value_in_bytes_list = getsizeof(values)
print(f"Bytes(List): {value_in_bytes_list}")

# Generation
# A função dela é usar menos memoria do que as listas

values = (x * 10 for x in range(150)) # [] -> ()
value_in_bytes_gen = getsizeof(values)
print(f"Bytes(Generation): {value_in_bytes_gen}")

print(f"Difference: {value_in_bytes_list - value_in_bytes_gen} bytes")