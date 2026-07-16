import module_sample as sample
from module_sample import add as sample_add

add_result = sample.add(3, 6)
sample_add_result = sample_add(3, 6)

print(add_result, sample_add_result)