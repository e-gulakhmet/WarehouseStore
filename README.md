# WarehouseStore
Service that synchronize Orders in the Store with Orders in the Warehouse

---

Docker is used to run services.
So just run the command:
```shell
docker-compose up
```

---

### Create admin

Store:
```shell
docker exec -it store.1 python manage.py createsuperuser
```

Warehouse:
```shell
docker exec -it warehouse.1 python manage.py createsuperuser
```

### Dump default Store and Warehouse accounts based on services that specified in docker-compose:

Warehouse:
```shell
docker exec warehouse.1 python manage.py loaddata warehouse_1.json
```

Store:
```shell
docker exec store.1 python manage.py loaddata store_1.json
```

### Using:

Store service: `http://0.0.0.0:8001/admin/`

Warehouse service: `http://0.0.0.0:8000/admin/`
