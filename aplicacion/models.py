from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Producto(models.Model):
    bicicleta = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    talla = models.CharField(max_length=15, choices=[
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
    ])
    aro = models.CharField(max_length=15, choices=[
        ('26', '26'),
        ('27.5', '27.5'),
        ('29', '29'),
    ])
    precio = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(999999999)])
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self): 
        return f"{self.marca} {self.modelo} ({self.talla})"

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombusuario = models.CharField(max_length=20, null=False)
    correo_electronico = models.EmailField(unique=True, null=False)
    pwd = models.CharField(max_length=128, null=False)  # La longitud debe ser suficiente para almacenar hashes de contraseñas

    def __str__(self):
        return self.nombusuario


class Arriendo(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    deposito_garantia = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    cantidad_dias = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()

    def __str__(self):
        return f"Arriendo de {self.producto} por {self.usuario}"
