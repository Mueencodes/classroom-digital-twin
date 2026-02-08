import streamlit as st
from fpdf import FPDF
import sqlite3
from datetime import datetime
import pandas as pd
import altair as alt
# from PIL import Image

# ---- SQLite Database Setup ----
conn = sqlite3.connect("classroom_history.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    class TEXT,
    subject TEXT,
    engagement TEXT,
    efficiency REAL,
    health REAL
)
""")
conn.commit()

st.set_page_config(page_title="Classroom Digital Twin", layout="wide")

# -----------------------
# Sidebar Navigation
# -----------------------
page = st.sidebar.radio("Navigation", ["Home", "Insights", "Log", "About"])

# -----------------------
# Home / Portfolio Page
# -----------------------
if page == "Home":
    st.set_page_config(page_title="Classroom Digital Twin", layout="wide")
    
    # ---- Hero Section ----
    st.markdown("""
    <div style='text-align:center; padding:30px; background:linear-gradient(135deg, #0D1B2A, #1B263B);color:#f5f5f5; border-radius:8px'>
        <h1 style='font-size:50px'>📊 Classroom Digital Twin</h1>
        <p style='font-size:20px; max-width:700px; margin:auto;'>
        An AI-powered classroom simulation tool to monitor student engagement, teaching efficiency,
        and overall classroom health. Get actionable insights to optimize learning outcomes.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ---- Features Section ----
    st.markdown("### 🚀 Key Features")
    st.markdown("""
    <div style='display:flex; flex-wrap:wrap; gap:20px; justify-content:center;'>
        <div style='flex:1; min-width:220px; background:linear-gradient(135deg, #A8E6CF, #DCEDC1); padding:20px; border-radius:5px; text-align:center;box-shadow: 0 4px 8px rgba(0,0,0,0.1);transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.3)'>
            <h3>🎯 Student Engagement</h3>
            <p>Track participation levels and detect disengaged students.</p>
        </div>
        <div style='flex:1; min-width:220px; background:linear-gradient(135deg, #A8E6CF, #DCEDC1); padding:20px; border-radius:5px; text-align:center;box-shadow: 0 4px 8px rgba(0,0,0,0.1);transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.3)'>
            <h3>⚙️ Teaching Efficiency</h3>
            <p>Measure teacher effectiveness and lesson delivery.</p>
        </div>
        <div style='flex:1; min-width:220px; background:linear-gradient(135deg, #A8E6CF, #DCEDC1); padding:20px; border-radius:5px; text-align:center;box-shadow: 0 4px 8px rgba(0,0,0,0.1);transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.3)'>
            <h3>🩺 Classroom Health</h3>
            <p>Monitor environmental conditions like temperature & noise.</p>
        </div>
        <div style='flex:1; min-width:220px; background:linear-gradient(135deg, #A8E6CF, #DCEDC1); padding:20px; border-radius:5px; text-align:center;box-shadow: 0 4px 8px rgba(0,0,0,0.1);transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.3)'>
            <h3>🚨 Issue Detection</h3>
            <p>Identify learning or classroom problems instantly.</p>
        </div>
        <div style='flex:1; min-width:220px; background:linear-gradient(135deg, #A8E6CF, #DCEDC1); padding:20px; border-radius:5px; text-align:center;box-shadow: 0 4px 8px rgba(0,0,0,0.1);transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.3)'>
            <h3>🛠 Smart Suggestions</h3>
            <p>Get actionable tips to improve class performance.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # ---- Workflow / Flowchart Section ----
    st.markdown("### 🔁 How It Works")
    st.markdown("""
    <div style='display:flex; justify-content:center; align-items:center; gap:20px; flex-wrap:wrap;'>
        <div style='min-width:200px; background:linear-gradient(135deg, #cce0ff, #ffffff); padding:15px; border-radius:5px; text-align:center;box-shadow: 0 4px 8px rgba(0,0,0,0.1);transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.3)'>
            <h4>📝 Input Data</h4>
            <p>Class & Subject Details</p>
        </div>
        <div style='font-size:30px;'>↔</div>
        <div style='min-width:200px; background:linear-gradient(135deg, #cce0ff, #ffffff); padding:15px; border-radius:5px; text-align:center;box-shadow: 0 4px 8px rgba(0,0,0,0.1);transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.3)'>
            <h4>🏃 Run Simulation</h4>
            <p>Calculate Engagement, Efficiency, Health</p>
        </div>
        <div style='font-size:30px;'>↔</div>
        <div style='min-width:200px; background:linear-gradient(135deg, #cce0ff, #ffffff); padding:15px; border-radius:5px; text-align:center;box-shadow: 0 4px 8px rgba(0,0,0,0.1);transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.3)'>
            <h4>📊 View Metrics</h4>
            <p>Classroom Dashboard & Charts</p>
        </div>
        <div style='font-size:30px;'>↔</div>
        <div style='min-width:200px; background:linear-gradient(135deg, #cce0ff, #ffffff); padding:15px; border-radius:5px; text-align:center;box-shadow: 0 4px 8px rgba(0,0,0,0.1);transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.3)'>
            <h4>🔮 Trend Analysis</h4>
            <p>Learning Risk & Smart Suggestions</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # ---- About / Footer Section ----
    st.markdown("### ℹ️ About the Project")
    st.markdown("""
    **Classroom Digital Twin** is a simulation system designed to model classroom dynamics and provide actionable insights.
    
    **Main Goals:**
    - Measure engagement, efficiency, and health
    - Detect learning issues and environmental problems
    - Suggest improvements for better learning outcomes

    **Future Vision:** Live data integration, predictive analytics, multi-class dashboards, and richer interactive visualizations.
    """)
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #0D1B2A;
        color: white;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
        z-index: 100;
        font-family: Arial, sans-serif;
    }

    .footer-icons {
        position: fixed;
        bottom: 10px;
        right: 20px;
        z-index: 101;
    }

    .footer-icons a {
        margin-left: 10px;
        text-decoration: none;
    }

    .footer-icons img {
        width: 25px;
        height: 25px;
        filter: invert(100%);
        transition: transform 0.2s;
    }

    .footer-icons img:hover {
        transform: scale(1.2);
    }
    </style>

    <div class="footer">
        © 2026 Classroom Digital Twin All Rights Reserved | Created by <b>Mueen Shah<b>
    </div>

    <div class="footer-icons">
        <a href="https://github.com/Mueencodes" target="_blank">
            <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" alt="GitHub">
        </a>
        <a href="https://linkedin.com/in/mueenshah" target="_blank">
            <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg" alt="LinkedIn">
        </a>
        <a href="mailto:urfavakhi79@gmail.com" target="_blank">
            <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/gmail.svg" alt="Gmail">
        </a>
    </div>
    """, unsafe_allow_html=True)

# -----------------------
# Simulation Page
# -----------------------
elif page == "Insights":
    st.title("Classroom Simulation Dashboard")

    # Default Trend & Risk
    trend = "Not enough data"
    risk_level = "unknown"
    # ---- Inputs ----
    with st.sidebar.form("simulation_form"):
        st.header("Classroom Inputs")
        class_name = st.text_input("Class", "1st Year CS")
        subject = st.text_input("Subject", "ICT")
        subject_complexity = st.slider("Subject Complexity (0-10)", 0, 10, 7)
        temperature = st.number_input("Temperature (°C)", 0, 50, 25)
        noise_level = st.slider("Noise Level (0-10)", 0, 10, 5)
        participation = st.slider("Participation Level (0-10)", 0, 10, 7)
        teacher_speed = st.slider("Teacher Speed (0-10)", 0, 10, 6)


        # ---- Submit Button ----
        submitted = st.form_submit_button("Run Simulation")
    
    if submitted:
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

         # ---- Classroom Stability Score ----
        stability = (efficiency + health + (engagement_score * 5)) / 3
        stability = max(0, min(100, stability))

        if stability >= 80:
            stability_label = "Stable"
            stability_color = "#00C851"
            stability_icon = "🟢"
        elif stability >= 60:
            stability_label = "Moderate"
            stability_color = "#FFA500"
            stability_icon = "🟡"
        else:
            stability_label = "Unstable"
            stability_color = "#FF4B4B"
            stability_icon = "🔴"

        # ---- Learning Risk Predictor ----
        risk_score = 100 - ((efficiency + health + (engagement_score * 5)) / 3)
        risk_score = max(0, min(100, risk_score))

        if risk_score <= 30:
            risk_label = "Low Risk"
            risk_color = "#00C851"
            risk_icon = "🟢"
        elif risk_score <= 60:
            risk_label = "Medium Risk"
            risk_color = "#FFA500"
            risk_icon = "🟡"
        else:
            risk_label = "High Risk"
            risk_color = "#FF4B4B"
            risk_icon = "🔴"

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

        # ---- Save Simulation to Database ----
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("""
        INSERT INTO history (timestamp, class, subject, engagement, efficiency, health)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (timestamp, class_name, subject, engagement, efficiency, health))
        conn.commit()

         # ---- Display Metrics with Progress Bars ----
        st.subheader("📊 Latest Classroom Metrics")
        col1, col2, col3, col4, col5 = st.columns(5)

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
        with col4:
            st.markdown(f"<div style='background-color:#f0f0f0; padding:10px; border-radius:10px; text-align:center'>"
                        f"<h3>Stability Score</h3>"
                        f"<h2 style='color:{stability_color}'>{stability:.1f}% {stability_icon}</h2>"
                        f"<p><b>{stability_label}</b></p></div>", unsafe_allow_html=True)
            st.progress(int(stability))
        with col5:
            st.markdown(f"<div style='background-color:#f0f0f0; padding:10px; border-radius:10px; text-align:center'>"
                        f"<h3>Learning Risk</h3>"
                        f"<h2 style='color:{risk_color}'>{risk_score:.1f}% {risk_icon}</h2>"
                        f"<p><b>{risk_label}</b></p></div>", unsafe_allow_html=True)
            st.progress(int(risk_score))
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
# History Page
# -----------------------
elif page == "Log":
    st.title("📚 Simulation History")

    # ---- Clear Database Button ----
    if st.button("⚠️ Clear All Simulation History"):
        c.execute("DELETE FROM history")
        conn.commit()
        st.success("✅ All simulation history cleared!")

    # ---- Fetch & Display Historical Data ----
    c.execute("SELECT timestamp, class, subject, engagement, efficiency, health FROM history ORDER BY id ASC")
    rows = c.fetchall()

    if rows:
        df = pd.DataFrame(rows, columns=['Timestamp', 'Class', 'Subject', 'Engagement', 'Efficiency', 'Health'])
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        st.subheader("📝 Historical Data Table")
        st.dataframe(df)

        # ---- Last 10 Simulations Trend Graph ----
        df_last10 = df.tail(10)
        df_last10['EngagementNumeric'] = df_last10['Engagement'].map({'Low': 40, 'Medium': 70, 'High': 100})
        df_last10['CombinedScore'] = (df_last10['Efficiency'] + df_last10['Health'] + df_last10['EngagementNumeric']) / 3

        # Trend Calculation
        if df_last10['CombinedScore'].iloc[0] < df_last10['CombinedScore'].iloc[-1]:
            trend = "Improving"; risk_level = "Low"
        elif df_last10['CombinedScore'].iloc[0] > df_last10['CombinedScore'].iloc[-1]:
            trend = "Declining"; risk_level = "High"
        else:
            trend = "Stable"; risk_level = "Medium"

        st.subheader("🔮 Learning Trend Predictor (Last 10 Simulations)")
        if risk_level == "Low":
            st.success(f"🟢 Trend: {trend} → Learning Risk: LOW")
        elif risk_level == "Medium":
            st.warning(f"🟡 Trend: {trend} → Learning Risk: MEDIUM")
        else:
            st.error(f"🔴 Trend: {trend} → Learning Risk: HIGH")

        chart = alt.Chart(df_last10).transform_fold(
            ['EngagementNumeric', 'Efficiency', 'Health'],
            as_=['Metric', 'Value']
        ).mark_line(point=True).encode(
            x='Timestamp:T',
            y='Value:Q',
            color='Metric:N',
            tooltip=['Timestamp:T','Metric:N','Value:Q']
        ).properties(
            width=700,
            height=300,
            title="📈 Last 10 Simulations Metrics Trend"
        )
        st.altair_chart(chart, use_container_width=True)
    else:
        st.info("No simulation history found. Run some simulations first.")

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