while True:
    errors = {"404":"not found","403":"forbidden","402":"payment required","401":"unauthorized","400":"bad request","405":"method not allowed","406":"not acceptable","407":"Proxy Authentication Required","408":"Request Timeout","409":"Conflict","410":"gone","411":"Length Required","412":"Precondition Failed","413":"Content Too Large","414":"URI Too Long","415":"Unsupported Media Type","416":"Range Not Satisfiable","417":"Expectation Failed","418":"I'm a teapot(april fools joke)"}
    e = input("enter your error number: ")
    if e in errors:
        print("your error is this: "+errors[e])
    else:
        print("error not found sorry")