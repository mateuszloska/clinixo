from django.db import models
from django.contrib.auth import get_user_model

#role manager
class RoleManager():
    def __init__(self, current_roles=[""]):
        self.possible_roles = ('role_manager', 'visit_manager', 'contact_manager', 'patient')
        self.roles = current_roles.split(",")

    def grant_role(self, role):
        if (role in self.possible_roles) and (role not in self.roles):
            self.roles.append(role)

    def remove_role(self, role):
        if role in self.roles:
            self.roles.remove(role)
    
    def is_granted(self, role):
        if role in self.roles:
            return True
        else:
            return False

    def stringrify(self):
        return ",".join(self.roles)

    def unstringify(self, roles):
        self.roles=roles.split(",")

#contacts profiles for all system-users
class ContactProfile(models.Model):
    user = models.ForeignKey(get_user_model(),
        on_delete=models.CASCADE,
        related_name="contact_profile",
        default=None, null=True, blank=True)
        #foreign key as a physician could be a patient and worker as example
    
    phone_number = models.CharField(max_length=30)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)

    CONTACT_TYPE_CHOISES = (('patient','Patient'),
                            ('physician','Physician'),
                            ('manager', 'Manager'),
                            ('reception','Reception'),
                            ('other-stuff','Other-Stuff'),
                            )

    contact_type = models.CharField(max_length=20,
                choices = CONTACT_TYPE_CHOISES,
                default='patient')

    roles = models.TextField()

    def grant_role(self,role):
        rm = RoleManager(self.roles)
        rm.grant_role(role)
        self.roles = rm.stringrify()
        print(f"Current roles = {self.roles}")

    def __str__(self):
        return "contact for {} {}".format(self.first_name, self.last_name)

#patient profiles
class PatientProfile(models.Model):
    contact = models.OneToOneField(ContactProfile,
        on_delete=models.CASCADE,
        related_name="patient_profile")

    insurance_number = models.CharField(max_length=50)
