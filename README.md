# map_generator
## 作者的话
这些是我为了实践并提升c语言水平而尝试完成的一个项目，希望它对你们有帮助。
## 程序介绍
运行C程序，会生成一个输入文件，文件中会有一些随机的数字，用空格隔开。如果当前目录下的配置文件(config.txt)不存在，
则会生成一个默认配置文件。配置文件中，说明了数字与字符的对应关系。当然，你也可以更改它成为自定义配置。
## 运行
下载.c后缀的c语言文件，通过gcc,tcc,visual C 等编译器编译后运行即可，推荐使用c99标准。
## 运行参数
这些参数可作用于生成输入文件。在运行程序时加上这些参数即可。
例如:  map_generator.exe -l 30 -w 30 -t 10

-l 长度（默认30）
-w 宽度（默认30）
-t 转换后元素类型数量   （默认10，例如-t 3 ,则生成的输入文件只会有 0、1、2这三种数字）
