import streamlit as st
from supabase import create_client, Client
import pandas as pd

st.title("Events List")

# Supabase credentials
SUPABASE_URL = 'https://cqgrvyatmwgbyqbxzvew.supabase.co'  # Replace with your Supabase URL
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxZ3J2eWF0bXdnYnlxYnh6dmV3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc0NTE5OTksImV4cCI6MjA1MzAyNzk5OX0.GNJUamMMz78VBD91-rEjHKt9gVUFD_VgootE4WqaGdI'  # Replace with your Supabase API Key

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Dropdown selection
a = st.selectbox("Select the Event", [
    "W - Chatbots and Beyond: Create GenAI Apps with RAG",
    "W - ASIC Digital Design Flow using HDL",
    "W - IoT Integrated Embedded systems for Next - Gen Smart Grid Technologies",
    "NTE - Memory Maze",
    "W - Predictive Analytics - Forecasting Through Visualizations",
    "NTE - Get SHERLOCKED",
    "W - CyberSec Bootcamp: Mastering Ethical Hacking and Security Essentials",
    "W - Design a humanoid Robot - A Fun Learning experience",
    "NTE - IPL Auction",
    "W - Unleashing the Power of Generative AI and Intelligent Agents: Transforming the Future",
    "NTE - Melody Makers",
    "W - Multi modal AI System for Autonomous diagnosis",
    "W - RTPCR",
    "NTE - Tune Quest",
    "W - Drone Dynamics: Master the Art of Flying and Innovation",
    "W - Design Sprint: Crafting Intuitive UI/UX and Innovative Products",
    "TE - UXPERIENCE XPLOSION",
    "TE - DECODEX",
    "TE - BROKE TO BILLIONAIRE",
    "W - Rocketry and Model Rocket Launch",
    "W - Tiny ML in Health care Systems",
    "TE - BIOCANVAS",
    "NTE - Face To Face",
    "TE - VIRTUAL TRADING",
    "TE - TECH TANK",
    "W - Insights Unleashed: Modern Data Visualization and Storytelling",
    "TE - SOCIOPRENEUR",
    "NTE - Brain Escape Room",
    "NTE - Tamil Odu Vilayadu",
    "Beat the Street : Feel the Pulse Own The Street",
    "TE - CRAFT CLASH",
    "TE - CRYPTIC HUNT",
    "NTE - Water Rocketry",
    "NTE - Pixel Perfection",
    "NTE - Mic Masters",
    "TE - DIGITAL DAVINCI",
    "TE - PROMPTFORGE",
    "TE - B-MERGE 1.0",
    "TE - SITE REVAMPX",
    "TE - CODECRAFT CARNIVAL",
    "TE - CODE CRACKING",
    "NTE - Thread Canvas",
    "NTE - Reel-o-Mania",
    "W - The Chemistry of Clean Energy: Powering Tomorrow",
    "NTE - Edible Artistry",
    "NSE banner - Trading Fundamental and technical workshop",
    "TE - CIRCUIT SURGE",
    "TE - VOLT-WARRIORS",
    "Brainwave Entrepreneurial Workshop",
    "Translation Studies",
    "W - Smart Cities towards Sustainable Development Goals",
    "TE - POSTERVERSE",
    "Chorus Clash : The Ultimate Group Singing Show",
    "INNO PAPERS",
    "NTE - E-Sports",
    "NTE - Squid Game",
    "NTE - E-Sports",
    "TE - CODECRAFT CARNIVAL",
    "NTE - Photo Scavenger Hunt",
    "TE - ROBO ROUTE",
    "TE - SMART AUDITOR",
    "TE - MYSTERY BOX",
    "NTE - Tamil Odu Vilayadu",
    "TE - BYTE BREAKERS",
    "TE - CUBE CONTEST",
    "NTE - Family Feud",
    "NTE - Speed Pictionary",
    "TE - Mind Maze Escapade",
    "TE - CASE CLASH: THE ULTIMATE BUSINESS SHOWDOWN",
    "TE - PROMPTFORGE",
    "NTE - Checkmate",
    "TE - FETCHING FORTUNES",
    "TE - CAD CRAZE",
    "INNO PAPERS",
    "TE - FIRELESS COOKING",
    "NTE - Ink and Insights",
    "NTE - Model a Musing",
    "NTE - Turn Into Art",
    "NTE - Nail Tales",
    "Cine Bites: Savor The Art Of Short Films",
    "PROJECT HORIZON",
    "TE - SPARK-O-MANIA",
    "TE - CULINARY KING",
    "NTE - Logo Lab",
    "TE - BLOGSPHERE",
    "TE - BIZLEADER",
    "TE - GRAPHICRAFT",
    "TE - FINIS CRISIS",
    "NTE - Pixel Perfection",
    "MBA Poster Presentation",
    "W - Rocketry and Model Rocket Launch",
    "W - Multi modal AI System for Autonomous diagnosis",
    "NTE - Brain Escape Room",
    "TE - CIRCUIT SURGE",
    "NTE - Tune Quest",
    "TE - BROKE TO BILLIONAIRE"
])

# Fetch Data on Button Click
if st.button("Fetch"):
    try:
        # Fetch participants where the selected event is in any column and payment is successful
        query = (
            supabase.table("Participants")
            .select("Name, Email, Phone")  # Selecting specific columns
            .or_(
                f"Event_1_Day3.eq.{a},"
                f"Event_2_Day3.eq.{a},"
                f"Event_3_Day3.eq.{a},"
                f"Event_4_Day3.eq.{a},"
                f"Event_1_Day4.eq.{a}"
            )
            .eq("Payment", "Successful")  # Correct way to filter where Payment is "Successful"
            .limit(None)  # No limit on fetched rows
            .execute()
        )

        # Convert response to DataFrame
        if query.data:
            df = pd.DataFrame(query.data)
            st.subheader(f"Count of the Event: {len(df)}")
            st.dataframe(df)  # Display in Streamlit
        else:
            st.warning(f"No participants found for '{a}' with successful payment.")

    except Exception as e:
        st.error(f"Error fetching data: {e}")
