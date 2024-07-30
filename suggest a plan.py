import streamlit as st

def future_value(invested_monthly, yrs, annual_roi = 12):
    compounded_roi = annual_roi/100/12
    fv = float(invested_monthly) * ((1+compounded_roi)**(yrs*12)-1) * (1+compounded_roi)/compounded_roi 
    fv = round(fv, 0)
    return fv

def total_invested(invested_monthly, yrs):
    total_money = invested_monthly * 12 * yrs
    total_money = round(total_money, 0)
    return total_money


st.header("Suggest a plan:")

st.write(
    """Suggest plan is a feature of this investment recommendation system  which 
    works upon what is your monthy income, your age and your occupation.
    Based upon these parameters the system predicts what amount of money one needs 
    to invest, what needs to be saved, and what should be use.
"""
)

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

amount = st.number_input("Enter your monthly income:",min_value=5000, step=5000)

st.text("")

age = st.number_input("Enter your age:", min_value=1, step=1)

st.text("")

occupation = st.selectbox("Enter your occupation:",("Employee", "Student", "Businessman", "Housewife", "Other"))

str1 = ""

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

if not amount or not age:
        str1 += "Dear User,\nPlease fill all the fields.\n\nYou may press RESET to reset fields."

elif not isfloat(amount) or not isfloat(age):
        str1 += "Dear User,\nPlease enter appropriate values for amount and age.\n\n\t>> Income    =>    Integer or Float\n\t>> Age         =>    Preferably an Integer"

elif float(amount) < 0 or int(age) <= 0:
        str1 += "Dear User,\nPlease enter a positive value for amount and age.\n\nYou may press RESET to reset fields."

else:
    age = int(age)
    amount = float(amount)
    per50 = float(amount)*0.5
    per40 = float(amount)*0.4
    per30 = float(amount)*0.3
    per20 = float(amount)*0.2
        
    per50 = str(round(per50, 0))
    per40 = str(round(per40, 0))
    per30 = str(round(per30, 0))
    per20 = str(round(per20, 0))

    pie_labels = ["Total Invested", "Total Returns"]
        

    if age<1 or age>130:
        str1 += "Dear User,\nPlease enter an appropriate age.\nAge should be between 1 year and 130 years.\n\nYou may press RESET to reset fields."

    else:
        if age < 18:
            str1 += "Dear user,\nAs your age is below 18 years,\nIt won't be possible for you to invest in Stocks or Mutual Funds.\nBut you may study about stock market to get a basic idea about the same.\n\nYou may read the following books to increase your knowledge.\n\n1. The Intelligent Investor\n2. Rich Dad Poor Dad"

                

        else:
            if 18<=age<=35:
                    
                str1 += "Dear user,\nAs you are young, we recommend you the following investment strategies.\n\n>> 50% - For your needs (food, rent, EMI, etc.)\n\t[50 %    =>    ~ " + per50 + "    INR]\n\n>> 30% - For your wants (vacations, gadgets, etc.)\n\t[30 %    =>    ~ " + per30 + "    INR]\n\n>> 20% - Savings and Investments (Stocks, Mutual Funds, FD, etc.)\n\t[20 %    =>    ~ " + per20 + "    INR]\n"

                str1 += "\n\n>> If you follow this Financial Discipline, \nEstimated Returns (at 12% Compound Interest) :"

                invested = float(amount) * 0.2
                invested = round(invested, 0)
                str1 += "\nInvested/month      =>      " + str(invested) + " INR"
                    
                str1 += "\n\nPeriod\tInvested (INR)\t\tFuture Value (INR)\n---------------------------------------------------------------"

                str1 += "\n2 yrs\t~ " + str(total_invested(invested, 2)) + "\t\t~ " + str(future_value(invested, 2))                    
                str1 += "\n5 yrs\t~ " + str(total_invested(invested, 5)) + "\t\t~ " + str(future_value(invested, 5))
                str1 += "\n10 yrs\t~ " + str(total_invested(invested, 10)) + "\t\t~ " + str(future_value(invested, 10))

                    

                    

            elif age>35:
                str1 += "Dear user,\nAs you are elder, we recommend you the following investment strategies.\n\n>> 40% - For your needs (food, rent, EMI, etc.)\n\t[40 %    =>    ~ " + per40 + "    INR]\n\n>> 20% - For your wants (vacations, gadgets, etc.)\n\t[20 %    =>    ~ " + per20 + "    INR]\n\n>> 40% - Savings and Investments (Stocks, Mutual Funds, FD, etc.)\n\t[40 %    =>    ~ " + per40 + "    INR]\n"

                str1 += "\n\n>> If you follow this Financial Discipline, \nEstimated Returns (at 12% Compound Interest) :"

                invested = float(amount) * 0.4
                invested = round(invested, 0)
                str1 += "\nInvested/month      =>      " + str(invested) + " INR"
                
                str1 += "\n\nPeriod\tInvested (INR)\t\tFuture Value (INR)\n---------------------------------------------------------------"

                str1 += "\n2 yrs\t~ " + str(total_invested(invested, 2)) + "\t\t~ " + str(future_value(invested, 2))                    
                str1 += "\n5 yrs\t~ " + str(total_invested(invested, 5)) + "\t\t~ " + str(future_value(invested, 5))
                str1 += "\n10 yrs\t~ " + str(total_invested(invested, 10)) + "\t\t~ " + str(future_value(invested, 10))


        if occupation=="Student":
            str1 += "\n\n\n>> Self Investment is the Best Investment.\nAs you are a student, you may invest your time and energy in learning via various resources such as Online Courses.\nWe recommend checking out courses on the following sites:\n1. www.coursera.org\n2. www.udemy.com"

        elif occupation=="Employee":
            str1 += "\n\n\n>> Self Investment is the Best Investment.\nAs you are an employee, you may invest your time and energy in learning via various resources, reading books.\nWe recommend checking out courses on the following sites:\n1. www.coursera.org\n2. www.udemy.com\n\n>> This surely increases your chances of promotion and gives the most returns!"

        elif occupation=="Business":
            str1 += "\n\n\n>> Self Investment is the Best Investment.\nAs you are into business, you may invest your time in reading books which help grow your business.\nWe recommend checking out the following books:\n1. Think and Grow Rich\n2. Zero to One\n3. Rich Dad Poor Dad\n\n>> This surely increases your chances of growing your business and gives the most returns!"

        elif occupation=="Housemaker":
            str1 += "\n\n\n>> Self Investment is the Best Investment.\nAs you are a housemaker, you may invest your time in learning new skills at home.\nYou may help people through these skills via social media.\nHence, you can earn money via Digital Marketing.\nWe recommend you to learn about:\n1. Digital Marketing\n2. Adsense\n3. Blogging\n\n>> This surely increases your chances of improving your skills, make money as well as help others!"

        elif occupation=="Other":
            str1 += "\n\n\n>> Self Investment is the Best Investment.\nWe recommend you to invest your time and energy to learn new skills and try to be a better person.\n\nYou may read the following books to be a better version of yourself!\n1. Getting Things Done\n2. The 7 Habits of Highly Effective People\n3. Think and Grow Rich"



def outdata():
    st.text_area("output:", str1, height = 600)

st.button(label="SUBMIT", on_click=outdata())



