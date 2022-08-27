# ansible 

### 资产清单

有时候是 hosts 

```shell
cat > inventory << 'EOF'
192.168.20.1

[all:vars]
ansible_connection=ssh
ansible_user=root
EOF
```


```shell
ansible -i inventory all -m ping
```

