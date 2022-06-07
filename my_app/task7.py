# from user_models.models import Product

# # Insert a new product into the Product Model
# new_product = Product(product_name="Popcorn" , product_price=3000)
# #save new product
# new_product.save()

# # get all records in product table
# all_products = Product.objects.all()

# # filter products by their name
# # this command filters for products with product name 'utensils' and returns the products in a list
# Product.objects.filter(product_name="utensils")

# # Get a single record from the Product Table
# # This command gets the first product in the product group 'utensils'
# Product.objects.filter(product_group="utensils").first()
# # this command gets the product whose group is 'utensils' but name is 'spoon'
# Product.objects.filter(product_group="utensils").filter(product_name="spoon").first()

# #Change the product Price
# product = Product.objects.filter(product_name="garri").first()
# # assign a new product price
# product.product_price = 100
# product.product_price
# #save new product price
# product.save()