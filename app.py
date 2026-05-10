import streamlit as st
import mysql.connector

# --- DATABASE CONNECTION ---
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # change to your MySQL username
        password="password",  # change to your MySQL password
        database="gaming_db"
    )

# --- BACKEND FUNCTIONS ---
def fetch_tournaments():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tournaments")
    data = cursor.fetchall()
    conn.close()
    return data

def fetch_tournament_options():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM tournaments")
    results = cursor.fetchall()
    conn.close()
    return {row['name']: row['id'] for row in results}

def register_player(player_name, email, tournament_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO players (player_name, email, tournament_id) VALUES (%s, %s, %s)"
    cursor.execute(query, (player_name, email, tournament_id))
    conn.commit()
    conn.close()

def fetch_registrations():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT players.player_name, players.email, tournaments.name AS tournament
        FROM players
        JOIN tournaments ON players.tournament_id = tournaments.id
    """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

# --- FRONTEND ---
st.title("🎮 Gaming Tournament Portal")
menu = ["View Tournaments", "Register Player", "Admin Dashboard"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "View Tournaments":
    st.subheader("Available Tournaments")
    st.table(fetch_tournaments())

elif choice == "Register Player":
    st.subheader("Join a Tournament")
    options = fetch_tournament_options()
    with st.form("reg_form"):
        name = st.text_input("Player Name")
        email = st.text_input("Email")
        tournament = st.selectbox("Select Tournament", list(options.keys()))
        if st.form_submit_button("Register Now"):
            register_player(name, email, options[tournament])
            st.success(f"Registered {name} for {tournament}!")

elif choice == "Admin Dashboard":
    st.subheader("All Registrations")
    st.table(fetch_registrations())
