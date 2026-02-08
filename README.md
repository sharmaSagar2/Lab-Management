# Lab Management Dashboard

A professional, responsive web application for managing laboratory operations with multiple labs, time slots, and rider assignments.

## Features

✨ **Home Page (Lab Dashboard)**
- Display 4 clickable lab tiles in a grid layout
- Each tile shows:
  - Lab Name
  - List of assigned riders
  - Overall Lab Status (Active/Inactive - read-only)
- Click anywhere on the tile to navigate to Lab Details

⏰ **Lab Details Page (Time Slot View)**
- Display selected lab name at the top
- Show all time slots for that lab
- Each time slot card displays:
  - Time slot (e.g., 09:00–11:00)
  - Assigned rider name
  - Rider status (read-only)
  - Test and vehicle information
- Click to navigate to Rider Details

👤 **Rider Details Page**
- Display detailed form for selected rider and time slot
- Editable fields:
  - Rider Name (read-only)
  - Time Slot (read-only)
  - Test Type (dropdown)
  - Fuel Type (dropdown)
  - Vehicle Class (dropdown)
  - Remarks (text area)
  - Status (Active/Inactive)
- Save/Update button to persist changes
- Updated data reflects on previous pages

📊 **Data Management**
- All data loaded from Excel sheet (lab_data.xlsx)
- Excel includes: Lab Name, Rider Name, Time Slot, Test Type, Fuel Type, Vehicle Class, Remarks, Status
- Dynamic data reading and updating

🎨 **UI/UX**
- Clean, professional dashboard design
- Card-based layout
- Fully responsive design (desktop, tablet, mobile)
- Color-coded status indicators:
  - Green → Active
  - Red → Inactive
- Simple navigation with breadcrumbs
- Smooth transitions and hover effects

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step 1: Install Dependencies
```bash
cd c:\Users\sagar\OneDrive\Desktop\web
pip install -r requirements.txt
```

### Step 2: Create Sample Data
```bash
python create_sample_data.py
```
This will generate `data/lab_data.xlsx` with sample lab, rider, and time slot data.

### Step 3: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

## Project Structure

```
web/
├── app.py                    # Flask application and routes
├── create_sample_data.py     # Script to generate sample Excel data
├── requirements.txt          # Python dependencies
├── data/
│   └── lab_data.xlsx        # Excel data file (auto-generated)
├── templates/
│   ├── base.html            # Base template with navbar
│   ├── home.html            # Home page (lab dashboard)
│   ├── lab_details.html     # Lab details page
│   └── rider_details.html   # Rider details page
└── static/
    ├── style.css            # Main stylesheet
    └── script.js            # JavaScript functionality
```

## Usage

1. **Home Page**: View all available labs in a grid. Click any lab tile to see its time slots.

2. **Lab Details**: See all time slots for a specific lab with assigned riders. Click any time slot to edit rider details.

3. **Rider Details**: Edit test configuration and remarks for a specific rider. Click Save/Update to persist changes.

4. **Data Persistence**: All changes are automatically saved to the Excel file.

## Adding More Labs/Riders

Edit `data/lab_data.xlsx` to add more labs, riders, or time slots. The application will automatically load the updated data.

### Excel File Format
| Lab Name | Rider Name | Time Slot | Test Type | Fuel Type | Vehicle Class | Remarks | Status |
|----------|-----------|-----------|-----------|-----------|----------------|---------|--------|
| Lab A | John Smith | 09:00–11:00 | Emission Test | Petrol | Two-Wheeler | Notes here | Active |

## Customization

### Colors & Styling
Edit `static/style.css` to customize:
- Primary color: `--primary-color`
- Success (Active) color: `--success-color`
- Danger (Inactive) color: `--danger-color`
- Background and text colors

### Dropdown Options
Edit `templates/rider_details.html` to add/modify:
- Test Types
- Fuel Types
- Vehicle Classes

## Browser Compatibility
- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- IE11: ⚠️ Not recommended

## Support

For issues or questions, check:
1. Ensure all dependencies are installed (`pip install -r requirements.txt`)
2. Verify Excel file exists at `data/lab_data.xlsx`
3. Check Flask console for error messages
4. Ensure no other application is using port 5000

## License
This project is for internal lab management use.
