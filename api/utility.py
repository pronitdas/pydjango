from .models import Usersignup, Trainersignup
import datetime
import re

def validate_email(data,pk,modelObj):
    print "pankaj" + pk

    email = data['email_id']

    if pk != "":
        user = modelObj.objects.get(user_id=pk)
        if user.email_id == email:
            return ""

    user_qs = modelObj.objects.filter(email_id=email)
    if user_qs.exists():
        return "email already exits."
    return ""

def check_Token(user,request):
    print "aaaa==" + request.META['HTTP_ACCESSTOKEN']
    if user.access_token != request.META['HTTP_ACCESSTOKEN']:
        return "Access token is not valid"
    return ""

def validate_date(date_text, validate_str):
    try:
        datetime.datetime.strptime(date_text, validate_str)
        return True
    except ValueError:
        print "Incorrect data format, date should be YYYY-MM-DD HH:mm:ss"
        return False
        #raise ValueError("Incorrect data format, date should be YYYY-MM-DD HH:mm:ss")

def validate(data):
        if data.get('password'):
            if  re.match(r'.{8,15}$', data.get('password')):
                return True
            else:

                return False

        return True

def trainersignup_validation(request):
        validate_str = validate_email(request.data, "", Trainersignup)
        isvalidate = validate_date(request.data['birth_date'], '%Y-%m-%d')
        isvalidate = validate(request.data)

        if request.data['first_name'] == "":
            return "Please enter first name"
        
        elif request.data['last_name'] == "":
            return "Please enter last name"
        
        elif validate_str != "":
            return validate_str

        elif isvalidate == False:
            return "Password should be 8 to 15 charaters"

        elif isvalidate == False:
            return "Incorrect data format, date should be YYYY-MM-DD"

        elif request.data['gender'] == "":
            return "Please enter gender"
        
        elif request.data['city'] == "":
            return "Please enter city"
        
        elif request.data['state'] == "":
            return "Please enter state"

        elif request.data['postal_code'] == "":
            return "Please enter postal_code"
        
        elif request.data['address'] == "":
            return "Please enter address"
        
        elif request.data['phone'] == "":
            return "Please enter phone"
        
        elif (request.data.get('image', "") == ""):
            return "Image can not be blank"
            
        return  ""

def usersignup_validation(request):
        validate_str = validate_email(request.data, "", Usersignup)
        isvalidate = validate(request.data)

        if request.data['first_name'] == "":
            return "Please enter first name"
        
        elif request.data['last_name'] == "":
            return "Please enter last name"
        
        elif validate_str != "":
            return validate_str

        elif isvalidate == False:
            return "Password should be 8 to 15 charaters"

        elif request.data['gender'] == "":
            return "Please enter gender"
        
        elif request.data['age'] == "":
            return "Please enter age"
        
        elif request.data['level'] == "":
            return "Please enter level"
        
        elif (request.data.get('image', "") == ""):
            return "Image can not be blank"

        return ""

def session_validation(request):
        user = Usersignup.objects.get(user_id = request.data['user_id'])
        token_str = check_Token(user, request)
        isvalidate = validate_date(request.data['session_time'], '%Y-%m-%d %H:%M:%S')

        if token_str != "":
            return token_str
        
        elif request.data['session_type'] == "":
            return "Please select session type"
        
        elif request.data['session_duration'] == "":
            return "Please select session duration"
        
        elif request.data['session_time'] == "":
            return "Please select session time"

        elif isvalidate == False:
            return "Incorrect data format, date should be YYYY-MM-DD HH:mm:ss"

        elif request.data['session_address'] == "":
            return "Please enter session address"

        if request.data['session_type'] == "book_for_a_friend":
            request.data['squad_size'] == ""
            if request.data['first_name'] == "":
                return "Please enter first name"

            elif request.data['last_name'] == "":
                return "Please enter last name"

            elif request.data['gender'] == "":
                return "Please select gender"
            
            elif request.data['level'] == "":
                return "Please select level"
            

        if request.data['session_type'] == "squad_session":
            request.data['first_name'] == ""
            request.data['last_name'] == ""
            request.data['gender'] == ""
            request.data['level'] == ""
            if request.data['squad_size'] == "":    
                return "Please select squad size"
        return ""

def editprofile_validation(request, user):

        token_str = check_Token(user,request)

        validate_str = validate_email(request.data, request.data['user_id'], Usersignup)

        if token_str != "":
            return token_str

        elif request.data['first_name'] == "":
            return "Please enter first name"
        
        elif request.data['last_name'] == "":
            return "Please enter last name"
        
        elif validate_str != "":
            return validate_str

        elif request.data['gender'] == "":
            return "Please enter gender"
        
        elif request.data['age'] == "":
            return "Please enter age"
        
        elif request.data['level'] == "":
            return "Please enter level"
        
        elif (request.data.get('image', "") == ""):
            return "Image can not be blank"
        
        elif request.data['health_issue'] == "":
            return "Please enter health_issue"
        
        elif request.data['health_condition'] == "":
            return "Please enter health_condition"

        elif request.data['height'] == "":
            return "Please enter height"
        
        elif request.data['weight'] == "":
            return "Please enter weight"

        elif request.data['fitness_goals'] == "":
            return "Please enter fitness_goals"
        

        return ""


def excuate_query(request):
    from django.db import connection
    cursor = connection.cursor()
    latitude = "18.5935"
    longitude = "73.7929"
    query = "SELECT user_id ,( 6371 * acos( cos( radians(%s) ) * cos( radians( latitude ) ) * cos( radians( longitude ) - radians(%s) ) + sin( radians(%s) ) * sin( radians( latitude ) ) ) ) AS distance FROM trainersignup HAVING distance < 15" % ( latitude, longitude, latitude)
    cursor.execute(query)
    row = cursor.fetchall()
    for r in row:
        try:
            user = Trainersignup.objects.get(user_id=r[0])
            print user.first_name

        except:
            print "pankaj"
    #user = Trainersignup.objects.get(user_id=row)
    #print user.first_name
    return row