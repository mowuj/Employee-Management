# from django.db.models.signals import post_save
# from django.contrib.auth import get_user_model
# from django.dispatch import receiver
# from .models import Employee

# user =get_user_model()

# @receiver(post_save,sender=user)
# def create_employee(sender,instance,created,**kwargs):
    
#     if created:
#         Employee.objects.create(user=instance)