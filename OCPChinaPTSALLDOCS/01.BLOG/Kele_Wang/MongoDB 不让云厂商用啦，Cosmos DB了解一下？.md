前段时间开源数据库界很热闹，大家都纷纷跳出来指责云厂商使用代码但是不回馈社区。MongoDB更是直接换了开源许可证不让云厂商使用了。
https://www.sohu.com/a/260120443_465914

MongoDB还想上云咋办，除了用MongoDB自己的Atlas之外，微软Azure还有个Cosmos DB了解一下？完全兼容MongoDB，并且轻松跨Region全球部署。

接下来我们用CosmosDB替换MongoDB搭MEAN栈的Web服务器

# 部署Cosmos DB
登陆Azure Portal，搜索MongoDB，可以看到直接就有一个Database as a service for MongoDB啦，这其实就是Cosmos DB的Mongo API版

**创建Cosmos DB**

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/MongoDB%20%E4%B8%8D%E8%AE%A9%E4%BA%91%E5%8E%82%E5%95%86%E7%94%A8%E5%95%A6%EF%BC%8CCosmos%20DB%E4%BA%86%E8%A7%A3%E4%B8%80%E4%B8%8B%EF%BC%9F01.webp)

按照界面填好设置点击Review+Create简单两部就创建好了

**创建Cosmos DB**

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/MongoDB%20%E4%B8%8D%E8%AE%A9%E4%BA%91%E5%8E%82%E5%95%86%E7%94%A8%E5%95%A6%EF%BC%8CCosmos%20DB%E4%BA%86%E8%A7%A3%E4%B8%80%E4%B8%8B%EF%BC%9F02.webp)

点击Connection String记录数据库连接信息

**image.png**

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/MongoDB%20%E4%B8%8D%E8%AE%A9%E4%BA%91%E5%8E%82%E5%95%86%E7%94%A8%E5%95%A6%EF%BC%8CCosmos%20DB%E4%BA%86%E8%A7%A3%E4%B8%80%E4%B8%8B%EF%BC%9F03.webp)

接下来我们可以创建数据库test

**创建数据库**

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/MongoDB%20%E4%B8%8D%E8%AE%A9%E4%BA%91%E5%8E%82%E5%95%86%E7%94%A8%E5%95%A6%EF%BC%8CCosmos%20DB%E4%BA%86%E8%A7%A3%E4%B8%80%E4%B8%8B%EF%BC%9F04.webp)

数据库建好，接下来就可以搭Web服务器了。我们这次使用的是Ubuntu 18.04

# 安装Node.js
```
sudo apt-get install -y nodejs
```

# 设置服务器
首先还需要安装body-parser包，用来处理请求中的JSON

安装npm包管理器以及正文分析包
```
sudo apt-get install npm
sudo npm install body-parser
```

创建名为Books的文件夹，在该文件夹中建立server.js文件，内容如下
```
var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());
require('./apps/routes')(app);
app.set('port', 3300);
app.listen(app.get('port'), function() {
    console.log('Server up: http://localhost:' + app.get('port'));
});
```

# 安装 Express 并设置服务器的路由
Express 是一个微型的灵活 Node.js Web 应用程序框架，为 Web 和移动应用程序提供功能。 本教程使用 Express 将书籍信息传入和传出 MongoDB 数据库。 Mongoose 提供简洁的基于架构的解决方案来为应用程序数据建模。 本教程使用 Mongoose 来为数据库提供书籍架构。

安装 Express 和 Mongoose。
```
sudo npm install express mongoose
```

在 Books 文件夹中，创建名为 apps 的文件夹，并添加包含所定义的 Express 路由的、名为 routes.js 的文件。
```
var Book = require('./models/book');
module.exports = function(app) {
  app.get('/book', function(req, res) {
    Book.find({}, function(err, result) {
      if ( err ) throw err;
      res.json(result);
    });
  }); 
  app.post('/book', function(req, res) {
    var book = new Book( {
      name:req.body.name,
      isbn:req.body.isbn,
      author:req.body.author,
      pages:req.body.pages
    });
    book.save(function(err, result) {
      if ( err ) throw err;
      res.json( {
        message:"Successfully added book",
        book:result
      });
    });
  });
  app.delete("/book/:isbn", function(req, res) {
    Book.findOneAndRemove(req.query, function(err, result) {
      if ( err ) throw err;
      res.json( {
        message: "Successfully deleted the book",
        book: result
      });
    });
  });
  var path = require('path');
  app.get('*', function(req, res) {
    res.sendfile(path.join(__dirname + '/public', 'index.html'));
  });
};
```

在 apps 文件夹中，创建名为 models 的文件夹，并添加包含所定义的书籍模型配置的、名为 book.js 的文件。将其中的mongodb连接串替换成之前创建的。
```
var mongoose = require('mongoose');
mongoose.connect('mongodb://kelemongodbtest.documents.azure.cn:10255/test?ssl=true&replicaSet=globaldb',{
        auth:{
                user:'kelemongodbtest',
                password:'2vsIXLu1aVyrnxpcjrKGOdzA2n7dwgKmfTEpD3XyckNMpu8mAVQK48oCEjJZVMeMsQTurjEVxMZvDZOvA0gM5Q=='
        }
        });
mongoose.connection;
mongoose.set('debug', true);
var bookSchema = mongoose.Schema( {
  name: String,
  isbn: {type: String, index: true},
  author: String,
  pages: Number
});
var Book = mongoose.model('Book', bookSchema);
module.exports = mongoose.model('Book', bookSchema);
```

# 使用 AngularJS 访问路由
AngularJS 提供一个 Web 框架用于在 Web 应用程序中创建动态视图。 本教程使用 AngularJS 将网页与 Express 相连接，并针对书籍数据库执行操作。

将目录切换回到 Books (cd ../..)，然后创建名为 public 的文件夹，并添加包含所定义的控制器配置的、名为 script.js 的文件。
```
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http) {
  $http( {
    method: 'GET',
    url: '/book'
  }).then(function successCallback(response) {
    $scope.books = response.data;
  }, function errorCallback(response) {
    console.log('Error: ' + response);
  });
  $scope.del_book = function(book) {
    $http( {
      method: 'DELETE',
      url: '/book/:isbn',
      params: {'isbn': book.isbn}
    }).then(function successCallback(response) {
      console.log(response);
    }, function errorCallback(response) {
      console.log('Error: ' + response);
    });
  };
  $scope.add_book = function() {
    var body = '{ "name": "' + $scope.Name + 
    '", "isbn": "' + $scope.Isbn +
    '", "author": "' + $scope.Author + 
    '", "pages": "' + $scope.Pages + '" }';
    $http({
      method: 'POST',
      url: '/book',
      data: body
    }).then(function successCallback(response) {
      console.log(response);
    }, function errorCallback(response) {
      console.log('Error: ' + response);
    });
  };
});
```

在 public 文件夹中，创建包含所定义的网页的、名为 index.html 的文件。
```
<!doctype html>
<html ng-app="myApp" ng-controller="myCtrl">
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular.min.js"></script>
    <script src="script.js"></script>
  </head>
  <body>
    <div>
      <table>
        <tr>
          <td>Name:</td> 
          <td><input type="text" ng-model="Name"></td>
        </tr>
        <tr>
          <td>Isbn:</td>
          <td><input type="text" ng-model="Isbn"></td>
        </tr>
        <tr>
          <td>Author:</td> 
          <td><input type="text" ng-model="Author"></td>
        </tr>
        <tr>
          <td>Pages:</td>
          <td><input type="number" ng-model="Pages"></td>
        </tr>
      </table>
      <button ng-click="add_book()">Add</button>
    </div>
    <hr>
    <div>
      <table>
        <tr>
          <th>Name</th>
          <th>Isbn</th>
          <th>Author</th>
          <th>Pages</th>
        </tr>
        <tr ng-repeat="book in books">
          <td><input type="button" value="Delete" data-ng-click="del_book(book)"></td>
          <td>{{book.name}}</td>
          <td>{{book.isbn}}</td>
          <td>{{book.author}}</td>
          <td>{{book.pages}}</td>
        </tr>
      </table>
    </div>
  </body>
</html>
```

# 运行应用程序
将目录切换回到 Books (cd ..)，并通过运行以下命令启动服务器：
```
nodejs server.js
```

打开 Web 浏览器并导航到针对 VM 记录的地址。 例如，http://13.72.77.9:3300。 应显示以下页面所示的内容：

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/MongoDB%20%E4%B8%8D%E8%AE%A9%E4%BA%91%E5%8E%82%E5%95%86%E7%94%A8%E5%95%A6%EF%BC%8CCosmos%20DB%E4%BA%86%E8%A7%A3%E4%B8%80%E4%B8%8B%EF%BC%9F05.webp)

刷新页面之后能看到书已经添加成功了

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/MongoDB%20%E4%B8%8D%E8%AE%A9%E4%BA%91%E5%8E%82%E5%95%86%E7%94%A8%E5%95%A6%EF%BC%8CCosmos%20DB%E4%BA%86%E8%A7%A3%E4%B8%80%E4%B8%8B%EF%BC%9F06.webp)

回到Data Explorer，也能看到数据库里面已经有了。

![images](https://github.com/CohenLyon/OCPChinaPTSALLDOCS/blob/patch-1/01.BLOG/images/MongoDB%20%E4%B8%8D%E8%AE%A9%E4%BA%91%E5%8E%82%E5%95%86%E7%94%A8%E5%95%A6%EF%BC%8CCosmos%20DB%E4%BA%86%E8%A7%A3%E4%B8%80%E4%B8%8B%EF%BC%9F07.webp)

# 总结
所以虽然MongoDB现在已经收紧了开源的License，但是微软的Azure上我们还是有对应的产品能够满足大家的需求，并且CosmosDB还有一些其他的特性，比如全球部署，精确定义好的一致性级别。更多信息可以去https://docs.azure.cn/zh-cn/cosmos-db/ 查看

# 参考资料
https://docs.azure.cn/zh-cn/virtual-machines/linux/tutorial-mean-stack
