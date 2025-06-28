@echo off
setlocal enabledelayedexpansion

:: 检查Python环境
where python >nul 2>&1
if !errorlevel! neq 0 (
    echo 错误：未找到Python环境，请先安装Python并添加到PATH。
    exit /b 1
)

:: 安装/升级必要工具
python -m pip install --upgrade pip setuptools wheel twine
if !errorlevel! neq 0 (
    echo 错误：安装依赖失败，请检查网络连接。
    exit /b 1
)

:: 清理旧构建输出（可选）
if exist dist (
    echo 清理旧构建输出...
    rmdir /s /q dist
)
if exist build (
    rmdir /s /q build
)
if exist PyFeishuGroupBot.egg-info (
    rmdir /s /q PyFeishuGroupBot.egg-info
)

:: 构建源分发和wheel包
echo 开始构建包...
python setup.py sdist bdist_wheel
if !errorlevel! neq 0 (
    echo 错误：构建失败，请检查setup.py配置。
    exit /b 1
)

:: 上传到PyPI
echo 开始上传到PyPI...
python -m twine upload dist/*
if !errorlevel! neq 0 (
    echo 错误：上传失败，请检查PyPI凭证或网络。
    exit /b 1
)

echo 操作成功完成！
exit /b 0