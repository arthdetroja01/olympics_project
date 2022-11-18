# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Nation(models.Model):
    nation = models.CharField(primary_key=True, max_length=10000)
    national_anthem = models.CharField(max_length=10000)

    class Meta:        
        db_table = 'NATION'

class CountryAdmin(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=10000)
    last_name = models.CharField(max_length=10000)
    gender = models.CharField(max_length=10000, blank=True, null=True)
    phone_number = models.IntegerField()
    nation = models.ForeignKey('Nation', models.DO_NOTHING, db_column='nation')
    address = models.CharField(max_length=10000)

    class Meta:        
        db_table = 'COUNTRY_ADMIN'

class Fitness(models.Model):
    fitness_id = models.IntegerField(primary_key=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    doping_results = models.CharField(max_length=10000)

    class Meta:        
        db_table = 'FITNESS'
        
class CurrentPlayer(models.Model):
    player_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=10000)
    last_name = models.CharField(max_length=10000)
    address = models.CharField(max_length=10000, blank=True, null=True)
    email = models.CharField(max_length=10000)
    marital_status = models.CharField(max_length=10000)
    gender = models.CharField(max_length=10000, blank=True, null=True)
    phone_number = models.IntegerField()
    dob = models.DateField()
    fitness_id = models.ForeignKey('Fitness', models.DO_NOTHING, db_column='fitness_id')
    nation = models.ForeignKey('Nation', models.DO_NOTHING, db_column='nation')

    class Meta:        
        db_table = 'CURRENT_PLAYER'


class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=10000)
    world_record = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:        
        db_table = 'EVENT'


class GuestOfHonor(models.Model):
    guest_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=10000)
    last_name = models.CharField(max_length=10000)
    dob = models.DateField()
    designation = models.CharField(max_length=10000, blank=True, null=True)
    year = models.IntegerField()
    nation = models.ForeignKey('Nation', models.DO_NOTHING, db_column='nation')
    event = models.ForeignKey('Event', models.DO_NOTHING)

    class Meta:        
        db_table = 'GUEST_OF_HONOR'


class Measurement(models.Model):
    height = models.IntegerField(primary_key=True)
    weight = models.IntegerField()
    bmi = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        
        db_table = 'MEASUREMENT'
        unique_together = (('height', 'weight'),)


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=10000)
    last_name = models.CharField(max_length=10000)
    address = models.CharField(max_length=10000, blank=True, null=True)
    email = models.CharField(max_length=10000)
    marital_status = models.CharField(max_length=10000)
    gender = models.CharField(max_length=10000, blank=True, null=True)
    phone_number = models.IntegerField()
    dob = models.DateField()
    nation = models.ForeignKey('Nation', models.DO_NOTHING, db_column='nation')

    class Meta:
        
        db_table = 'PLAYER'


class Schedule(models.Model):
    event = models.OneToOneField(Event, models.DO_NOTHING, primary_key=True)
    year = models.IntegerField()
    location = models.CharField(max_length=10000, blank=True, null=True)
    start = models.DateField()
    end = models.DateField()

    class Meta:
        
        db_table = 'SCHEDULE'
        unique_together = (('event', 'year'),)


class Umpire(models.Model):
    umpire_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=10000)
    last_name = models.CharField(max_length=10000)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=10000)
    gender = models.CharField(max_length=10000)
    umpire_dob = models.DateField()
    nation = models.ForeignKey('Nation', models.DO_NOTHING, db_column='nation')
    event = models.ForeignKey('Event', models.DO_NOTHING)

    class Meta:
        
        db_table = 'UMPIRE'


class LegacyRecord(models.Model):
    event = models.OneToOneField(Event, models.DO_NOTHING, primary_key=True)
    player = models.ForeignKey('Player', models.DO_NOTHING)
    year = models.IntegerField()
    medal_gold = models.IntegerField()
    medal_silver = models.IntegerField()
    medal_bronze = models.IntegerField()

    class Meta:        
        db_table = 'LEGACY_RECORD'
        unique_together = (('event', 'player', 'year'),)

class CurrentRecord(models.Model):
    event = models.OneToOneField('Event', models.DO_NOTHING, primary_key=True)
    player = models.ForeignKey('Player', models.DO_NOTHING)
    medal_gold = models.IntegerField()
    medal_silver = models.IntegerField()
    medal_bronze = models.IntegerField()

    class Meta:        
        db_table = 'CURRENT_RECORD'
        unique_together = (('event', 'player'),)

"""
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:        
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:        
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:        
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        
        db_table = 'django_session'
"""