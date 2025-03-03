import streamlit as st

# Define the subjects for each branch and common subjects
subjects = {
    "Computer Science": {
        "Programming": 10,
        "Data Structures & Algorithms": 10,
        "Operating Systems": 9,
        "Computer Networks": 9,
        "Database Management Systems": 9,
        "Software Engineering": 8,
        "Web Technologies": 7,
        "Compiler Design": 7,
        "Object-Oriented Programming": 9,
        "Cryptography & Network Security": 8,
        "Software Testing": 7,
        "Data Mining & Data Warehousing": 8,
        "Business Communication & Ethics": 6,
        "Business Analytics": 7,
        "Digital Marketing": 5,
    },
    "Artificial Intelligence": {
        "Artificial Intelligence": 10,
        "Machine Learning": 10,
        "Deep Learning": 9,
        "Data Science & Analytics": 9,
        "Natural Language Processing": 8,
        "Neural Networks": 9,
        "Reinforcement Learning": 8,
        "Computer Vision": 8,
        "Linear Algebra for ML": 9,
        "Data Visualization": 9,
        "Data Mining & Data Warehousing": 9,
    },
    "Electrical Engineering": {
        "Circuit Theory": 8,
        "Digital Logic Design": 9,
        "Analog & Digital Electronics": 9,
        "Signals & Systems": 8,
        "Microprocessors & Microcontrollers": 9,
        "Communication Systems": 8,
        "VLSI Design": 7,
        "Antennas & Wave Propagation": 7,
        "Embedded Systems": 9,
        "Optical Communication": 7,
        "IoT & Wireless Sensor Networks": 8,
        "Electrical Circuits": 8,
        "Control Systems": 9,
        "Power Systems": 8,
        "Electrical Machines": 8,
        "Power Electronics": 9,
        "Digital Signal Processing": 9,
        "High Voltage Engineering": 7,
        "Renewable Energy Systems": 8,
        "Industrial Automation": 8,
    },
    "Mechanical Engineering": {
        "Engineering Mechanics": 9,
        "Strength of Materials": 9,
        "Thermodynamics": 9,
        "Fluid Mechanics": 8,
        "Manufacturing Processes": 8,
        "Heat & Mass Transfer": 9,
        "Machine Design": 9,
        "Robotics": 8,
        "CAD/CAM": 9,
        "Automotive Engineering": 7,
        "Industrial Engineering": 8,
    },
    "Civil Engineering": {
        "Structural Analysis": 9,
        "Surveying": 8,
        "Fluid Mechanics": 8,
        "Geotechnical Engineering": 9,
        "Construction Materials": 8,
        "Transportation Engineering": 8,
        "Environmental Engineering": 8,
        "Hydrology & Water Resources": 7,
        "Building Design & Architecture": 8,
        "Earthquake Engineering": 8,
    },
}

common_subjects = {
    "Engineering Mathematics": 10,
    "Engineering Physics": 8,
    "Engineering Chemistry": 6,
    "Programming": 9,
    "Data Structures & Algorithms": 8,
    "Probability & Statistics": 10,
    "Basic Electrical Engineering": 7,
    "Engineering Drawing": 7,
    "Engineering Economics & Financial Management": 6,
}

# Streamlit App
st.title("Subject Selection App")

# Step 1: Select Branch
branch = st.selectbox("Select your branch:", list(subjects.keys()))

# Step 2: Display Common Subjects
st.header("Common Subjects")
common_selections = {}
for subject, rating in common_subjects.items():
    common_selections[subject] = st.checkbox(f"{subject} ({rating}/10)")

# Step 3: Display Branch-Specific Subjects
st.header(f"{branch} Subjects")
branch_selections = {}
for subject, rating in subjects[branch].items():
    branch_selections[subject] = st.checkbox(f"{subject} ({rating}/10)")

# Step 4: Show Selected Subjects
if st.button("Submit"):
    st.header("Selected Subjects")
    st.subheader("Common Subjects:")
    for subject, selected in common_selections.items():
        if selected:
            st.write(f"- {subject}")

    st.subheader(f"{branch} Subjects:")
    for subject, selected in branch_selections.items():
        if selected:
            st.write(f"- {subject}")import streamlit as st

# Define the subjects for each branch and common subjects
subjects = {
    "Computer Science": {
        "Programming": 10,
        "Data Structures & Algorithms": 10,
        "Operating Systems": 9,
        "Computer Networks": 9,
        "Database Management Systems": 9,
        "Software Engineering": 8,
        "Web Technologies": 7,
        "Compiler Design": 7,
        "Object-Oriented Programming": 9,
        "Cryptography & Network Security": 8,
        "Software Testing": 7,
        "Data Mining & Data Warehousing": 8,
        "Business Communication & Ethics": 6,
        "Business Analytics": 7,
        "Digital Marketing": 5,
    },
    "Artificial Intelligence": {
        "Artificial Intelligence": 10,
        "Machine Learning": 10,
        "Deep Learning": 9,
        "Data Science & Analytics": 9,
        "Natural Language Processing": 8,
        "Neural Networks": 9,
        "Reinforcement Learning": 8,
        "Computer Vision": 8,
        "Linear Algebra for ML": 9,
        "Data Visualization": 9,
        "Data Mining & Data Warehousing": 9,
    },
    "Electrical Engineering": {
        "Circuit Theory": 8,
        "Digital Logic Design": 9,
        "Analog & Digital Electronics": 9,
        "Signals & Systems": 8,
        "Microprocessors & Microcontrollers": 9,
        "Communication Systems": 8,
        "VLSI Design": 7,
        "Antennas & Wave Propagation": 7,
        "Embedded Systems": 9,
        "Optical Communication": 7,
        "IoT & Wireless Sensor Networks": 8,
        "Electrical Circuits": 8,
        "Control Systems": 9,
        "Power Systems": 8,
        "Electrical Machines": 8,
        "Power Electronics": 9,
        "Digital Signal Processing": 9,
        "High Voltage Engineering": 7,
        "Renewable Energy Systems": 8,
        "Industrial Automation": 8,
    },
    "Mechanical Engineering": {
        "Engineering Mechanics": 9,
        "Strength of Materials": 9,
        "Thermodynamics": 9,
        "Fluid Mechanics": 8,
        "Manufacturing Processes": 8,
        "Heat & Mass Transfer": 9,
        "Machine Design": 9,
        "Robotics": 8,
        "CAD/CAM": 9,
        "Automotive Engineering": 7,
        "Industrial Engineering": 8,
    },
    "Civil Engineering": {
        "Structural Analysis": 9,
        "Surveying": 8,
        "Fluid Mechanics": 8,
        "Geotechnical Engineering": 9,
        "Construction Materials": 8,
        "Transportation Engineering": 8,
        "Environmental Engineering": 8,
        "Hydrology & Water Resources": 7,
        "Building Design & Architecture": 8,
        "Earthquake Engineering": 8,
    },
}

common_subjects = {
    "Engineering Mathematics": 10,
    "Engineering Physics": 8,
    "Engineering Chemistry": 6,
    "Programming": 9,
    "Data Structures & Algorithms": 8,
    "Big Data Technologies": 8,
    "Cloud Computing": 8,
    "Cyber Security": 8,
    "Blockchain Technology": 7,
    "IoT (Internet of Things)": 7,
    "Introduction to Artificial Intelligence": 8,
    "Probability & Statistics": 10,
    "Basic Electrical Engineering": 7,
    "Engineering Drawing": 7,
    "Engineering Economics & Financial Management": 6,
}

# Streamlit App
st.title("Subject Selection App")

# Step 1: Select Branch
branch = st.selectbox("Select your branch:", list(subjects.keys()))

# Step 2: Display Common Subjects
st.header("Common Subjects")
common_selections = {}
for subject, rating in common_subjects.items():
    common_selections[subject] = st.checkbox(f"{subject} ({rating}/10)")

# Step 3: Display Branch-Specific Subjects
st.header(f"{branch} Subjects")
branch_selections = {}
for subject, rating in subjects[branch].items():
    branch_selections[subject] = st.checkbox(f"{subject} ({rating}/10)")

# Step 4: Show Selected Subjects
if st.button("Submit"):
    st.header("Selected Subjects")
    st.subheader("Common Subjects:")
    for subject, selected in common_selections.items():
        if selected:
            st.write(f"- {subject}")

    st.subheader(f"{branch} Subjects:")
    for subject, selected in branch_selections.items():
        if selected:
            st.write(f"- {subject}")
