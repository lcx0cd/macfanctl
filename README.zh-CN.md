# macfanctl

`macfanctl` 是一个运行在 macOS 上的无界面风扇控制桥。

[English README](README.md)

它不点击 UI，不依赖界面自动化。它直接写入 `Macs Fan Control` 的 `ActivePreset`，
再把 `Macs Fan Control` 以隐藏方式重启，从而复用它已经安装好的提权 helper，
给别的热管理程序、菜单栏工具、桌宠或自动化脚本提供一个干净的 CLI。

## 这个项目为什么存在

- 现在的固态存储和内存贵得像黄金
- 高温会伤害昂贵的存储环境
- `Mac mini` 自带风扇反而是便宜得多的消耗件
- 在大约 `1800 RPM` 时，`Mac mini` 的风扇几乎听不到
- 如果能用几乎听不到的噪音和风扇寿命，去换更好的外接 SSD 热管理，这笔账是成立的

一句话版本：

> 风扇比存储便宜太多了。  
> 如果 `1800 RPM` 几乎听不到，那就应该优先消费风扇寿命，而不是消费昂贵存储的寿命和稳定性。

## 它做什么

- 提供 `auto / fixed / status / raw` 这几个简单命令
- 把固定转速编码成 `Macs Fan Control` 使用的 `ActivePreset`
- 以隐藏方式启动 `Macs Fan Control`
- 避免把 GUI 当成自动化接口

## 命令

```bash
macfanctl status
macfanctl auto
macfanctl fixed 1800
macfanctl raw Unsaved:VU5TQVZFRHwxLDE4MDA=
```

## 本地使用

不安装也可以直接运行：

```bash
/Users/lvchuanxin/macfanctl/bin/macfanctl status
/Users/lvchuanxin/macfanctl/bin/macfanctl fixed 1800
/Users/lvchuanxin/macfanctl/bin/macfanctl auto
```

可编辑安装：

```bash
cd /Users/lvchuanxin/macfanctl
python3 -m pip install -e .
macfanctl status
```

## 当前模型

- `auto`
  - 写入 `Predefined:0`
- `fixed <rpm>`
  - 把 `UNSAVED|1,<rpm>` 编码成 `Macs Fan Control` 的 `ActivePreset`
- `status`
  - 读取当前 preset，并尽量解码成可读状态

## 依赖

- macOS
- `/Applications/Macs Fan Control.app`
- 为隐藏 app 进程授予辅助功能权限

## 备注

- 当前主要针对单风扇 `Mac mini` 一类设备
- 这个项目没有去硬逆向私有 SMC 写入接口
- 它选择复用 `Macs Fan Control` 已有的 helper，把真正值得开源的部分收敛成一个小而稳的 CLI
