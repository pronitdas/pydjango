from .models import Signup


def validate_email(data,pk):
    email = data['email_id']

    if pk != "":
        user = Signup.objects.get(pk=pk)
        if user.email_id == email:
            return ""

    user_qs = Signup.objects.filter(email_id=email)
    if user_qs.exists():
        return "email already exits."
    return ""

def check_Token(user,request):
    if user.access_token != request.META['HTTP_ACCESSTOKEN']:
        return "Access token is not valid"
    return ""

