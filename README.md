# drf-vue-element-admin
# 系统演示
![image](https://github.com/mattF76/drf-vue-element-admin/blob/main/pics/login.png)
![image](https://github.com/mattF76/drf-vue-element-admin/blob/main/pics/account.png)
![image](https://github.com/mattF76/drf-vue-element-admin/blob/main/pics/role.png)
![image](https://github.com/mattF76/drf-vue-element-admin/blob/main/pics/permission.png)
![image](https://github.com/mattF76/drf-vue-element-admin/blob/main/pics/django%20admin.png)

# 运行
进入后端项目backend目录，运行`docker-compose up --build`即可。浏览器访问http://127.0.0.1:9080/  
系统登录的账号需要先进入django admin在Account创建一个admin账号。  
django admin后台账户需要进入api容器，运行`python manage.py createsuperuser`创建账号。django admin访问地址是http://127.0.0.1:9080/admin/  

# 开发
## 后端本地开发运行
进入backend目录，修改setting.py，选择使用sqlite数据库，注释掉mysql数据库。  
```
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }
```
运行`python manage.py runserver`启动后端。  
## 前端本地开发运行
进入front目录，运行`npm run dev`。  
根据对应需求，修改vue.config.js中这部分代码。若前端mocks后端接口，则无需设置proxy部分配置。
```
  // 本地开发，前端mocks接口
  // devServer: {
  //   host: "localhost",
  //   port: port,
  //   open: true,
  //   overlay: {
  //     warnings: false,
  //     errors: true
  //   },
  //   before: require('./mock/mock-server.js')
  // },

  // 本地开发，前端联调后端接口
  devServer: {
    host: "localhost",
    port: port,
    open: true,
    overlay: {
      warnings: false,
      errors: true
    },
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        ws: true,
        changeOrigin: true
      }
    },
  },
```
## 生产环境部署
进入front目录，运行`npm run build:prod`。把在dist目录生成的前端代码复制到backend/deployment/nginx/vue目录下。  

修改backend/mattAdmin/setting.py，选择使用mysql数据库。  
运行`docker-compose up --build`，构建镜像，启动容器。