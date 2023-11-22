from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from disneyland.models import *
from hello_world import *
import pandas as pd

#  nltk - text sentiment analysis
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Create your views here.

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def home(request):
    context = {}
    return render(request, "webpages/home.html", context=context)



def register(request):
    if request.method == 'POST':
        username = request.POST['r_username']
        name = request.POST['r_name']
        email = request.POST['r_email']
        password = request.POST['r_password']
        confirmpassword = request.POST['r_cpassword']
        if not username or not name or not email or not password or not confirmpassword:
            context_data ={
                "message":"Fill a form "
            }
            return render(request,"webpages/register.html",context_data)
        if userInfo.objects.filter(userName=username).exists():
            context_data ={
                "message":"Registered username"
            }
            return render(request,"webpages/register.html",context_data)
        if userInfo.objects.filter(email=email).exists():
            context_data ={
                "message":"Registered email"
            }
            return render(request,"webpages/register.html",context_data)
        new_item = userInfo (
                userName = username,
                name = name,
                email = email,
                passWord = password,
                confirmpass = confirmpassword
            )   
        new_item.save()
        alert_message = "Registration successful! You can now log in."
        return render(request, "webpages/login.html", {"alert_message": alert_message})
    return render(request, "webpages/register.html")


def login(request):
    if request.method == 'POST':
        email = request.POST.get('l_email')
        password = request.POST.get('l_password')
        if not email or not password:
            context_data = {
                "message": "Please fill in both email and password fields."
            }
            return render(request, "webpages/login.html", context_data)

        if (userInfo.objects.filter(email=email).exists() and userInfo.objects.filter(passWord=password).exists()):
            # Log in successful, you can redirect to the home page or any other page
            return redirect('../account/home')
        else:
            # Authentication failed
            context_data = {
                "message": "Wrong email or password"
            }
            return render(request, "webpages/login.html", context_data)
    return render(request, "webpages/login.html")


def profile(request):
    # Check whether there is a user account
    try:
        latest_user = userInfo.objects.latest()
    except userInfo.DoesNotExist:
        context_data = {'message': 'User not found. Please register first.'}
        return render(request, "webpages/register.html", context_data)

    # Pass the user data to the template
    context = {'user': latest_user}

    # If the form is submitted (DELETE)
    if request.method == 'POST':
        latest_user.delete()
        context_data = {'message': 'Account deleted successfully.'}
        return render(request, "webpages/home.html", context_data)

    # Render the profile page for the GET request
    return render(request, "webpages/profile.html", context)


def editprofile(request):
    # Retrieve the latest user data
    latest_user = userInfo.objects.latest()
    context = {'user': latest_user}

    # If the user submits the form
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('u_username', '')
        name = request.POST.get('u_name', '')
        email = request.POST.get('u_email', '')
        password = request.POST.get('u_password', '')
        confirmpassword = request.POST.get('u_cpassword', '')

        # Check if any values have changed and update the existing user object
        if username:
            latest_user.userName = username
        if name:
            latest_user.name = name
        if email:
            latest_user.email = email
        if password:
            latest_user.passWord = password
        if confirmpassword:
            latest_user.confirmpass = confirmpassword

        # Save the changes
        latest_user.save()
        context_data = {
            "message": "Profile updated successfully!",
            'user': latest_user
        }
        return render(request, "webpages/profile.html", context_data)

    return render(request, "webpages/editprofile.html", context)



def import_data_csv(request):
    csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS4EPpyFHzOACG9rfzqk3bJ0PbCawzX24IgYrYptGgi0cvDo4IH7frGmYuNBdLBzYuW0MHxv8EYoBDA/pub?output=csv'
    df = pd.read_csv(csv_url)
    data_sets = df[["Review_ID","Rating","Review_Text","Branch"]]
    sucesss = []
    errors = []
    for index, row in data_sets.iterrows():
        instance = DisneylandReview(
            review_id = int(row['Review_ID']),
            rating = int(row['Rating']),
            text = row['Review_Text'],
            branch = row['Branch'],
        )
        try:
            instance.save()
            sucesss.append(index)
        except:
            errors.append(index)
    return JsonResponse({"success_indexes":sucesss,"error_index":errors})

def places(request):
    
    return render(request, 'webpages/places.html',)


#text analysis function-> Negative(-1 - -0.25) Neutral(-0.25 - 0) Positive(+1)
nltk.download('vader_lexicon')

def sentiment(text):
    text_score = SentimentIntensityAnalyzer().polarity_scores(text)
    return text_score['compound']

def classify_sentiment(score):
    if score and score > 0:
        return 'positive'
    elif score and score < 0:
        return 'negative'
    else:
        return 'neutral'

def calculate_sentiment_percentage(df):
    total_count = len(df)
    positive_percentage = (df[df['sentiment_category'] == 'positive'].shape[0] / total_count) * 100
    neutral_percentage = (df[df['sentiment_category'] == 'neutral'].shape[0] / total_count) * 100
    negative_percentage = (df[df['sentiment_category'] == 'negative'].shape[0] / total_count) * 100
    return positive_percentage, neutral_percentage, negative_percentage

def sentiment_HongKong(request):
    reviews_hongkong = DisneylandReview.objects.filter(branch='Disneyland_HongKong')
    df_hongkong = pd.DataFrame(list(reviews_hongkong.values()))

    df_hongkong['sentiment'] = df_hongkong['text'].apply(sentiment)
    df_hongkong['sentiment_category'] = df_hongkong['sentiment'].apply(classify_sentiment)
    positive_percentage, neutral_percentage, negative_percentage = calculate_sentiment_percentage(df_hongkong)
    print(df_hongkong)
    # print(df_hongkong[['review_id','text']])
    print("Branch: Hong Kong")
    print(f"Positive Percentage: {positive_percentage}")
    print(f"Neutral Percentage: {neutral_percentage}")
    print(f"Negative Percentage: {negative_percentage}")
    
    context = {
        'branch': 'Hong Kong',
        'positive_percentage': positive_percentage,
        'neutral_percentage': neutral_percentage,
        'negative_percentage': negative_percentage,
    }
    return context

def sentiment_Paris(request):
    reviews_paris = DisneylandReview.objects.filter(branch='Disneyland_Paris')
    df_paris = pd.DataFrame(list(reviews_paris.values()))

    df_paris['sentiment'] = df_paris['text'].apply(sentiment)
    df_paris['sentiment_category'] = df_paris['sentiment'].apply(classify_sentiment)
    positive_percentage, neutral_percentage, negative_percentage = calculate_sentiment_percentage(df_paris)
    print(df_paris)
    # print(df_hongkong[['review_id','text']])
    print("Branch: Paris")
    print(f"Positive Percentage: {positive_percentage}")
    print(f"Neutral Percentage: {neutral_percentage}")
    print(f"Negative Percentage: {negative_percentage}")
    
    context = {
        'branch': 'Paris',
        'positive_percentage': positive_percentage,
        'neutral_percentage': neutral_percentage,
        'negative_percentage': negative_percentage,
    }
    return  context

def sentiment_California(request):
    reviews_california = DisneylandReview.objects.filter(branch='Disneyland_California')
    df_california = pd.DataFrame(list(reviews_california.values()))

    df_california['sentiment'] = df_california['text'].apply(sentiment)
    df_california['sentiment_category'] = df_california['sentiment'].apply(classify_sentiment)
    positive_percentage, neutral_percentage, negative_percentage = calculate_sentiment_percentage(df_california)
    print(df_california)
    # print(df_hongkong[['review_id','text']])
    print("Branch: California")
    print(f"Positive Percentage: {positive_percentage}%")
    print(f"Neutral Percentage: {neutral_percentage}%")
    print(f"Negative Percentage: {negative_percentage}%")
    
    context = {
        'branch': 'California',
        'positive_percentage': positive_percentage,
        'neutral_percentage': neutral_percentage,
        'negative_percentage': negative_percentage,
    }
    return  context
def hk(request):
    review_texts = DisneylandReview.objects.filter(branch="Disneyland_HongKong").values('review_id', 'text')[:10]
    response = sentiment_HongKong(request)
    context_data = {
            "comments":  review_texts,
            "d3": response
        }   
    
    return render(request, 'webpages/places.html', context=context_data)

def cl (request):
    review_texts = DisneylandReview.objects.filter(branch="Disneyland_Californai").values('review_id', 'text')[:10]
    response = sentiment_California(request)
    context_datacl = {
            "comments":  review_texts,
            "d3": response
        }   
    
    return render(request, 'webpages/places.html', context=context_datacl)

def ps (request):
    review_texts = DisneylandReview.objects.filter(branch="Disneyland_Paris").values('review_id', 'text')[:10]
    response = sentiment_Paris(request)
    context_dataps = {
            "comments":  review_texts,
            "d3": response
        }   
    
    return render(request, 'webpages/places.html', context=context_dataps)