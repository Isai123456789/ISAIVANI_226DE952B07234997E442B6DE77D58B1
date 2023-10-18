python

# Sample list of products
product_list = ["apple", "banana", "orange", "apple", "grape", "apple"]

# Target product to search for
target_product = "apple"

# Call the function
result = linear_search_product(product_list, target_product)

# Print the result
print(result)  # Output: [0, 3, 5]
In this example, the target product "apple" appears at indices 0, 3, and 5 in the product_list, so the function returns the list [0, 3, 5].