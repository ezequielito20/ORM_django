# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcademicLevelPerson(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person = models.ForeignKey('Persons', models.DO_NOTHING)
    academic_level = models.ForeignKey('AcademicLevels', models.DO_NOTHING, db_comment='ID del nivel academico')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_level_person'
        unique_together = (('person', 'academic_level'),)
        db_table_comment = 'Tabla pivote para relacionar las niveles academicos con las personas'


class AcademicLevels(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del nivel academico')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_levels'
        db_table_comment = 'Niveles academicos'


class Areas(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    program = models.ForeignKey('Programs', models.DO_NOTHING, db_comment='ID del programa o carrera al que pertenece')
    name = models.CharField(max_length=191, db_comment='Nombre del Area')
    status = models.BooleanField(db_comment='true: Activo; false: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas'
        unique_together = (('name', 'program'),)
        db_table_comment = 'Areas para categorizar las Materias'


class Audits(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_type = models.CharField(max_length=191, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    event = models.CharField(max_length=191)
    auditable_type = models.CharField(max_length=191)
    auditable_id = models.BigIntegerField()
    old_values = models.TextField(blank=True, null=True)
    new_values = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=1023, blank=True, null=True)
    tags = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audits'
        db_table_comment = 'Bitacora o auditor├¡a de acciones dentro del sistema'


class Authorities(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    name = models.CharField(max_length=191, db_comment='Nombre de la autoridad')
    cedula = models.CharField(max_length=191, db_comment='Cedula de la autoridad')
    review = models.TextField(blank=True, null=True, db_comment='Rese├▒a de la autoriadad')
    position = models.CharField(max_length=191, blank=True, null=True, db_comment='Cargo de la autoridad')
    type_position = models.CharField(max_length=255, blank=True, null=True, db_comment='Univerisdad: autoridad de toda la universidad, Sede: autoridad para una sola sede')
    resenia = models.TextField(db_comment='Rese├▒a de la autoridad')
    img_photo = models.CharField(max_length=191, blank=True, null=True, db_comment='URL de la foto de la autoridad')
    img_firma = models.CharField(max_length=191, blank=True, null=True, db_comment='URL de la imagen de la firma de la autoridad')
    gazette = models.CharField(max_length=191, db_comment='Gaceta de la autoridad')
    date_gazette = models.DateField(db_comment='Fecha de la gaceta')
    date_cese = models.DateField(blank=True, null=True, db_comment='Fecha cese')
    file_curriculum = models.CharField(max_length=191, blank=True, null=True, db_comment='Documento del curriculum')
    status = models.CharField(max_length=255, db_comment='Status de la autoridad, 1: Activo, 0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authorities'
        db_table_comment = 'Autoridades por Institucion'


class BankAccounts(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    bank = models.ForeignKey('Banks', models.DO_NOTHING, db_comment='Id del banco al que corresponde la cuenta')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion')
    account_number = models.CharField(max_length=50, db_comment='Numero de la cuenta bancaria')
    status = models.BooleanField(db_comment='Status del registro true/1: Activo, false/0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_accounts'
        unique_together = (('account_number', 'bank'),)
        db_table_comment = 'Cuentas bancarias'


class Banks(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    country = models.ForeignKey('Countries', models.DO_NOTHING, db_comment='ID del pais al que pertenece la Entidad bancaria')
    name = models.CharField(max_length=191, db_comment='Nombre del banco')
    business_group = models.CharField(max_length=191, db_comment='Nombre de razon social o empresa de la entidad bancaria')
    bank_code = models.CharField(max_length=4, db_comment='Codigo Asignado a nivel central')
    phone = models.CharField(max_length=32, db_comment='Telefono principal del banco')
    status = models.BooleanField(db_comment='Status del registro true/1: Activo, false/0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banks'
        db_table_comment = 'Bancos'


class Banns(models.Model):
    person = models.ForeignKey('Persons', models.DO_NOTHING)
    description = models.CharField(max_length=191, db_comment='Descripcion de la restriccion')
    status = models.BooleanField(db_comment='Status del registro true/1: Activo, false/0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banns'
        db_table_comment = 'Tabla de restricciones o multas a las personas'


class Bloods(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=10, db_comment='Nombre del tipo de sangre')

    class Meta:
        managed = False
        db_table = 'bloods'
        db_table_comment = 'Tipos de sangre'


class Cache(models.Model):
    key = models.CharField(primary_key=True, max_length=191)
    value = models.TextField()
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cache'


class CacheLocks(models.Model):
    key = models.CharField(primary_key=True, max_length=191)
    owner = models.CharField(max_length=191)
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cache_locks'


class CampusGroups(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    name = models.CharField(max_length=191, db_comment='Nombre del grupo de sedes')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_groups'
        db_table_comment = 'Grupos de sedes'


class CampusProgram(models.Model):
    program = models.ForeignKey('Programs', models.DO_NOTHING, db_comment='ID del programa o carrera')
    campus = models.ForeignKey('Campuses', models.DO_NOTHING, db_comment='ID de la sede')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_program'
        unique_together = (('campus', 'program'),)
        db_table_comment = 'Programas habilitados por Sedes'


class CampusUser(models.Model):
    campus = models.ForeignKey('Campuses', models.DO_NOTHING, db_comment='ID de la Sede')
    user = models.ForeignKey('Users', models.DO_NOTHING, db_comment='ID del Usuario')
    created_at = models.DateTimeField(db_comment='Fecha de creaci├│n del registro')

    class Meta:
        managed = False
        db_table = 'campus_user'
        unique_together = (('campus', 'user'),)
        db_table_comment = 'Tabla pivote para relacionar los Usuarios con las Sedes'


class Campuses(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    campus_group = models.ForeignKey(CampusGroups, models.DO_NOTHING, blank=True, null=True, db_comment='ID de la Grupo de Sede a la que pertenece')
    name = models.CharField(max_length=191, db_comment='Nombre de la sede')
    detail = models.CharField(max_length=191, db_comment='Detalle de la sede')
    latitude = models.CharField(max_length=191, db_comment='latitud de la sede')
    longitude = models.CharField(max_length=191, db_comment='longitud de la sede')
    phone = models.CharField(max_length=191, db_comment='telefono de la sede')
    state = models.ForeignKey('States', models.DO_NOTHING, blank=True, null=True, db_comment='ID del Estado al que pertenece')
    address = models.CharField(max_length=191, db_comment='Direccion detallada de la sede')
    main_campus = models.BooleanField(db_comment='Define si la sede es una sede principal, 1:Principal, 0: Secundaria')
    status = models.BooleanField(db_comment='Status del registro true/1: Activo, false/0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campuses'
        db_table_comment = 'Sedes o Localizaciones de las Instituciones'


class CancellationPersonProgram(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person_program = models.ForeignKey('PersonProgram', models.DO_NOTHING, db_comment='ID del registro que asocia al programa con el estudiante')
    cancellation = models.ForeignKey('Cancellations', models.DO_NOTHING, db_comment='ID de la causa de cancelacion o retiro')
    cancellation_date = models.DateField(db_comment='Fecha de cancelacion o retiro')
    details = models.CharField(max_length=191, db_comment='Detalles adicionales de la cancelacion o retiro')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancellation_person_program'
        db_table_comment = 'Retiros o cancelaciones por persona'


class Cancellations(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    name = models.CharField(max_length=191, db_comment='Nombre de la causa')
    status = models.BooleanField(db_comment='Status del registro true/1: Activo, false/0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancellations'
        db_table_comment = 'Causas de Retiro o Cancelaci├│n de las Instituciones'


class Capabilities(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre de la capacidad')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'capabilities'
        db_table_comment = 'Capacidades destacadas'


class CapabilityPersons(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person = models.ForeignKey('Persons', models.DO_NOTHING)
    capability = models.ForeignKey(Capabilities, models.DO_NOTHING, db_comment='ID de la capacidad')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'capability_persons'
        db_table_comment = 'Tabla pivote para relacionar las capacidades destacadas con las personas'


class Channels(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(unique=True, max_length=191, db_comment='Nombre del medio informativo de la Institucion')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    status = models.BooleanField(db_comment='Status del registro, 1: Activo, 0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'channels'
        db_table_comment = 'Canales o medios informativos o promocionales de la Institucion'


class ChartData(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=191)
    value = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chart_data'


class Cities(models.Model):
    name = models.CharField(max_length=191, db_comment='Nombre de la ciudad')
    state = models.ForeignKey('States', models.DO_NOTHING, db_comment='ID del Estado al que pertenece')
    capital = models.BooleanField(db_comment='Es capital del pa├¡s')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'
        db_table_comment = 'Ciudades'


class CivilStatuses(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del status civil')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'civil_statuses'
        db_table_comment = 'Estados civiles para las personas'


class ClassroomPerson(models.Model):
    classroom = models.ForeignKey('Classrooms', models.DO_NOTHING, db_comment='ID de la Infraestructura')
    person = models.ForeignKey('Persons', models.DO_NOTHING, db_comment='ID de la Persona')
    created_at = models.DateTimeField(db_comment='Fecha de creaci├│n del registro')

    class Meta:
        managed = False
        db_table = 'classroom_person'
        unique_together = (('classroom', 'person'),)
        db_table_comment = 'Tabla pivote para relacionar las Personas con las Infraestructuras'


class ClassroomTypes(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    name = models.CharField(max_length=80, db_comment='Nombre del tipo de aula')
    category = models.CharField(max_length=255, db_comment='Categoria del tipo de infraestructura')
    status = models.BooleanField(db_comment='1/true: Activo; 0/false: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classroom_types'
        unique_together = (('name', 'institution'),)
        db_table_comment = 'Tipos de Aulas de clases'


class Classrooms(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    campus = models.ForeignKey(Campuses, models.DO_NOTHING, db_comment='ID de la sede a la que pertenece el Aula')
    classroom_type = models.ForeignKey(ClassroomTypes, models.DO_NOTHING, db_comment='ID del tipo de aula al que pertenece')
    name = models.CharField(max_length=80, db_comment='Nombre del aula')
    capacity = models.SmallIntegerField(db_comment='Capacidad maxima del aula')
    description = models.CharField(max_length=191, db_comment='Descripcion detallada del aula')
    academic_offer = models.BooleanField(db_comment='1/true: Activo; 0/false: Inactivo')
    status = models.BooleanField(db_comment='1/true: Activo; 0/false: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classrooms'
        unique_together = (('name', 'campus'),)
        db_table_comment = 'Aulas de clases'


class Conditions(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion')
    name = models.CharField(max_length=191, db_comment='Nombre de la condicion')
    code = models.CharField(max_length=50, db_comment='Codigo o abreviacion de la condicion')
    type = models.CharField(max_length=255, db_comment='Funcion que cumple la condicion')
    note_approved = models.BooleanField(db_comment='Funcion que cumple sobre una Nota 1/true: Aprueba nota, 0/false: Reprueba nota')
    status = models.BooleanField(db_comment='Status de la condicion (1: Activa, 0: Inactiva)')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conditions'
        db_table_comment = 'Condiciones Academicas'


class ConflictPersons(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person = models.ForeignKey('Persons', models.DO_NOTHING)
    conflict = models.ForeignKey('Conflicts', models.DO_NOTHING, db_comment='ID del conflicto')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conflict_persons'
        db_table_comment = 'Tabla pivote para relacionar los conflictos con las personas'


class Conflicts(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del tipo de conflicto')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conflicts'
        db_table_comment = 'Tipos de conflictos que pueden afectar a las personas'


class ContactInstitutions(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    phone = models.CharField(max_length=100, db_comment='Telefono de la Institucion')
    email = models.CharField(max_length=100, db_comment='Correo de la Institucion')
    twitter = models.CharField(max_length=100, blank=True, null=True, db_comment='Correo de la Institucion')
    instagram = models.CharField(max_length=100, blank=True, null=True, db_comment='Correo de la Institucion')
    facebook = models.CharField(max_length=100, blank=True, null=True, db_comment='Correo de la Institucion')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_institutions'
        db_table_comment = 'Datos de contacto de las Instituciones educativas'


class ContactPersons(models.Model):
    person = models.ForeignKey('Persons', models.DO_NOTHING)
    name = models.CharField(max_length=191, db_comment='Nombre o identificacion de la persona')
    social_network = models.CharField(max_length=255, db_comment='Red social con la que se relaciona el registro')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_persons'
        db_table_comment = 'Contacto o redes sociales de la persona'


class Countries(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del pais')
    iso_3366_1 = models.CharField(max_length=10, db_comment='Codigo ISO 3366-1 alpha-2 para paises')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'
        db_table_comment = 'Paises'


class CourseUser(models.Model):
    course = models.ForeignKey('Courses', models.DO_NOTHING, db_comment='ID de la Materia')
    user = models.ForeignKey('Users', models.DO_NOTHING, db_comment='ID del Usuario')
    created_at = models.DateTimeField(db_comment='Fecha de creaci├│n del registro')

    class Meta:
        managed = False
        db_table = 'course_user'
        unique_together = (('course', 'user'),)
        db_table_comment = 'Tabla pivote para relacionar los Usuarios con las Materias'


class Courses(models.Model):
    program = models.ForeignKey('Programs', models.DO_NOTHING, db_comment='ID del programa')
    semester = models.ForeignKey('Semesters', models.DO_NOTHING, db_comment='ID del anio o semestre')
    area_id = models.SmallIntegerField(db_comment='ID del area en caso de que existan Areas en el Pensum')
    name = models.CharField(max_length=191, db_comment='Nombre de la Materia')
    code_course = models.CharField(max_length=20, db_comment='Codigo de materia')
    quantitative = models.CharField(max_length=255, db_comment='0: Cualitativa. 1: Cuantitativa. 2:Mixta')
    mandatory = models.BooleanField(db_comment='0/false: Electiva. 1/true: Obligatoria')
    allowed_recovery = models.BooleanField(db_comment='1/true: si se puede reparar, 0/false: No se puede reparar')
    credit_units = models.SmallIntegerField(db_comment='Unidades de Credito')
    weekly_hours = models.SmallIntegerField(db_comment='Intensidad horaria semanal en horas')
    theory_hours = models.SmallIntegerField(db_comment='Intensidad horaria total en horas')
    practical_hours = models.SmallIntegerField(db_comment='Horas Practicas')
    evaluate_close = models.BooleanField(db_comment='Evaluar para cerrar. 1/true: Si,  0/false: No')
    modules = models.SmallIntegerField(db_comment='Numero de Modulos')
    promotion = models.BooleanField(db_comment='1/true: Activo; 0/false: Inactivo')
    description = models.TextField(db_comment='Contenido Programatico o Descripcion')
    moodle_uri = models.CharField(max_length=191, db_comment='Uri a webservices de Moodle para este Programa')
    moodle_token = models.CharField(max_length=100, db_comment='Token de seguridad asociado a la URI de Moodle')
    status = models.BooleanField(db_comment='1/true: Activo; 0/false: Inactivo')

    class Meta:
        managed = False
        db_table = 'courses'
        db_table_comment = 'Materias o Asignaturas'


class Departments(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del departmento')
    telefono = models.CharField(max_length=191, db_comment='Tel├®fono del departmento')
    correo = models.CharField(max_length=191, db_comment='Correo del departmento')
    extension = models.CharField(max_length=191, db_comment='Extensi├│n telef├│nica del departmento')
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, db_comment='ID del Departamento Padre')
    campus = models.ForeignKey(Campuses, models.DO_NOTHING, blank=True, null=True, db_comment='ID del Campus')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'
        db_table_comment = 'Departamentos o dependencias de las Instituciones'


class Disabilities(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre de la discapacidad')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disabilities'
        db_table_comment = 'Discapacidades'


class DisabilityPerson(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person = models.ForeignKey('Persons', models.DO_NOTHING)
    disability = models.ForeignKey(Disabilities, models.DO_NOTHING, db_comment='ID de la discapacidad')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disability_person'
        db_table_comment = 'Tabla pivote para relacionar las discapacidades con las personas'


class DisorderPersons(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person = models.ForeignKey('Persons', models.DO_NOTHING)
    disorder = models.ForeignKey('Disorders', models.DO_NOTHING, db_comment='ID del desorden')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disorder_persons'
        db_table_comment = 'Tabla pivote para relacionar los desordenes con las personas'


class Disorders(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del desorden')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disorders'
        db_table_comment = 'Desordenes mentales o psicologicos'


class DocumentTypes(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del tipo de documento')
    validation = models.CharField(max_length=191, blank=True, null=True, db_comment='Expresion regular para validacion del documento')
    status = models.BooleanField(db_comment='Status del tipo de documento, 1: Activo, 0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_types'
        db_table_comment = 'Tipos de documento de identidad de las personas'


class EmployeeCategories(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    role_institution = models.ForeignKey('RoleInstitutions', models.DO_NOTHING, blank=True, null=True, db_comment='ID del Rol')
    name = models.CharField(unique=True, max_length=191, db_comment='Nombre de la Categoria')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_categories'
        db_table_comment = 'Categorias de Empleados'


class EmployeeCategoryInstitution(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    employee_category = models.ForeignKey(EmployeeCategories, models.DO_NOTHING, db_comment='ID de la categoria')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    name = models.CharField(unique=True, max_length=191, db_comment='Nombre de la Categoria')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_category_institution'
        db_table_comment = 'Categorias de Empleados'


class Employees(models.Model):
    person = models.ForeignKey('Persons', models.DO_NOTHING, db_comment='ID de la Persona')
    position = models.ForeignKey('Positions', models.DO_NOTHING, db_comment='ID del Cargo')
    department = models.ForeignKey(Departments, models.DO_NOTHING, db_comment='ID del Departamento')
    expediente = models.CharField(max_length=30, blank=True, null=True, db_comment='Nro de expediente')
    salary = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, db_comment='Monto de Salario')
    date_start = models.DateField(db_comment='Fecha en que comienza el cargo')
    date_end = models.DateField(blank=True, null=True, db_comment='Fecha en que culmina el cargo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'
        db_table_comment = 'Asignaci├│n de cargo de administrativo u obrero'


class EtniaGroups(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del grupo de etnias')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etnia_groups'
        db_table_comment = 'Grupos de etnias'


class EtniaPersons(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person = models.ForeignKey('Persons', models.DO_NOTHING)
    etnia = models.ForeignKey('Etnias', models.DO_NOTHING, db_comment='ID del etnia')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etnia_persons'
        db_table_comment = 'Tabla pivote para relacionar los etnias con las personas'


class Etnias(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    country = models.ForeignKey(Countries, models.DO_NOTHING, db_comment='ID del pais al que pertenece el estado')
    name = models.CharField(max_length=191, db_comment='Nombre de la Etnia')
    etnia_group = models.ForeignKey(EtniaGroups, models.DO_NOTHING, db_comment='ID de la grupo de etnias al que pertenece')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etnias'
        db_table_comment = 'Etnias indigenas'


class EventColors(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=50, db_comment='Nombre o descripcion del color')
    hexadecimal = models.CharField(max_length=7, db_comment='Codigo hexadecimal del color')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_colors'
        db_table_comment = 'Colores para las categorias o tipos de evento'


class EventTypes(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=50, db_comment='Nombre del tipo de evento')
    event_color = models.ForeignKey(EventColors, models.DO_NOTHING, db_comment='ID del color para el tipo de evento')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_types'
        db_table_comment = 'Categorias o tipos de eventos'


class Events(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    title = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField(blank=True, null=True)
    color = models.CharField(max_length=191, blank=True, null=True)
    backgroundcolor = models.CharField(db_column='backgroundColor', max_length=191, blank=True, null=True)  # Field name made lowercase.
    bordercolor = models.CharField(db_column='borderColor', max_length=191, blank=True, null=True)  # Field name made lowercase.
    textcolor = models.CharField(db_column='textColor', max_length=191, blank=True, null=True)  # Field name made lowercase.
    event_type = models.ForeignKey(EventTypes, models.DO_NOTHING)
    url = models.CharField(max_length=191, blank=True, null=True)
    allday = models.BooleanField(db_column='allDay')  # Field name made lowercase.
    classname = models.CharField(db_column='className', max_length=191, blank=True, null=True)  # Field name made lowercase.
    editable = models.BooleanField()
    starteditable = models.BooleanField(db_column='startEditable')  # Field name made lowercase.
    durationeditable = models.BooleanField(db_column='durationEditable')  # Field name made lowercase.
    resourceeditable = models.BooleanField(db_column='resourceEditable')  # Field name made lowercase.
    display = models.CharField(max_length=191)
    overlap = models.BooleanField()
    constraint = models.TextField(blank=True, null=True)  # This field type is a guess.
    source = models.CharField(max_length=191, blank=True, null=True)
    extendedprops = models.TextField(db_column='extendedProps', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'
        db_table_comment = 'Eventos definidos en el calendario'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    uuid = models.CharField(unique=True, max_length=191)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Icons(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(unique=True, max_length=50, db_comment='Nombre o descripcion del Icono')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icons'
        db_table_comment = 'Nombre de Iconos'


class IndicatorNote(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    note = models.ForeignKey('Notes', models.DO_NOTHING, db_comment='ID de la nota')
    indicator = models.ForeignKey('Indicators', models.DO_NOTHING, db_comment='ID del indicador')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicator_note'
        unique_together = (('indicator', 'note'),)
        db_table_comment = 'Indicadores por Nota'


class IndicatorTypes(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Identificador del tipo de indicador. Clave primaria')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    name = models.CharField(unique=True, max_length=191, db_comment='Nombre del tipo de indicador')
    abbreviation = models.CharField(max_length=20, db_comment='Codigo o nombre corto del tipo de indicador')
    reached = models.CharField(max_length=255, db_comment='Indica si ese tipo de indicador corresponde con un logro alcanzado')
    status = models.BooleanField(db_comment='1/true: Activo; 0/false: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicator_types'
        db_table_comment = 'Tipos de Indicadores academicos para asignar a Notas'


class Indicators(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Identificador del Indicador. Clave primaria')
    description = models.TextField(db_comment='Descripcion del indicador')
    code = models.CharField(max_length=20, db_comment='Codigo del indicador')
    indicator_type = models.ForeignKey(IndicatorTypes, models.DO_NOTHING, db_comment='Tipo de indicador')
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_comment='ID de la Materia')
    period = models.ForeignKey('Periods', models.DO_NOTHING, db_comment='Periodo Academico')
    person = models.ForeignKey('Persons', models.DO_NOTHING, db_comment='ID del Profesor')
    institution_scale_id = models.SmallIntegerField(db_comment='Escala de Notas')
    status = models.BooleanField(db_comment='1/true: Activo; 0/false: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicators'
        unique_together = (('code', 'indicator_type', 'course', 'period'),)
        db_table_comment = 'Indicadores academicos para asignar a Notas'


class InscriptionAbsences(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    schedule_section = models.ForeignKey('ScheduleSection', models.DO_NOTHING, db_comment='ID del bloque horario en el que se registra la inasistencia')
    inscription = models.ForeignKey('Inscriptions', models.DO_NOTHING, db_comment='ID de la inscripcion')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inscription_absences'
        unique_together = (('schedule_section', 'inscription'),)
        db_table_comment = 'Inasistencias por inscripcion'


class Inscriptions(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    section = models.ForeignKey('Sections', models.DO_NOTHING, db_comment='Identificador de la seccion en la que se inscribio')
    person = models.ForeignKey('Persons', models.DO_NOTHING, db_comment='ID del Estudiante inscrito')
    program = models.ForeignKey('Programs', models.DO_NOTHING, db_comment='ID de Carrera en la que se inscribe')
    period_id = models.SmallIntegerField(db_comment='Auxiliar, Periodo en el que se realizo la inscripcion')
    cedula_student = models.BigIntegerField(db_comment='Auxiliar, Cedula de Estudiante que se inscribe')
    course_id = models.IntegerField(db_comment='Auxiliar, ID de la materia inscrita')
    note = models.CharField(max_length=5, blank=True, null=True, db_comment='Nota definitiva')
    recovery = models.CharField(max_length=5, blank=True, null=True, db_comment='Nota de recuperacion')
    absences = models.SmallIntegerField(db_comment='Total acumulado de Inasistencias')
    observation = models.CharField(max_length=5, blank=True, null=True, db_comment='Observaciones')
    recovery_requested = models.CharField(max_length=255, blank=True, null=True, db_comment='Solicitudes de reparacion. 1 = El estudiante solicito reparacion.')
    recovery_granted = models.CharField(max_length=255, blank=True, null=True, db_comment='Recuperacion concedida')
    closed_notes = models.CharField(max_length=255, db_comment='Notas cerradas para modificaciones')
    mig_aux = models.CharField(max_length=50, db_comment='ID generado solo para migracion ')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inscriptions'
        unique_together = (('person', 'section'),)
        db_table_comment = 'Inscripciones'


class InstitutionCategories(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=50, db_comment='Nombre del tipo de instituciones')
    status = models.BooleanField(db_comment='Status true/1: Activo, false/0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institution_categories'
        db_table_comment = 'Tipos de instituci├│n o empresa'


class InstitutionScales(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    name = models.CharField(max_length=191, db_comment='Nombre de la Escala de Notas')
    abbreviation = models.CharField(max_length=191, db_comment='Abreviatura de la Escala de Notas')
    minimal = models.CharField(max_length=191, db_comment='Nota minima de la Institucion')
    maximal = models.CharField(max_length=191, db_comment='Nota maxima de la Institucion')
    minimal_approved = models.CharField(max_length=191, db_comment='Nota minima de aprovacion de la Institucion')
    status = models.BooleanField(db_comment='Status de la Escala de notas, 1: Activo, 0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institution_scales'
        db_table_comment = 'Escala de notas por Institucion'


class InstitutionStats(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    students_first_year = models.IntegerField(blank=True, null=True, db_comment='Cantidad de alumnos inscritos en el primer a├▒o de la universidad')
    new_students = models.IntegerField(blank=True, null=True, db_comment='Cantidad de alumnos nuevos ingresos')
    students_active = models.IntegerField(blank=True, null=True, db_comment='Cantidad de alumnos activos')
    students_inactive = models.IntegerField(blank=True, null=True, db_comment='Cantidad de alumnos inactivos')
    students_graduated = models.IntegerField(blank=True, null=True, db_comment='Cantidad de alumnos egresados')
    students_female = models.IntegerField(blank=True, null=True, db_comment='Cantidad de alumnos femeninos')
    students_male = models.IntegerField(blank=True, null=True, db_comment='Cantidad de alumnos masculinos')
    students_disabilities = models.IntegerField(blank=True, null=True, db_comment='Cantidad de alumnos discapacitados')
    students_pregnant = models.IntegerField(blank=True, null=True, db_comment='Cantidad de alumnas embarazadas')
    students_talented = models.IntegerField(blank=True, null=True, db_comment='Cantidad de alumnos con talento')
    defections = models.IntegerField(blank=True, null=True, db_comment='Cantidad de deserciones')
    teachers_total = models.IntegerField(blank=True, null=True, db_comment='Cantidad de profesores')
    instructor = models.IntegerField(blank=True, null=True, db_comment='Cantidad de Instructor')
    assistant = models.IntegerField(blank=True, null=True, db_comment='Cantidad de asistentes')
    aggregate = models.IntegerField(blank=True, null=True, db_comment='Cantidad de agregados')
    associated = models.IntegerField(blank=True, null=True, db_comment='Cantidad de asocioado')
    headline = models.IntegerField(blank=True, null=True, db_comment='Cantidad de profesores titulares')
    teaching_assistant = models.IntegerField(blank=True, null=True, db_comment='Cantidad de profesores auxiliar docente')
    research_assistant = models.IntegerField(blank=True, null=True, db_comment='Cantidad de profesores Auxiliar de Investigaci├│n')
    researchers = models.IntegerField(blank=True, null=True, db_comment='Cantidad de investigadores')
    free_teacher = models.IntegerField(blank=True, null=True, db_comment='Cantidad de docente libre')
    hired_teacher = models.IntegerField(blank=True, null=True, db_comment='Cantidad de doncente contratado')
    honorary_professors = models.IntegerField(blank=True, null=True, db_comment='Cantidad de profesor honorario')
    administrative_total = models.IntegerField(blank=True, null=True, db_comment='Cantidad de personal administrativo')
    administrative_female = models.IntegerField(blank=True, null=True, db_comment='Cantidad de personal administrativo femenino')
    administrative_male = models.IntegerField(blank=True, null=True, db_comment='Cantidad de personal administrativo masculino')
    administrative_foreign = models.IntegerField(blank=True, null=True, db_comment='Cantidad de personal administrativo extranjero')
    administrative_venezuelan = models.IntegerField(blank=True, null=True, db_comment='Cantidad de personal administrativo venezolano')
    worker = models.IntegerField(blank=True, null=True, db_comment='Cantidad de personal obrero')
    worker_female = models.IntegerField(blank=True, null=True, db_comment='Cantidad de personal obrero femenino')
    worker_male = models.IntegerField(blank=True, null=True, db_comment='Cantidad de personal obrero masculino')
    worker_active = models.IntegerField(blank=True, null=True, db_comment='Cantidad de personal obrero activo')
    transport_units = models.IntegerField(blank=True, null=True, db_comment='Cantidad de unidades totales')
    transport_units_active = models.IntegerField(blank=True, null=True, db_comment='Cantidad de unidades operativas')
    transport_units_seats = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de asientos disponibles')
    dining_rooms = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de comedores')
    dining_rooms_active = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de comedores operativos')
    diners = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de comensales')
    maintenance_digs = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de cavas de mantenimiento')
    freezing_cellars = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de cavas de congelacion')
    boilers = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de calderas')
    buildings = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de edificios')
    libraries = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de bibliotecas')
    sports_fields = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de canchas deportivas')
    auditoriums = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de auditorios')
    conference_rooms = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de Salas de conferencia')
    cultural_areas = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de areas culturales')
    classrooms = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de aulas')
    recreation_areas = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de areas de esparcimiento')
    laboratories = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de laboratorios')
    teacher_training_room = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de aulas de capacitacion docente')
    computer_room = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de sala de computacion')
    training_schools = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de escuelas de formacion')
    medical_service = models.IntegerField(blank=True, null=True, db_comment='Cantidad total de servicio medico')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institution_stats'
        db_table_comment = 'Estadisticas de las Instituciones'


class InstitutionUser(models.Model):
    institution = models.ForeignKey('Institutions', models.DO_NOTHING, db_comment='ID de la Institucion')
    user = models.ForeignKey('Users', models.DO_NOTHING, db_comment='ID del Usuario')
    created_at = models.DateTimeField(db_comment='Fecha de creaci├│n del registro')

    class Meta:
        managed = False
        db_table = 'institution_user'
        unique_together = (('institution', 'user'),)
        db_table_comment = 'Tabla pivote para relacionar los Usuarios con las Instituciones y Asignar permisos'


class Institutions(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre de la Institucion')
    abbreviation = models.CharField(max_length=191, db_comment='abreviatura de la Institucion')
    type = models.CharField(max_length=255, db_comment='tipo de universidad')
    institution_category = models.ForeignKey(InstitutionCategories, models.DO_NOTHING, blank=True, null=True, db_comment='ID de la categoria de Institucion al que pertenece')
    img_logo = models.CharField(max_length=191, blank=True, null=True, db_comment='imagen del logo')
    mission = models.TextField(db_comment='mision de la Institucion')
    vision = models.TextField(db_comment='vision de la Institucion')
    description = models.TextField(db_comment='descripcion de la Institucion')
    portal = models.CharField(max_length=191, db_comment='portal de la Institucion')
    rif = models.CharField(max_length=191, blank=True, null=True, db_comment='rif de la Institucion')
    phone = models.CharField(max_length=30, blank=True, null=True, db_comment='eslogan de la Institucion')
    slogan = models.CharField(max_length=191, blank=True, null=True, db_comment='eslogan de la Institucion')
    resolution = models.CharField(max_length=191, blank=True, null=True, db_comment='documento de la resolucion')
    img_marker = models.CharField(max_length=191, blank=True, null=True, db_comment='marcador de la Institucion')
    img_shield = models.CharField(max_length=191, blank=True, null=True, db_comment='imagen del escudo de la Institucion')
    img_cover = models.CharField(max_length=191, blank=True, null=True, db_comment='imagen de la portada de la Institucion')
    config_note = models.CharField(max_length=191, blank=True, null=True, db_comment='configuracion de nota')
    state = models.ForeignKey('States', models.DO_NOTHING, db_comment='ID del Estado al que pertenece')
    latitude = models.CharField(max_length=191, blank=True, null=True, db_comment='latitud de la institucion')
    longitude = models.CharField(max_length=191, blank=True, null=True, db_comment='longitud de la institucion')
    gazette_number = models.CharField(max_length=50, blank=True, null=True, db_comment='Drecreo y/o gaceta de la creacion de la universidad')
    file = models.CharField(max_length=191, blank=True, null=True, db_comment='Ruta del archivo de la gaceta')
    gazette_url = models.CharField(max_length=191, blank=True, null=True, db_comment='Drecreo y/o gaceta de la creacion de la universidad')
    created = models.DateField(blank=True, null=True, db_comment='fecha de inauguracion de la universidad')
    zoom = models.CharField(max_length=191, blank=True, null=True, db_comment='zoom de la institucion')
    config_recovery = models.CharField(max_length=191, blank=True, null=True, db_comment='configuracion de recuperacion')
    index_formula = models.CharField(max_length=191, blank=True, null=True, db_comment='formula de indice')
    status = models.BooleanField(db_comment='Status de la Institucion, true: Activo, false: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institutions'
        db_table_comment = 'Instituciones educativas'


class Jobs(models.Model):
    person = models.ForeignKey('Persons', models.DO_NOTHING, db_comment='Relacion con la tabla de personas')
    position = models.CharField(max_length=191, db_comment='Nombre del cargo que ocupa la persona en la Empresa')
    company = models.CharField(max_length=191, db_comment='Empresa donde ocupa ese cargo la persona')
    date_start = models.DateField(db_comment='Fecha de inicio del trabajo')
    date_end = models.DateField(blank=True, null=True, db_comment='Fecha de inicio del trabajo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'
        db_table_comment = 'Historial de trabajos de las persionas, curriculo'


class Languages(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del idioma')
    status = models.BooleanField(db_comment='Status del idioma, 1/true: Activo, 0/false: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'
        db_table_comment = 'Idiomas'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class ModelHasPermissions(models.Model):
    permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)  # The composite primary key (permission_id, model_id, model_type) found, that is not supported. The first column is selected.
    model_type = models.CharField(max_length=191)
    model_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_permissions'
        unique_together = (('permission', 'model_id', 'model_type'),)


class ModelHasRoles(models.Model):
    role = models.OneToOneField('Roles', models.DO_NOTHING, primary_key=True)  # The composite primary key (role_id, model_id, model_type) found, that is not supported. The first column is selected.
    model_type = models.CharField(max_length=191)
    model_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_roles'
        unique_together = (('role', 'model_id', 'model_type'),)


class Municipalities(models.Model):
    name = models.CharField(max_length=191, db_comment='Nombre del municipio')
    state = models.ForeignKey('States', models.DO_NOTHING, db_comment='ID del Estado al que pertenece')
    id_municipio = models.CharField(max_length=20, blank=True, null=True, db_comment='ID del municipio migracion')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipalities'
        db_table_comment = 'Municipios'


class Notes(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    inscription = models.ForeignKey(Inscriptions, models.DO_NOTHING, db_comment='Id del registro de inscripcion')
    section_module = models.ForeignKey('SectionModules', models.DO_NOTHING, db_comment='Modulo al que pertenece la nota')
    person_id = models.IntegerField(db_comment='Campo auxiliar, ID del Estudiante inscrito')
    cedula_student = models.BigIntegerField(db_comment='Campo auxiliar, Cedula del estudiante')
    person_id_prof = models.IntegerField(db_comment='ID del profesor que cargo la nota')
    person_id_emp = models.IntegerField(db_comment='ID del empleado que cargo la nota')
    person_id_prof_responsible = models.BigIntegerField(db_comment='Campo auxiliar, Cedula del profesor que cargo la nota')
    person_id_emp_responsible = models.BigIntegerField(db_comment='Campo auxiliar, En caso de que el empleado cargue o modifique la nota, se almacena su cedula')
    note = models.CharField(max_length=5, db_comment='Calificacion obtenida')
    recovery = models.CharField(max_length=5, db_comment='Calificacion de recuperacion')
    observation = models.CharField(max_length=5, db_comment='Observacion de negacion o aprobacion de la nota')
    state = models.CharField(max_length=2, db_comment='Estado del registro')

    class Meta:
        managed = False
        db_table = 'notes'
        unique_together = (('inscription', 'section_module'),)
        db_table_comment = 'Notas'


class Parishes(models.Model):
    name = models.CharField(max_length=100, db_comment='Nombre de la parroquia')
    municipality = models.ForeignKey(Municipalities, models.DO_NOTHING, db_comment='ID del municipio')
    id_municipio = models.CharField(max_length=20, db_comment='ID del municipio migracion')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parishes'
        db_table_comment = 'Parroquias'


class PasswordResetTokens(models.Model):
    email = models.CharField(primary_key=True, max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_reset_tokens'


class PaymentMethods(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(unique=True, max_length=191, db_comment='Nombre del metodo de pago')
    status = models.BooleanField(db_comment='Status del registro true/1: Activo, false/0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_methods'
        db_table_comment = 'Formas o Metodos de pago'


class PeriodProgram(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    program = models.ForeignKey('Programs', models.DO_NOTHING, db_comment='ID del Programa academico')
    period = models.ForeignKey('Periods', models.DO_NOTHING, db_comment='ID del periodo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'period_program'
        db_table_comment = 'Programas academicos aperturados por Periodo'


class Periods(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Identificador del Periodo, Clave primaria')
    institution = models.ForeignKey(Institutions, models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    name = models.CharField(max_length=191, db_comment='Nombre del periodo academico')
    code = models.CharField(max_length=30, db_comment='Codigo o nombre abreviado del Periodo Academico')
    year = models.SmallIntegerField(db_comment='A├▒o del Periodo Academico')
    order = models.SmallIntegerField(db_comment='Orden dentro del Anio')
    start_date = models.DateField(db_comment='Fecha de Inicio')
    end_date = models.DateField(db_comment='Fecha de fin')
    start_evaluations = models.DateField(db_comment='Fecha de inicio de evaluaciones')
    end_evaluations = models.DateField(db_comment='Fecha de Fin de las evaluaciones')
    start_recovery = models.DateField(db_comment='Fecha de Inicio de las Recuperaciones')
    end_recovery = models.DateField(db_comment='Fecha de Fin de las Recuperaciones')
    max_indicators = models.SmallIntegerField(db_comment='Maximo Numero de Indicadores para el Periodo')
    max_percent_absences = models.SmallIntegerField(db_comment='Porcentaje Maximo de Inasistencias para el Periodo')
    percentage_correlation = models.SmallIntegerField(db_comment='Porcentaje de Ponderacion de Las evaluaciones en el Periodo con relacion a la materia inscrita en ese Anio o Ciclo Lectivo superior')
    deadline_lists = models.DateField(db_comment='Fecha l├¡mite listas')
    resolution_number = models.CharField(max_length=191, db_comment='Nro o Identificacion de la Resolucion donde se formaliza la creacion del Periodo Academico')
    status = models.BooleanField(db_comment='1/true: Activo; 0/false: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periods'
        unique_together = (('institution', 'name', 'year'),)
        db_table_comment = 'Periodos Academicos'


class Permissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    guard_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'
        unique_together = (('name', 'guard_name'),)


class PermitPerson(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person = models.ForeignKey('Persons', models.DO_NOTHING, db_comment='ID de la Persona')
    permit = models.ForeignKey('Permits', models.DO_NOTHING, db_comment='ID del Permiso')
    details = models.CharField(max_length=191, db_comment='Detalles acerca del permiso')
    date_start = models.DateField(db_comment='Fecha en que comienza el permiso')
    date_end = models.DateField(blank=True, null=True, db_comment='Fecha en que culmina el permiso')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permit_person'
        db_table_comment = 'Permisos por persona'


class Permits(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del tipo de permiso')
    paid = models.BooleanField(db_comment='Condicion remuneratoria del tipo de permiso, 1: Remunerado, 0: No remunerado')
    status = models.BooleanField(db_comment='Status del registro true/1: Activo, false/0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permits'
        db_table_comment = 'Tipos de Permiso'


class PersonLanguages(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person = models.ForeignKey('Persons', models.DO_NOTHING, db_comment='ID de la Persona')
    language = models.ForeignKey(Languages, models.DO_NOTHING, db_comment='ID del idioma')
    reading = models.CharField(max_length=255, db_comment='Nivel de Lectura de la persona en el idioma')
    writing = models.CharField(max_length=255, db_comment='Nivel de Escritura de la persona en el idioma')
    speaking = models.CharField(max_length=255, db_comment='Nivel de Hablado de la persona en el idioma')
    certification = models.CharField(max_length=100, blank=True, null=True, db_comment='Nombre de la certificacion obtenida en el idioma')
    level = models.CharField(max_length=100, blank=True, null=True, db_comment='Nivel de la certificacion obtenida en el idioma')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_languages'
        unique_together = (('person', 'language'),)
        db_table_comment = 'Tabla pivote para relacionar los idiomas con las personas'


class PersonProfessions(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person = models.ForeignKey('Persons', models.DO_NOTHING, db_comment='ID de la Persona')
    profession = models.ForeignKey('Professions', models.DO_NOTHING, db_comment='ID de la profesion')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_professions'
        db_table_comment = 'Tabla pivote para relacionar las profesiones con las personas'


class PersonProgram(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person = models.ForeignKey('Persons', models.DO_NOTHING, db_comment='ID de la Persona Estudiante')
    program = models.ForeignKey('Programs', models.DO_NOTHING, db_comment='ID del programa asignado al estudiante')
    campus = models.ForeignKey(Campuses, models.DO_NOTHING, db_comment='ID de la Sede')
    shift = models.ForeignKey('Shifts', models.DO_NOTHING, db_comment='ID del Turno')
    resource_id = models.SmallIntegerField(db_comment='ID de la fuente de recursos para ingresar al programa')
    enrollment_code = models.CharField(max_length=20, db_comment='Codigo de Matricula')
    status = models.CharField(max_length=255, db_comment='Status de la carrera asociada al estudiante')
    academic_index = models.FloatField(blank=True, null=True, db_comment='Indice academico del estudiante en el programa')
    approved_credit_units = models.SmallIntegerField(db_comment='Total de unidades de credito aprobadas por el estudiante en el programa')
    period_id = models.SmallIntegerField(blank=True, null=True, db_comment='Periodo de Ingreso al programa')
    condition = models.CharField(max_length=5, blank=True, null=True, db_comment='Campo auxiliar')
    graduation_date = models.DateField(db_comment='Fecha de graduacion')
    observations = models.CharField(max_length=191, db_comment='Observaciones adicionales ')
    migrated = models.CharField(max_length=255, db_comment='1: Migrado, 0: NO Migrado')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_program'
        unique_together = (('person', 'program'),)
        db_table_comment = 'Programas academicos por persona'


class PersonRequirement(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    requirement = models.ForeignKey('Requirements', models.DO_NOTHING, db_comment='Id del documento')
    requirement_status = models.ForeignKey('RequirementStatuses', models.DO_NOTHING, db_comment='ID del Status del requerimiento')
    person_program = models.ForeignKey(PersonProgram, models.DO_NOTHING, db_comment='Id de la carrera asignada al estudiante')
    stated = models.BooleanField(db_comment='Requisito consignado 1/true: consignado, 0/false: Por consignar')
    file = models.CharField(max_length=191, db_comment='Ubicacion o ruta del archivo digitalizado')
    details = models.CharField(max_length=191, db_comment='Detalles adicionales del documento o requisito')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_requirement'
        unique_together = (('requirement', 'person_program'),)
        db_table_comment = 'Requisitos relacionados con los programas cursados por un estudiante'


class PersonRoles(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person = models.ForeignKey('Persons', models.DO_NOTHING)
    institution = models.ForeignKey(Institutions, models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    role_institution = models.ForeignKey('RoleInstitutions', models.DO_NOTHING, db_comment='ID del Rol con que se relaciona')
    created_at = models.DateTimeField(db_comment='Fecha de creaci├│n del registro')

    class Meta:
        managed = False
        db_table = 'person_roles'
        db_table_comment = 'Tabla pivote para relacionar las personas con los roles por institucion'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    tokenable_type = models.CharField(max_length=191)
    tokenable_id = models.BigIntegerField()
    name = models.CharField(max_length=191)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class Persons(models.Model):
    institution = models.ForeignKey(Institutions, models.DO_NOTHING, blank=True, null=True, db_comment='ID de la Institucion a la que pertenece')
    document_type = models.ForeignKey(DocumentTypes, models.DO_NOTHING)
    cedula = models.CharField(max_length=191, db_comment='Numero de Cedula o Documento de la persona')
    img_cedula = models.CharField(max_length=100, blank=True, null=True, db_comment='Imagen de cedula o documento proncipal')
    cedula_municipality_id = models.IntegerField(blank=True, null=True, db_comment='ID de la tabla Municipios donde se expide el documento')
    cedula_address = models.CharField(max_length=191, blank=True, null=True, db_comment='Direccion especifica de expedicion del documento')
    name = models.CharField(max_length=191, db_comment='Primer nombre de la persona')
    second_name = models.CharField(max_length=191, blank=True, null=True, db_comment='Segundo nombre de la persona')
    surname = models.CharField(max_length=191, db_comment='Primer apellido de la persona')
    second_surname = models.CharField(max_length=191, blank=True, null=True, db_comment='Segundo apellido de la persona')
    gender = models.CharField(max_length=255, db_comment='Sexo de la persona, M: Masculino, F: Femenino')
    birthdate = models.DateField(db_comment='Fecha de nacimiento')
    age = models.IntegerField(db_comment='Edad')
    blood = models.ForeignKey(Bloods, models.DO_NOTHING)
    civil_status = models.ForeignKey(CivilStatuses, models.DO_NOTHING)
    address_municipality_id = models.IntegerField(blank=True, null=True, db_comment='ID de la tabla Municipios donde nacio')
    address_parish_id = models.IntegerField(blank=True, null=True, db_comment='ID de la Parroquia donde reside')
    address = models.CharField(max_length=191, blank=True, null=True, db_comment='Direccion de habitacion de la persona')
    room = models.ForeignKey('Rooms', models.DO_NOTHING, blank=True, null=True, db_comment='ID de la Habitacion de la Residencia Universitaria Asignada')
    birth_municipality_id = models.IntegerField(blank=True, null=True, db_comment='ID de la tabla Municipios donde nacio')
    birth_parish_id = models.IntegerField(blank=True, null=True, db_comment='ID de la Parroquia donde nacio')
    birth_address = models.CharField(max_length=200, blank=True, null=True, db_comment='Direccion de nacimiento')
    children_number = models.SmallIntegerField(db_comment='Total de hijos')
    email = models.CharField(max_length=100, blank=True, null=True, db_comment='Correo electronico')
    phone = models.CharField(max_length=20, blank=True, null=True, db_comment='Numero de telefono')
    home_phone = models.CharField(max_length=20, blank=True, null=True, db_comment='Numero de telefono residencial')
    img_photo = models.CharField(max_length=100, blank=True, null=True, db_comment='Imagen de photo')
    register_code = models.CharField(max_length=20, blank=True, null=True, db_comment='Codigo usado para poder registrarse')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    institution_origin = models.CharField(max_length=191, blank=True, null=True, db_comment='Institucion de procedencia')
    institution_origin_type = models.CharField(max_length=255, blank=True, null=True, db_comment='Tipo de institucion de procedencia')

    class Meta:
        managed = False
        db_table = 'persons'
        db_table_comment = 'Personas'


class PositionGroups(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    employee_category = models.ForeignKey(EmployeeCategories, models.DO_NOTHING, db_comment='ID de la categoria')
    name = models.CharField(unique=True, max_length=191, db_comment='Nombre del Grupo de cargos')
    group_code = models.CharField(max_length=10, blank=True, null=True, db_comment='Codigo del Grupo de cargos')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position_groups'
        db_table_comment = 'Grupos de cargos para Empleados'


class Positions(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    position_group = models.ForeignKey(PositionGroups, models.DO_NOTHING, db_comment='ID del Grupo')
    name = models.CharField(max_length=191, db_comment='Nombre del Cargo')
    position_code = models.CharField(max_length=20, db_comment='Codigo del Cargo')
    opsu_points = models.SmallIntegerField(db_comment='Puntos segun manual de cargos')
    opsu_level = models.SmallIntegerField(db_comment='Nivel segun manual de cargos')
    status = models.BooleanField(db_comment='Status del registro true/1: Activo, false/0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'positions'
        db_table_comment = 'Cargos de Empleados'


class Professions(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre de la profesion')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professions'
        db_table_comment = 'Profesiones u Ocupaciones'


class Profiles(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del Perfil')
    status = models.BooleanField(db_comment='true: Activo; false: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'
        db_table_comment = 'Perfiles para los usuarios con rol de Empleado'


class ProgramGroups(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    campus = models.ForeignKey(Campuses, models.DO_NOTHING, blank=True, null=True, db_comment='ID del Campus')
    name = models.CharField(max_length=191, db_comment='Nombre de la facultad de la Institucion')
    abbreviation = models.CharField(max_length=191, db_comment='Abreviatura de la facultad')
    status = models.BooleanField(db_comment='Status del registro, true: Activo, false: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program_groups'
        db_table_comment = 'Facultades y Decanatos de la Institucion para agrupar los programas academicos'


class ProgramScales(models.Model):
    id = models.SmallAutoField(primary_key=True)
    institution = models.ForeignKey(Institutions, models.DO_NOTHING, db_comment='ID de la Instituci├│n')
    program = models.ForeignKey('Programs', models.DO_NOTHING, db_comment='ID del Programa')
    name = models.CharField(max_length=191, db_comment='Nombre de la escala')
    abbreviation = models.CharField(max_length=191, db_comment='Abreviatura de la escala')
    minimal = models.DecimalField(max_digits=5, decimal_places=2, db_comment='Nota m├¡nima')
    maximal = models.DecimalField(max_digits=5, decimal_places=2, db_comment='Nota m├íxima')
    minimal_approved = models.DecimalField(max_digits=5, decimal_places=2, db_comment='Nota m├¡nima aprobatoria')
    status = models.BooleanField(db_comment='Estado de la escala')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program_scales'


class ProgramUser(models.Model):
    program = models.ForeignKey('Programs', models.DO_NOTHING, db_comment='ID del Programa')
    user = models.ForeignKey('Users', models.DO_NOTHING, db_comment='ID del Usuario')
    created_at = models.DateTimeField(db_comment='Fecha de creaci├│n del registro')

    class Meta:
        managed = False
        db_table = 'program_user'
        unique_together = (('program', 'user'),)
        db_table_comment = 'Tabla pivote para relacionar los Usuarios con los Programas'


class Programs(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del programa acad├®mico o carrera')
    mention = models.CharField(max_length=191, db_comment='Menci├│n o Pensum del programa')
    abbreviation = models.CharField(max_length=30, db_comment='Nombre abreviado para el programa')
    formal_name = models.CharField(max_length=191, db_comment='Nombre para constancias y procesos formales como grados')
    program_group = models.ForeignKey(ProgramGroups, models.DO_NOTHING, db_comment='ID de la Facultad o Decanato al que pertenece el Programa')
    program_type = models.CharField(max_length=255, db_comment='Tipo de Programa o Carrera')
    modality = models.CharField(max_length=255, db_comment='Duracion de carrea de Pregrado')
    definition = models.CharField(max_length=255, db_comment='Definicion del formato para el programa')
    resolution_number = models.CharField(max_length=20, db_comment='Numero Resolucion autorizaci├│n')
    resolution_date = models.DateField(blank=True, null=True, db_comment='Fecha Resolucion autorizaci├│n')
    code = models.CharField(max_length=30, db_comment='Codigo de Aprobacion')
    pre_register = models.BooleanField(db_comment='Aplica para preinscripciones')
    groups = models.BooleanField(db_comment='Aplica para grupos')
    degree = models.BooleanField(db_comment='El programa es Conducente a Grado Academico. true: Si, false: No')
    status = models.BooleanField(db_comment='Status del programa, true: activo, false:Inactivo')
    total_credit_units = models.SmallIntegerField(db_comment='Total de UC')
    name_program = models.CharField(max_length=255, db_comment='Nombre de la Carrera en los Formatos')
    name_course = models.CharField(max_length=255, db_comment='Nombre de las Materias en los Formatos')
    moodle_uri = models.CharField(max_length=191, db_comment='Uri a webservices de Moodle para este Programa')
    moodle_token = models.CharField(max_length=100, db_comment='Token de seguridad asociado a la URI de Moodle')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programs'
        db_table_comment = 'Programas acad├®micos o Carreras'


class RequirementStatuses(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(unique=True, max_length=191, db_comment='Nombre del Status del requisito')
    status = models.BooleanField(db_comment='Status del registro 1/true: Activo, 0/false: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirement_statuses'
        db_table_comment = 'Status de los Requisitos consignados por el estudiante'


class Requirements(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(unique=True, max_length=191, db_comment='Nombre del requisito')
    mandatory = models.BooleanField(db_comment='Define si es obligatorio 1/true: Si, 0/false: No')
    by_program = models.BooleanField(db_comment='Indica si un requisito es requerido por cada carrera cursada o es un requisito unico para el estudiante (1/true: por carrera, 0/false: para cualquier carrera)')
    status = models.BooleanField(db_comment='Status del requisito, 1/true: activo, 0/false:Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirements'
        db_table_comment = 'Requisitos a consignar por el estudiante'


class Residences(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    institution = models.ForeignKey(Institutions, models.DO_NOTHING)
    campus = models.ForeignKey(Campuses, models.DO_NOTHING, blank=True, null=True)
    capacity = models.IntegerField()
    location = models.CharField(max_length=191, blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    kitchens = models.IntegerField()
    dining_rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    common_kitchen = models.BooleanField()
    common_dining_room = models.BooleanField()
    common_bathroom = models.BooleanField()
    details = models.CharField(max_length=191, blank=True, null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'residences'


class Resources(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre de la fuente de recursos')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resources'
        db_table_comment = 'Fuentes de recursos utilizadas por las personas para ingresar a un programa academico'


class RoleHasPermissions(models.Model):
    permission = models.OneToOneField(Permissions, models.DO_NOTHING, primary_key=True)  # The composite primary key (permission_id, role_id) found, that is not supported. The first column is selected.
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_has_permissions'
        unique_together = (('permission', 'role'),)


class RoleInstitutions(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    campus = models.ForeignKey(Campuses, models.DO_NOTHING, blank=True, null=True, db_comment='ID del Campus')
    name = models.CharField(max_length=191, db_comment='Nombre del rol')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_institutions'
        db_table_comment = 'Tipos de roles para los usuarios de las instituciones'


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    guard_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'
        unique_together = (('name', 'guard_name'),)


class Rooms(models.Model):
    residence = models.ForeignKey(Residences, models.DO_NOTHING)
    room_number = models.CharField(unique=True, max_length=191)
    capacity = models.IntegerField()
    details = models.CharField(max_length=191)
    status = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rooms'


class ScheduleSection(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    section = models.ForeignKey('Sections', models.DO_NOTHING, db_comment='ID de la Seccion')
    schedule = models.ForeignKey('Schedules', models.DO_NOTHING, db_comment='ID del Bloque horario')
    classroom = models.ForeignKey(Classrooms, models.DO_NOTHING, db_comment='ID del aula')
    day = models.CharField(max_length=255, db_comment='Dias de la semana empezando por Domingo 0:Domingo, 6:Sabado')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule_section'
        unique_together = (('section', 'schedule'),)
        db_table_comment = 'Horarios por Seccion'


class Schedules(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey(Institutions, models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    start_hour = models.SmallIntegerField(db_comment='Hora de inicio del bloque en formato militar')
    end_hour = models.SmallIntegerField(db_comment='Hora de fin del bloque en formato militar')
    status = models.BooleanField(db_comment='Status del registro true/1: Activo, false/0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedules'
        db_table_comment = 'Bloques Horarios de las Instituciones'


class ScholarshipPaymentDates(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey(Institutions, models.DO_NOTHING, db_comment='ID de la institucion')
    campus = models.ForeignKey(Campuses, models.DO_NOTHING, blank=True, null=True, db_comment='ID del Campus')
    name = models.CharField(max_length=80, db_comment='Nombre de la nomina')
    fecha_pago = models.DateField(db_comment='Fecha en que se paga o ejecuta la beca')
    retroactivo = models.SmallIntegerField(db_comment='id de la nomina raiz')
    retroactivo_monto = models.DecimalField(max_digits=10, decimal_places=2, db_comment='monto a pagar por concepto de retroactivo')
    status = models.BooleanField(db_comment='Estado actual de la Fecha de Pago')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scholarship_payment_dates'
        db_table_comment = 'Datos de pago de las becas asignadas a estudiantes'


class ScholarshipPayments(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    scholarship_payment_date = models.ForeignKey(ScholarshipPaymentDates, models.DO_NOTHING, db_comment='ID de la fecha de Pago')
    person_program = models.ForeignKey(PersonProgram, models.DO_NOTHING, db_comment='id en la tabla de carreras del estudiante')
    scholarship_type = models.ForeignKey('ScholarshipTypes', models.DO_NOTHING, db_comment='ID del tipo de beca asignada al estudiante')
    bank = models.ForeignKey(Banks, models.DO_NOTHING, db_comment='ID del banco donde el estudiante tiene cuenta')
    numero_cuenta = models.CharField(max_length=20, db_comment='Numero de cuenta bancario del estudiante')
    monto = models.DecimalField(max_digits=10, decimal_places=2, db_comment='Monto a Cobrar en la Beca')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scholarship_payments'
        db_table_comment = 'Tipos de Beca'


class ScholarshipStudent(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person_program = models.ForeignKey(PersonProgram, models.DO_NOTHING, db_comment='ID en la tabla de carreras del estudiante')
    scholarship_type = models.ForeignKey('ScholarshipTypes', models.DO_NOTHING, db_comment='ID del tipo de beca asignada al estudiante')
    bank_id = models.SmallIntegerField(blank=True, null=True, db_comment='ID del Banco')
    numero_cuenta = models.CharField(max_length=20, db_comment='N├║mero de cuenta bancaria del estudiante')
    fecha_asignada = models.DateField(blank=True, null=True, db_comment='Fecha en que se le asigna la beca')
    suspendida = models.BooleanField(db_comment='Resultado de la validaci├│n: true = Suspendida, false = Validada.')
    fecha_suspendida = models.DateField(blank=True, null=True, db_comment='Fecha en que se suspende la Beca')
    status = models.BooleanField(db_comment='Estado actual de la Beca')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scholarship_student'
        db_table_comment = 'Becas asignadas a estudiantes'


class ScholarshipTypes(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey(Institutions, models.DO_NOTHING, db_comment='ID de la Institucion')
    campus = models.ForeignKey(Campuses, models.DO_NOTHING, blank=True, null=True, db_comment='ID del Campus')
    name = models.CharField(max_length=80, db_comment='Nombre del tipo de Beca')
    abreviatura = models.CharField(max_length=20, db_comment='Nombre abreviado del Tipo de Beca')
    indice = models.DecimalField(max_digits=8, decimal_places=2, db_comment='Indice Academico minimo para obtener la Beca')
    porcentaje_uc = models.SmallIntegerField(db_comment='Porcentaje de UC aprobadas requeridas para obtener la beca')
    monto = models.DecimalField(max_digits=10, decimal_places=2, db_comment='Monto a Cobrar en la Beca')
    status = models.BooleanField(db_comment='Status del Tipo de Beca 1: Activo, 0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scholarship_types'
        unique_together = (('name', 'institution'),)
        db_table_comment = 'Tipos de Beca'


class SectionModules(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    section = models.ForeignKey('Sections', models.DO_NOTHING)
    module = models.CharField(max_length=191, db_comment='Nombre o Descripcion corta del Modulo')
    percent = models.SmallIntegerField(db_comment='Porcentaje de la Nota a evaluar en este Modulo')
    order = models.SmallIntegerField(db_comment='Orden del Modulo al visualizar las notas')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section_modules'
        db_table_comment = 'Modulos por seccion'


class Sections(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    period = models.ForeignKey(Periods, models.DO_NOTHING, db_comment='ID del Periodo Academico')
    semester = models.ForeignKey('Semesters', models.DO_NOTHING, db_comment='ID del Semestre')
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_comment='ID de la Materia')
    campus = models.ForeignKey(Campuses, models.DO_NOTHING, db_comment='ID de la sede')
    condition = models.ForeignKey(Conditions, models.DO_NOTHING, db_comment='ID de la Condicion')
    shift = models.ForeignKey('Shifts', models.DO_NOTHING, db_comment='ID del Turno')
    teacher_id = models.IntegerField(db_comment='ID del Profesor Responsable')
    name = models.CharField(max_length=50, db_comment='Nombre o descripcion para la seccion')
    capacity = models.SmallIntegerField(db_comment='Cantidad de Estudiantes permitidos')
    modules = models.SmallIntegerField(db_comment='Modulos a cargar')
    evalutation_type = models.SmallIntegerField(db_comment='Tipo de Evaluacion a realizar')
    status = models.BooleanField(db_comment='1/true: Activo; 0/false: Inactivo')
    moodle_course_id = models.BigIntegerField(db_comment='ID del curso en plataforma Moodle ')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sections'
        unique_together = (('course', 'period', 'campus', 'condition', 'shift', 'name'),)
        db_table_comment = 'Secciones ofertadas'


class Semesters(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    program = models.ForeignKey(Programs, models.DO_NOTHING, db_comment='ID del programa o carrera al que pertenece el semestre')
    order = models.SmallIntegerField(db_comment='Ordenamiento del semestre')
    name = models.CharField(max_length=150, db_comment='Nombre del a├▒o o semestre')
    status = models.BooleanField(db_comment='1/true: Activo; 0/false: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semesters'
        unique_together = (('name', 'program'),)
        db_table_comment = 'A├▒os o Semestres en los que se dividen los Programas Academicos'


class Sessions(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    user_id = models.BigIntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    payload = models.TextField()
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Shifts(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    institution = models.ForeignKey(Institutions, models.DO_NOTHING, db_comment='ID de la Institucion a la que pertenece')
    name = models.CharField(max_length=191, db_comment='Nombre del Turno')
    abbreviation = models.CharField(max_length=191, db_comment='Detalle del Turno')
    status = models.BooleanField(db_comment='Status del registro true/1: Activo, false/0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shifts'
        db_table_comment = 'Turnos de las Instituciones'


class States(models.Model):
    country = models.ForeignKey(Countries, models.DO_NOTHING, db_comment='ID del pais al que pertenece el estado')
    name = models.CharField(max_length=191, db_comment='Nombre del estado')
    iso_3366_2 = models.CharField(max_length=10, db_comment='Codigo ISO para principales subdivisiones de los paises')
    category = models.CharField(max_length=191, blank=True, null=True, db_comment='Nombre de la categoria')
    zoom = models.CharField(max_length=191, blank=True, null=True, db_comment='zoom del estado')
    region = models.CharField(max_length=191, blank=True, null=True, db_comment='Nombre de la region')
    latitude_center = models.CharField(max_length=191, blank=True, null=True, db_comment='Latitud para centrar el mapa con respecto al estado')
    longitude_center = models.CharField(max_length=191, blank=True, null=True, db_comment='Longitud para centrar el mapa con respecto al estado')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'
        db_table_comment = 'Estados, Provincias o Departamentos'


class Students(models.Model):
    person = models.ForeignKey(Persons, models.DO_NOTHING, db_comment='ID de la Persona')
    campus = models.ForeignKey(Campuses, models.DO_NOTHING, blank=True, null=True, db_comment='ID del Campus')
    status = models.BooleanField(db_comment='Status del registro true/1: Activo, false/0: Inactivo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class Supplies(models.Model):
    id = models.SmallAutoField(primary_key=True)
    residence = models.ForeignKey(Residences, models.DO_NOTHING)
    name = models.CharField(max_length=191)
    type = models.CharField(max_length=191)
    quantity = models.IntegerField()
    monthly_supplies = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplies'


class TeacherDedications(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del tipo de dedicacion')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher_dedications'
        db_table_comment = 'Tipos de dedicacion o contrato de profesores'


class TeacherLevels(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191, db_comment='Nombre del escalafon o nivel del profesor')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher_levels'
        db_table_comment = 'Escalafones o Niveles de profesores'


class Teachers(models.Model):
    id = models.SmallAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    person = models.ForeignKey(Persons, models.DO_NOTHING, db_comment='ID de la persona')
    teacher_level = models.ForeignKey(TeacherLevels, models.DO_NOTHING, db_comment='ID del Escalafon')
    teacher_dedication = models.ForeignKey(TeacherDedications, models.DO_NOTHING, db_comment='ID del tipo de Dedicacion')
    date_start = models.DateField(db_comment='Fecha en que comienza el cargo')
    date_end = models.DateField(blank=True, null=True, db_comment='Fecha en que culmina el cargo')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teachers'
        db_table_comment = 'Asignacion de funciones de Profesor'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Clave primaria de la tabla')
    name = models.CharField(max_length=191)
    email = models.CharField(unique=True, max_length=191)
    password = models.CharField(max_length=191)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    person_id = models.BigIntegerField(blank=True, null=True, db_comment='ID de la tabla de personas')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
