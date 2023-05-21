# Prueba Técnica Django Backend Developer Getxerpa- Patricio Espinoza

## Instalación y Ejecución via Docker

1. Clonar repositorio del proyecto
```
git clone https://github.com/espinozapato/test-getxerpa-2.git
```
2. Ejecutar Docker Compose
```
docker-compose up
```
3. Cargar App 
```
http://127.0.0.1:8000/
```

## Instalación y Ejecución Localmente

1. Clonar repositorio del proyecto
```
git clone https://github.com/espinozapato/test-getxerpa-2.git
```
2. Instalar Python Version 3.x

3. Instalar dependencias
```
pip install -r requirements.txt
```
4. Ejecutamos la Aplicación
```
python manage.py runserver
```
5. Cargar App 
```
http://127.0.0.1:8000/
```

## EndPoints App

-   CRUD Categorias [GET, POST, PUT, DELETE]
```
/categorias/
```
-   CRUD Transacción [GET, POST, PUT, DELETE]
```
/transacciones/
```

-   Filtros Categorias 
```
/categorias/?filter=exceeds-limit
```
```
/categorias/?filter=not-exceeds-limit
```

## Ejecutar Tests

```
python manage.py test
```

## Postman Workspace - Collection

```
test-getxerpa-2.postman_collection
```