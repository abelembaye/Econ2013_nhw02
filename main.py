import pdfkit
#path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe' #comment this line when deploying in streamlit
#config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf) #comment this line when deploying in streamlit
import os
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(layout="centered", page_icon="", page_title=" HW02")
st.title("Econ 2013 News Analysis HW02")

# Load HTML template
env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())

# here the template is directly in the main .py file which is not ideal
template = env.get_template("template2.html")
st.write("Answer the following questions based on the assignment post on Blackboard:")
form = st.form("template_form")

student_name = form.text_input("Full NAME", placeholder="John Doe")
#q01 = form.text_area(label="One line answer:", height=200, max_chars=500, placeholder="No place like Economics!")
q01=form.text_input("Q1. ", placeholder="one line answer to q1", key="q01", max_chars=100)
q02=form.text_input("Q2. ", placeholder="one line answer to q2", key="q02", max_chars=100)
q03=form.text_input("Q3. ", placeholder="one line answer to q3", key="q03", max_chars=100)
q04=form.text_input("Q4. ", placeholder="one line answer  to q4", key="q04", max_chars=100)
# Handle multiple image uploads

image_base64_list = []
for i in range(1):  # Change '2' to the number of images you want the user to upload
    uploaded_file = form.file_uploader(f"Q{i+5}.1 Upload Image {i+1}", type=["png", "jpg", "jpeg"], key=f"q{i+1}")
    if uploaded_file is not None:
        # Read the image
        image = Image.open(uploaded_file)
        # Convert image to base64 string
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        image_base64_list.append(image_base64)        
q05_2=form.text_input("Q5.2 ", placeholder="one line answer  to q5.2", key="q05.2", max_chars=100)
q05_3=form.text_input("Q5.3 ", placeholder="one line answer  to q5.3", key="q05.3", max_chars=100)
q05_4=form.text_input("Q5.4 ", placeholder="one line answer  to q5.4", key="q05.4", max_chars=100)
submit = form.form_submit_button("Generate PDF")

if submit:
    # Render the HTML template
    html = template.render(
        student_name=student_name,
        #course="Report Generation in Streamlit",  # You can update the course name here
        #date=date.today().strftime("%B %d, %Y"),
        #grade="97",  # You can update the grade here
        q01=q01,
        q02=q02 ,
        q03=q03 ,
        q04=q04 ,
        image_base64_list=image_base64_list,
        q05_2=q05_2,
        q05_3=q05_3,
        q05_4=q05_4,

    )

   # pdf = pdfkit.from_string(html, configuration=config)
    pdf = pdfkit.from_string(html , False) # use this one when deploying in streamlit
    st.balloons()

    st.success("🎉 Your PDF file has been generated! you can  download it by clicking the below button to save it and submit it in gradescope assignment!")
    st.download_button(
        "⬇️ Download pdf",
        data=pdf,
        file_name="AssignX.pdf",
        mime="application/octet-stream",
    )

#This file uses the virt env at
# conda deactivate
# ../venv4pdfgen/Scripts/activate.ps1
# streamlit run ./nhw01.py
