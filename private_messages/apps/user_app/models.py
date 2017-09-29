from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0_9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, username, email, password, c_password):
        errors = []

        if len(username) < 1:
            errors.append('Username is required')
        elif len(username) < 3:
            errors.append('Username must be 3 characters or more')
        
        if len(email) < 1:
            errors.append('Email is required')
        elif not EMAIL_REGEX.match(email):
            errors.append('Invalid email')
        else: 
            user = User.userManager.filter(email=email.lower())
            if len(user) > 0:
                errors.append('Email already in use')

        if len(password) < 1:
            errors.append('Password is required')
        elif len(password) < 8:
            errors.append('Password must be 8 characters or more')
        
        if len(c_password) < 1:
            errors.append('Confirm password is required')
        elif password != c_password:
            errors.append('Password and Confirm password must match')             
                
        if len(errors) > 0:
            return (False, errors)
        else:
            user = User.userManager.create(username=username, email=email.lower(), password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
            return (True, user)
    
    def login(self, email, password):
        errors = []

        if len(email) < 1:
            errors.append('Email is required')
        if not EMAIL_REGEX.match(email):
            errors.append('Invalid email')
        else: 
            user = User.userManager.filter(email=email.lower())
            if len(user) == 0:
                errors.append('Email not found')

        if len(password) < 1:
            errors.append('Password is required')
        elif len(password) < 8:
            errors.append('Password must be 8 characters or more')
                            
        if len(errors) > 0:
            return (False, errors)
        else:
            if bcrypt.checkpw(password.encode(), user[0].password.encode()):
                return (True, user[0])
            else:
                return (False, ['Incorrect password'])

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()

# shows data in command prompt
    def __repr__(self):
        return '<User: {} {}>'.format(self.username, self.email)