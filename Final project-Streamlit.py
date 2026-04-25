#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install streamlit_jupyter
import streamlit as st
from streamlit_jupyter import StreamlitPatcher
StreamlitPatcher().jupyter()


# In[ ]:


st.write('Final Project: Improving health through reducing sedentary screen time')

import matplotlib.pyplot as plt

# Convert hours + minutes into decimal hours
us_average = 7 + 2/60        # 7 hours 2 minutes
world_average = 6 + 54/60    # 6 hours 54 minutes
negative_threshold = 2       # 2 hours recreational screen time


st.write("What are your screen habits?")
st.write("If you have a smartphone, access your average daily screen time through your device settings.")

phone_screen_time = float(input("Enter your daily smartphone screen time average in hours: "))

# Bar graph comparing user to averages
labels = ["Your Phone Use", "U.S. Average", "Worldwide Average"]
values = [phone_screen_time, us_average, world_average]

plt.bar(labels, values, color=['blue','red','green'])
plt.ylabel("Hours per day")
plt.title("Daily Screen Time Comparison")
st.pyplot(fig)


st.write("\nScreen time for recreation is appealing to many because it can feel relaxing.")
st.write("However, too much recreational screen time may be linked to negative health outcomes.")

guess = float(input("How many hours of recreational screen time per day do you think is the threshold for negative health outcomes? "))

if guess == negative_threshold:
    st.write("Precisely!")
elif guess < negative_threshold:
    st.write("Not quite — the threshold is a little higher.")
else:
    st.write("It is actually less than that.")

st.write("The threshold is about 2 hours per day.")
st.write("\nFurthermore:")
st.write("If excessive recreational screen time threshold is regularly exceeded, being physically active may not fully offset the negative health effects.")

st.write("\nScreen time is also unavoidable in many settings, such as work or school.")
non_leisure_screen_time = float(input("How many hours of unavoidable non-leisure screen time do you spend per day? "))


recreational_screen_time = ask_float("Enter your average daily recreational TV, video game, computer, and/or tablet screen time in hours (do not include smartphone): ")

total_screen_time = phone_screen_time + non_leisure_screen_time + recreational_screen_time

st.write(f"\nYour estimated total daily screen time is {total_screen_time:.2f} hours.")
st.write("Note: Total screen time is an approximation.")

# Second graph
labels = ["Phone Leisure\nScreen Time", "Other Leisure\nScreen Time", "Unavoidable\nScreen Time", "Total\nScreen Time"]
values = [phone_screen_time, recreational_screen_time, non_leisure_screen_time, total_screen_time]

plt.bar(labels, values, color=['cyan','magenta','yellow','red'])
plt.ylabel("Hours per day")
plt.title("Your Estimated Daily Screen Time")
st.pyplot(fig)


# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit


#creating functions 

def ask_float(prompt):
    """asking user to input a number. repeats until valid input is typed in"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            st.write("Please enter a number (e.g., 3.5)")


def ask_yes_no(prompt):
    """true for yes, false for no"""
    while True:
        answer = input(prompt + " ").lower().strip()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            st.write("Please enter yes or no.")


def show_bar_graph(labels, values, title, ylabel="Hours per day"):
    """Create a simple bar graph."""
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=20)
    plt.tight_layout()
    st.pyplot(fig)


def st.write_table(data, title):
    """st.write a pandas table with a title."""
    st.write("\n" + title)
    st.write("-" * len(title))
    df = pd.DataFrame(data)
    st.write(df.to_string(index=False))
    return df


#symptom checklist 

symptoms = [
    "difficulty sleeping",
    "anxiety",
    "depression",
    "eye strain or headaches",
    "neck, shoulder, or back pain",
    "difficulty focusing"
]

symptom_results = []

st.write("\nWhich of the following have you experienced after high-screen-time days?")

for symptom in symptoms:
    experienced = ask_yes_no(f"Have you experienced {symptom}? yes/no:")
    symptom_results.append({
        "Symptom": symptom,
        "User Experiences This?": "Yes" if experienced else "No"
    })

symptom_df = st.write_table(symptom_results, "Your Symptom Checklist")

number_of_symptoms = sum(row["User Experiences This?"] == "Yes" for row in symptom_results)

if number_of_symptoms == 0:
    st.write("\nWow, that's great! You may not be noticing obvious side effects right now.")
else:
    st.write("\nYou're not alone!")
    st.write("Excessive sedentary screen time has been associated with sleep problems, mental health challenges, eye strain, headaches, and body pain.")


# -----------------------------
# Section 3: Motivation / Continue Logic
# -----------------------------

st.write("\nSo... do you want to proceed and learn how to improve your quality of life and reduce these symptoms?")

wants_to_continue = ask_yes_no("Enter yes or no:")

if wants_to_continue:
    st.write("\nGreat :) let's continue!")
else:
    st.write("\nEven if you live an otherwise healthy, active lifestyle, excessive passive screen time may still affect long-term health.")
    st.write("Research suggests that physical activity may not fully erase the negative effects of high sedentary TV/screen time.")

    wants_to_continue = ask_yes_no("\nWhat about now? Do you want to learn how to make your life easier and healthier? yes/no:")

    if wants_to_continue:
        st.write("\nGreat :) let's continue!")
    else:
        st.write("\nOkay, that's fine.")
        st.write("Outside of screens, are there any habits you wish to change or begin?")
        st.write("The same behavior-change principles can apply to many habits.")

        st.write("\n1. No, my life is already perfect and I do not want to change anything.")
        st.write("2. I want to learn more.")

        choice = input("Enter 1 or 2: ").strip()

        if choice == "2":
            st.write("\nGreat :) let's continue!")
        else:
            st.write("\nOkay, well I guess you can stop reading this now...")
            st.write("But this is literally my research project, so it would be kind of boring if you ended it here.")

            st.write("\n1. Continue and learn")
            st.write("2. Stop program here")

            choice = input("Enter 1 or 2: ").strip()

            if choice == "1":
                st.write("\nGreat :) Let's continue!")
            else:
                st.write("\nProgram terminated.")
                raise SystemExit

st.write("\nDo you already incorporate any of the following screen-time reduction strategies?")
st.write("Type yes or no for each option.\n")

strategies = [
    "use app time limits",
    "disable non-essential notifications",
    "have a screen-free time of day, such as before bed",
    "keep your phone out of reach while studying or working",
]

used_strategies = []

for strategy in strategies:
    answer = input(f"Do you use {strategy}? ").lower()

    if answer == "yes":
        used_strategies.append(strategy)

st.write("\nYou currently use", len(used_strategies), "screen-time reduction strategies.")

if len(used_strategies) == 0:
    st.write("That's okay — this gives you a clear starting point.")
elif len(used_strategies) <= 2:
    st.write("Nice start! There is still room to add a few more supports.")
else:
    st.write("Great job — you already have several helpful strategies in place.")
# -----------------------------
# Section 4: Strategy Checklist
# -----------------------------

strategy_categories = {
    "Movement During Unavoidable Screen Time": [
        "standing desk",
        "walking pad",
        "under-desk pedal device",
        "taking movement breaks during work/school screen time"
    ],
    "Increasing Friction Against Recreational Screen Use": [
        "app time limits",
        "disabling non-essential notifications",
        "deleting or hiding distracting apps",
        "keeping phone away from bed",
        "creating screen-free zones"
    ],
    "Decreasing Friction for Physical Activity": [
        "placing workout equipment in visible areas",
        "watching TV only while walking/stretching",
        "using VR fitness or active video games",
        "planning non-screen hobbies in advance"
    ]
}

strategy_results = []
category_scores = {}

st.write("\nAre you interested in any of the following screen-time reduction strategies?")

for category, strategies in strategy_categories.items():
    st.write(f"\nCategory: {category}")
    used_count = 0

    for strategy in strategies:
        uses_strategy = ask_yes_no(f"Would you use this strategy: {strategy}? yes/no:")

        if uses_strategy:
            used_count += 1

        strategy_results.append({
            "Category": category,
            "Strategy": strategy,
            "Interested?": "Yes" if uses_strategy else "No"
        })

    category_scores[category] = used_count

st.write("\nSummary")

strategy_df = st.write_table(strategy_results, "Your Screen Time Strategy Checklist")


def show_donut_chart(labels, data, title):

    # Prevent errors if no strategies selected
    if sum(data) == 0:
        st.write("No strategies were selected, so no donut chart can be displayed.")
        return

    colors = ['#6BAED6', '#74C476', '#FDAE6B']

    # Slight "pop out" effect
    explode = [0.05]*len(data)

    plt.figure(figsize=(8,8))

    plt.pie(
        data,
        labels=labels,
        colors=colors,
        explode=explode,
        autopct='%1.1f%%',
        pctdistance=0.82
    )

    # Create donut hole
    centre_circle = plt.Circle((0,0),0.65,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.title(title)
    plt.tight_layout()
    st.pyplot(fig)

# -----------------------------
# Section 5: Personalized Recommendations
# -----------------------------

recommendations = []

for category, strategies in strategy_categories.items():
    used_in_category = category_scores[category]
    total_in_category = len(strategies)

    if used_in_category == 0:
        recommendation = "High priority: consider implementing at least one strategy from this category."
    elif used_in_category < total_in_category / 2:
        recommendation = "Moderate priority: you have selected some strategies, but could add more support."
    else:
        recommendation = "Strong area: you have selected several strategies here."

    recommendations.append({
        "Intervention Category": category,
        "Strategies": f"{used_in_category}/{total_in_category}",
    })

recommendation_df = st.write_table(recommendations, "Personalized Intervention Recommendations")

# -----------------------------
# Section 8: Final Summary
# -----------------------------

st.write("\nSummary")

strategy_df = st.write_table(strategy_results, "Your Screen Time Strategy Checklist")

show_donut_chart(
    list(category_scores.keys()),
    list(category_scores.values()),
    "Distribution of Screen-Time Strategies You're Interested In"
)

st.write("-------------")
st.write(f"Estimated total daily screen time: {total_screen_time:.2f} hours")
st.write(f"Estimated recreational screen time: {recreational_screen_time:.2f} hours")
st.write(f"Number of strategies of interest: {sum(category_scores.values())}")

st.write("\nYour strongest strategy category:")

strongest_category = max(category_scores, key=category_scores.get)
weakest_category = min(category_scores, key=category_scores.get)

st.write(f"Strongest: {strongest_category}")
st.write(f"Needs most improvement: {weakest_category}")

st.write("\nMain takeaway:")
st.write("The most effective approach is usually not one single strategy category.")
st.write("A stronger plan combines movement during unavoidable screen time, more friction against recreational screen use,")
st.write("and easier access to physical activity or active alternatives.")


# In[ ]:




