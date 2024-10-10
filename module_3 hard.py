sum_elements = 0
def calculate_structure_sum(data_structure):
    global sum_elements
    for element in data_structure:
        if isinstance(element, int):
            sum_elements += element
        elif isinstance(element, str):
            sum_elements += len(element)
        elif isinstance(element, (list, tuple, set)):
            calculate_structure_sum(element)
        elif isinstance(element, dict):
            calculate_structure_sum(element.items())
    return sum_elements

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
