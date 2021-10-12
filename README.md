# map_generator
## 作者的话
这些是我为了实践并提升c语言及python水平而尝试完成的一个项目，希望它对你们有帮助。
## 程序清单
1. map_generator.exe ----- 生成配置文件和输出文件供渲染
2. map_render.exe ----- 把输出文件以配置文件中的对应关系渲染为图片
## 程序介绍
运行C程序 ***map_generator***，会在当前目录下生成一个输出文件(export.txt)，文件中会有一些随机的数字，用空格隔开。如果当前目录下的配置文件不存在，
则会生成一个默认配置文件(config.txt)。配置文件中，说明了数字与贴图文件名的对应关系。当然，你也可以更改它成为自定义配置。

运行python程序 ***map_render***，程序会在当前目录的texture文件夹内，寻找config文件中所对应的文件名，再读取当前目录的export.txt, 按照配置文件中所描述的对应关系
渲染为图片并显示。
## 运行源代码文件
下载.c后缀的c语言文件，通过gcc,tcc,visual C 等编译器编译后运行，推荐使用c99标准。map_render.py按照一般的python文件方法运行即可，
你需要确保生成的 ***config.txt*** 、 ***export.txt*** 与map_render.py在同级目录下，
## 运行打包后的exe文件(in releases)
下载 ***releases***中的压缩包，解压此压缩包并打开，先运行map_generator.exe,再运行map_render.exe。
## 高级
### 运行参数
这些参数可作用于生成输入文件。在运行 ***map_generator*** 程序时可以加上这些参数。
例如:  map_generator.exe -l 30 -w 30 -t 10

-l 长度（默认30）
-w 宽度（默认30）
-t 转换后元素类型数量   （默认10，例如-t 3 ,则生成的输入文件只会有 0、1、2这三种数字）
![运行实例](https://i.loli.net/2021/10/02/u3sPVJe2y5KgnTj.png)
### 自定义贴图
把贴图存放在 ***map_render*** 程序所在目录下的  ***texture*** 文件夹内，并在config.txt文件中把对应的贴图文件名(带后缀)写在数字后，以空格隔开

