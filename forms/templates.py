PERSONAL_DETAILS_SECTION = {
    "title": "Personal Details",
    "questions": [
        {"type": "text", "label": "First Name", "placeholder": "First Name", "required": True, "id": "firstName"},
        {"type": "text", "label": "Last Name", "placeholder": "Last Name", "required": True, "id": "lastName"},
        {"type": "file", "label": "Upload copy of ID", "required": True, "id": "idFile"},
        {"type": "text", "label": "Email", "placeholder": "Email", "required": True, "id": "email"},
        {"type": "tel", "label": "Cellphone number", "placeholder": "Cellphone number", "required": True,
         "id": "cellphone"},
        {"type": "dropdown", "label": "Country of Birth", "options": ["South Africa", "Other"], "required": True,
         "id": "countryOfBirthDropdown"},
        {"type": "text", "label": "If 'Other', please specify", "placeholder": "Country of birth", "required": False,
         "id": "countryOfBirth"},
        {"type": "dropdown", "label": "Marital Status", "options": ["Single", "Married"], "required": True,
         "id": "maritalStatus"},
        {"type": "dropdown", "label": "Number of Vehicles", "options": ["0", "1", "2", "3", "4"], "required": True,
         "id": "numVehicles"},
    ]
}

CURRENT_ADDRESS_DETAILS = {
    "title": "Current residence",
    "questions": [
        {'type': 'checkbox', 'label': 'Are you currently renting a property?', 'id': 'isRenting'},
        {"type": "textarea", "label": "Current address",
         "placeholder": "12 Rothburn Street \nGoodwood \nCape Town", "required": True,
         "id": "currentAddress"},
        {"type": "text", "label": "Please specify the owner's name", "placeholder": "Owner's name",
         "required": False, "id": "ownerName"},
        {"type": "tel", "label": "Owner's cellphone number", "placeholder": "Owner's cellphone number",
         "required": False,
         "id": "ownerCellphone"},
    ]
}

PETS_DETAILS = {
    "title": "Pets",
    "questions": [
        {"type": "dropdown", "label": "Number of pets", "options": ["0", "1", "2", "3", "4"], "required": True,
         "id": "numPets"},
    ]
}

WORK_DETAILS_SECTION = {
    'title': 'Employment Details',
    'questions': [
        {"type": "dropdown", "label": "Employment status", "options": ["Employed", "Unemployed", "Self-employed"],
         "required": True, "id": "employmentStatus"},
        {"type": "text", "label": "Employer's name (if employed)", "placeholder": "Employer's name",
         "required": False, "id": "employerName"},
        {"type": "tel", "label": "Employer's contact number (if employed)", "placeholder": "Employer's contact number",
         "required": False,
         "id": "employerContactNumber"},
        {"type": "text", "label": "Brutto income", "placeholder": "Brutto income", "required": True,
         "id": "bruttoIncome"},
        {"type": "file", "label": "Copy of employment confirmation", "required": False, "id": "employmentConfirmation"},
        {"type": "file", "label": "Three months bank statement", "required": True, "id": "bankstatement"},
    ]
}

EXPENSES_DETAILS_SECTION = {
    'title': 'Monthly Expenses',
    'questions': [
        {"type": "text", "label": "Monthly expenses", "placeholder": "i.e. R8000", "required": True,
         "id": "monthlyExpenses"},
    ]
}

RELATIVE_DETAILS = {
    "title": "Details of friend / relative not living with you",
    "questions": [
        {"type": "text", "label": "First Name", "placeholder": "First Name", "required": True,
         "id": "relativeFirstName"},
        {"type": "text", "label": "Last Name", "placeholder": "Last Name", "required": True, "id": "relativeLastName"},
        {"type": "tel", "label": "Cellphone number", "placeholder": "Cellphone number", "required": True,
         "id": "relativeCellphone"},
        {"type": "file", "label": "Upload copy of ID", "required": True, "id": "idFile"},
    ]
}

OTHER_DETAILS = {
    "title": "Other",
    "questions": [
        {'type': 'checkbox',
         'label': 'Has there been any judgement or eviction order instituted or granted against you?',
         'id': 'evictionInstituted'},
        {'type': 'checkbox', 'label': 'Are there any pending civil or criminal actions against you?',
         'id': 'criminalRecord'},
        {'type': 'checkbox', 'label': 'Have you previously refused to pay rent for any reason?',
         'id': 'hasRefusedToPayRent'},
        {"type": "textarea", "label": "If yes to the above, please specify",
         "placeholder": "Specify reason for refusal to pay rent", "required": False, "id": "refusalReason"},
        {'type': 'checkbox',
         'label': 'I acknowledge that the above information is correct and accurate at the date of signature',
         'id': 'acknowledgementCheckbox'}
    ]
}

# PLEASE PROVIDE THE FOLLOWING DOCUMENTS WITH THE SIGNED APPLICATION;
# • CERTIFIED ID COPY OF ALL THE OCCUPANTS
# • GROSS SALARY MUST BE 3X THE RENTAL
# • 3 MONTHS BANK STATEMENTS WITH BANK STAMP (RECENT)
# • 3 MONTHS PAYSLIPS (RECENT)
# • LETTER CONFIRMING EMPLOYMENT
# • CURRENT LANDLORD REFERENCE LETTER

APPLICATION_FORM_TEMPLATE_CONFIG = [
    PERSONAL_DETAILS_SECTION,
    CURRENT_ADDRESS_DETAILS,
    PETS_DETAILS,
    WORK_DETAILS_SECTION,
    EXPENSES_DETAILS_SECTION,
    RELATIVE_DETAILS,
    OTHER_DETAILS,
]
