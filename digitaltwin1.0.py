import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="Classroom Digital Twin", layout="wide")

# -----------------------
# Sidebar Navigation
# -----------------------
page = st.sidebar.radio("Navigation", ["Home", "Simulation", "About"])

# -----------------------
# Home Page
# -----------------------
if page == "Home":
    st.title("📊 Classroom Digital Twin")
    st.markdown("""
**Welcome to Classroom Digital Twin!**  

This intelligent system simulates classroom conditions and predicts:

- 🎯 Student Engagement  
- ⚙️ Teaching Efficiency  
- 🩺 Classroom Health Index  
- 🚨 Issues Detection  
- 🛠 Smart Suggestions  

Use the sidebar to navigate to **Simulation** and start analyzing classroom conditions.
    """)
    # st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)

# -----------------------
# Simulation Page
# -----------------------
elif page == "Simulation":
    st.title("Classroom Simulation Dashboard")

    # ---- Inputs ----
    st.sidebar.header("Classroom Inputs")
    class_name = st.sidebar.text_input("Class", "1st Year CS")
    subject = st.sidebar.text_input("Subject", "ICT")
    subject_complexity = st.sidebar.slider("Subject Complexity (0-10)", 0, 10, 7)
    temperature = st.sidebar.number_input("Temperature (°C)", 0, 50, 25)
    noise_level = st.sidebar.slider("Noise Level (0-10)", 0, 10, 5)
    participation = st.sidebar.slider("Participation Level (0-10)", 0, 10, 7)
    teacher_speed = st.sidebar.slider("Teacher Speed (0-10)", 0, 10, 6)

    # ---- Engagement Calculation ----
    engagement_score = participation + teacher_speed
    if noise_level >= 8: engagement_score -= 3
    elif noise_level <= 3: engagement_score += 2
    if subject_complexity >= 8: engagement_score -= 3
    elif subject_complexity <= 3: engagement_score += 2
    if temperature < 18 or temperature > 30: engagement_score -= 2

    if engagement_score <= 8:
        engagement = "Low"; engagement_factor = 0.6; eng_color = "#FF4B4B"; eng_icon = "😴"
    elif engagement_score <= 14:
        engagement = "Medium"; engagement_factor = 0.8; eng_color = "#FFA500"; eng_icon = "🙂"
    else:
        engagement = "High"; engagement_factor = 1.0; eng_color = "#00C851"; eng_icon = "💡"

    # ---- Efficiency Calculation ----
    base_efficiency = teacher_speed * 10
    efficiency = base_efficiency * engagement_factor
    if temperature < 18 or temperature > 30: efficiency -= 10
    if noise_level >= 8: efficiency -= 10
    if subject_complexity >= 8 and participation <= 4: efficiency -= 10
    efficiency = max(0, min(100, efficiency))

    # ---- Classroom Health Index ----
    health = (efficiency + engagement_score * 5)/2
    health = max(0, min(100, health))

    # ---- Issue Detection ----
    issues = []
    if noise_level >= 8: issues.append("High Noise Level")
    if temperature < 18 or temperature > 30: issues.append("Uncomfortable Temperature")
    if subject_complexity >= 8 and participation <= 4: issues.append("Students overloaded by subject complexity")
    if teacher_speed >= 8 and participation <= 4: issues.append("Teaching speed too fast")
    if participation <= 3: issues.append("Low student participation")

    # ---- Smart Suggestions ----
    suggestions = []
    for issue in issues:
        if "Noise" in issue: suggestions.append("Reduce classroom noise, adjust seating, or apply attention activities.")
        if "Temperature" in issue: suggestions.append("Improve ventilation, fan usage, or give a short break.")
        if "complexity" in issue: suggestions.append("Simplify explanation and use real-life examples.")
        if "speed" in issue: suggestions.append("Slow down teaching and recap important points.")
        if "participation" in issue: suggestions.append("Encourage discussion and interactive questioning.")

    # ---- Teaching Tip ----
    if subject_complexity <= 3: teaching_tip = "Normal pace is fine, minimal examples needed."
    elif subject_complexity <= 7: teaching_tip = "Use interactive examples and check understanding."
    else: teaching_tip = "Slow pace, multiple examples, short quizzes recommended."

    # ---- Display Metrics with Progress Bars ----
    st.subheader("📊 Classroom Metrics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"<div style='background-color:#f0f0f0; padding:10px; border-radius:10px; text-align:center'>"
                    f"<h3 style='color:{eng_color}'>Engagement</h3>"
                    f"<h2>{engagement} {eng_icon}</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='background-color:#f0f0f0; padding:10px; border-radius:10px; text-align:center'>"
                    "<h3>Efficiency (%)</h3></div>", unsafe_allow_html=True)
        st.metric("", f"{efficiency:.1f}%")
        st.progress(int(efficiency))
    with col3:
        st.markdown("<div style='background-color:#f0f0f0; padding:10px; border-radius:10px; text-align:center'>"
                    "<h3>Health Index (%)</h3></div>", unsafe_allow_html=True)
        st.metric("", f"{health:.1f}%")
        st.progress(int(health))

    st.divider()

    # ---- Issues ----
    st.subheader("🚨 Detected Issues")
    if issues:
        for idx, issue in enumerate(issues, start=1): st.error(f"{idx}. {issue}")
    else:
        st.success("No major issues detected.")

    # ---- Suggestions ----
    st.subheader("🛠 Smart Suggestions")
    if suggestions:
        for tip in suggestions: st.info(tip)
    else:
        st.success("Excellent conditions!")

    # ---- Classroom Mood ----
    st.subheader("📋 Classroom Mood")

    if engagement == "High" and efficiency >= 80:
        mood_text = "Excellent Class: Students are highly engaged and learning is very effective."
        st.success("🟢 " + mood_text)

    elif engagement == "High" and efficiency < 80:
        mood_text = "Fun but Inefficient: Students are active, but learning output is low."
        st.warning("🟡 " + mood_text)

    elif engagement == "Medium" and efficiency >= 80:
        mood_text = "Silent but Smart: Students are less expressive but learning effectively."
        st.info("🔵 " + mood_text)

    elif engagement == "Medium" and efficiency < 80:
        mood_text = "Average Class: Moderate engagement and learning."
        st.warning("🟡 " + mood_text)

    elif engagement == "Low" and efficiency >= 80:
        mood_text = "Rote Learning Detected: Learning is happening, but interest is low."
        st.info("🟣 " + mood_text)

    else:
        mood_text = "Critical Condition: Low engagement and poor learning."
        st.error("🔴 " + mood_text)
    st.caption("System-generated classroom mood based on engagement & efficiency metrics.")

    # ---- Teaching Tip ----
    st.subheader("💡 Teaching Tip Based on Subject Complexity")
    st.info(teaching_tip)

    # ---- PDF Report ----
    st.subheader("💾 Download Simulation Report as PDF")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Classroom Digital Twin Report", ln=True, align='C')
    pdf.ln(5)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 8, f"""
Class: {class_name}
Subject: {subject}

Inputs:
- Subject Complexity: {subject_complexity}
- Temperature: {temperature}°C
- Noise Level: {noise_level}
- Participation Level: {participation}
- Teacher Speed: {teacher_speed}

Outputs:
- Engagement: {engagement}
- Efficiency: {efficiency:.1f}%
- Health Index: {health:.1f}%

Detected Issues: {', '.join(issues) if issues else 'None'}
Smart Suggestions: {', '.join(suggestions) if suggestions else 'None'}
Teaching Tip: {teaching_tip}
Classroom Mood: {mood_text}
""")
    pdf_output = pdf.output(dest='S').encode('latin1')

    st.download_button(
        label="Download PDF Report",
        data=pdf_output,
        file_name="Classroom_DigitalTwin_Report.pdf",
        mime='application/pdf'
    )

# -----------------------
# About Page
# -----------------------
elif page == "About":
    st.title("ℹ️ About Classroom Digital Twin")
    st.markdown("""
**Classroom Digital Twin** is an AI-inspired simulation system that models real classroom conditions.

### Objectives:
- Measure classroom engagement
- Calculate teaching efficiency
- Evaluate overall classroom health
- Detect learning issues
- Provide smart improvement suggestions
- Offer teaching tips based on subject complexity

The system simulates class behavior and gives improvement suggestions without real-time sensors.

Future: Live data, predictive AI, historical analytics, multi-class dashboards.
""")