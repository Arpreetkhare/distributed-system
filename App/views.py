import json
import uuid
from django.http import JsonResponse
from django.shortcuts import render
from .models import User,Product,Order

# Create your views here.


def create_user(request):
    
    if request.method == "POST":
        try:

            data = json.loads(request.body)
            user_id = data.get("user_id")
            name  = data.get("name")
            email = data.get("email")

            if not name or not email:
                return JsonResponse({"message": "Name and email are required."}, status=400)




            user = User.objects.filter(user_id = user_id) 

            if user.exists() :
                return JsonResponse ({"message" : "User allready There"},status=400)
            

            new_user = User.objects.create(
                user_id = user_id,
                name = name,
                email = email
                

            )

             # Return a success response
            return JsonResponse(
                {"message": "User created successfully.", "user": new_user.user_id},
                status=201 ) 
        
        
        except Exception as e:
            return JsonResponse({"message": "Internal server error.", "error": str(e)}, status=500)
        

    return JsonResponse({"message": "Invalid request method."}, status=405)    




def create_product(request):
    if request.method == "POST":
        try:

            
                        

            data = json.loads(request.body)

            product_id = data.get("product_id")
            name = data.get("name")
            price = data.get("price")

            if not name or not price:
                return JsonResponse({"message": "Name and price are required."}, status=400)

            product = Product.objects.filter(product_id = product_id)
            
            if product.exists() :
                return JsonResponse ({"message" : " product allready There"},status=400)
            


            



            new_product = Product.objects.create(
                product_id = product_id,
                name = name,
                price=price
                

            )

             # Return a success response
            return JsonResponse(
                {"message": " product created successfully.", "product": new_product.product_id},
                status=201 ) 
        
        
        except Exception as e:
            return JsonResponse({"message": "Internal server error.", "error": str(e)}, status=500)
        

    return JsonResponse({"message": "Invalid request method."}, status=405)    



def create_order (request) :

    if request.method == "POST":
        try:


            data = json.loads(request.body)
            
            order_id = data.get("order_id")
            user_id = data.get("user_id")
            product_id  = data.get("product_id")
            quantity = data.get("quantity")

            if not user_id or not product_id or not quantity:
                return JsonResponse({"message": "User ID, product ID, and quantity are required."}, status=400)

            user = User.objects.filter(user_id=user_id).first()

            if not user:
                return JsonResponse({"message": "User not found."}, status=404)

            product = Product.objects.filter(product_id=product_id).first()

            if not product:
                return JsonResponse({"message": "Product not found."}, status=404)




            new_order = Order.objects.create(

                order_id = order_id,
                user = user,
                product = product,
                quantity = quantity
            ) 

            return JsonResponse(
                {"message": " order created successfully.", "order": new_order.order_id},
                status=201 ) 
        
        
        except Exception as e:
            return JsonResponse({"message": "Internal server error.", "error": str(e)}, status=500)
        

    return JsonResponse({"message": "Invalid request method."}, status=405)    

           


    
