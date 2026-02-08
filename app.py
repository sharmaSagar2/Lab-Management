from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
import os
from datetime import datetime
from datetime import time as dt_time

app = Flask(__name__)

# Use absolute path for data folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, 'data')
app.config['UPLOAD_FOLDER'] = DATA_FOLDER

# Ensure data folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

EXCEL_FILE = os.path.join(app.config['UPLOAD_FOLDER'], 'lab_data.xlsx')

def is_time_in_slot(current_time, time_slot_str):
    """Check if current time falls within a time slot"""
    try:
        # Parse time slot string like "09:00–11:00" or "09:00-11:00"
        times = time_slot_str.replace('–', '-').split('-')
        if len(times) != 2:
            return False
        
        start_time_str = times[0].strip()
        end_time_str = times[1].strip()
        
        # Parse times
        start_time = datetime.strptime(start_time_str, '%H:%M').time()
        end_time = datetime.strptime(end_time_str, '%H:%M').time()
        
        # Check if current time is within the slot
        return start_time <= current_time <= end_time
    except Exception as e:
        print(f"Error parsing time slot '{time_slot_str}': {e}")
        return False

def load_data():
    """Load data from Excel file"""
    print(f"DEBUG: Attempting to load from: {EXCEL_FILE}")
    print(f"DEBUG: File exists: {os.path.exists(EXCEL_FILE)}")
    if not os.path.exists(EXCEL_FILE):
        return None
    try:
        df = pd.read_excel(EXCEL_FILE)
        print(f"DEBUG: Successfully loaded {len(df)} records")
        return df
    except Exception as e:
        print(f"Error loading Excel: {e}")
        import traceback
        traceback.print_exc()
        return None

def get_unique_labs():
    """Get list of unique labs with riders"""
    df = load_data()
    if df is None:
        print("DEBUG: No data returned from load_data()")
        return []
    
    print(f"DEBUG: Loaded {len(df)} records from Excel")
    
    # Get current time
    current_time = datetime.now().time()
    print(f"DEBUG: Current time: {current_time}")
    
    labs_data = {}
    for _, row in df.iterrows():
        lab_name = row['Lab Name']
        rider_name = row['Rider Name']
        status = row['Status']
        time_slot = row['Time Slot']
        
        if lab_name not in labs_data:
            labs_data[lab_name] = {
                'name': lab_name,
                'riders': set(),
                'active_now': False
            }
        
        labs_data[lab_name]['riders'].add(rider_name)
        
        # Check if this rider is active right now
        if status == 'Active' and is_time_in_slot(current_time, time_slot):
            labs_data[lab_name]['active_now'] = True
            print(f"DEBUG: {rider_name} in {lab_name} is active at {time_slot} (current: {current_time})")
    
    # Convert sets to lists and determine lab status based on active riders right now
    labs_list = []
    for lab in labs_data.values():
        lab_status = 'Active' if lab['active_now'] else 'Inactive'
        
        labs_list.append({
            'name': lab['name'],
            'riders': sorted(list(lab['riders'])),
            'status': lab_status
        })
    
    return labs_list

def get_lab_time_slots(lab_name):
    """Get all time slots for a specific lab"""
    df = load_data()
    if df is None:
        return []
    
    lab_data = df[df['Lab Name'] == lab_name]
    time_slots = []
    
    for _, row in lab_data.iterrows():
        time_slots.append({
            'time_slot': row['Time Slot'],
            'rider_name': row['Rider Name'],
            'status': row['Status'],
            'test_type': row['Test Type'],
            'fuel_type': row['Fuel Type'],
            'vehicle_class': row['Vehicle Class'],
            'remarks': row['Remarks']
        })
    
    return time_slots

def get_rider_details(lab_name, rider_name, time_slot):
    """Get detailed information for a rider"""
    df = load_data()
    if df is None:
        return None
    
    rider_data = df[
        (df['Lab Name'] == lab_name) & 
        (df['Rider Name'] == rider_name) & 
        (df['Time Slot'] == time_slot)
    ]
    
    if rider_data.empty:
        return None
    
    row = rider_data.iloc[0]
    return {
        'lab_name': lab_name,
        'rider_name': rider_name,
        'time_slot': time_slot,
        'test_type': row['Test Type'],
        'fuel_type': row['Fuel Type'],
        'vehicle_class': row['Vehicle Class'],
        'remarks': row['Remarks'],
        'status': row['Status']
    }

def update_rider_details(lab_name, rider_name, time_slot, data):
    """Update rider details in Excel"""
    df = load_data()
    if df is None:
        return False
    
    # Find and update the row
    mask = (
        (df['Lab Name'] == lab_name) & 
        (df['Rider Name'] == rider_name) & 
        (df['Time Slot'] == time_slot)
    )
    
    if mask.any():
        df.loc[mask, 'Test Type'] = data.get('test_type', '')
        df.loc[mask, 'Fuel Type'] = data.get('fuel_type', '')
        df.loc[mask, 'Vehicle Class'] = data.get('vehicle_class', '')
        df.loc[mask, 'Remarks'] = data.get('remarks', '')
        df.loc[mask, 'Status'] = data.get('status', 'Active')
        
        try:
            df.to_excel(EXCEL_FILE, index=False)
            return True
        except Exception as e:
            print(f"Error saving Excel: {e}")
            return False
    
    return False

def add_new_entry(data):
    """Add a new entry to Excel file"""
    try:
        df = load_data()
        
        # If file doesn't exist, create a new dataframe with required columns
        if df is None:
            df = pd.DataFrame(columns=[
                'Lab Name', 'Rider Name', 'Time Slot', 'Test Type', 
                'Fuel Type', 'Vehicle Class', 'Status', 'Remarks'
            ])
        
        # Create new row as a dictionary
        new_row = {
            'Lab Name': data.get('lab_name', ''),
            'Rider Name': data.get('rider_name', ''),
            'Time Slot': data.get('time_slot', ''),
            'Test Type': data.get('test_type', ''),
            'Fuel Type': data.get('fuel_type', ''),
            'Vehicle Class': data.get('vehicle_class', ''),
            'Status': data.get('status', 'Active'),
            'Remarks': data.get('remarks', '')
        }
        
        # Check if entry already exists
        existing = df[
            (df['Lab Name'] == new_row['Lab Name']) & 
            (df['Rider Name'] == new_row['Rider Name']) & 
            (df['Time Slot'] == new_row['Time Slot'])
        ]
        
        if not existing.empty:
            return False, "This entry already exists!"
        
        # Add new row using concat (pandas 2.0+)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        
        # Save to Excel
        df.to_excel(EXCEL_FILE, index=False)
        print(f"DEBUG: Successfully added new entry - {new_row['Rider Name']} to {new_row['Lab Name']}")
        return True, "Entry added successfully!"
        
    except Exception as e:
        print(f"Error adding entry: {e}")
        import traceback
        traceback.print_exc()
        return False, f"Error: {str(e)}"

@app.route('/')
def home():
    """Home page - Lab Dashboard"""
    labs = get_unique_labs()
    print(f"DEBUG: home() returned {len(labs)} labs")
    return render_template('home.html', labs=labs)

@app.route('/add-entry')
def add_entry():
    """Add Entry page - Form to add new lab-rider assignment"""
    return render_template('add_entry.html')

@app.route('/lab/<lab_name>')
def lab_details(lab_name):
    """Lab Details page - Time Slot View"""
    time_slots = get_lab_time_slots(lab_name)
    return render_template('lab_details.html', lab_name=lab_name, time_slots=time_slots)

@app.route('/rider/<lab_name>/<rider_name>/<time_slot>')
def rider_details(lab_name, rider_name, time_slot):
    """Rider Details page"""
    rider = get_rider_details(lab_name, rider_name, time_slot)
    
    if not rider:
        return redirect(url_for('home'))
    
    return render_template('rider_details.html', rider=rider)

@app.route('/api/rider/update', methods=['POST'])
def update_rider():
    """API endpoint to update rider details"""
    data = request.json
    
    success = update_rider_details(
        data['lab_name'],
        data['rider_name'],
        data['time_slot'],
        data
    )
    
    return jsonify({'success': success})

@app.route('/api/entry/add', methods=['POST'])
def add_entry_api():
    """API endpoint to add new entry to Excel"""
    data = request.json
    success, message = add_new_entry(data)
    return jsonify({'success': success, 'message': message})

if __name__ == '__main__':
    app.run(debug=True)
