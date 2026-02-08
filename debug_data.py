import sys
import os
import pandas as pd

# Add current dir to path
sys.path.insert(0, os.getcwd())

print("Current Working Directory:", os.getcwd())
print("Excel file path:", os.path.join('data', 'lab_data.xlsx'))
print("File exists:", os.path.exists('data/lab_data.xlsx'))

EXCEL_FILE = os.path.join('data', 'lab_data.xlsx')

def load_data():
    """Load data from Excel file"""
    print(f"\n🔍 Attempting to load: {EXCEL_FILE}")
    if not os.path.exists(EXCEL_FILE):
        print("❌ File NOT found!")
        return None
    try:
        print("✅ File found, reading...")
        df = pd.read_excel(EXCEL_FILE)
        print(f"✅ Loaded {len(df)} records")
        print(f"✅ Columns: {list(df.columns)}")
        return df
    except Exception as e:
        print(f"❌ Error loading Excel: {e}")
        import traceback
        traceback.print_exc()
        return None

def get_unique_labs():
    """Get list of unique labs with riders"""
    df = load_data()
    if df is None:
        print("❌ No data loaded!")
        return []
    
    print(f"\n📊 Processing {len(df)} rows...")
    labs_data = {}
    for idx, row in df.iterrows():
        try:
            lab_name = row['Lab Name']
            rider_name = row['Rider Name']
            status = row['Status']
            
            print(f"  Row {idx}: {lab_name} | {rider_name} | {status}")
            
            if lab_name not in labs_data:
                labs_data[lab_name] = {
                    'name': lab_name,
                    'riders': set(),
                    'status': status
                }
            labs_data[lab_name]['riders'].add(rider_name)
        except Exception as e:
            print(f"  ❌ Error processing row {idx}: {e}")
    
    # Convert sets to lists
    labs_list = [
        {
            'name': lab['name'],
            'riders': sorted(list(lab['riders'])),
            'status': lab['status']
        }
        for lab in labs_data.values()
    ]
    
    print(f"\n✅ Found {len(labs_list)} unique labs")
    for lab in labs_list:
        print(f"  - {lab['name']}: {len(lab['riders'])} riders")
    
    return labs_list

# Test it
labs = get_unique_labs()
print(f"\n🎯 Final result: {len(labs)} labs")
if labs:
    print("✅ Data loaded successfully!")
else:
    print("❌ No labs found!")
