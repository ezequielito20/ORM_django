from django.db import models
from datetime import date

from django.utils.text import slugify


class ModeloAuditoria(models.Model):
    fecha_crea = models.DateTimeField(auto_now_add=True)
    fecha_modifica = models.DateTimeField(auto_now=True)
    
    ACTIVO = 'Activo'
    INACTIVO = 'Inactivo'
    ESTADO_OPCIONES = [
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inactivo'),
    ]
    
    estado = models.CharField(max_length=8, choices=ESTADO_OPCIONES, default=ACTIVO)
    activo = models.BooleanField(default=True)
    
    
    class Meta:
        abstract = True

class Categoria(ModeloAuditoria):
    # nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=50, unique=True)
    

    # lo que se mostrara cuando se imprime el objeto
    def __str__(self):
        return self.descripcion
    
    # sobrescribimos save para que la descripcion se guarde en mayusculas porque asi lo deseamos
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()
        
    # definimos el nombre en plural del modelo
    class Meta:
        # esto es para que si estas trabajando con el admin de Django se muestre en plural el modelo
        verbose_name_plural = "Categorias"
        
class Persona(ModeloAuditoria):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    # definimos el nombre en plural del modelo
    
    @property
    def edad(self):
        today = date.today()
        age = today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return age
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
    def save(self):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()
        super(Persona, self).save()

    class Meta:
        verbose_name_plural = "Personas"
        
class Animal(ModeloAuditoria):
    nombre = models.CharField(max_length=50)
    patas = models.IntegerField(default=2)
    
    def __str__(self):
        return self.nombre
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Animal, self).save()
    
    class Meta:
        verbose_name_plural = "Animales"
        
class Libro(ModeloAuditoria):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(default=1, help_text='En Dolares')
    peso = models.PositiveIntegerField(help_text='En Libras')
    TIPOS = [('virtual','virtual'),('fisico','fisico')]
    tipo = models.CharField(max_length=7, choices=TIPOS, default='virtual')
    url = models.URLField(default=None,help_text='URL del libro')
    
    def __str__(self):
        return self.nombre+' '+self.tipo
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Libro, self).save()
    
    class Meta:
        verbose_name_plural = "Libros"
        
        # agregar condiciones de unique pero que combinen e involucren dos campos se usa:
        unique_together = (('nombre', 'tipo'),)
        
class Progenitor(ModeloAuditoria):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    padre = models.CharField(max_length=50)
    madre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.persona + ' - ' + self.padre + ' - ' + self.madre
    
    class Meta:
        verbose_name_plural = "Progenitores"
        
        
class Padre(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Padres"

class Hijo(models.Model):
    nombre = models.CharField(max_length=50)
    padre = models.ForeignKey(Padre, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre+' hijo de '+self.padre.nombre
    
    class Meta:
        verbose_name_plural = "Hijos"

class Publicacion(ModeloAuditoria):
    titulo = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, default='', unique=True)
    
    def __str__(self):
        return self.titulo
    
    def save(self):
        self.slug = slugify(self.titulo)
        super(Publicacion, self).save()
    
    class Meta:
        verbose_name_plural = "Publicaciones"

class Articulo(ModeloAuditoria):
    titular  = models.CharField(max_length=50)
    publicaciones = models.ManyToManyField(Publicacion, related_name='articulos')
    
    def __str__(self):
        return self.titular
    
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nombre 
    
    class Meta:
        verbose_name_plural = "Empleados"
        
class Employee(models.Model):
    nombre = models.CharField(max_length=50)
    supervisor = models.ForeignKey('app1.Employee', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nombre 
    
    class Meta:
        verbose_name_plural = "Empleados"

class NuevoNombre(models.Model):
    nombre = models.CharField(max_length=50)
    a = models.CharField(max_length=50, 
                        db_column='nombre_columna',
                        default='')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'el_nombre_que_se_guarda'
        
class Unico(models.Model):
    nombre = models.CharField(max_length=50)
    
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)
    
    @classmethod
    def truncate(cls):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE %s CASCADE' % cls._meta.db_table)    