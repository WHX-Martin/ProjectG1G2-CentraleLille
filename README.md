# ProjectG1G2 — Presets Correction

> Centrale Lille · Projet G1G2

舞台灯具（grandMA3 / MVR）**预设值测量与校正工具**。

由于灯具实际安装位置与理论位置存在偏差，加上 pan/tilt 机械响应的非线性，直接使用理论算出的
preset 会出现打偏。本项目通过传感器实测数据，用**最小二乘法**反解出灯具的真实位置偏移与
朝向误差，并输出修正后的 preset。

---

## 功能

程序为图形界面，共 5 个标签页，按顺序使用即可完成一次完整校正：

| 标签页 | 功能 |
| --- | --- |
| **Select Model** | 选择/新建灯具模型。模型描述 tilt 的理论值→实际值映射：<br>`y = ax + b (x >= 0)`、`y = cx + d (x < 0)`，参数保存在 `data/data.json` |
| **Presets To Excel** | 批量读取 XML preset 文件，导出为 Excel 表格 |
| **MVR To Config** | 解析 `.mvr` 场景文件，导出 config Excel（灯具理论位置、旋转矩阵等） |
| **Correction** | 核心步骤。输入 config、传感器实测数据、待修正 preset，计算误差并输出修正结果 |
| **Excel To Presets** | 把修正后的 Excel 数据写回 XML preset |

## 目录结构

```
├── Modif_fichier_preset/          # 主程序（GUI 与应用逻辑）
│   ├── ui_start.py                # ★ 程序入口
│   ├── ui_Interface.py            # 界面逻辑 + 各功能实现
│   ├── Interface.ui               # Qt Designer 界面源文件
│   ├── new_interface.py           # 界面代码（新版，未启用）
│   ├── GUI.py / read_excel.py / read_preset.py
│   │                              # 旧版 tkinter 界面（Change Presets V1.0）
│   ├── readConfig.py              # 读取 config Excel（Sensors / Spotlights 表）
│   ├── Read_mvr.py                # 解压并解析 .mvr 场景文件
│   ├── create_config.py           # 生成 config Excel 模板
│   └── presets_change/            # preset 修改后的输出目录
├── calcul_erreur/                 # 误差计算与最小二乘求解
│   ├── resolution.py              # ★ 当前使用的求解算法
│   ├── change_angle.py            # 旋转矩阵与角度变换工具
│   ├── corrige.py                 # 校正流程编排（tilt 映射 + 调用求解器）
│   └── resolution_*_bouteille.py  # 4 / 5 传感器版本（备选实现）
├── data/
│   └── data.json                  # 灯具模型参数（a, b, c, d）
├── grandMA3API/                   # 实验性：Lua 调用 Python（lupa）验证
├── test_verification/             # 测试数据与验证用例
├── ui_start.spec                  # PyInstaller 打包配置
├── ui_start_modified.spec         # PyInstaller 打包配置（输出名 PresetsCorrection）
├── requirements.txt               # 运行依赖
├── requirements-dev.txt           # 开发 / 打包依赖
├── dev.env                        # 开发环境变量（PYTHONPATH）
└── log/                           # 运行日志（按日期命名）
```

## 环境要求

- **Python 3.10+**（开发环境为 3.10.5）
- 安装依赖：

```bash
pip install -r requirements.txt
```

主要依赖：`PySide6`、`qt-material`、`pandas`、`openpyxl`、`numpy`、`scipy`

> 旧版 tkinter 界面（`GUI.py`）只需 `openpyxl`、`pandas`，无需额外安装（tkinter 随 Python 自带）。
>
> `requirements*.txt` 刻意保持**纯 ASCII 注释**：pip 会按系统区域设置（简体中文 Windows 下为 GBK）
> 解码该文件，含中文会导致 `UnicodeDecodeError`。

## 运行

```bash
cd Modif_fichier_preset
python ui_start.py
```

程序启动后会在 `log/` 下按日期生成日志文件（`YYYY-MM-DD.log`）。

## 打包

使用 PyInstaller 打包为独立可执行文件（需先装开发依赖）：

```bash
pip install -r requirements-dev.txt
pyinstaller ui_start_modified.spec
```

产物输出到 `PresetsCorrection-x.x.x/output/`，主程序名为 `PresetsCorrection.exe`。
打包结果中已包含 `data/` 目录（见 spec 文件中的 `datas` 配置）。

## 配置文件格式

`data/data.json` 保存各灯具模型的 tilt 校正参数：

```json
{
  "projecteur1": { "a": 0.857, "b": 0.0, "c": 0.857, "d": 0.0 }
}
```

config Excel 需包含两张表（可用 `create_config.py` 生成模板）：

- **Sensors**：传感器名称与位置 `Name, x, y, z`
- **Spotlights**：灯具 ID、理论位置、轴定义、旋转矩阵、朝向

> ⚠️ **注意**：Excel 中各工作表（Sheet）的**名称必须与要修改的 preset XML 文件名一致**。
> 可参考 `Modif_fichier_preset/PresetTest.xlsx`。

## 使用流程

1. 用 **MVR To Config** 从 `.mvr` 导出场地配置 Excel
2. 用 **Presets To Excel** 把待修正的 preset 导出为 Excel
3. 现场测量各传感器数据，填入 Excel_Config / Excel_M\*
4. 在 **Select Model** 中选定灯具并确认参数 a/b/c/d
5. 在 **Correction** 中选择传感器数量（4 或 5）并执行校正
6. 用 **Excel To Presets** 将结果写回 XML preset

## 说明

- `calcul_erreur/` 下保留了多个求解器版本（4 传感器、5 传感器、OSSEKOUR 版本等），
  **当前启用的是 `resolution.py`**，其余为历史实现，仅供对照参考。
- `grandMA3API/` 为技术验证用例（Lua 通过 lupa 调用 Python），尚未集成到主程序。
- 项目未跟踪的文件（构建产物、日志、Excel/XML/ZIP 等）见 `.gitignore`。

---

*Projet G1G2 — Centrale Lille*
