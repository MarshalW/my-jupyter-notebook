[[Obsidian]]

## 基本使用设置

### 设置

- 设置为 ”源码模式“，写 markdown 直观
- 启用大纲视图，方便切换
- 可打开核心插件 “幻灯片”，通过 `---` 拆分，会增加 “开始演示” 菜单条
- 设置当前模版时间，快捷键，cmd+shift+z
- 设置日记，打开/新建今天日记，快捷键，cmd+shift+j

### 使用

- 对最近要持续几天写的笔记 - 加星
- 内部链接，是 obsidian 重要的组成部分
- 反向链接，谁链接了当前笔记 - 是 obsidian 最有用的功能之一
- 将提到当前文件名的笔记内容，转化为内链
- 使用工作区，保存当前打开的笔记页面等布局
- [[在 Obsidian 中使用数学符号]]
- [[Obsidian 使用图表]] - Obsidian 自带对图表的支持，通过 Mermaid
- 在当前笔记中引用其他笔记的部分内容：`![[Some note#some heading]]`
- cmd+shift+v, 复制纯文本
- 怎样引用其他 vault 的笔记:
	- `[note in other vault](obsidian://vault/other_vault/note)`
	- https://forum.obsidian.md/t/is-there-a-way-to-quickly-link-to-another-vault/20652
- 一个观点是，尽量少用标签
  - 标签用来，已读，未读等状态信息
  - 用双链取代标签
  - 见：https://forum-zh.obsidian.md/t/topic/440/8

### 快捷键

- 切换编辑模式/预览模式，cmd+e
- 插入 markdown 链接，cmd+k
- 查看关系图谱，cmd+g

## 怎么同步 

### iCloud

[[iCloud]]

- 使用 iCloud, iPhone/iPad/macOS 之间同步
- 需要
	- 先在 iOS 设备上创建 iCloud vault，设置为 store in iCloud
	- 然后在 macOS 的 iCloud/obsidian/xxx 打开
	- 如果在 iOS 设备创建新的文件，可能需要在 macOS finder "现在下载"
		- macOS 的 obsidian App 不能读取未下载的文件，即使在 finder 中可见
 - 问题
	 -  不能端到端加密
  

### 其他

-  LiveSync? - 需要准备一个 couchDB 库
- Remotely save
- oneDrive?

## 概念


## 插件

- [[obsidian 导出 word 格式]]

## 疑问

- [?] 怎么自动美化 markdown 文件
- [x] 怎么使用标签 - 用于临时标记，比如 todo
- [ ] 笔记别名，内链别名
- [ ] 怎样使用嵌套标签
- [ ] 模版是干啥用的 - 插入模版
- [x] 工作区？
- [ ] 总结内链 `[[]]`
- [ ] 移动笔记到其他目录下的情况
- [x] 使用数学符号 `$$a^2=b^2+c^2$$`, `$$\begin{aligned} a\\ b\\ c \end{aligned} $$`
- [ ] 插入图片和多媒体文件
- [x] 使用图表：Obsidian 通过 [Mermaid](https://mermaid-js.github.io/) 生成图表
- [ ] 使用第三方插件，思维导图，https://github.com/MarkMindCkm/obsidian-markmind
- [ ] 阅读 [Obsidian教程二](https://zhuanlan.zhihu.com/p/492199426) - 有很多示例可以总结出来


## 存在的问题

-  不支持 HEIC 图片格式， 造成，使用 iphone 复制的hei图片无法显示 [
HEIC Image Format Support](https://forum.obsidian.md/t/heic-image-format-support/4934) 







