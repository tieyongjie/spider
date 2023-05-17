# spider
this is test spider in docker 
## kubernetes常用命令

### 1.获取节点

```shell
kubectl get nodes
```

### 2.使用Docker Desktop创建的Kubernetes的Context名作叫做docker-desktop

```shell
kubectl config use-context docker-desktop
```

### 3.查看namespace,会列出所有的namespace,都是k8s内置的

```shell
kubectl get namespaces
```

### 4.创建一个service的namespace

```shell
kubectl create namespace service
```

### 5.定义一个Deployment对象

创建文件deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: testserver
  namespace: service
  labels:
    app: testserver
spec:
  replicas: 3
  selector:
    matchLabels:
      app: testserver
  template:
    metadata:
      labels:
        app: testserver
    spec:
      containers:
        - name: testserver
          image: germey/testserver
          ports:
            - containerPort: 80
```

### 6.deployment定义之后,运行

```shell
kubectl apply -f deployment.yaml
```

运行之后会有下列结果,已经运行成功

deployment.app/testservice created

### 7.获取对应namespace下pod运行状态,显示结果如下

```shell
kubectl get pod -n service
```

```
NAME                         READY   STATUS    RESTARTS        AGE
testserver-84754df7c-cfmf8   1/1     Running   1 (4h22m ago)   11h
testserver-84754df7c-gvm85   1/1     Running   1 (4h22m ago)   11h
testserver-84754df7c-jzzsq   1/1     Running   1 (4h22m ago)   11h

```

可以看到创建了三个pod,(replicas指定参数为3),都是running状态

### 8.声明一个service对象,文件名为service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: testserver
  namespace: service
spec:
  type: NodePort
  selector:
    app: testserver
  ports:
    - protocol: TCP
      port: 8888
      targetPort: 80
```

可以采用端口转发的方式将kuberneters中的service转发到本机的某个端口上面

```shell
kubectl port-forward service/testserver 9999:8888 -n service

# 显示结果如下
Forwarding from 127.0.0.1:9999 -> 80
Forwarding from [::1]:9999 -> 80
```

输出的其实是9999映射到80端口,这里显示的容器的端口

### 9.查看deployment信息

```shell
# 查看service的deployment信息
kubectl get deployment -n service
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
testserver   3/3     3            3           32h
# 删除deployment配置
kubectl delete deployment testserver -n service
# 提示如下 deployment.apps "testserver" deleted
```

### 10.查看pod日志信息

查看100条日志

```shell
kubectl logs --tail=100 accountpool-7d45b9dfc9-2jkgx -n crawler
```

### 11.删除命名空间

```shell
kubectl delete ns [namespace]
```

### 12.pod扩容

```
kubectl scale deployment/nginx-deployment  --replicas=2  -n default
```

```shell
$ kubectl get deployment -n service
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
testserver   3/3     3            3           10m
# 指定控制器名称，指定扩容pod的数量扩容
$ kubectl scale deployment/testserver --replicas=5 -n service
deployment.apps/testserver scaled
# 执行之后输出结果如下
deployment.apps/testserver scaled
$ kubectl get deployment -n service
# 输出结果如下
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
testserver   5/5     5            5           11m

```

