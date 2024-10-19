#!/bin/bash

echo "Сборка Docker-образа..."
make build

echo "Пуш Docker-образа в реестр..."
make push

echo "Перезапуск подов в Kubernetes..."
make restart

echo "Проверка состояния подов..."
kubectl get pods

echo "Готово!"
