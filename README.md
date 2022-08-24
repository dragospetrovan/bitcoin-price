This repo has the code for 2 applications named bitcoin-price and rest-api which are suppose to run on a kubernetes cluser. 

prerequisite:
    - azure acount 
    - azure cli loggend into the azure account
    - helm3 and https://charts.helm.sh/stable added (helm repo add stable https://charts.helm.sh/stable\n)
    - kubectl


to deploy the cluster run:
aks-engine deploy --dns-prefix dragos-k8s --resource-group dragos-k8s --location FranceCentral --api-model aks/kubernetes-calico-azure.json

this will dpeploy a one node cluster in your azure account.

After the k8s is up and running export the kubeconfig path

export KUBECONFIG=$PWD/_output/dragos-k8s/kubeconfig/kubeconfig.francecentral.json


Install nginx ingress

helm install nginx-ingress stable/nginx-ingress    --set rbac.create=true

Add the docker registry secret

kubectl  create secret docker-registry acr-secret \
    --docker-server=dragosRegistry.azurecr.io \
    --docker-username=5d6cbf44-67fd-40f2-b378-bafd0b4d375c \
    --docker-password=9928Q~j1UfZh5ehKdepJZSl7UXYHdEd3XTI_La4V


Create the 2 namespaces
kubectl create ns bitcoin-price
kubectl create ns rest-api

deploy the services and the ingress

kubectl create -f ./bitcoin_price.yaml
kubectl create -f ./bitcoin_price_ingress.yaml

kubectl create -f ./rest_api.yaml
kubectl create - ./rest_api_ingress.yaml



To test you have to get the nginx ingress IP, and point in your /etc/hosts the ip to bitcoin-price.test.ogfg.link and to rest-api.test.ogfg.link

to deploy the services you can run deploy_all.sh