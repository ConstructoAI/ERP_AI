@echo off
chcp 65001 >nul
echo ╔══════════════════════════════════════════════════════════════╗
echo ║     PUSH RAPIDE VERS GITHUB - CONSTRUCTO AI                 ║
echo ╔══════════════════════════════════════════════════════════════╝
echo.

cd /d "E:\09. LOGICIELS\GITHUB\ERP_AI-main"

echo 📝 Ajout des fichiers...
git add .

echo.
echo 💾 Création du commit...
git commit -m "Mise à jour: Ajout 120 postes de travail construction"

echo.
echo 🚀 Envoi vers GitHub...
git push

if %errorlevel% eq 0 (
    echo.
    echo ✅ SUCCÈS ! Modifications envoyées sur GitHub
    echo 📍 https://github.com/ConstructoAI/ERP_AI
) else (
    echo.
    echo ❌ Erreur lors du push
    echo Essayez le fichier sync_github_constructo.bat pour une configuration complète
)

echo.
pause