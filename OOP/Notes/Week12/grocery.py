"""
read a file with grocery items in the format:
    category,name,price
    create a grocery store of the items from the file
    create a class to perform statistical analysis given a grocery store
        - figure out the most expensive and cheapest items in each category
        - figure out the average price of an item in each category

class Product
    - category,name,price
class GroceryStore
    - mapping of category to list of products
    - should be able to retrieve all products given a category
    - should be able to add a product to a category
class StatisticalAnalysis
    - get_max given a category and a grocery store
    - get_min given a category and a grocery store
    - get_average price given a category and a grocery store
    - one instance of this class should be able to handle multiple grocery stores
        - a grocery store shouldn't be a propery of the class, it should be an argument for an instance method