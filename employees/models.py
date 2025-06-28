from django.db import models

class StaffBase(models.Model):
    """
    Abstract base model for common staff fields
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

    def get_role(self):
        return "Staff"

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)

    def __str__(self):
        return f"Manager: {self.first_name} {self.last_name}"

    def get_role(self):
        return "Manager"

class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='interns')
    internship_end = models.DateField()

    def __str__(self):
        return f"Intern: {self.first_name} {self.last_name}"

    def get_role(self):
        return "Intern"

class Address(models.Model):
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE, null=True, blank=True, related_name='addresses')
    intern = models.ForeignKey('Intern', on_delete=models.CASCADE, null=True, blank=True, related_name='addresses')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"
