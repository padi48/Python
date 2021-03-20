 #This is a very basic quote generator I made.
 #I'll upload a much better version of this in the near future.
 
 import random

def goodDay():
    goodQuotes = [
        "“The Best Way To Get Started Is To Quit Talking And Begin Doing.”",
        "“The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.”",
        "“Don’t Let Yesterday Take Up Too Much Of Today.”",
        "“You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.”",
        "“It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.”",
        "“If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.”",
        "“People Who Are Crazy Enough To Think They Can Change The World, Are The Ones Who Do.”",
        "“Failure Will Never Overtake Me If My Determination To Succeed Is Strong Enough.”",
        "“We May Encounter Many Defeats But We Must Not Be Defeated.”",
        "“Knowing Is Not Enough; We Must Apply. Wishing Is Not Enough; We Must Do.”"
    ]

    return random.choice(goodQuotes)

def badDay():
    badQuotes = [
        "“Breathe. It’s just a bad day, not a bad life.”",
        "“Difficult roads often lead to beautiful destinations.”",
        "“A bad day only lasts 24 hours.”",
        "“On the other side of the clouds is a bright blue sky.”",
        "“No rain, no flowers.”",
        "“Look for something positive in each day, even if some days you have to look a little harder.”",
        "“Was it a bad day? Or was it five minutes that you milked all day?”",
        "“Life is tough, but so are you.”",
        "“Storms don’t last forever.”",
        "“You have to experience sadness to know happiness.”"
    ]

    return random.choice(badQuotes)

def getUserDay():
    userDay = input("How was your day? (Good / Bad) ")

    if userDay == "Good":
        print(goodDay())

    elif userDay == "Bad":
        print(badDay())

    else:
        print("Please enter Good or Bad!")

getUserDay()
