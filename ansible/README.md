# ansible 

https://cn-ansibledoc.readthedocs.io/zh_CN/latest/

https://ansible.leops.cn/dev/plugins/Inventory-csv/

https://xiaorui.cc/archives/category/ansible

https://lotabout.me/2020/Ansible-Introduction/

https://itcn.blog/p/542797859.html

### 资产清单

https://segmentfault.com/a/1190000039142973

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
ansible -i '10.10.2.6, 10.10.2.4' -m ping all

ansible -i inventory all -m ping
```

#### Dynamic Inventory 

```bash
python3 dynamic_inventory.py --

```

### Ansible API

https://www.361way.com/ansible-api/4446.html
