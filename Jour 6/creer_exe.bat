@echo off
echo ========================================
echo Installation des dependances...
echo ========================================
pip install -r requirements.txt

echo.
echo ========================================
echo Creation du fichier .exe...
echo ========================================
python setup_exe.py

echo.
echo ========================================
echo Terminé!
echo Le fichier .exe se trouve dans le dossier "dist"
echo ========================================
pause
