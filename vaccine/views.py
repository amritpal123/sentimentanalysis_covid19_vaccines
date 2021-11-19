from django.shortcuts import render,redirect

from .extract import vaccine

from .country import Country

from .barchartcompare import barcompare

from .barchart import bar

from .donut import donut


from .labeling import sentiMent

from .sentipie import sentiFig


from .wordc import makeWordCloud


from .retweetana import reTweetData

import pandas as pd


from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login,logout,authenticate

from .signupform import SignUpForm

from django.contrib import  messages


def signup(request):

    if request.method=="POST":

        form=SignUpForm(request.POST)

        if form.is_valid():
            user=form.save()
            '''
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            '''
            login(request,user)
            messages.success(request,"Successfully Sign up")
            return redirect("/")
        else:
            print('error')

            for msg in form.error_messages:
                messages.error(request,f'{form.error_messages[msg]}')


    form =SignUpForm()
    return render(request,'signup.html',context={'form':form})


def login1(request):
    return render(request,'login.html')


def home(request):

    try:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

    except:
        pass

    if user is None:

        return redirect("http://127.0.0.1:8000/")
    login(request, user)
    context={"username":user}

    return render(request,'home.html',context)

def logout_request(request):

    global user

    logout(request)
    user=None
    return redirect("/")

def analize(request,i):
    print(i)

    if i=="AstraZeneca":
        list1=["AstraZeneca","astrazenecavaccine","OXFORDVACCINE","GenXZeneca"]
    elif i == "Covaxin":
        list1=["#covaxin", "#covaxine", "#BharatBiotech", "#covaxininhungary", "#COVAXIN"]
    elif i=="Covishield":
        list1=["covishield","covishieldvaccine","covishieldsideeffects"]
    elif i=="Moderna":
        list1 = ["Moderna"]
    elif i=="SputnikV":
        list1=["SputnikV","sputnik","SputnikLight"]
    elif i=="Pfizer":
        list1=["Pfizer","PfizerVaccine"]

    df = vaccine(list1, 100)

    print(len(df))
    df=sentiMent(df)
    df = Country(df)

    print(df)
    img=sentiFig(df)
    img2=makeWordCloud(df)
    df2 = dict(df['Country'].value_counts())
    sentiment = []
    for i in df2.keys():
        df1=pd.DataFrame(columns=['DateTime', 'Tweet_Id', 'Tweet', 'User_Id', 'Retweet', 'Location', 'Label','Country'])
        for j in range(len(df)):
            if i == df['Country'][j]:
                df1=df1.append(df.iloc[j])
        print(df1['Label'].value_counts())
        sentiment.append([df1['Label'].value_counts()])

    reTweetDic=reTweetData(df)

    data={'senti':sentiment,'retweet':reTweetDic,'keys': img}#df2.keys()}
    print(data)
    return render(request,'analize.html',data)

def analizekey(request):

    i=request.GET.get('keyword1')
    j=request.GET.get('keyword2')
    print(i)
    print(j)

    if i == "AstraZeneca":
        df1=pd.read_csv("D:/vaccine/AstraZenecaLive.csv")
    elif i == "Covaxin":
        df1=pd.read_csv("D:/vaccine/CovaxinLive.csv")
    elif i == "Covishield":
        df1=pd.read_csv("D:/vaccine/CovishieldLive.csv")
    elif i == "Moderna":
        df1=pd.read_csv("D:/vaccine/ModernaLive.csv")
    elif i == "SputnikV":
        df1=pd.read_csv("D:/vaccine/SputnikVLive.csv")
    elif i == "Pfizer":
        df1=pd.read_csv("D:/vaccine/PfizerLive.csv")



    if j == "AstraZeneca":
        df2 = pd.read_csv("D:/vaccine/AstraZenecaLive.csv")
    elif j == "Covishield":
        df2 = pd.read_csv("D:/vaccine/CovishieldLive.csv")
    elif j == "Moderna":
        df2 = pd.read_csv("D:/vaccine/ModernaLive.csv")
    elif j == "SputnikV":
        df2 = pd.read_csv("D:/vaccine/SputnikVLive.csv")
    elif j == "Pfizer":
        df2 = pd.read_csv("D:/vaccine/PfizerLive.csv")

    tempdf = [[i, df1], [j, df2]]

    vaccine1=sep(tempdf)

    img1 = barcompare(vaccine1)

    return render(request,"bar1.html")


def summary(dataset):
    tempdf = pd.DataFrame(columns=["Name", "Total_Tweets", "Positive_Tweets_per", "NonPositive_Tweets_per"])

    for name, df in dataset:
        total = 0
        temp = df['Label'].value_counts()
        for i in temp.values:
            total += i
        print(temp)

        pos = temp['Highly_Positive'] + temp['Weakly_Positive']
        neg = ((total - pos) / total) * 100
        pos=(pos/total) * 100
        pos=round(pos,2)
        neg = round(neg, 2)

        list1 = [name, total, pos, neg]
        tempdf = tempdf.append(
            pd.Series(list1, index=["Name", "Total_Tweets", "Positive_Tweets_per", "NonPositive_Tweets_per"]),ignore_index=True)
    tempdf=tempdf.sort_values(by=['Positive_Tweets_per'],ascending=False)
    tempdf=tempdf.reset_index()
    return tempdf

def sep(dataset):
    tempdf = pd.DataFrame(columns=["Name", "Positive_Tweets_per", "Negative_Tweets_per", "Neutral_Tweets_per"])

    for name, df in dataset:
        total = 0
        temp = df['Label'].value_counts()
        for i in temp.values:
            total += i
        print(temp)

        pos = temp['Highly_Positive']+temp['Weakly_Positive']
        neg = ((total-pos-temp["Neutral"]) / total) * 100
        pos=(pos/total)*100
        pos=round(pos,2)
        neg=round(neg,2)

        neu=(temp['Neutral']/total)*100
        list1 = [name, pos, neg, neu]

        tempdf = tempdf.append(
            pd.Series(list1, index=["Name", "Positive_Tweets_per", "Negative_Tweets_per", "Neutral_Tweets_per"]),ignore_index=True)

    tempdf=tempdf.sort_values(by=['Positive_Tweets_per'],ascending=False)

    tempdf=tempdf.reset_index()

    return tempdf

def rank(request):
    list2 = ['AstraZeneca','Covishield','Moderna','SputnikV','Pfizer',"Covaxin"]
    for i in list2:
        if i == "AstraZeneca":
            list1 = ["AstraZeneca", "astrazenecavaccine", "OXFORDVACCINE", "GenXZeneca"]
        elif i == "Covishield":
            list1 = ["covishield", "covishieldvaccine", "covishieldsideeffects"]
        elif i == "Moderna":
            list1 = ["Moderna"]
        elif i == "SputnikV":
            list1 = ["SputnikV", "sputnik", "SputnikLight"]
        elif i == "Pfizer":
            list1 = ["Pfizer", "PfizerVaccine"]
        elif i == "Covaxin":
            list1 = ["#covaxin", "#covaxine", "#BharatBiotech", "#covaxininhungary", "#COVAXIN"]

        df = vaccine(list1, 100)

        if i == "AstraZeneca":
            df1 = df
        elif i == "Covishield":
            df2 = df
        elif i == "Moderna":
            df3 = df
        elif i == "SputnikV":
            df4 = df
        elif i == "Pfizer":
            df5 = df
        elif i == "Covaxin":
            df6 = df


    df1 = sentiMent(df1)
    df1 = Country(df1)
    df1.to_csv("D:/vaccine/AstraZenecaLive.csv")
    df2 = sentiMent(df2)
    df2 = Country(df2)
    df2.to_csv("D:/vaccine/CovishieldLive.csv")
    df3 = sentiMent(df3)
    df3 = Country(df3)
    df3.to_csv("D:/vaccine/ModernaLive.csv")
    df4 = sentiMent(df4)
    df4 = Country(df4)
    df4.to_csv("D:/vaccine/SputnikVLive.csv")
    df5 = sentiMent(df5)
    df5 = Country(df5)
    df5.to_csv("D:/vaccine/PfizerLive.csv")
    df6 = sentiMent(df6)
    df6 = Country(df6)
    df6.to_csv("D:/vaccine/CovaxinLive.csv")

    tempdf = [["AstraZeneca", df1], ["Covishield", df2], ["Moderna", df3], ["SputnikV", df4], ["Pfizer", df5], ["Covaxin", df6]]
    d = summary(tempdf)
    img1 = donut(d)
    img2 = bar(d)
    d = d.transpose()

    data = {"Rank1": d[0], "Rank2": d[1], "Rank3": d[2], "Rank4": d[3], "Rank5": d[4], "Rank6": d[5]}
    return render(request, 'rank.html', data)

def paidvsfree(request):
    list3=['paid','free']
    for i in list3:
        if i =='paid':
            list4 = ['#paidvaccination','#PaidVaccination','#paidvaccine']
        elif i=='free':
            list4=['#freevaccination','#vaccinationcamp',"#FreeVaccine","#FreeVaccineForAll"]
        df = vaccine(list4, 100)

        if i == "paid":
            df1 = df
        elif i == "free":
            df2 = df

    df1 = sentiMent(df1)

    df2 = sentiMent(df2)

    tempdf = [['paid', df1], ['free', df2]]

    vaccine1 = sep(tempdf)

    img1 = barcompare(vaccine1)
    return render(request, 'paidvsfree.html')
