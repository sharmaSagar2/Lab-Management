# Testing & Validation Checklist

Use this checklist to verify all features are working correctly.

## ✅ Setup & Installation

- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] Sample data created: `python create_sample_data.py`
- [ ] Excel file exists: `data/lab_data.xlsx`
- [ ] Flask app runs without errors: `python app.py`
- [ ] Application accessible at: `http://localhost:5000`

## 🏠 Home Page (Lab Dashboard)

### Layout & Display
- [ ] Page title: "🔬 Lab Management System" visible in navbar
- [ ] Subtitle: "Lab Dashboard" with description text
- [ ] 4 lab tiles displayed in grid layout
- [ ] Grid is responsive (2 columns on tablet, 1 on mobile)

### Lab Tile Content
- [ ] Lab name displayed prominently
- [ ] Status badge shows "Active" or "Inactive"
- [ ] Green badge for Active, Red for Inactive
- [ ] Rider names listed under "Assigned Riders"
- [ ] All rider names visible (not cut off)

### Interactivity
- [ ] Hover effect on lab tiles (shadow & color change)
- [ ] Clicking on lab tile navigates to Lab Details page
- [ ] Breadcrumb shows "Home" as active

## 🔬 Lab Details Page (Time Slot View)

### Navigation
- [ ] Breadcrumb shows: Home / Lab Name
- [ ] Back button is available
- [ ] Clicking Home breadcrumb returns to dashboard
- [ ] Browser back button works correctly

### Content Display
- [ ] Page title shows selected lab name
- [ ] Subtitle shows "Time Slots & Assigned Riders"
- [ ] All time slots for lab are displayed
- [ ] Time slots displayed in card layout

### Time Slot Card Content
- [ ] Time slot badge shows time range (⏰ symbol)
- [ ] Rider name displayed prominently
- [ ] Status badge visible (green/red)
- [ ] Test Type shown (Emission Test, etc.)
- [ ] Fuel Type shown (Petrol, Diesel, etc.)
- [ ] Vehicle Class shown (Two-Wheeler, Four-Wheeler, etc.)

### Interactivity
- [ ] Hover effect on time slot cards
- [ ] Clicking time slot navigates to Rider Details
- [ ] Card shows "Click to edit details →" indicator

## 👤 Rider Details Page

### Navigation
- [ ] Breadcrumb shows: Home / Lab Name / Rider Name
- [ ] Back button available
- [ ] Breadcrumb navigation works

### Read-Only Fields
- [ ] Rider Name field is read-only
- [ ] Time Slot field is read-only
- [ ] Fields have gray background indicating disabled state

### Editable Dropdown Fields
- [ ] Test Type dropdown has all options:
  - Emission Test
  - Performance Test
  - Safety Test
  - Durability Test
  - Noise Test
- [ ] Fuel Type dropdown has all options:
  - Petrol
  - Diesel
  - CNG
  - LPG
  - Electric
  - Hybrid
- [ ] Vehicle Class dropdown has all options:
  - Two-Wheeler
  - Three-Wheeler
  - Four-Wheeler
  - Heavy-Duty
  - Light Commercial
- [ ] Status dropdown has:
  - Active (selected for active riders)
  - Inactive (selected for inactive riders)

### Text Area Field
- [ ] Remarks text area is editable
- [ ] Current remarks value loaded correctly
- [ ] Text area allows multiple lines

### Form Actions
- [ ] "Save / Update" button visible
- [ ] "Back" button visible
- [ ] Buttons properly styled and clickable

## 💾 Data Persistence

### Saving Changes
- [ ] Modify any field (test type, fuel type, remarks, status)
- [ ] Click "Save / Update" button
- [ ] Success notification appears (green banner)
- [ ] Page navigates back to Lab Details after 1.5 seconds

### Verification
- [ ] Go back to the time slot (click back button)
- [ ] Click the same time slot again
- [ ] Verify all changes are saved and displayed
- [ ] Go to Lab Details - verify data persists

### Excel File Update
- [ ] Open `data/lab_data.xlsx` in Excel
- [ ] Find the updated rider row
- [ ] Verify all changes are saved in Excel
- [ ] Close Excel file

## 🎨 Styling & UI

### Colors & Status Indicators
- [ ] Active status badges are green (#16a34a)
- [ ] Inactive status badges are red (#dc2626)
- [ ] Primary color (blue) used consistently
- [ ] No color inconsistencies

### Responsive Design
- [ ] **Desktop (1920px)**: 4 columns for labs, wide cards
- [ ] **Tablet (800px)**: Resize browser to test
  - Labs in 2-column grid
  - Cards remain readable
- [ ] **Mobile (375px)**: Resize to mobile
  - Labs in 1-column grid
  - Time slots in 1-column layout
  - Form readable and usable
  - Breadcrumb simplified

### Typography
- [ ] Headers are larger and prominent
- [ ] Labels are bold and clear
- [ ] Text is readable (no too-small fonts)
- [ ] No text overflow or cutoff

### Spacing & Layout
- [ ] Proper padding around content
- [ ] Cards have consistent spacing
- [ ] Form fields have proper margins
- [ ] No cramped or squeezed elements

## 🔗 Navigation

### Overall Navigation
- [ ] All links work correctly
- [ ] No broken navigation paths
- [ ] Browser back/forward buttons work
- [ ] Breadcrumbs are clickable

### Page Flow
- [ ] Home → Lab Details (✓)
- [ ] Lab Details → Rider Details (✓)
- [ ] Rider Details → Back to Lab Details (✓)
- [ ] Lab Details → Back to Home (✓)
- [ ] Home → Back to Home (✓ - no error)

## 🐛 Error Handling

### Missing Data
- [ ] If no labs exist: "No labs available" message shown
- [ ] If no time slots: "No time slots found" message shown
- [ ] If invalid lab name: Redirect to home or 404

### Form Submission
- [ ] Required fields marked with *
- [ ] Form won't submit if required fields empty (browser validation)
- [ ] Invalid data doesn't crash application

## ⚡ Performance

- [ ] Page loads quickly (< 2 seconds)
- [ ] No console errors (open DevTools: F12)
- [ ] Smooth animations and transitions
- [ ] No lag when clicking buttons

## 📊 Data Validation

### Sample Data
- [ ] 4 labs loaded correctly
- [ ] 14 total rider assignments
- [ ] All riders visible on home page
- [ ] All time slots visible on lab details

### Field Values
- [ ] Test Types match dropdown options
- [ ] Fuel Types match dropdown options
- [ ] Vehicle Classes match dropdown options
- [ ] Status values are "Active" or "Inactive"

## 🌐 Browser Compatibility

- [ ] **Chrome/Edge**: All features work
- [ ] **Firefox**: All features work
- [ ] **Safari**: All features work
- [ ] **Mobile browsers**: Responsive and functional

## 📱 Mobile Experience

- [ ] Tap targets are large enough (> 44px)
- [ ] No horizontal scroll on mobile
- [ ] Form is usable on small screens
- [ ] Dropdowns work on mobile
- [ ] Buttons are easily clickable

## 📝 Documentation

- [ ] README.md exists and is readable
- [ ] QUICKSTART.md provides clear setup steps
- [ ] CONFIGURATION.md covers customization
- [ ] All code comments are present

---

## Summary

**Total Checks**: 100+

**Pass Rate**: ___%

**Issues Found**: 

1. _______________
2. _______________
3. _______________

**Notes**:
_________________________________________________________________

---

**Tester Name**: _________________  
**Date**: _________________  
**Version**: 1.0  

✅ **All checks passed - Ready for use!**
