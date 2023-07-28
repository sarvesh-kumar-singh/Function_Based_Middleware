def my_middleware(get_response):
    print("One Time Initialization !!")




    def my_function(request):
        print("this before View")
        # Jis Code Ko Aapko Views se pehle Chalana ho use yha pr code kre !!!

        response=get_response(request)
        
        print("This is After View!")
        # Jis Code Ko Aapko Views ke baad Chalana ho use yha pr code kre !!!


        
        return response
    return my_function
    