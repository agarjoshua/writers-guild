from calendar import c
from email import message
from email.headerregistry import Address
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponse
from django.shortcuts import render, redirect

#formimports
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

#mailer imports
import smtplib, ssl

# Create your views here.
def index(request):
    return render(request, 'index/home.html')

def orderView(request): 
    print(request.POST)
    if request.method == 'POST':
        message = []
        pages = request.POST["pages"]

        email = request.POST["email"]
        answer1 = request.POST.get("drop1", False)
        academic_level = options_dict[answer1]
        answer2 = request.POST.get("drop2", False)
        type_of_paper = options_dict[answer2]
        answer3 = request.POST.get("drop3", False)
        deadline = options_dict[answer3]

        ac_level = pricing_dict[answer1]
        ac_deadline = pricing_dict[answer3]
        total_price = (int(ac_level) +  int(ac_deadline)) * int(pages)
        print(pages)
        print(total_price)

        message.extend((academic_level,type_of_paper,deadline, pages, email, total_price))
        str_message = message
        # try:
        #     mailer(str_message)
        # except Exception:
        #     return 'Hi there seems to be an error \n {Exception},\n Kindly contact the site admin'

    return render(request, "index/email.html")

options_dict = {
"96035":"High School",
"96036":"College",
"96037":"Undergraduate",
"96038":"Masters",
"96039":"PHD",
"118205":"Book Report",
"118206":"Book Review",
"118207":"Moview Review",
"118208":"Dissertation",
"118209":"Thesis",
"118210":"Thesis Proposal",
"118211":"Dissertation Chapter-Abstract",
"118212":"Dissertation Chapter-Introduction Chapter",
"118213":"Dissertation Chapter-Literature Review",
"118214":"Dissertation Chapter-Methodology",
"118215":"Dissertation Chapter-Results",
"118216":"Dissertation Chapter-Discussion",
"118217":"Article Critique",
"118218":"Research Proposal",
"118219":"Case Study",
"118220":"Research Paper",
"118221":"Term Paper",
"118222":"Essay",
"118223":"Dissertation Services-Editing",
"118224":"Dissertation Services-Proofreading",
"118225":"Lab Report",
"118226":"Math Problem",
"118227":"Statistics Project",
"118228":"Multiple choice questions(None Time framed)",
"118229":"Reaction Paper",
"118230":"Annotated Bibliography",
"118231":"Article",
"118232":"Speech Presentation",
"118233":"Proofreading",
"118234":"Editing",
"118235":"Formatting",
"118236":"Admission Services-Admission Essay",
"118237":"Admission Services-Scholarship Essay",
"118238":"Admission Services-Pesonal Statement",
"118239":"Admission Services-Editing",
"118240":"Coursework ",
"118241":"Powerpoint Presentation ",
"118242":"Other (Not listed) ",
"118243":"Coursework AS and A-Level" ,
"118244":"Coursework GCSE ",
"118245":"Assignment ",
"118246":"Admission - Application Essay ",
"118247":"Capstone Project",
"118248":"Discussion Post",
"118249":"Poster",
"118250":"Bronchure",
"2681":"3 hrs",
"2682":"8 hrs",
"2683":"12 hrs",
"2684":"24 hrs",
"2685":"2 days",
"2686":"3 days",
"2687":"5 days",
"2688":"7 days",
"2689":"10 days",
"2692":"14 days",
"2690":"20 days",
"2691":"30 days",
}

pricing_dict = {
    "2681":"59",
    "2682":"38",
    "2684":"26",
    "2686":"22",
    "2688":"18",
    "2692":"16",
    "96035":"1",
    "96036":"2",
    "96037":"3",
    "96038":"4",
    "96039":"5"
}

def mailer(str_message):
    port = 465  # For SSL
    smtp_server = "mail.essaylancing.com"
    sender_email = "contact@essaylancing.com"  # Enter your address
    receiver_email = ["contact@essaylancing.com"]  # Enter receiver address
    password = 'h,Y;c;_)g7=0'

    print(str_message)
    message = f"""From: contact@essaylancing.com \n
        To: {receiver_email} \n
        Hi admin, This is a new request for a: {str_message[1]}\n
        of the academic level: {str_message[0]}\n
        with: {str_message[3]} pages,\n
        And its needed in {str_message[2]}.\n
        The total cost is {str_message[5]}.\n
        You can contact me, the client, using the email: {str_message[4]}\n"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        except Exception as e:
        # Print any error messages to stdout
            print(e)