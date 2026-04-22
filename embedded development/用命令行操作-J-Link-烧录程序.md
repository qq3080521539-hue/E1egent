---
title: 用命令行操作 J-Link 烧录程序
date: 2026-04-19
source: 抖音视频 - 嵌入式开发小技能，怎么用命令行操作 J-LINK 烧录程序
video_url: https://v.douyin.com/J9fy0OxlbNk/
author: 电流秩序
tags:
  - 嵌入式开发
  - J-Link
  - 烧录程序
  - 命令行
  - 自动化
aliases:
  - J-Link 命令行操作
  - J-Link 自动化烧录
cssclass:
  - wide-page
---

# 用命令行操作 J-Link 烧录程序

> [!info] 笔记信息
> - 📅 **整理时间**：2026-04-19
> - 🎯 **适用场景**：嵌入式开发、自动化烧录、量产烧录
> - 🎬 **视频作者**：电流秩序
> - 🏷️ **关键词**：J-Link、命令行、烧录程序、自动化

---

## 为什么要用命令行操作 J-Link？

> [!important] 核心优势
>
> 1. **方便 AI 自动化调用**：可以通过脚本自动化烧录流程
> 2. **烧录命令可嵌入脚本**：集成到 CI/CD 流水线中
> 3. **适用于研发和生产阶段**：
>    - 研发阶段：快速调试、自动化测试
>    - 生产阶段：批量烧录、统一流程

---

## 操作步骤

### 1. 安装 J-Link 驱动

首先需要安装 J-Link 驱动程序：

1. 访问 SEGGER 官网下载 J-Link 软件包：
   - https://www.segger.com/downloads/jlink/
2. 下载并安装与你系统对应的版本（Windows/Linux/macOS）
3. 安装完成后，检查安装目录

### 2. 添加环境变量

将 J-Link 的安装目录添加到系统环境变量中：

**Windows 系统**：
```
1. 右键 "此电脑" → 属性 → 高级系统设置 → 环境变量
2. 在 "系统变量" 中找到 "Path"，点击编辑
3. 添加 J-Link 安装目录，例如：
   - C:\Program Files\SEGGER\JLink\
4. 点击确定保存
5. 重启命令行窗口验证
```

**验证安装**：
```powershell
# 打开命令行，输入：
JLinkExe -v
# 应该显示 J-Link 版本信息
```

### 3. 编写脚本文件

创建一个 J-Link 脚本文件（通常以 `.jlink` 结尾）：

**示例脚本：`flash.jlink`**
```jlink
# 选择目标芯片
device STM32F103C8

# 选择接口类型（SWD或JTAG）
if SWD
speed 4000

# 连接目标
connect

# 擦除 Flash
erase

# 加载程序文件
loadfile program.hex

# 复位并运行
r
g

# 退出
qc
```

### 4. 在命令行调用 J-Link 程序

**Windows 命令行**：
```powershell
# 基本命令格式
JLinkExe -Device STM32F103C8 -If SWD -Speed 4000 -CommanderScript flash.jlink

# 或者使用简写
JLinkExe flash.jlink
```

**Linux/macOS 终端**：
```bash
# 基本命令格式
JLinkExe -Device STM32F103C8 -If SWD -Speed 4000 -CommanderScript flash.jlink
```

---

## 完整示例

### Windows PowerShell 自动化脚本

创建 `flash_stm32.ps1`：
```powershell
# J-Link 命令行烧录脚本
Write-Host "开始烧录程序..."

# 设置路径
$jlinkPath = "C:\Program Files\SEGGER\JLink\JLinkExe.exe"
$scriptFile = "flash.jlink"
$hexFile = "program.hex"

# 检查文件是否存在
if (-Not (Test-Path $hexFile)) {
    Write-Host "错误：找不到程序文件 $hexFile" -ForegroundColor Red
    exit 1
}

if (-Not (Test-Path $scriptFile)) {
    Write-Host "错误：找不到脚本文件 $scriptFile" -ForegroundColor Red
    exit 1
}

# 执行烧录
Write-Host "正在烧录..." -ForegroundColor Yellow
& $jlinkPath -Device STM32F103C8 -If SWD -Speed 4000 -CommanderScript $scriptFile

# 检查执行结果
if ($LASTEXITCODE -eq 0) {
    Write-Host "烧录成功！" -ForegroundColor Green
} else {
    Write-Host "烧录失败！错误代码：$LASTEXITCODE" -ForegroundColor Red
}
```

### Windows 批处理脚本

创建 `flash.bat`：
```batch
@echo off
echo 开始烧录程序...

REM 设置路径
set JLINK_PATH="C:\Program Files\SEGGER\JLink\JLinkExe.exe"
set SCRIPT_FILE=flash.jlink
set HEX_FILE=program.hex

REM 检查文件是否存在
if not exist %HEX_FILE% (
    echo 错误：找不到程序文件 %HEX_FILE%
    pause
    exit /b 1
)

if not exist %SCRIPT_FILE% (
    echo 错误：找不到脚本文件 %SCRIPT_FILE%
    pause
    exit /b 1
)

REM 执行烧录
echo 正在烧录...
%JLINK_PATH% -Device STM32F103C8 -If SWD -Speed 4000 -CommanderScript %SCRIPT_FILE%

REM 检查执行结果
if %ERRORLEVEL% EQU 0 (
    echo 烧录成功！
) else (
    echo 烧录失败！错误代码：%ERRORLEVEL%
)

pause
```

### Linux/macOS Shell 脚本

创建 `flash.sh`：
```bash
#!/bin/bash
echo "开始烧录程序..."

# 设置路径
JLINK_PATH="JLinkExe"
SCRIPT_FILE="flash.jlink"
HEX_FILE="program.hex"

# 检查文件是否存在
if [ ! -f "$HEX_FILE" ]; then
    echo "错误：找不到程序文件 $HEX_FILE"
    exit 1
fi

if [ ! -f "$SCRIPT_FILE" ]; then
    echo "错误：找不到脚本文件 $SCRIPT_FILE"
    exit 1
fi

# 执行烧录
echo "正在烧录..."
$JLINK_PATH -Device STM32F103C8 -If SWD -Speed 4000 -CommanderScript $SCRIPT_FILE

# 检查执行结果
if [ $? -eq 0 ]; then
    echo "烧录成功！"
else
    echo "烧录失败！错误代码：$?"
fi
```

---

## J-Link 常用命令

### 基本连接命令

```jlink
# 选择目标芯片
device STM32F103C8
device ATSAMD21G18
device nRF52840

# 选择接口
if SWD        # 使用 SWD 接口
if JTAG       # 使用 JTAG 接口

# 设置速度
speed 1000   # 1000 kHz
speed 4000   # 4000 kHz
speed auto   # 自动适配

# 连接目标
connect
```

### Flash 操作命令

```jlink
# 擦除操作
erase              # 擦除整片 Flash
erase <addr> <len> # 擦除指定范围
erase sector <sector> # 擦除指定扇区

# 加载程序
loadfile <file>    # 加载文件（支持 .hex, .bin, .elf）
loadbin <file> <addr> # 加载二进制文件到指定地址
loadfile <file> <addr> # 加载文件到指定地址

# 读取 Flash
savebin <file> <addr> <len> # 保存指定范围的 Flash 内容
```

### 运行控制命令

```jlink
# 复位
r
reset

# 运行
g
go

# 停止
h
halt

# 单步执行
s
step
```

### 内存操作命令

```jlink
# 读取内存
w4 <addr> <value>  # 写入 32 位数据
w2 <addr> <value>  # 写入 16 位数据
w1 <addr> <value>  # 写入 8 位数据

# 读取内存
mem <addr> <len>   # 读取内存
mdw <addr> <len>   # 以 32 位显示内存
mdh <addr> <len>   # 以 16 位显示内存
mdb <addr> <len>   # 以 8 位显示内存
```

### 退出命令

```jlink
# 退出
q
quit
qc               # 退出并关闭连接
exit
```

---

## 不同芯片的配置示例

### STM32 系列

**STM32F103C8**：
```jlink
device STM32F103C8
if SWD
speed 4000
connect
erase
loadfile program.hex
r
g
qc
```

**STM32F407VG**：
```jlink
device STM32F407VG
if SWD
speed 4000
connect
erase
loadfile program.hex
r
g
qc
```

### ATmega 系列

**ATmega328P**：
```jlink
device ATmega328P
if JTAG
speed 1000
connect
erase
loadfile program.hex
r
g
qc
```

### nRF5 系列

**nRF52840**：
```jlink
device nRF52840_xxAA
if SWD
speed 4000
connect
erase
loadfile program.hex
r
g
qc
```

---

## 常见问题排查

### 1. 找不到 JLinkExe 命令

**问题**：命令行提示 `'JLinkExe' 不是内部或外部命令`

**解决**：
```
1. 确认 J-Link 是否正确安装
2. 检查环境变量 Path 是否包含 J-Link 安装目录
3. 重启命令行窗口
4. 使用绝对路径调用，例如：
   "C:\Program Files\SEGGER\JLink\JLinkExe.exe"
```

### 2. 连接失败

**问题**：提示找不到设备或连接失败

**检查**：
```
1. J-Link 是否正确连接到电脑
2. 目标芯片是否正确连接到 J-Link
3. 接口选择是否正确（SWD/JTAG）
4. 设备名称是否正确
5. 尝试降低连接速度
```

### 3. 擦除或烧录失败

**问题**：擦除或烧录过程中出错

**解决**：
```
1. 检查目标芯片供电是否正常
2. 确认 Flash 保护位是否设置
3. 尝试降低连接速度
4. 使用完整擦除而不是扇区擦除
5. 检查程序文件格式是否正确（.hex/.bin）
```

---

## 高级用法

### 1. 批量烧录脚本

创建 `batch_flash.bat`：
```batch
@echo off
echo 开始批量烧录...

set JLINK_PATH="C:\Program Files\SEGGER\JLink\JLinkExe.exe"
set SCRIPT_FILE=flash.jlink
set COUNT=0

:loop
echo.
echo ======================================
echo 准备烧录第 %COUNT% 个设备...
echo 请连接设备，按任意键继续...
pause > nul

%JLINK_PATH% -Device STM32F103C8 -If SWD -Speed 4000 -CommanderScript %SCRIPT_FILE%

if %ERRORLEVEL% EQU 0 (
    echo 第 %COUNT% 个设备烧录成功！
    set /a COUNT+=1
) else (
    echo 第 %COUNT% 个设备烧录失败！
)

echo.
echo 继续烧录下一个？(Y/N)
set /p choice=
if /i "%choice%"=="Y" goto loop

echo.
echo 批量烧录完成！共烧录 %COUNT% 个设备。
pause
```

### 2. 集成到 CI/CD 流水线

可以将 J-Link 命令行操作集成到 GitHub Actions、GitLab CI 等 CI/CD 平台中，实现自动化编译和烧录。

**GitHub Actions 示例**：
```yaml
name: Flash Firmware
on: [push]
jobs:
  build-and-flash:
    runs-on: [self-hosted, windows]
    steps:
      - uses: actions/checkout@v3
      
      - name: Build Firmware
        run: make
      
      - name: Flash Firmware
        run: |
          JLinkExe -Device STM32F103C8 -If SWD -Speed 4000 -CommanderScript flash.jlink
```

---

## 总结

> [!important] 核心要点
>
> 1. **安装配置**：
>    - 安装 J-Link 驱动
>    - 添加环境变量
>
> 2. **脚本编写**：
>    - 选择目标芯片
>    - 配置接口和速度
>    - 编写擦除、加载、运行流程
>
> 3. **命令调用**：
>    - 使用 JLinkExe 命令
>    - 指定脚本文件
>    - 自动化集成
>
> 4. **适用场景**：
>    - 研发阶段：快速调试
>    - 生产阶段：批量烧录
>    - AI 自动化：脚本集成

---

*📝 笔记说明：基于"嵌入式开发小技能，怎么用命令行操作 J-LINK 烧录程序"抖音视频整理，结合评论区核心内容和 J-Link 官方文档系统梳理。*

