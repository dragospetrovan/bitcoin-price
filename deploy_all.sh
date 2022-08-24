#!/bin/bash


aks-engine deploy --dns-prefix dragos-k8s --resource-group dragos-k8s --location FranceCentral --api-model aks/kubernetes-calico-azure.json
export KUBECONFIG=$PWD/_output/dragos-k8s/kubeconfig/kubeconfig.francecentral.json

helm repo add stable https://charts.helm.sh/stable
helm repo update
helm install nginx-ingress stable/nginx-ingress  --set rbac.create=true

kubectl  create secret docker-registry acr-secret \
    --docker-server=dragosRegistry.azurecr.io \
    --docker-username=5d6cbf44-67fd-40f2-b378-bafd0b4d375c \
    --docker-password=9928Q~j1UfZh5ehKdepJZSl7UXYHdEd3XTI_La4V

kubectl create ns bitcoin-price
kubectl create ns rest-api

kubectl create -f ./aks/bitcoin_price.yaml
kubectl create -f ./aks/bitcoin_price_ingress.yaml

kubectl create -f ./aks/rest_api.yaml
kubectl create -f ./aks/rest_api_ingress.yaml
