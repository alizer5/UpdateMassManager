{
    "name": "Mass Employee Update Manager",
    "version": "17.0.1.0.0",
    "author": "Ali Zer",
    "category": "Human Resources",
    "summary": "Mass update employee manager and job positions in HR module.",
    "description": """
        This module allows updating multiple employees' managers and job positions at once.
        Features:
        - Bulk update manager
        - Bulk update job position
        - User-friendly wizard for batch updates
    """,
    "license": "LGPL-3",
    "depends": ["hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/emp.xml",
        "wizard/mass_manager.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
