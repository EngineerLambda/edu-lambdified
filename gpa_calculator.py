import streamlit as st
import time
from langchain_google_genai import GoogleGenerativeAI


template = """
You are an AI assistant for a student GPA calculator app, based on student's CGPA, give recommendations for both high performing and low
performing students, give words of encouragement to students who do not perform well, and known approaches to getting their grades up
Using these details:
cgpa: {gpa}/{expected}
""" 
llm = GoogleGenerativeAI(model="gemini-1.5-flash")

st.set_page_config(page_title="GpCalc by Lambda", page_icon="📙")

with st.container():
    st.write(
        """
    ### GPA/CGPA CALCULATOR
    ### This is a GPA calculator based on both 4.0 and 5.0 system
    """
    )

with st.expander("How to use?"):
    st.write(
        """
    1. Check the side bar on the left to select your GPA system, it is set to 5.0 system by default
    2. Select whether you want to calculate a fresh CGPA or you want to enter a previous CGPA with the previous number of units.
    3. If `Old` is selected (***skip this step otherwise***), enter the number of units from your previous CGPA and the CGPA value using the appropriate spaces provided.
    2. Fill in the number of courses you want to use in the calculation of your GPA, in the provided field
    3. select the unit and grade in the approproiate selection box provided
    4. Don't worry if you are not sure yet, you can always add a new field by clicking on the plus sign on the input field
    5. If you make any mistake while selecting either the unit or the grade, you can edit it 
    without losing the information previously provided for other courses, 
    makes it easy for you to do try and error with expected grades even before your results are out
    """
    )


with st.sidebar:
    system = st.radio("What is your preferred GPA system? ", options=["5.0", "4.0"])

    if system == "5.0":
        grade_dict = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}
        grades_array = ["A", "B", "C", "D", "E", "F"]
    else:
        grade_dict = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
        grades_array = ["A", "B", "C", "D", "F"]


def main():
    n_courses = st.number_input(
        "Enter the number of courses you offered", step=1, min_value=1, format="%i"
    )

    def positions(num):
        num_str = str(num)
        if len(num_str) >= 2 and num_str[-2] == "1":
            return str(num) + "th"
        else:
            if num_str[-1] == "1":
                num_str += "st"
            elif num_str[-1] == "2":
                num_str += "nd"
            elif num_str[-1] == "3":
                num_str += "rd"
            else:
                num_str += "th"
            return num_str

    total_points = 0
    total_unit = 0
    for i in range(1, 1 + int(n_courses)):
        col1, col2 = st.columns(spec=2, gap="medium")
        with col1:
            unit = st.selectbox(
                f"Select the unit of the {positions(i)} course", range(1, 7)
            )
        with col2:
            grades = st.selectbox("Select your grade", grades_array, key=i)
            grade_val = grade_dict[grades]
        point = unit * grade_val
        total_points += point
        total_unit += unit

    return total_points, total_unit


def get_class_5(val):
    if 4.5 <= val <= 5.0:
        st.balloons()
        return st.success("FIRST CLASS, KEEP IT UP", icon="🚀")
    elif 3.5 <= val <= 4.5:
        return st.success("SECOND CLASS (UPPER), KEEP IT UP", icon="🔥")
    elif 2.4 <= val <= 3.5:
        return st.warning("SECOND CLASS (LOWER), YOU CAN DO MORE", icon="💪")
    else:
        return st.error("KEEP ON GROWING, YOU WILL GET THERE SOON", icon="💪")


def get_class_4(val):
    if 3.5 <= val <= 4.0:
        st.balloons()
        return st.success("FIRST CLASS, KEEP IT UP", icon="🚀")
    elif 3.0 <= val <= 3.5:
        return st.success("SECOND CLASS (UPPER), KEEP IT UP", icon="🔥")
    elif 2.0 <= val <= 3.0:
        return st.warning("SECOND CLASS (LOWER), YOU CAN DO MORE", icon="💪")
    else:
        return st.error("KEEP ON GROWING, YOU WILL GET THERE SOON", icon="💪")


def bt(gp_spec):
    if st.button("CALCULATE"):
        with st.spinner("Crunching numbers ..."):
            time.sleep(2)
            st.write(f"Your GPA is {gp_spec:.2f}")
            if system == "5.0":
                get_class_5(gp_spec)
            else:
                get_class_4(gp_spec)


new_choice = st.selectbox(
    label="Do you want to calculate a new gp, or merge with old cgpa?",
    options=["New", "Old"],
)
if new_choice == "New":
    points, units = main()
    gp_new = points / units
    final_temp = template.format(gpa=gp_new, expected=system)
    bt(gp_new)
    
    with st.expander("## AI Summary"):
        ai_summary = llm(final_temp)   
        st.write(ai_summary)
    
else:
    max_val = 5.0 if system == "5.0" else 4.0
    old_input = st.number_input(
        label="Enter your previous cgpa", step=1.0, max_value=max_val
    )
    old_units = st.number_input(
        label="Enter your previous total number of units", step=1
    )
    new_total, new_units = main()

    old_total = round(old_input * old_units)

    cumm_total = old_total + new_total
    cumm_units = old_units + new_units

    final_cgpa = cumm_total / cumm_units
    final_temp = template.format(gpa=final_cgpa, expected=system)
    bt(final_cgpa)
    
    with st.expander("## AI Summary"):
        ai_summary = llm(final_temp)   
        st.write(ai_summary)

    