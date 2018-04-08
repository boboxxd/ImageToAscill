# ImageToAscill

若是pip没有安装，可以使用命令`sudo easy_install pip`（保证mac连接互联网）

安装pip之后，可以使用命令`sudo pip install PIL`来安装操作图片的模块了。

若是安装正常，那皆大欢喜了。在我电脑安装时，却出现了问题。

*could not find a version that satisfies the requirement PIL.(form versions:)*
*No matching distribution found for PIL.*

这个是说明PIL已经找不到，其实现在已经用Pillow代替了PIL，在使用方面没有不同，API都是相同的。
既然如此，咱们就直接安装Pillow模块吧，执行`sudo pip install Pillow`

安装这个模块时，发现它会依赖另外一个模块：multiprocessing
只能先把multiprocessing模块安装好再执行上面的命令了，`sudo pip install multiprocessing`即可正常安装，非常小的一个模块

接着再执行sudo pip install Pillow命令，就可以正常安装模块了，自动安装好之后，就可以正常使用了。
使用时需要注意的是引入模块要按照下面的方式写（注意大小写）

第一种：`from PIL import Image`
第二种：from PIL.Image(用这种方式时，下面使用时也得写成PIL.Image.open('1.png')，个人觉得不太好看，可以在引入时修改下模块名，如`from PIL.Image as image`)
