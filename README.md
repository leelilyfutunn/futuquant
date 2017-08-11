# futuquant document

gh-pages分支是由mkdocs生成的文档，不需要手动修改，可以用以下方式自动生成。

### mkdocs安装

``` python
pip install mkdocs
```

(在master分支下)

### 生成文档

```
mkdocs build --clean
```

生成的文档位于site文件夹下。

### 本地预览

```
mkdocs serve
```

即可在浏览器中，通过127.0.0.1:8000查看文档。

(gh-pages分支gh )

### 文档更新

将site文件夹下的内容复制到根目录，即完成文档的更新。