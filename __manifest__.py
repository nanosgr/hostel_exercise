{
    'name': "Hostel Management",
    'summary': "Manage Hostel easily",
    'description': """
        Efficiently manage the entire residential facility in the school.", # Supports reStructuredText(RST)
        format (description is Deprecated),
        """,
    'author': "Sebastian Rios",
    'sequence': -105,
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '18.0.1.0.0',
    'depends': ['base'],
    'data': [
        "security/hostel_security.xml",
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/hostel.xml",
        "views/hostel_amenities.xml",
        "views/hostel_categ.xml",
        "views/hostel_room.xml",
        "views/hostel_student.xml",
    ],
}