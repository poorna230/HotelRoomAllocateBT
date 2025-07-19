# 🏨 Hotel Room Allocation App

## 📌 Overview
A web app built with Streamlit that automatically assigns hotel rooms to guests based on their preferences using a First-Come, First-Served (FCFS) approach.

## 🚀 Features
- Upload an Excel file with `Rooms` and `Guests` sheets
- Automatic room allocation using a simple logic
- View uploaded and allocated data as interactive tables
- Download results as a new Excel file
- Clean and user-friendly interface

## 📂 Excel File Format

**Sheet 1: Rooms**
| room_id | room_type |
|---------|-----------|
| 101     | Deluxe    |
| 102     | Standard  |

**Sheet 2: Guests**
| guest_id | requested_type |
|----------|----------------|
| G01      | Standard        |
| G02      | Deluxe          |

## 🛠 Requirements

Install necessary Python libraries with:

```bash
pip install streamlit pandas openpyxl xlsxwriter
