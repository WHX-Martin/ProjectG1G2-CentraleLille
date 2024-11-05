-- Lua 脚本，调用 Python 函数
local python = require("lupa").python

-- 创建 Python 环境
local py = python.import("python_module")

-- 调用 Python 函数并获取返回结果
local result = py.add(10, 20)

-- 输出结果
print("The result of 10 + 20 is:", result)
