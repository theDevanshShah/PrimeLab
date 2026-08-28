"""A beginner-friendly lesson on inheritance in Python."""


class Employee:
    """Base class containing behavior common to every employee."""

    login_time = 10
    logout_time = 7

    def change_login_time(self, new_login_time):
        self.login_time = new_login_time

    def change_logout_time(self, new_logout_time):
        self.logout_time = new_logout_time

    def work(self):
        return "Employee is working"


class Manager(Employee):
    """Manager inherits the schedule and methods from Employee."""

    def __init__(self, department):
        self.department = department

    def work(self):
        return f"Manager is managing the {self.department} department"


class Developer(Employee):
    def __init__(self, role):
        self.role = role

    def work(self):
        return f"Developer is working as a {self.role}"


class SeniorManager(Manager):
    """SeniorManager inherits from Manager and Employee."""

    def __init__(self, project, department):
        super().__init__(department)
        self.project = project

    def work(self):
        return f"Senior manager is leading the {self.project} project"


class ManagingDeveloper(Manager, Developer):
    """A class can inherit from more than one parent class."""

    def __init__(self, department, role):
        Manager.__init__(self, department)
        Developer.__init__(self, role)

    def work(self):
        return f"Managing developer leads {self.department} as a {self.role}"