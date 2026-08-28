"""Executable examples for the inheritance lesson."""

from inheritance import Developer
from inheritance import Employee
from inheritance import Manager
from inheritance import ManagingDeveloper
from inheritance import SeniorManager


# =============================================================================
# 1. INHERITED ATTRIBUTES AND METHODS
# =============================================================================

manager1 = Manager("HR")
print("Manager department:", manager1.department)
print("Default schedule:", manager1.login_time, "to", manager1.logout_time)
print(manager1.work())

manager2 = Manager("Accounts")
manager2.change_login_time(12)
manager2.change_logout_time(8)
print("Updated manager schedule:", manager2.login_time, "to", manager2.logout_time)

developer1 = Developer("Mobile developer")
developer1.change_login_time(7)
developer1.change_logout_time(4)
print("Developer schedule:", developer1.login_time, "to", developer1.logout_time)
print(developer1.work())


# =============================================================================
# 2. MULTILEVEL INHERITANCE AND super()
# =============================================================================

senior_manager1 = SeniorManager("APAC website", "Web")
print(
    "Senior manager:",
    senior_manager1.project,
    "project,",
    senior_manager1.department,
    "department",
)
print("Inherited schedule:", senior_manager1.login_time, "to", senior_manager1.logout_time)
print(senior_manager1.work())


# =============================================================================
# 3. MULTIPLE INHERITANCE
# =============================================================================

managing_developer1 = ManagingDeveloper("Accounts", "Mobile developer")
print(
    "Managing developer:",
    managing_developer1.department,
    "department,",
    managing_developer1.role,
    "role",
)
print("Inherited joining time:", managing_developer1.login_time)
print(managing_developer1.work())


# =============================================================================
# 4. METHOD OVERRIDING AND MRO
# =============================================================================

employee = Employee()
print("Parent method:", employee.work())
print("Manager's overridden method:", manager1.work())
print("ManagingDeveloper MRO:")
for class_name in ManagingDeveloper.__mro__:
    print("-", class_name.__name__)


# =============================================================================
# 5. QUICK SUMMARY
# =============================================================================

print("\n--- Quick Summary ---")
print("Parent class: provides common attributes and methods")
print("Child class: inherits and may add or override behavior")
print("Single inheritance: one child has one parent")
print("Multilevel inheritance: inheritance continues through multiple levels")
print("Multiple inheritance: one child has more than one parent")
print("super(): calls behavior from the next class in the MRO")
print("Method overriding: a child replaces a parent method with its own version")
