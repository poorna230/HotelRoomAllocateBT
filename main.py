import streamlit as st
import pandas as pd
from io import BytesIO

# Room and Guest Classes
class Room:
    def __init__(self, room_id, room_type, is_available=True):
        self.room_id = room_id
        self.room_type = room_type
        self.is_available = is_available

class GuestRequest:
    def __init__(self, guest_id, requested_type):
        self.guest_id = guest_id
        self.requested_type = requested_type

# FCFS Allocation (modified from backtracking)
def assign_rooms(rooms, guest_requests):
    allocation = {}
    for request in guest_requests:
        for room in rooms:
            if room.is_available and room.room_type == request.requested_type:
                room.is_available = False
                allocation[request.guest_id] = room.room_id
                break  # Move to next guest after assigning one room
        if all(not room.is_available for room in rooms):
            break
    return allocation if allocation else None

# Streamlit UI
def main():
    st.set_page_config(page_title="Hotel Room Allocation", layout="centered")
    st.title("🏨 Hotel Room Allocation using FCFS")

    uploaded_file = st.file_uploader("📁 Upload Excel File with Rooms & Guests", type=["xlsx"])

    if uploaded_file:
        try:
            xls = pd.ExcelFile(uploaded_file)
            df_rooms = pd.read_excel(xls, sheet_name="Rooms")
            df_guests = pd.read_excel(xls, sheet_name="Guests")

            st.subheader("📌 Uploaded Room Data")
            st.dataframe(df_rooms)

            st.subheader("📌 Uploaded Guest Data")
            st.dataframe(df_guests)

            # Parse data into objects
            rooms = [Room(row['room_id'], row['room_type']) for _, row in df_rooms.iterrows()]
            guests = [GuestRequest(row['guest_id'], row['requested_type']) for _, row in df_guests.iterrows()]

            if st.button("🚀 Allocate Rooms"):
                with st.spinner("Allocating rooms based on FCFS..."):
                    result = assign_rooms(rooms, guests)

                st.subheader("✅ Allocation Result")
                if result:
                    df_result = pd.DataFrame(list(result.items()), columns=["Guest ID", "Assigned Room"])
                    st.dataframe(df_result)

                    # Download button
                    output = BytesIO()
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        df_result.to_excel(writer, index=False, sheet_name="Allocation")
                    output.seek(0)

                    st.download_button(
                        "📥 Download Allocation",
                        data=output,
                        file_name="room_allocation.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                else:
                    st.warning("No valid room allocation could be found.")
        except Exception as e:
            st.error(f"Error reading Excel file: {e}")

if __name__ == "__main__":
    main()
