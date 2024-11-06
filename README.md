## Challenge_Cybersecurity_-_Prex

Este proyecto consiste en una aplicación que recolecta información del sistema y la envía a una API para su almacenamiento y consulta.

### Funcionalidades


### Buenas Practicas de la APP.

* Estructura de un proyecto base (API REST)
* Implementación de controllers, service, storage y adapters usando buenas prácticas
* Implementación de buenas prácticas de desarrollo: manejo de errores, dataclasses, logs, etc.
* Utiliza Bearer Token en los endpoint el token esta en el .env , menos en el del healtcheck.
* La aplicación está configurada para recopilar información del sistema cada 24 horas utilizando la libreria BackgroundScheduler.
* Podes modificar la frecuencia de recolección en el código.

* **Agente:** Recopila información del sistema, como:
    * Información del procesador
    * Procesos en ejecución
    * Usuarios con sesión activa
    * Nombre y versión del sistema operativo
* **API:** 
    * Recibe la información del agente y la almacena en una base de datos PostgreSQL.
    * Ofrece tres endpoints:
        * `'/ping'` (GET): Devuelve un "pong" como healthcheck de la aplicacion.
        * `/information_system` (POST): Recibe la información del agente.
        * `/information_system/<ip>` (GET): Consulta la información almacenada por IP.

### Requerimientos

* AWS EC2 (Ubuntu)
* SSH
* Clave SSH (.pem)
* Git
* PostgreSQL
* Python 3
* `virtualenv`
* `pip`

### Instalación y ejecución

**1. Configuración de la instancia EC2:**

* Crea una instancia EC2 Ubuntu con la capa gratuita.
* Configura los Security Groups para permitir el acceso SSH solo desde tu IP.
* Conéctate a la instancia por SSH:

```bash
ssh -i "/ruta/a/tu/prex.pem" ubuntu@<tu_ip_publica>
```

* Instala las dependencias:

```bash
sudo apt update
sudo apt install git postgresql postgresql-contrib
```

* Inicia PostgreSQL y verifica su estado:

```bash
sudo systemctl start postgresql
sudo systemctl status postgresql
```

* Accede a la línea de comandos de PostgreSQL:

```bash
sudo -u postgres psql
```

**2. Configuración del proyecto:**

* Clona el repositorio:

```bash
git clone git@github.com:f-jzito/Challenge_Cybersecurity_-_Prex.git
cd Challenge_Cybersecurity_-_Prex/
```

* Crea y configura el archivo `.env` con las credenciales de la base de datos.

* Crea un entorno virtual e instala las dependencias:

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt
```

**3. Ejecución de la aplicación:**

* Ejecuta la aplicación:

```bash
python3 run.py
```

* La aplicación recopilará la información del sistema y la enviará a la API.

**4. Uso de la API:**

* Envía información del sistema al endpoint `/information_system` usando una herramienta como Postman.
* Consulta la información almacenada por IP usando el endpoint `/information_system/<ip>`.

### Visualización de la información

* Puedes usar pgAdmin4 para conectarte a la base de datos y visualizar la información almacenada.
* La API también proporciona un endpoint para consultar la información por IP.

### Ejemplos de uso

* **Enviar información del sistema:**

```
POST /information_system HTTP/1.1
Content-Type: application/json

{
  "procesador": "...",
  "procesos": "...",
  ...
}
```

* **Consultar información por IP:**

```
GET /information_system/192.168.1.36 HTTP/1.1
```

### Capturas de pantalla


![image](https://github.com/user-attachments/assets/35042c38-e96a-49ad-a062-d2be4bb9d0bd)

![image](https://github.com/user-attachments/assets/48af0e88-317b-4e48-8a51-83fb11cfce11)

Informacion del agente obtenida y enviada a la API.
![image](https://github.com/user-attachments/assets/a2c49d38-b491-4f43-bb7f-784dec556601)

Buscamos en la DB creada en aws.

![image](https://github.com/user-attachments/assets/9b81540a-6191-4772-93d0-b319e05b3722)

![image](https://github.com/user-attachments/assets/dd60b7d6-20da-4f45-aae1-e1eb648dd479)

Entramos a pgAdmin4 para validar si existe la db:

![image](https://github.com/user-attachments/assets/996cbcce-c6fb-495c-a85c-c4cb557b5638)


Se crea la tabla, obtiene todos los datos del agente que va a correr cada 1 dia y guardar todos los datos de este cliente en la db utilizando el siguiente esquema ejecutando el endpoint http://127.0.0.1:8080/information_system [POST] con su respectivo body.

![image](https://github.com/user-attachments/assets/401dcb80-1778-46d8-83da-3f87233f129a)

![image](https://github.com/user-attachments/assets/d1f6404c-8f1f-438d-8710-6e7921bbed45)

![image](https://github.com/user-attachments/assets/2dd63e78-661c-453f-8fba-8123fa4f3473)



<img width="1336" alt="image" src="https://github.com/user-attachments/assets/4ffac429-3e68-4b27-a779-0762e33f92f0">
timestamp:
1.

<img width="1297" alt="image" src="https://github.com/user-attachments/assets/c2b65db3-2ed5-4c08-a03f-992600b59909">

2.

<img width="836" alt="image" src="https://github.com/user-attachments/assets/f19a0562-6b07-4b5a-9c47-cb66088086df">



La diferencia de registros.


Este README mejorado proporciona una descripción más clara y concisa del proyecto, incluyendo las funcionalidades, los requerimientos, la instalación, la ejecución y ejemplos de uso. También se han añadido secciones para las capturas de pantalla y las notas adicionales.







